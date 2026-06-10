import React, { useEffect, useState } from 'react';
import {
  Alert,
  FlatList,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';
import {
  Calendar,
  LocaleConfig,
} from 'react-native-calendars';

import {
  DEFAULT_CATEGORY,
  getNotes,
  saveNotes,
} from '../utils/storage';

LocaleConfig.locales.pl = {
  monthNames: [
    'Styczeń',
    'Luty',
    'Marzec',
    'Kwiecień',
    'Maj',
    'Czerwiec',
    'Lipiec',
    'Sierpień',
    'Wrzesień',
    'Październik',
    'Listopad',
    'Grudzień',
  ],
  monthNamesShort: [
    'Sty',
    'Lut',
    'Mar',
    'Kwi',
    'Maj',
    'Cze',
    'Lip',
    'Sie',
    'Wrz',
    'Paź',
    'Lis',
    'Gru',
  ],
  dayNames: [
    'Niedziela',
    'Poniedziałek',
    'Wtorek',
    'Środa',
    'Czwartek',
    'Piątek',
    'Sobota',
  ],
  dayNamesShort: [
    'Niedz.',
    'Pon.',
    'Wt.',
    'Śr.',
    'Czw.',
    'Pt.',
    'Sob.',
  ],
  today: 'Dzisiaj',
};

LocaleConfig.defaultLocale = 'pl';

const getNoteDate = (note) =>
  note.date || String(note.createdAt).split('T')[0];

const buildMarkedDates = (notes, selectedDate) => {
  const marked = notes.reduce((acc, note) => {
    const date = getNoteDate(note);

    acc[date] = {
      marked: true,
      dotColor: '#ff85de',
    };

    return acc;
  }, {});

  if (selectedDate) {
    marked[selectedDate] = {
      ...marked[selectedDate],
      selected: true,
      selectedColor: '#00bafa',
      selectedTextColor: 'white',
      dotColor: '#ffffff',
    };
  }

  return marked;
};

const getRandomDateLastWeek = () => {
  const randomDaysAgo = Math.floor(Math.random() * 7);
  const date = new Date();
  date.setDate(date.getDate() - randomDaysAgo);

  return {
    date: date.toISOString().split('T')[0],
    timestamp: date.getTime().toString(),
  };
};

const makeUniqueTitle = (base, notes) => {
  const titles = notes.map((note) => note.title);
  let candidate = base;
  let suffix = 1;

  while (titles.includes(candidate)) {
    candidate = `${base}-${suffix}`;
    suffix += 1;
  }

  return candidate;
};

const CalendarScreen = ({ navigation }) => {
  const [allNotes, setAllNotes] = useState([]);
  const [markedDates, setMarkedDates] = useState({});
  const [selectedDate, setSelectedDate] = useState('');
  const [dayNotes, setDayNotes] = useState([]);

  const loadNotes = async () => {
    const notes = await getNotes();

    setAllNotes(notes);
    setMarkedDates(buildMarkedDates(notes, selectedDate));

    if (selectedDate) {
      setDayNotes(
        notes.filter(
          (note) => getNoteDate(note) === selectedDate
        )
      );
    }
  };

  useEffect(() => {
    loadNotes();
    const unsubscribe = navigation.addListener(
      'focus',
      loadNotes
    );
    return unsubscribe;
  }, [navigation, selectedDate]);

  const handleDayPress = (day) => {
    setSelectedDate(day.dateString);
    setDayNotes(
      allNotes.filter(
        (note) => getNoteDate(note) === day.dateString
      )
    );
    setMarkedDates(
      buildMarkedDates(allNotes, day.dateString)
    );
  };

  const deleteNote = async (id) => {
    const updatedNotes = allNotes.filter(
      (note) => note.id !== id
    );

    await saveNotes(updatedNotes);

    setAllNotes(updatedNotes);
    setDayNotes((prev) =>
      prev.filter((note) => note.id !== id)
    );
    setMarkedDates(
      buildMarkedDates(updatedNotes, selectedDate)
    );
  };

  const confirmDelete = (id) => {
    Alert.alert(
      'Usuń notatkę',
      'Czy chcesz usunąć tę notatkę?',
      [
        {
          text: 'Anuluj',
          style: 'cancel',
        },
        {
          text: 'Usuń',
          style: 'destructive',
          onPress: () => deleteNote(id),
        },
      ]
    );
  };

  const generateRandom = async () => {
    try {
      const notes = await getNotes();
      const newNotes = [];

      for (let i = 0; i < 10; i++) {
        const { date, timestamp } =
          getRandomDateLastWeek();

        const baseTitle =
          `Losowa_notatka_${i + 1}_${timestamp}`;
        const title = makeUniqueTitle(baseTitle, [
          ...notes,
          ...newNotes,
        ]);

        newNotes.push({
          id: `${Date.now()}-${i}`,
          title,
          desc:
            `Przykładowa notatka stworzona automatycznie dla daty ${date}.`,
          category: DEFAULT_CATEGORY.name,
          date,
          createdAt: new Date(
            Number(timestamp)
          ).toISOString(),
        });
      }

      await saveNotes([...notes, ...newNotes]);
      await loadNotes();
    } catch (error) {
      console.log(
        'Błąd generowania notatek:',
        error
      );
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Kalendarz notatek</Text>

      <TouchableOpacity
        style={styles.generateButton}
        onPress={generateRandom}
      >
        <Text style={styles.generateText}>
          Generuj losowe notatki
        </Text>
      </TouchableOpacity>

      <Calendar
        style={styles.calendar}
        onDayPress={handleDayPress}
        firstDay={1}
        markingType="simple"
        markedDates={markedDates}
      />

      <View style={styles.noteListHeader}>
        <Text style={styles.subTitle}>
          {selectedDate
            ? `Notatki z ${selectedDate}`
            : 'Wybierz dzień, aby zobaczyć notatki'}
        </Text>

        {selectedDate ? (
          <Text style={styles.countText}>
            {dayNotes.length}{' '}
            {dayNotes.length === 1
              ? 'notatka'
              : 'notatek'}
          </Text>
        ) : null}
      </View>

      {selectedDate && dayNotes.length === 0 ? (
        <Text style={styles.emptyText}>
          Brak notatek dla wybranego dnia.
        </Text>
      ) : null}

      <FlatList
        data={dayNotes}
        keyExtractor={(item) => item.id.toString()}
        contentContainerStyle={styles.flatList}
        renderItem={({ item }) => (
          <TouchableOpacity
            style={styles.note}
            onPress={() =>
              navigation.navigate('Screen04', {
                noteId: item.id,
              })
            }
            onLongPress={() => confirmDelete(item.id)}
          >
            <Text style={styles.noteCategory}>
              {item.category}
            </Text>
            <Text style={styles.noteTitle}>
              {item.title}
            </Text>
            <Text style={styles.noteDesc} numberOfLines={3}>
              {item.desc}
            </Text>
          </TouchableOpacity>
        )}
      />
    </View>
  );
};

export default CalendarScreen;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f7fbff',
    padding: 15,
  },

  title: {
    fontSize: 22,
    fontWeight: '700',
    color: '#1f2d5a',
    textAlign: 'center',
    marginBottom: 12,
  },

  generateButton: {
    backgroundColor: '#ff85de',
    borderRadius: 8,
    padding: 12,
    alignItems: 'center',
    marginBottom: 12,
  },

  generateText: {
    color: 'white',
    fontWeight: '700',
  },

  calendar: {
    borderWidth: 1,
    borderColor: '#93d8ff',
    borderRadius: 8,
    backgroundColor: '#ffffff',
    marginBottom: 18,
    elevation: 2,
  },

  noteListHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
    gap: 10,
  },

  subTitle: {
    flex: 1,
    fontSize: 18,
    fontWeight: '600',
    color: '#273c75',
  },

  countText: {
    fontSize: 14,
    color: '#5d6b8a',
  },

  flatList: {
    paddingBottom: 20,
  },

  emptyText: {
    color: '#556171',
    fontSize: 15,
    textAlign: 'center',
    marginVertical: 12,
  },

  note: {
    backgroundColor: 'white',
    borderRadius: 8,
    padding: 14,
    marginBottom: 10,
    borderWidth: 1,
    borderColor: '#d8ecff',
  },

  noteCategory: {
    alignSelf: 'flex-start',
    backgroundColor: '#dbeafe',
    color: '#2563eb',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 20,
    fontSize: 12,
    fontWeight: '600',
    marginBottom: 8,
  },

  noteTitle: {
    color: '#1f2d5a',
    fontSize: 17,
    fontWeight: '700',
    marginBottom: 6,
  },

  noteDesc: {
    color: '#556171',
    fontSize: 14,
    lineHeight: 20,
  },
});

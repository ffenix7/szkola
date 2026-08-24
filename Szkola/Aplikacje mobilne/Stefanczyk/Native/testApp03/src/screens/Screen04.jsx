import React from 'react';
import {
  Alert,
  Button,
  StyleSheet,
  Text,
  TextInput,
  View,
} from 'react-native';
import { Picker } from '@react-native-picker/picker';

import {
  DEFAULT_CATEGORY,
  getCategories,
  getNotes,
  saveNotes,
} from '../utils/storage';

const sameId = (first, second) =>
  String(first) === String(second);

const Screen04 = ({ navigation, route }) => {
  const noteId = route.params?.noteId;
  const [title, setTitle] = React.useState('');
  const [desc, setDesc] = React.useState('');
  const [cat, setCat] = React.useState(DEFAULT_CATEGORY.name);
  const [categories, setCategories] = React.useState([DEFAULT_CATEGORY,]);
  const [noteFound, setNoteFound] = React.useState(true);

  const loadData = async () => {
    try {
      const [storedNotes, storedCategories] =
        await Promise.all([getNotes(), getCategories()]);

      const selectedNote = storedNotes.find((note) =>
        sameId(note.id, noteId)
      );

      setCategories(storedCategories);

      if (!selectedNote) {
        setNoteFound(false);
        return;
      }

      setNoteFound(true);
      setTitle(selectedNote.title);
      setDesc(selectedNote.desc);
      setCat(selectedNote.category || DEFAULT_CATEGORY.name);
    } catch (error) {
      console.log('Błąd ładowania notatki:', error);
      Alert.alert(
        'Błąd',
        'Nie udało się wczytać notatki'
      );
    }
  };

  React.useEffect(() => {
    const unsubscribe = navigation.addListener(
      'focus',
      loadData
    );

    loadData();

    return unsubscribe;
  }, [navigation, noteId]);

  const saveChanges = async () => {
    if (
      title.trim() === '' ||
      desc.trim() === '' ||
      cat.trim() === ''
    ) {
      Alert.alert(
        'Błąd',
        'Wszystkie pola muszą być uzupełnione'
      );
      return;
    }

    try {
      const storedNotes = await getNotes();
      const updatedNotes = storedNotes.map((note) => {
        if (sameId(note.id, noteId)) {
          return {
            ...note,
            title: title.trim(),
            desc: desc.trim(),
            category: cat,
          };
        }

        return note;
      });

      await saveNotes(updatedNotes);

      Alert.alert('Sukces', 'Notatka została zapisana');
      navigation.navigate('Screen02');
    } catch (error) {
      console.log('Błąd zapisu notatki:', error);
      Alert.alert(
        'Błąd',
        'Nie udało się zapisać notatki'
      );
    }
  };

  if (!noteFound) {
    return (
      <View style={styles.container}>
        <Text style={styles.header}>Nie znaleziono notatki</Text>
        <Button
          title="Wróć do notatek"
          onPress={() => navigation.navigate('Screen02')}
        />
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Edytuj notatkę</Text>

      <TextInput
        style={styles.input}
        placeholder="Tytuł"
        value={title}
        onChangeText={setTitle}
      />

      <TextInput
        style={[styles.input, styles.textArea]}
        placeholder="Opis"
        value={desc}
        onChangeText={setDesc}
        multiline
      />

      <View style={styles.pickerContainer}>
        <Picker
          selectedValue={cat}
          onValueChange={(itemValue) => setCat(itemValue)}
        >
          {categories.map((item) => (
            <Picker.Item
              key={item.id}
              label={item.name}
              value={item.name}
            />
          ))}
        </Picker>
      </View>

      <Button title="Zapisz zmiany" onPress={saveChanges} />
    </View>
  );
};

export default Screen04;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#f5f7fa',
  },

  header: {
    fontSize: 24,
    marginBottom: 20,
    fontWeight: 'bold',
    color: '#111',
  },

  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 12,
    marginBottom: 15,
    borderRadius: 8,
    backgroundColor: 'white',
  },

  textArea: {
    height: 150,
    textAlignVertical: 'top',
  },

  pickerContainer: {
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 8,
    marginBottom: 20,
    backgroundColor: 'white',
    overflow: 'hidden',
  },
});

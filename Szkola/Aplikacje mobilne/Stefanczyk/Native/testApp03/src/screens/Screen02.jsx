import {
  Alert,
  FlatList,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from 'react-native';
import { useEffect, useState } from 'react';

import {
  backupNotesToServer,
  restoreNotesFromServer,
} from '../utils/api';
import {
  clearNotes,
  getNotes,
  saveNotes,
} from '../utils/storage';

const filterNotes = (items, search) => {
  const phrase = search.trim().toLowerCase();

  if (!phrase) {
    return items;
  }

  return items.filter((note) => {
    const title = note.title.toLowerCase();
    const desc = note.desc.toLowerCase();
    const category = note.category.toLowerCase();

    return (
      title.includes(phrase) ||
      desc.includes(phrase) ||
      category.includes(phrase)
    );
  });
};

const Screen02 = ({ navigation }) => {
  const [notes, setNotes] = useState([]);
  const [allNotes, setAllNotes] = useState([]);
  const [search, setSearch] = useState('');

  const setVisibleNotes = (items, phrase = search) => {
    setAllNotes(items);
    setNotes(filterNotes(items, phrase));
  };

  const loadNotes = async () => {
    try {
      const storedNotes = await getNotes();
      setVisibleNotes(storedNotes);
    } catch (error) {
      console.log('Error loading notes', error);
    }
  };

  const handleSearch = (text) => {
    setSearch(text);
    setNotes(filterNotes(allNotes, text));
  };

  const deleteNote = async (id) => {
    try {
      const storedNotes = await getNotes();
      const updatedNotes = storedNotes.filter(
        (note) => note.id !== id
      );

      await saveNotes(updatedNotes);
      setVisibleNotes(updatedNotes);
    } catch (error) {
      console.log('Error deleting note', error);
    }
  };

  const clearLocalNotes = () => {
    Alert.alert(
      'Czyszczenie notatek',
      'Usunąć wszystkie notatki z aplikacji mobilnej?',
      [
        {
          text: 'Anuluj',
          style: 'cancel',
        },
        {
          text: 'Usuń',
          style: 'destructive',
          onPress: async () => {
            await clearNotes();
            setSearch('');
            setAllNotes([]);
            setNotes([]);
          },
        },
      ]
    );
  };

  const backupNotes = async () => {
    try {
      const result = await backupNotesToServer();

      Alert.alert(
        'Backup',
        `Zapisano notatki na serwerze: ${
          result?.count ?? allNotes.length
        }`
      );
    } catch (error) {
      Alert.alert('Błąd backupu', error.message);
    }
  };

  const restoreNotes = () => {
    Alert.alert(
      'Restore',
      'Pobrać notatki z serwera i zastąpić lokalne dane?',
      [
        {
          text: 'Anuluj',
          style: 'cancel',
        },
        {
          text: 'Pobierz',
          onPress: async () => {
            try {
              const restoredNotes =
                await restoreNotesFromServer();

              setSearch('');
              setVisibleNotes(restoredNotes, '');

              Alert.alert(
                'Restore',
                `Pobrano notatki: ${restoredNotes.length}`
              );
            } catch (error) {
              Alert.alert(
                'Błąd restore',
                error.message
              );
            }
          },
        },
      ]
    );
  };

  useEffect(() => {
    const unsubscribe = navigation.addListener(
      'focus',
      loadNotes
    );

    return unsubscribe;
  }, [navigation, search]);

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Twoje notatki</Text>

      <TextInput
        style={styles.input}
        placeholder="Szukaj notatki"
        value={search}
        onChangeText={handleSearch}
      />

      <View style={styles.actions}>
        <TouchableOpacity
          style={[styles.actionButton, styles.backupButton]}
          onPress={backupNotes}
        >
          <Text style={styles.actionText}>Backup</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={[styles.actionButton, styles.restoreButton]}
          onPress={restoreNotes}
        >
          <Text style={styles.actionText}>Restore</Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={[styles.actionButton, styles.clearButton]}
          onPress={clearLocalNotes}
        >
          <Text style={styles.actionText}>Wyczyść</Text>
        </TouchableOpacity>
      </View>

      <FlatList
        data={notes}
        numColumns={2}
        keyExtractor={(item) => item.id.toString()}
        columnWrapperStyle={{
          justifyContent: 'space-between',
        }}
        contentContainerStyle={{
          paddingBottom: 20,
        }}
        ListEmptyComponent={
          <Text style={styles.empty}>Brak notatek</Text>
        }
        renderItem={({ item }) => (
          <TouchableOpacity
            style={styles.card}
            activeOpacity={0.8}
            onPress={() =>
              navigation.navigate('Screen04', {
                noteId: item.id,
              })
            }
            onLongPress={() => deleteNote(item.id)}
          >
            <Text style={styles.category}>
              {item.category}
            </Text>

            <Text style={styles.title}>{item.title}</Text>

            <Text style={styles.desc} numberOfLines={4}>
              {item.desc}
            </Text>
          </TouchableOpacity>
        )}
      />
    </View>
  );
};

export default Screen02;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#f5f7fa',
  },

  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 10,
    marginBottom: 15,
    borderRadius: 5,
    backgroundColor: 'white',
  },

  header: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    color: '#222',
  },

  actions: {
    flexDirection: 'row',
    gap: 8,
    marginBottom: 16,
  },

  actionButton: {
    flex: 1,
    minHeight: 44,
    borderRadius: 8,
    alignItems: 'center',
    justifyContent: 'center',
    paddingHorizontal: 8,
  },

  backupButton: {
    backgroundColor: '#16a34a',
  },

  restoreButton: {
    backgroundColor: '#2563eb',
  },

  clearButton: {
    backgroundColor: '#dc2626',
  },

  actionText: {
    color: 'white',
    fontWeight: '700',
    fontSize: 14,
  },

  card: {
    backgroundColor: 'white',
    width: '48%',
    padding: 15,
    borderRadius: 8,
    marginBottom: 15,
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.08,
    shadowRadius: 4,
    elevation: 3,
  },

  category: {
    alignSelf: 'flex-start',
    backgroundColor: '#dbeafe',
    color: '#2563eb',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 20,
    fontSize: 12,
    fontWeight: '600',
    marginBottom: 10,
  },

  title: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#111',
    marginBottom: 8,
  },

  desc: {
    fontSize: 14,
    color: '#555',
    lineHeight: 20,
  },

  empty: {
    color: '#666',
    textAlign: 'center',
    marginTop: 30,
    fontSize: 16,
  },
});

import {
  Text,
  View,
  FlatList,
  TouchableOpacity,
  StyleSheet,
  TextInput,
} from 'react-native';

import { useEffect, useState } from 'react';
import * as SecureStore from 'expo-secure-store';

import NoteModal from '../Components/NoteModal.jsx';

const Screen02 = ({ navigation }) => {
  const [notes, setNotes] = useState([]);
  const [allNotes, setAllNotes] = useState([]);
  const [search, setSearch] = useState('');

  const [selectedNote, setSelectedNote] =
    useState(null);

  const [modalVisible, setModalVisible] =
    useState(false);

  const loadNotes = async () => {
    try {
      const storedNotes =
        await SecureStore.getItemAsync('notes');

      if (storedNotes) {
        const parsedNotes = JSON.parse(
          storedNotes
        );

        setNotes(parsedNotes);
        setAllNotes(parsedNotes);
      } else {
        setNotes([]);
        setAllNotes([]);
      }
    } catch (e) {
      console.log('Error loading notes', e);
    }
  };

  const handleSearch = (text) => {
    setSearch(text);

    if (text.trim() === '') {
      setNotes(allNotes);
      return;
    }

    const filteredNotes = allNotes.filter(
      (note) =>
        note.title
          .toLowerCase()
          .startsWith(text.toLowerCase()) ||
        note.category
          .toLowerCase()
          .startsWith(text.toLowerCase()) ||
        note.desc
          .toLowerCase()
          .startsWith(text.toLowerCase())
    );

    setNotes(filteredNotes);
  };

  const deleteNote = async (id) => {
    try {
      const storedNotes =
        await SecureStore.getItemAsync('notes');

      if (!storedNotes) return;

      const parsedNotes = JSON.parse(
        storedNotes
      );

      const updatedNotes = parsedNotes.filter(
        (note) => note.id !== id
      );

      await SecureStore.setItemAsync(
        'notes',
        JSON.stringify(updatedNotes)
      );

      setNotes(updatedNotes);
      setAllNotes(updatedNotes);
    } catch (e) {
      console.log('Error deleting note', e);
    }
  };

  useEffect(() => {
    const unsubscribe =
      navigation.addListener(
        'focus',
        () => {
          loadNotes();
        }
      );

    return unsubscribe;
  }, [navigation]);

  return (
    <View style={styles.container}>
      <Text style={styles.header}>
        Twoje notatki
      </Text>

      <TextInput
        style={styles.input}
        placeholder="Szukaj notatki"
        value={search}
        onChangeText={handleSearch}
      />

      <FlatList
        data={notes}
        numColumns={2}
        keyExtractor={(item) =>
          item.id.toString()
        }
        columnWrapperStyle={{
          justifyContent: 'space-between',
        }}
        contentContainerStyle={{
          paddingBottom: 20,
        }}
        renderItem={({ item }) => (
          <TouchableOpacity
            style={styles.card}
            activeOpacity={0.8}
            onPress={() => {
              setSelectedNote(item);
              setModalVisible(true);
            }}
            onLongPress={() =>
              deleteNote(item.id)
            }
          >
            <Text style={styles.category}>
              {item.category}
            </Text>

            <Text style={styles.title}>
              {item.title}
            </Text>

            <Text
              style={styles.desc}
              numberOfLines={4}
            >
              {item.desc}
            </Text>
          </TouchableOpacity>
        )}
      />

      <NoteModal
        visible={modalVisible}
        note={selectedNote}
        onClose={() => setModalVisible(false)}
        onSave={loadNotes}
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

  card: {
    backgroundColor: 'white',
    width: '48%',
    padding: 15,
    borderRadius: 12,
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
});
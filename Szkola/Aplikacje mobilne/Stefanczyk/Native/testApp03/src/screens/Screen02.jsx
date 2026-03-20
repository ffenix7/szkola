import { Button, Text, View, FlatList, TouchableOpacity } from 'react-native';
import { useEffect, useState } from 'react';
import * as SecureStore from 'expo-secure-store';

const Screen02 = ({ navigation }) => {

  const [notes, setNotes] = useState([]);

  const loadNotes = async () => {
    const storedNotes = await SecureStore.getItemAsync("notes");

    if (storedNotes) {
      setNotes(JSON.parse(storedNotes));
    } else {
      setNotes([]);
    }
  };

  const deleteNote = async (id) => {
    try {
      const storedNotes = await SecureStore.getItemAsync("notes");

      if (!storedNotes) return;

      const notes = JSON.parse(storedNotes);

      const updatedNotes = notes.filter(note => note.id !== id);

      await SecureStore.setItemAsync("notes", JSON.stringify(updatedNotes));

      setNotes(updatedNotes);
    } catch (e) {
      console.log("Error deleting note", e);
    }
  };

  useEffect(() => {
    const unsubscribe = navigation.addListener('focus', () => {
      console.log("screen focused");
      loadNotes();
    });

    return unsubscribe;
  }, [navigation]);

  return (
    <View>
      <Text>Screen 2</Text>

      <FlatList
        numColumns={2}
        data={notes}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <TouchableOpacity
            style={{ margin: 10, backgroundColor: "aqua", padding: 10, borderRadius: 10 }}
            onLongPress={() => deleteNote(item.id)}
          >
            <Text style={{fontSize: 30, }}>{item.title}</Text>
            <Text>{item.desc}</Text>
          </TouchableOpacity>
        )}
      />
    </View>
  );
};

export default Screen02;
import { Text, View, TextInput, Button } from 'react-native';
import * as SecureStore from 'expo-secure-store';
import * as React from 'react';

const Screen01 = ({navigation}) => {
  const [id, setID] = React.useState(1);
  const [title, setTitle] = React.useState('');
  const [desc, setDesc] = React.useState('');

  const addNote = async () => {
  try {
    const storedNotes = await SecureStore.getItemAsync("notes");

    let notes = [];

    if (storedNotes) {
      const parsed = JSON.parse(storedNotes);
      notes = Array.isArray(parsed) ? parsed : [];
    }

    const newNote = {
      id: id,
      title: title,
      desc: desc
    };

    notes.push(newNote);

    await SecureStore.setItemAsync("notes", JSON.stringify(notes));

    console.log("Saved notes:", notes);

    setID(prev => prev + 1);
    setTitle('');
    setDesc('');
  } catch (e) {
    console.log("Error saving note", e);
  }
  navigation.navigate("S2")
};

  return (
    <View>
      <Text>Screen 1</Text>

      <TextInput
        placeholder="Tytuł"
        value={title}
        onChangeText={setTitle}
      />

      <TextInput
        placeholder="Opis"
        value={desc}
        onChangeText={setDesc}
      />

      <Button
        title="Dodaj notatke"
        onPress={addNote}
      />
    </View>
  );
};

export default Screen01;
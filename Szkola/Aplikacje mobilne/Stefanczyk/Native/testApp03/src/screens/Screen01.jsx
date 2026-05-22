import { Text, View, TextInput, Button } from 'react-native';
import * as SecureStore from 'expo-secure-store';
import * as React from 'react';
import { Picker } from '@react-native-picker/picker';

const Screen01 = ({ navigation }) => {
  const [id, setID] = React.useState(1);
  const [title, setTitle] = React.useState('');
  const [desc, setDesc] = React.useState('');
  const [cat, changeCat] = React.useState('');
  const [categories, setCategories] = React.useState([]);

  React.useEffect(() => {
    const loadCategories = async () => {
      try {
        const storedCats = await SecureStore.getItemAsync('categories');

        if (storedCats) {
          const parsed = JSON.parse(storedCats);
          setCategories(Array.isArray(parsed) ? parsed : []);
        }
      } catch (e) {
        console.log('Error loading categories', e);
      }
    };

    loadCategories();
  }, []);

  const addNote = async () => {
    try {
      const storedNotes = await SecureStore.getItemAsync('notes');
      let notes = [];

      if (storedNotes) {
        const parsed = JSON.parse(storedNotes);
        notes = Array.isArray(parsed) ? parsed : [];
      }

      const newNote = {
        id: id,
        title: title,
        desc: desc,
        category: cat,
      };

      notes.push(newNote);

      await SecureStore.setItemAsync('notes', JSON.stringify(notes));

      console.log('Saved notes:', notes);

      setID(prev => prev + 1);
      setTitle('');
      setDesc('');
      changeCat('');
    } catch (e) {
      console.log('Error saving note', e);
    }

    navigation.navigate('Screen02');
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

      <Picker
        selectedValue={cat}
        onValueChange={(itemValue) => {
          changeCat(itemValue);
        }}
      >
        {categories.map((item, index) => (
          <Picker.Item
            key={index}
            label={item.name}
            value={item.name}
          />
        ))}
      </Picker>

      <Button
        title="Dodaj notatke"
        onPress={addNote}
      />
    </View>
  );
};

export default Screen01;
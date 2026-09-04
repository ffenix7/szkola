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

const Screen01 = ({ navigation }) => {
  const [title, setTitle] = React.useState('');
  const [desc, setDesc] = React.useState('');
  const [cat, setCat] = React.useState(
    DEFAULT_CATEGORY.name
  );
  const [categories, setCategories] = React.useState([
    DEFAULT_CATEGORY,
  ]);

  React.useEffect(() => {
    const loadCategories = async () => {
      try {
        const storedCategories = await getCategories();

        setCategories(storedCategories);
        setCat(storedCategories[0].name);
      } catch (error) {
        console.log('Błąd ładowania kategorii:', error);
        setCategories([DEFAULT_CATEGORY]);
        setCat(DEFAULT_CATEGORY.name);
      }
    };

    const unsubscribe = navigation.addListener(
      'focus',
      loadCategories
    );

    loadCategories();

    return unsubscribe;
  }, [navigation]);

  const addNote = async () => {
    if (
      title.trim() === '' ||
      desc.trim() === '' ||
      cat.trim() === ''
    ) {
      Alert.alert('Błąd', 'Uzupełnij wszystkie pola');
      return;
    }

    try {
      const notes = await getNotes();
      const newNote = {
        id: Date.now(),
        title: title.trim(),
        desc: desc.trim(),
        category: cat,
        createdAt: new Date().toISOString(),
      };

      await saveNotes([...notes, newNote]);

      setTitle('');
      setDesc('');
      setCat(categories[0]?.name || DEFAULT_CATEGORY.name);

      navigation.navigate('Screen02');
    } catch (error) {
      console.log('Błąd zapisu notatki:', error);
      Alert.alert(
        'Błąd',
        'Nie udało się zapisać notatki'
      );
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Dodaj notatkę</Text>

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

      <Button title="Dodaj notatkę" onPress={addNote} />
    </View>
  );
};

export default Screen01;

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
    height: 120,
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

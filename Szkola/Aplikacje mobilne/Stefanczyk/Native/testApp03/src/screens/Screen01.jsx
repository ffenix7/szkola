import React from 'react';

import {
  View,
  Text,
  TextInput,
  Button,
  StyleSheet,
  Alert,
} from 'react-native';

import * as SecureStore from 'expo-secure-store';

import { Picker } from '@react-native-picker/picker';

const Screen01 = ({ navigation }) => {
  const [title, setTitle] = React.useState('');
  const [desc, setDesc] = React.useState('');

  const [cat, setCat] =
    React.useState('Ogólne');

  const [categories, setCategories] =
    React.useState([]);

  React.useEffect(() => {
    const loadCategories = async () => {
      try {
        const storedCats =
          await SecureStore.getItemAsync(
            'categories'
          );

        if (storedCats) {
          const parsed = JSON.parse(storedCats);

          if (
            Array.isArray(parsed) &&
            parsed.length > 0
          ) {
            setCategories(parsed);

            setCat(parsed[0].name);
          } else {
            const defaultCat = [
              { name: 'Ogólne' },
            ];

            setCategories(defaultCat);
            setCat('Ogólne');
          }
        } else {
          const defaultCat = [
            { name: 'Ogólne' },
          ];

          setCategories(defaultCat);
          setCat('Ogólne');
        }
      } catch (e) {
        console.log(
          'Błąd ładowania kategorii:',
          e
        );

        const defaultCat = [
          { name: 'Ogólne' },
        ];

        setCategories(defaultCat);
        setCat('Ogólne');
      }
    };

    loadCategories();
  }, []);

  const addNote = async () => {
    if (
      title.trim() === '' ||
      desc.trim() === '' ||
      cat.trim() === ''
    ) {
      Alert.alert(
        'Błąd',
        'Uzupełnij wszystkie pola'
      );

      return;
    }

    try {
      const storedNotes =
        await SecureStore.getItemAsync(
          'notes'
        );

      let notes = [];

      if (storedNotes) {
        const parsed = JSON.parse(
          storedNotes
        );

        if (Array.isArray(parsed)) {
          notes = parsed;
        }
      }

      const newNote = {
        id: Date.now(),
        title: title.trim(),
        desc: desc.trim(),
        category: cat,
      };

      notes.push(newNote);

      await SecureStore.setItemAsync(
        'notes',
        JSON.stringify(notes)
      );

      setTitle('');
      setDesc('');
      setCat(
        categories[0]?.name || 'Ogólne'
      );

      navigation.navigate('Screen02');
    } catch (e) {
      console.log(
        'Błąd zapisu notatki:',
        e
      );
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.header}>
        Dodaj notatkę
      </Text>

      <TextInput
        style={styles.input}
        placeholder="Tytuł"
        value={title}
        onChangeText={setTitle}
      />

      <TextInput
        style={[
          styles.input,
          styles.textArea,
        ]}
        placeholder="Opis"
        value={desc}
        onChangeText={setDesc}
        multiline
      />

      <View style={styles.pickerContainer}>
        <Picker
          selectedValue={cat}
          onValueChange={(itemValue) =>
            setCat(itemValue)
          }
        >
          {categories.map(
            (item, index) => (
              <Picker.Item
                key={index}
                label={item.name}
                value={item.name}
              />
            )
          )}
        </Picker>
      </View>

      <Button
        title="Dodaj notatkę"
        onPress={addNote}
      />
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
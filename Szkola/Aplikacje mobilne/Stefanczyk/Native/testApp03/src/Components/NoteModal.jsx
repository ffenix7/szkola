import React, {
  useEffect,
  useState,
} from 'react';

import {
  Modal,
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  TextInput,
  Alert,
} from 'react-native';

import * as SecureStore from 'expo-secure-store';

import { Picker } from '@react-native-picker/picker';

const NoteModal = ({
  visible,
  note,
  onClose,
  onSave,
}) => {
  const [title, setTitle] =
    useState('');

  const [desc, setDesc] =
    useState('');

  const [cat, setCat] =
    useState('');

  const [categories, setCategories] =
    useState([]);

  useEffect(() => {
    if (note) {
      setTitle(note.title);
      setDesc(note.desc);
      setCat(note.category);
    }
  }, [note]);

  useEffect(() => {
    const loadCategories = async () => {
      try {
        const storedCats =
          await SecureStore.getItemAsync(
            'categories'
          );

        if (storedCats) {
          const parsed = JSON.parse(
            storedCats
          );

          if (
            Array.isArray(parsed) &&
            parsed.length > 0
          ) {
            setCategories(parsed);
          } else {
            setCategories([
              { name: 'Ogólne' },
            ]);
          }
        } else {
          setCategories([
            { name: 'Ogólne' },
          ]);
        }
      } catch (e) {
        console.log(
          'Błąd ładowania kategorii:',
          e
        );

        setCategories([
          { name: 'Ogólne' },
        ]);
      }
    };

    loadCategories();
  }, []);

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
      const storedNotes =
        await SecureStore.getItemAsync(
          'notes'
        );

      if (!storedNotes) {
        Alert.alert(
          'Błąd',
          'Nie znaleziono notatek'
        );

        return;
      }

      const parsedNotes = JSON.parse(
        storedNotes
      );

      const updatedNotes = parsedNotes.map(
        (item) => {
          if (item.id === note.id) {
            return {
              ...item,
              title: title.trim(),
              desc: desc.trim(),
              category: cat,
            };
          }

          return item;
        }
      );

      await SecureStore.setItemAsync(
        'notes',
        JSON.stringify(updatedNotes)
      );

      if (onSave) {
        onSave();
      }

      Alert.alert(
        'Sukces',
        'Notatka została zapisana'
      );

      onClose();
    } catch (e) {
      console.log(
        'Błąd zapisu notatki:',
        e
      );

      Alert.alert(
        'Błąd',
        'Nie udało się zapisać notatki'
      );
    }
  };

  if (!note) return null;

  return (
    <Modal
      visible={visible}
      animationType="slide"
      transparent={true}
    >
      <View style={styles.overlay}>
        <View style={styles.modal}>
          <Text style={styles.header}>
            Edytuj notatkę
          </Text>

          <Text style={styles.label}>
            Tytuł
          </Text>

          <TextInput
            style={styles.input}
            value={title}
            onChangeText={setTitle}
            placeholder="Tytuł notatki"
          />

          <Text style={styles.label}>
            Opis
          </Text>

          <TextInput
            style={[
              styles.input,
              styles.textArea,
            ]}
            value={desc}
            onChangeText={setDesc}
            placeholder="Opis notatki"
            multiline
          />

          <Text style={styles.label}>
            Kategoria
          </Text>

          <View style={styles.pickerContainer}>
            <Picker
              selectedValue={cat}
              onValueChange={(
                itemValue
              ) => setCat(itemValue)}
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

          <TouchableOpacity
            style={styles.saveButton}
            onPress={saveChanges}
          >
            <Text style={styles.buttonText}>
              Zapisz zmiany
            </Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.closeButton}
            onPress={onClose}
          >
            <Text style={styles.buttonText}>
              Zamknij
            </Text>
          </TouchableOpacity>
        </View>
      </View>
    </Modal>
  );
};

export default NoteModal;

const styles = StyleSheet.create({
  overlay: {
    flex: 1,
    backgroundColor:
      'rgba(0,0,0,0.5)',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },

  modal: {
    width: '100%',
    backgroundColor: 'white',
    borderRadius: 20,
    padding: 20,
  },

  header: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    color: '#111',
    textAlign: 'center',
  },

  label: {
    fontSize: 16,
    fontWeight: '600',
    marginBottom: 6,
    marginTop: 10,
    color: '#222',
  },

  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 10,
    padding: 12,
    backgroundColor: 'white',
    fontSize: 16,
  },

  textArea: {
    minHeight: 120,
    textAlignVertical: 'top',
  },

  pickerContainer: {
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 10,
    marginTop: 5,
    overflow: 'hidden',
  },

  saveButton: {
    backgroundColor: '#16a34a',
    padding: 14,
    borderRadius: 10,
    alignItems: 'center',
    marginTop: 25,
    marginBottom: 10,
  },

  closeButton: {
    backgroundColor: '#2563eb',
    padding: 14,
    borderRadius: 10,
    alignItems: 'center',
  },

  buttonText: {
    color: 'white',
    fontWeight: 'bold',
    fontSize: 16,
  },
});
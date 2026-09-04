import React, { useEffect, useState } from 'react';
import {
  Alert,
  Modal,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from 'react-native';
import { Picker } from '@react-native-picker/picker';

import {
  DEFAULT_CATEGORY,
  getCategories,
  getNotes,
  saveNotes,
} from '../utils/storage';

const NoteModal = ({
  visible,
  note,
  onClose,
  onSave,
}) => {
  const [title, setTitle] = useState('');
  const [desc, setDesc] = useState('');
  const [cat, setCat] = useState(DEFAULT_CATEGORY.name);
  const [categories, setCategories] = useState([
    DEFAULT_CATEGORY,
  ]);

  useEffect(() => {
    if (note) {
      setTitle(note.title);
      setDesc(note.desc);
      setCat(note.category || DEFAULT_CATEGORY.name);
    }
  }, [note]);

  useEffect(() => {
    const loadCategories = async () => {
      try {
        setCategories(await getCategories());
      } catch (error) {
        console.log('Błąd ładowania kategorii:', error);
        setCategories([DEFAULT_CATEGORY]);
      }
    };

    if (visible) {
      loadCategories();
    }
  }, [visible]);

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

      if (!storedNotes.length) {
        Alert.alert('Błąd', 'Nie znaleziono notatek');
        return;
      }

      const updatedNotes = storedNotes.map((item) => {
        if (item.id === note.id) {
          return {
            ...item,
            title: title.trim(),
            desc: desc.trim(),
            category: cat,
          };
        }

        return item;
      });

      await saveNotes(updatedNotes);

      if (onSave) {
        onSave();
      }

      Alert.alert('Sukces', 'Notatka została zapisana');
      onClose();
    } catch (error) {
      console.log('Błąd zapisu notatki:', error);
      Alert.alert(
        'Błąd',
        'Nie udało się zapisać notatki'
      );
    }
  };

  if (!note) return null;

  return (
    <Modal visible={visible} animationType="slide" transparent>
      <View style={styles.overlay}>
        <View style={styles.modal}>
          <Text style={styles.header}>Edytuj notatkę</Text>

          <Text style={styles.label}>Tytuł</Text>
          <TextInput
            style={styles.input}
            value={title}
            onChangeText={setTitle}
            placeholder="Tytuł notatki"
          />

          <Text style={styles.label}>Opis</Text>
          <TextInput
            style={[styles.input, styles.textArea]}
            value={desc}
            onChangeText={setDesc}
            placeholder="Opis notatki"
            multiline
          />

          <Text style={styles.label}>Kategoria</Text>
          <View style={styles.pickerContainer}>
            <Picker
              selectedValue={cat}
              onValueChange={(itemValue) =>
                setCat(itemValue)
              }
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

          <TouchableOpacity
            style={styles.saveButton}
            onPress={saveChanges}
          >
            <Text style={styles.buttonText}>Zapisz zmiany</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.closeButton}
            onPress={onClose}
          >
            <Text style={styles.buttonText}>Zamknij</Text>
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
    backgroundColor: 'rgba(0,0,0,0.5)',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },

  modal: {
    width: '100%',
    backgroundColor: 'white',
    borderRadius: 8,
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
    borderRadius: 8,
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
    borderRadius: 8,
    marginTop: 5,
    overflow: 'hidden',
  },

  saveButton: {
    backgroundColor: '#16a34a',
    padding: 14,
    borderRadius: 8,
    alignItems: 'center',
    marginTop: 25,
    marginBottom: 10,
  },

  closeButton: {
    backgroundColor: '#2563eb',
    padding: 14,
    borderRadius: 8,
    alignItems: 'center',
  },

  buttonText: {
    color: 'white',
    fontWeight: 'bold',
    fontSize: 16,
  },
});

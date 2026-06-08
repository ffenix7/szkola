import React from 'react';
import {
  Alert,
  Button,
  StyleSheet,
  Text,
  TextInput,
  View,
} from 'react-native';

import { addCategory as saveCategory } from '../utils/storage';

const Screen03 = ({ navigation }) => {
  const [category, setCategory] = React.useState('');

  const addCategory = async () => {
    try {
      if (category.trim() === '') {
        Alert.alert('Błąd', 'Wpisz nazwę kategorii');
        return;
      }

      const result = await saveCategory(category.trim());

      if (!result.added) {
        Alert.alert(
          'Błąd',
          'Taka kategoria już istnieje'
        );
        return;
      }

      console.log('Zapisane kategorie:', result.categories);

      setCategory('');
      navigation.navigate('Screen02');
    } catch (error) {
      console.log('Error saving category:', error);
      Alert.alert(
        'Błąd',
        'Nie udało się zapisać kategorii'
      );
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Dodaj kategorię</Text>

      <TextInput
        style={styles.input}
        placeholder="Nazwa kategorii"
        value={category}
        onChangeText={setCategory}
      />

      <Button title="Dodaj kategorię" onPress={addCategory} />
    </View>
  );
};

export default Screen03;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
  },

  header: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },

  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 5,
    padding: 10,
    marginBottom: 20,
  },
});

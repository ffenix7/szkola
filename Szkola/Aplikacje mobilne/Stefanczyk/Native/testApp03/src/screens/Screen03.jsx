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

const Screen03 = ({ navigation }) => {
  const [category, setCategory] = React.useState('');

  const addCategory = async () => {
    try {
      if (category.trim() === '') {
        Alert.alert('Błąd', 'Wpisz nazwę kategorii');
        return;
      }

      const storedCategories =
        await SecureStore.getItemAsync('categories');

      let categories = [];

      if (storedCategories) {
        const parsed = JSON.parse(storedCategories);

        categories = Array.isArray(parsed)
          ? parsed
          : [];
      }

      const exists = categories.find(
        item =>
          item.name.toLowerCase() ===
          category.toLowerCase()
      );

      if (exists) {
        Alert.alert(
          'Błąd',
          'Taka kategoria już istnieje'
        );
        return;
      }

      const newCategory = {
        id: Date.now(),
        name: category,
      };

      categories.push(newCategory);

      await SecureStore.setItemAsync(
        'categories',
        JSON.stringify(categories)
      );

      console.log(
        'Zapisane kategorie:',
        categories
      );

      setCategory('');

      navigation.navigate('Screen02');
    } catch (e) {
      console.log(
        'Error saving category:',
        e
      );
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.header}>
        Dodaj kategorię
      </Text>

      <TextInput
        style={styles.input}
        placeholder="Nazwa kategorii"
        value={category}
        onChangeText={setCategory}
      />

      <Button
        title="Dodaj kategorię"
        onPress={addCategory}
      />
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
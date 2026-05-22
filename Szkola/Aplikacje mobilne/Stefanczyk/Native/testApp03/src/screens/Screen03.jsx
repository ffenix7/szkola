import { Text, View, TextInput, Button } from 'react-native';
import * as SecureStore from 'expo-secure-store';
import * as React from 'react';

const Screen03 = ({navigation}) => {
  const [id, setID] = React.useState(1);
  const [category, setCategory] = React.useState('');

  const addCategory = async () => {
  try {
    const storedCategories = await SecureStore.getItemAsync("categories");
    let categories = [];

    if (storedCategories) {
      const parsed = JSON.parse(storedCategories);
      categories = Array.isArray(parsed) ? parsed : [];
    }

    const newCategory = {
      id: id,
      name: category,
    };

    categories.push(newCategory);

    await SecureStore.setItemAsync("categories", JSON.stringify(categories));

    setID(prev => prev + 1);
    setCategory('');
  } catch (e) {
    console.log("Error saving category", e);
  }
  navigation.navigate("Screen02")
};

  return (
    <View>
      <Text>Screen 3</Text>

      <TextInput
        placeholder="Kategoria"
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
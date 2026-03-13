import { View, Text, TextInput, Button } from "react-native";
import React, { useEffect, useState } from "react";
import * as SecureStore from "expo-secure-store";

export default function Screen02({ navigation }) {
  const [text, setText] = useState('');
  const [data, setData] = useState("");

  useEffect(() => {
    async function loadData() {
      console.log("start");
      let temp = await SecureStore.getItemAsync("key");
      setData(temp);
    }
    loadData();
    const unsubscribe = navigation.addListener("focus", () => {
      console.log("start i każdy powrót");
    });
    return unsubscribe;
  }, [navigation]);

  async function addKey(){
    SecureStore.setItemAsync("key", text)
    setData(text)
    console.log(text)
  }

  async function deleteKey() {
    SecureStore.deleteItemAsync("key");
    setData("")
  }

  return (
    <View style={{display: "flex", gap: 10}}>
      <Text>Aktualny klucz: {data}</Text>
      <TextInput
              onChangeText={newText => setText(newText)}/>
      <Button title="Dodaj nowy klucz" onPress={() =>{addKey()}} />
      <Button title="Usuń klucz" onPress={() =>{deleteKey()}} />
    </View>
  );
}
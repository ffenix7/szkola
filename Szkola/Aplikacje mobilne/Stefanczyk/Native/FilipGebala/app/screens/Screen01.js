import { View, Text, Button, FlatList, StyleSheet, TextInput } from "react-native";
import VaultCard from "../components/VaultCard";
import React from "react";
import * as SecureStore from "expo-secure-store";

export default function Screen01({navigation}) {
  const [newVaultName, setNewVaultName] = React.useState("")
  const [value, setValue] = React.useState([])
  const [key, setKey] = React.useState("");
  
    React.useEffect(() => {
      fetch("http://192.168.119.103:3000/data")
        .then(response => response.json())
        .then(data => {
          console.log(data);
          setValue(data)
        })
    }, [])
    
    React.useEffect(() => {
        async function loadData() {
          console.log("start");
          let temp = await SecureStore.getItemAsync("key");
          setKey(temp);
        }
        loadData();
        const unsubscribe = navigation.addListener("focus", () => {
          console.log("start i każdy powrót");
        });
        return unsubscribe;
      }, [navigation]);

    async function addNewVault() {
      let result = await SecureStore.getItemAsync("key");
      if(result){
      fetch("http://192.168.119.103:3000/data", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          location: newVaultName
        })
      })
      .then(res => res.json())
      .then(newVault => {
        setValue(prev => [...prev, newVault])
        setNewVaultName("")
      })
      }
      else{
        alert("Ustaw klucz!")
      }

    }

  return (
    <View>
      <TextInput
        placeholder="Nowa nazwa sejfu"
        value={newVaultName}
        onChangeText={setNewVaultName}
      />
      <Button title="rejestruj"  onPress={() =>{addNewVault()}}/>
      <FlatList
      data={value}
      renderItem={({ item }) => <VaultCard props={{title: item.location, level: item.securityLevel}}></VaultCard>}
      keyExtractor={(item) => item.id}
      >
      </FlatList>
      <VaultCard props={{title:"Tytul", level:"Mid"}}  />
      <Button title="Zarządzaj kluczem" onPress={() => navigation.navigate("s2")} /> 
    </View>
  );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: 'lightblue',
        justifyContent: 'center',
    },
});
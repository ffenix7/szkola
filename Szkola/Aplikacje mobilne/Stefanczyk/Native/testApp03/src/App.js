import { StatusBar } from 'expo-status-bar';
import * as React from 'react';
import { Image, StyleSheet, Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import Screen01 from './screens/Screen01';
import Screen02 from './screens/Screen02';
import Screen03 from './screens/Screen03';
import Plus from "../assets/plus.png"
import {
 DrawerContentScrollView,
 DrawerItemList,
 DrawerItem
} from '@react-navigation/drawer';


const Drawer = createDrawerNavigator();

function CustomDrawerContent(props) {
  return (
    <DrawerContentScrollView {...props}>
      <DrawerItem
      label="Notatki"
      icon={() => <Image />}
      onPress={() => props.navigation.navigate("Screen02")}
      />
      
      <DrawerItem
      label="Dodaj notatkę"
      icon={() => <Image />}
      onPress={() => props.navigation.navigate("Screen01")}
      />

      <DrawerItem
      label="Dodaj kategorię"
      icon={() => <Image />}
      onPress={() => props.navigation.navigate("Screen03")}
      />

      <DrawerItem
      label="Info"
      icon={() => <Image />}
      onPress={() => console.log("Info")}
      />
    </DrawerContentScrollView>
  );
}

export default function App() {
  return (
    <NavigationContainer>
        <Drawer.Navigator drawerContent={(props) => <CustomDrawerContent {...props} />}>
            <Drawer.Screen name="Screen01" component={Screen01}  />
            <Drawer.Screen name="Screen02" component={Screen02} />
            <Drawer.Screen name="Screen03" component={Screen03} />
        </Drawer.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

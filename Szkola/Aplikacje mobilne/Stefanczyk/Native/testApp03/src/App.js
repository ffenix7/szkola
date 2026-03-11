import { StatusBar } from 'expo-status-bar';
import * as React from 'react';
import { Image, StyleSheet, Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import Screen1 from './screens/Screen01';
import Screen2 from './screens/Screen02';
import Plus from "../assets/plus.png"



const Drawer = createDrawerNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Drawer.Navigator >
        <Drawer.Screen name="S1" component={Screen1} options={{
          drawerIcon: () => (
            <Image style={{ width: 100, height: 100 }} source={Plus} />)}} />
        <Drawer.Screen name="S2" component={Screen2} />
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

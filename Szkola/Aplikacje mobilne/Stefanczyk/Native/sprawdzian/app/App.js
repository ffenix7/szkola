import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import Screen01 from "./screens/Screen01"
import Screen02 from "./screens/Screen02"


const Stack = createNativeStackNavigator();

function App() {
  return (
        <NavigationContainer>
            <Stack.Navigator>
                <Stack.Screen name="s1" component={Screen01}  />
                <Stack.Screen name="s2" component={Screen02}  />               
            </Stack.Navigator>
        </NavigationContainer>
  );
}

export default App;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

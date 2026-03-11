import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import Screen1 from "./screens/Screen01.jsx"
import Screen2 from "./screens/Screen02.jsx"

const Stack = createNativeStackNavigator();

function App() {
 return (
 <NavigationContainer>
    <Stack.Navigator>
        <Stack.Screen name="s1" component={Screen1} />
        <Stack.Screen name="s2" component={Screen2} /> 
    </Stack.Navigator>
 </NavigationContainer>
 );
}

export default App;
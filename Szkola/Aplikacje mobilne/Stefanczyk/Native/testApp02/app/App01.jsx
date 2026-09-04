import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import Screen1 from './screens/Screen01.jsx';
import Screen2 from './screens/Screen02.jsx';
import Screen3 from './screens/Screen03.jsx';

const Stack = createNativeStackNavigator();

const headerOptions = {
    headerStyle: { backgroundColor: '#4f5dff' },
    headerTintColor: '#ffffff',
    headerTitleAlign: 'center',
};

function App() {
    return (
        <NavigationContainer>
            <Stack.Navigator initialRouteName="Register">
                <Stack.Screen
                    name="Register"
                    component={Screen1}
                    options={{ headerShown: false }}
                />
                <Stack.Screen
                    name="Admin"
                    component={Screen2}
                    options={{ title: 'admin page', ...headerOptions }}
                />
                <Stack.Screen
                    name="Details"
                    component={Screen3}
                    options={{ title: 'details page', ...headerOptions }}
                />
            </Stack.Navigator>
        </NavigationContainer>
    );
}

export default App;
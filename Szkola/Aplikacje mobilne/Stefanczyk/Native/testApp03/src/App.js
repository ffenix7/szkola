import React, { useState } from 'react';
import { Alert, Image, StyleSheet } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import {
  DrawerContentScrollView,
  DrawerItem,
} from '@react-navigation/drawer';

import Plus from '../assets/plus.png';
import ServerConfigDialog from './Components/ServerConfigDialog';
import Screen01 from './screens/Screen01';
import Screen02 from './screens/Screen02';
import Screen03 from './screens/Screen03';
import Screen04 from './screens/Screen04';
import CalendarScreen from './screens/CalendarScreen';

const Drawer = createDrawerNavigator();

function CustomDrawerContent(props) {
  const { openServerDialog } = props;

  return (
    <DrawerContentScrollView {...props}>
      <DrawerItem
        label="Notatki"
        icon={() => null}
        onPress={() => props.navigation.navigate('Screen02')}
      />

      <DrawerItem
        label="Dodaj notatkę"
        icon={() => (
          <Image source={Plus} style={styles.drawerIcon} />
        )}
        onPress={() => props.navigation.navigate('Screen01')}
      />

      <DrawerItem
        label="Dodaj kategorię"
        icon={() => (
          <Image source={Plus} style={styles.drawerIcon} />
        )}
        onPress={() => props.navigation.navigate('Screen03')}
      />

      <DrawerItem
        label="Kalendarz"
        icon={() => null}
        onPress={() =>
          props.navigation.navigate('CalendarScreen')
        }
      />

      <DrawerItem
        label="Adres serwera"
        icon={() => null}
        onPress={openServerDialog}
      />

      <DrawerItem
        label="Info"
        icon={() => null}
        onPress={() =>
          Alert.alert('Info', 'Autor: Filip Gębala')
        }
      />
    </DrawerContentScrollView>
  );
}

export default function App() {
  const [dialogVisible, setDialogVisible] = useState(false);

  return (
    <>
      <NavigationContainer>
        <Drawer.Navigator
          initialRouteName="Screen02"
          drawerContent={(props) => (
            <CustomDrawerContent
              {...props}
              openServerDialog={() => setDialogVisible(true)}
            />
          )}
        >
          <Drawer.Screen
            name="Screen01"
            component={Screen01}
            options={{ title: 'Dodaj notatkę' }}
          />
          <Drawer.Screen
            name="Screen02"
            component={Screen02}
            options={{ title: 'Notatki' }}
          />
          <Drawer.Screen
            name="Screen03"
            component={Screen03}
            options={{ title: 'Dodaj kategorię' }}
          />
          <Drawer.Screen
            name="Screen04"
            component={Screen04}
            options={{ title: 'Edytuj notatkę' }}
          />
          <Drawer.Screen
            name="CalendarScreen"
            component={CalendarScreen}
            options={{ title: 'Kalendarz' }}
          />
        </Drawer.Navigator>
      </NavigationContainer>

      <ServerConfigDialog
        visible={dialogVisible}
        onClose={() => setDialogVisible(false)}
      />
    </>
  );
}

const styles = StyleSheet.create({
  drawerIcon: {
    width: 22,
    height: 22,
    resizeMode: 'contain',
  },
});

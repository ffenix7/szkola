import { FlatList, Image, StyleSheet, Text, View } from 'react-native';
import * as React from 'react';
import { useEffect } from 'react';

import MyButton from '../Components/MyButton';
import settings from '../Settings.json';

const Screen02 = ({ navigation }) => {
  const [users, setUsers] = React.useState([]);
  const baseUrl = `${settings.address}:${settings.port}`;

  const loadUsers = async () => {
    try {
      const response = await fetch(`${baseUrl}/users`);
      const data = await response.json();
      setUsers(Array.isArray(data) ? data : []);
    } catch (error) {
      setUsers([]);
    }
  };

  useEffect(() => {
    // initial load
    loadUsers();

    const unsubscribe = navigation.addListener('focus', () => {
      loadUsers();
    });

    return unsubscribe;
  }, [navigation]);

  const handleDelete = async (index) => {
    try {
      await fetch(`${baseUrl}/users/${index}`, { method: 'DELETE' });
      loadUsers();
    } catch (error) {
      console.error('Error deleting user:', error);
    }
  };

  const renderItem = ({ item, index }) => (
    <View style={styles.row}>
      <View style={styles.avatarWrap}>
        <Image
          source={require('../assets/icon.png')}
          style={styles.avatar}
        />
      </View>
      <View style={styles.rowInfo}>
        <Text style={styles.rowText}>{index}: {item.username}</Text>
        <View style={styles.rowButtons}>
          <MyButton
            text="DETAILS"
            color="#4f5dff"
            onPress={() => navigation.navigate('Details', { index })}
          />
          <MyButton
            text="DELETE"
            color="#4f5dff"
            onPress={() => handleDelete(index)}
          />
        </View>
      </View>
    </View>
  );

  return (
    <View style={styles.container}>
      <View style={styles.topButton}>
        <MyButton
          text="BACK TO LOGIN PAGE"
          color="#4f5dff"
          onPress={() => navigation.navigate('Register')}
        />
      </View>
      <FlatList
        data={users}
        keyExtractor={(_, index) => index.toString()}
        renderItem={renderItem}
        contentContainerStyle={styles.list}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f7f7f7',
  },
  topButton: {
    marginTop: 14,
    alignItems: 'center',
  },
  list: {
    paddingVertical: 20,
    paddingHorizontal: 18,
    gap: 18,
  },
  row: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 16,
  },
  avatarWrap: {
    width: 70,
    height: 70,
    borderRadius: 35,
    borderWidth: 2,
    borderColor: '#4f5dff',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#ffffff',
  },
  avatar: {
    width: 36,
    height: 36,
    tintColor: '#4f5dff',
  },
  rowInfo: {
    flex: 1,
  },
  rowText: {
    color: '#666666',
    marginBottom: 8,
    fontSize: 14,
  },
  rowButtons: {
    flexDirection: 'row',
    gap: 14,
    alignItems: 'center',
  },
});

export default Screen02;
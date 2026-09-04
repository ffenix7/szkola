import { Alert, StyleSheet, Text, TextInput, View } from 'react-native';
import * as React from 'react';

import MyButton from '../Components/MyButton';
import settings from '../Settings.json';

const Screen01 = ({ navigation }) => {
  const [username, setUsername] = React.useState('');
  const [password, setPassword] = React.useState('');
  const [loading, setLoading] = React.useState(false);

  const baseUrl = `${settings.address}:${settings.port}`;

  const handleRegister = async () => {
    if (!username || !password) {
      Alert.alert('Alert', 'Fill in login and password');
      return;
    }

    try {
      setLoading(true);
      const response = await fetch(`${baseUrl}/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
      });

      if (response.status === 409) {
        Alert.alert('Alert', 'server response\nUSEREXISTS');
        return;
      }

      if (!response.ok) {
        Alert.alert('Alert', 'server response\nERROR');
        return;
      }

      setUsername('');
      setPassword('');
      navigation.navigate('Admin');
    } catch (error) {
      Alert.alert('Alert', 'server response\nERROR');
    } finally {
      setLoading(false);
    }
  };

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Register App</Text>
        <Text style={styles.subtitle}>Sign in to continue</Text>
      </View>
      <View style={styles.form}>
        <TextInput
          placeholder="Login"
          value={username}
          onChangeText={setUsername}
          style={styles.input}
          autoCapitalize="none"
        />
        <TextInput
          placeholder="Password"
          value={password}
          onChangeText={setPassword}
          style={styles.input}
          secureTextEntry
        />
        <MyButton
          text={loading ? 'PLEASE WAIT' : 'REGISTER'}
          color="#4f5dff"
          onPress={handleRegister}
          disabled={loading}
        />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#ffffff',
  },
  header: {
    height: 230,
    backgroundColor: '#4f5dff',
    borderBottomLeftRadius: 160,
    borderBottomRightRadius: 160,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    color: '#ffffff',
    fontSize: 30,
    fontWeight: '600',
  },
  subtitle: {
    marginTop: 6,
    color: '#ffd36b',
    fontSize: 14,
    fontWeight: '600',
  },
  form: {
    marginTop: 70,
    alignItems: 'center',
    gap: 20,
  },
  input: {
    width: 220,
    borderBottomWidth: 1.5,
    borderBottomColor: '#4f5dff',
    paddingVertical: 6,
    fontSize: 16,
    textAlign: 'center',
  },
});

export default Screen01;
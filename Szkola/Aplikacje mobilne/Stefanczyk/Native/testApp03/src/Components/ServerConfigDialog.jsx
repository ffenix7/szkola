import React, { useEffect, useState } from 'react';
import { Alert } from 'react-native';
import Dialog from 'react-native-dialog';

import {
  DEFAULT_SERVER_CONFIG,
  getServerConfig,
  saveServerConfig,
} from '../utils/storage';

const ServerConfigDialog = ({ visible, onClose }) => {
  const [ip, setIp] = useState(
    DEFAULT_SERVER_CONFIG.ip
  );
  const [port, setPort] = useState(
    DEFAULT_SERVER_CONFIG.port
  );

  useEffect(() => {
    const loadConfig = async () => {
      const config = await getServerConfig();
      setIp(config.ip);
      setPort(config.port);
    };

    if (visible) {
      loadConfig();
    }
  }, [visible]);

  const saveConfig = async () => {
    const cleanIp = ip.trim();
    const cleanPort = port.trim();
    const portNumber = Number(cleanPort);

    if (
      !cleanIp ||
      !Number.isInteger(portNumber)
    ) {
      Alert.alert(
        'Błąd',
        'Podaj poprawny adres IP/host i port serwera.'
      );
      return;
    }

    await saveServerConfig({
      ip: cleanIp,
      port: cleanPort,
    });

    Alert.alert('Sukces', 'Adres serwera zapisany.');
    onClose();
  };

  return (
    <Dialog.Container visible={visible}>
      <Dialog.Title>Adres serwera</Dialog.Title>
      <Dialog.Description>
        Podaj IP lub host oraz port serwera Express.
      </Dialog.Description>
      <Dialog.Input
        label="IP / host"
        value={ip}
        onChangeText={setIp}
        autoCapitalize="none"
        autoCorrect={false}
      />
      <Dialog.Input
        label="Port"
        value={port}
        onChangeText={setPort}
        keyboardType="number-pad"
      />
      <Dialog.Button label="Anuluj" onPress={onClose} />
      <Dialog.Button label="Zapisz" onPress={saveConfig} />
    </Dialog.Container>
  );
};

export default ServerConfigDialog;

import { Pressable, StyleSheet, Text, View } from 'react-native';
import React from 'react';

const MyButton = ({ text, color, onPress, disabled = false }) => {
  return (
    <View style={styles.wrapper}>
      <Pressable
        onPress={onPress}
        disabled={disabled}
        style={({ pressed }) => [
          styles.button,
          { backgroundColor: color },
          pressed && !disabled ? styles.buttonPressed : null,
          disabled ? styles.buttonDisabled : null,
        ]}
      >
        <Text style={styles.text}>{text}</Text>
      </Pressable>
    </View>
  );
};

const styles = StyleSheet.create({
  wrapper: {
    alignItems: 'center',
  },
  button: {
    paddingVertical: 8,
    paddingHorizontal: 22,
    borderRadius: 16,
    minWidth: 110,
    alignItems: 'center',
  },
  buttonPressed: {
    opacity: 0.85,
  },
  buttonDisabled: {
    opacity: 0.6,
  },
  text: {
    color: '#ffffff',
    fontWeight: '600',
    fontSize: 13,
    letterSpacing: 0.5,
  },
});

export default MyButton;
import { Button, View } from 'react-native';
import React from 'react';

const MyButton = ({ text, color, onPress }) => {
  return (
    <View>
      <Button 
        title={text}
        color={color}
        onPress={onPress}
      />
    </View>
  );
};

export default MyButton;
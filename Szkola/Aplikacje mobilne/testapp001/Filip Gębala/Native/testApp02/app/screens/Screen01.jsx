import { Text, View, TextInput } from 'react-native';
import MyButton from '../Components/MyButton';
import * as React from 'react';


const Screen01 = ({ navigation }) => {
  const [text, setText] = React.useState('')
  return (
    <View>
      <Text> Screen 1 </Text>
      <TextInput
        placeholder="Login"
        onChangeText={newText => setText(newText)}
        defaultvalue={text}
      />
    </View>
  );
};

export default Screen01;
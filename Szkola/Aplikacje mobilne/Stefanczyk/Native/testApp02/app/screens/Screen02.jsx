import { Button, Text, View } from 'react-native';

const Screen02 = ({ navigation }) => {
  return (
    <View>
      <Text> Screen 2 </Text>
      <Button 
        title="Click" 
        onPress={() => navigation.navigate("s1")} 
      />
    </View>
  );
};

export default Screen02;
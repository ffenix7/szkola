import { StyleSheet, Text, View } from 'react-native'
import React from 'react'

const VaultCard = ({props}) => {
  console.log(props)
  return (
    <View style={styles.container}>
      <Text>{props.title}</Text>
      <Text>Poziom: {props.level}</Text>
    </View>
  )
}

export default VaultCard

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: 'lightblue',
        justifyContent: 'center',
        margin: 10,
        alignItems: "center"
    },
});
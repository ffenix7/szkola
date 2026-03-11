import { View, StyleSheet, Text } from "react-native"

const Component = (props) => {
    const styles = StyleSheet.create({
        text: { fontSize: 48, color: props.fontcolor},
        color: {backgroundColor: props.color, flex: 1},
    });

    return (
    <View style={styles.color}>
        <Text style={styles.text}> {props.text} </Text>
    </View>
    )
}


export default Component
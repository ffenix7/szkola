import { View, StyleSheet, Text } from "react-native"

const Content = () => {
    return (
    <View style={styles.container}>
        <Text style={styles.text}> Content </Text>
    </View>
    )
}

const styles = StyleSheet.create({
    text: { fontSize: 48, },
    container: { flex: 1, backgroundColor: "#00FF00" }
});

export default Content
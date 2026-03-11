import { View, StyleSheet, Text } from "react-native"

const Footer = () => {
    return (
    <View style={styles.container}>
        <Text style={styles.text}> Footer </Text>
    </View>
    )
}

const styles = StyleSheet.create({
    text: { fontSize: 48, },
    container: { flex: 1, backgroundColor: "#0000FF" }
});

export default Footer
import { View, StyleSheet, Text } from "react-native"

const Header = () => {
    return (
    <View style={styles.container}>
        <Text style={styles.text}> Header </Text>
    </View>
    )
}

const styles = StyleSheet.create({
    text: { fontSize: 48, },
    container: { flex: 1, backgroundColor: "#FF0000" }
});

export default Header
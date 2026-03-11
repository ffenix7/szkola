import { StyleSheet, Text, View, StatusBar } from 'react-native';
import Component from "./Components/Component.jsx"

export default function App() {
    return (
        <View style={styles.container}>
            <Component text="item=1" color="red" />
            <Component text="item=2" color="blue" />
            <Component text="item=3" color="green" />

            <StatusBar />
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#FFFFFF',
        justifyContent: 'center',
    }
});
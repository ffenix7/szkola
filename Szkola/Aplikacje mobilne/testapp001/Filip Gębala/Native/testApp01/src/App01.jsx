import { StyleSheet, Text, View, StatusBar } from 'react-native';

import Header from "./Components/Header"
import Content from "./Components/Content"
import Footer from "./Components/Footer"

export default function App() {
    return (
        <View style={styles.container}>
            <Header />
            <Content />
            <Footer />

            <StatusBar />
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#FFFFFF',
        justifyContent: 'center',
    },
    red: {
        color: 'red',
        backgroundColor: 'blue',
    },
});
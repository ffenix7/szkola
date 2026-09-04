import { StyleSheet, Text, View, StatusBar } from 'react-native';
import Component from "./Components/Component.jsx"

export default function App() {
    const styles = StyleSheet.create({
        container: {
            flex: 1,
            backgroundColor: '#FFFFFF',
            justifyContent: 'center',
        }
    });

    const colors = ["red", "yellow", "blue", "orange", "green", "purple"]
    const objects = colors.map((item, index) => {
        return <Component key={index} text={`item=${index}`} color={item} />
    })
    return (
        <View style={styles.container}>
            {objects}

            <StatusBar />
        </View>
    );
}

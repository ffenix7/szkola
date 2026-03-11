import { StyleSheet, Text, View, StatusBar } from 'react-native';
import Component from "./Components/Component.jsx"

export default function App() {
    const styles = StyleSheet.create({
        container: {
            flex: 1,
            backgroundColor: '#FFFFFF',
            justifyContent: 'center',
            flexDirection: "column"
        },
        containerReverse: {
            flex: 1,
            backgroundColor: '#FFFFFF',
            justifyContent: 'center',
            flexDirection: "column-reverse",
        }
    });

    const colors = ["red", "yellow", "blue", "orange", "green", "purple"]

    return (
        <View style={styles.container}>
                {
                    colors.map((item, index) => {
                        return <Component key={index} text={`item=${index + 1}`} color={item} fontcolor={'black'} />
                    })
                }

            <StatusBar />
        </View>
    );
}

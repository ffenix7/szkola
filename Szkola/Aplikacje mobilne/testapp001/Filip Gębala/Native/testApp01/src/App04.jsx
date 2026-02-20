import { StyleSheet, Text, View, StatusBar } from 'react-native';
import Component from "./Components/Component.jsx"

export default function App() {
    const styles = StyleSheet.create({
        twoColumns: {
            flex: 1,
            flexDirection: "row"
        },
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
    
    const objects2 = colors.reverse().map((item, index) => {
        return <Component key={index} text={`item=${index}`} color={item} />
    })

    return (
        <View style={styles.twoColumns}>
            <View style={styles.container}>
                {objects}
            </View>

            <View style={styles.container}>
                {objects2}
            </View>
            
            <StatusBar />
        </View>
    );
}

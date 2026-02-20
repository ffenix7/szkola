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
        },
        containerReverse: {
            flex: 1,
            backgroundColor: '#FFFFFF',
            justifyContent: 'center',
            flexDirection: "column-reverse",
        }
    });

    const colors = ["red", "yellow", "blue", "orange", "green", "purple"]
    
    const objects = colors.map((item, index) => {
        return <Component key={index} text={`item=${index+1}`} color={item} fontcolor={'white'} />
    })

    const objects2 = colors.map((item, index) => {
        return <Component key={index} text={`item=${index+1}`} color={item} fontcolor={'black'} />
    })

    return (
        <View style={styles.twoColumns}>
            <View style={styles.container}>
                {objects}
            </View>

            <View style={styles.containerReverse}>
                {objects2}
            </View>
            
            <StatusBar />
        </View>
    );
}

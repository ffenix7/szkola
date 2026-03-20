import { Image, StyleSheet, Text, View } from 'react-native';
import * as React from 'react';
import { useEffect } from 'react';

import settings from '../Settings.json';

const formatDate = (value) => {
    if (!value) {
        return '-';
    }

    const date = new Date(value);
    if (Number.isNaN(date.getTime())) {
        return '-';
    }

    const pad = (part) => part.toString().padStart(2, '0');
    return `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())} ${pad(date.getHours())}:${pad(date.getMinutes())}:${pad(date.getSeconds())}`;
};

const Screen03 = ({ route }) => {
    const { index } = route.params || {};
    const [user, setUser] = React.useState(null);
    const baseUrl = `${settings.address}:${settings.port}`;

    useEffect(() => {
        const loadUser = async () => {
            try {
                const response = await fetch(`${baseUrl}/users/${index}`);
                const data = await response.json();
                setUser(data);
            } catch (error) {
                setUser(null);
            }
        };

        if (index !== undefined && index !== null) {
            loadUser();
        }
    }, [baseUrl, index]);

    return (
        <View style={styles.container}>
            <View style={styles.avatarWrap}>
                <Image
                    source={require('../assets/icon.png')}
                    style={styles.avatar}
                />
            </View>
            <Text style={styles.label}>login:</Text>
            <Text style={styles.value}>{user?.username ?? '-'}</Text>
            <Text style={styles.label}>password:</Text>
            <Text style={styles.value}>{user?.password ?? '-'}</Text>
            <Text style={styles.label}>registered:</Text>
            <Text style={styles.date}>{formatDate(user?.createdAt)}</Text>
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#f7f7f7',
        alignItems: 'center',
        paddingTop: 36,
    },
    avatarWrap: {
        width: 130,
        height: 130,
        borderRadius: 65,
        borderWidth: 2,
        borderColor: '#4f5dff',
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: '#ffffff',
        marginBottom: 16,
    },
    avatar: {
        width: 70,
        height: 70,
        tintColor: '#4f5dff',
    },
    label: {
        color: '#666666',
        fontSize: 14,
        marginTop: 10,
    },
    value: {
        color: '#4f5dff',
        fontSize: 18,
        fontWeight: '600',
        marginTop: 2,
    },
    date: {
        color: '#4f5dff',
        fontSize: 16,
        fontWeight: '600',
        marginTop: 4,
    },
});

export default Screen03;

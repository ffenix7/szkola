import { useState } from 'react';
import Item from './Item07';

const App = () => {
    const [items, setItems] = useState([1, 2, 3]);

    function showDialog(idx) {
        const choice = confirm("Usunąć ten element?");
        if (choice) {
            setItems(items => items.filter((_, i) => i !== idx));
        }
    }

    return (
        <>
            {items.map((item, idx) => (
                <Item key={item} showDialog={() => showDialog(idx)} />
            ))}
        </>
    );
};

export default App;
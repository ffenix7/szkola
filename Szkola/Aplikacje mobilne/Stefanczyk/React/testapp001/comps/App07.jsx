import { useState } from 'react';
import Item from './Item07';

const App = () => {
    const [items, setItems] = useState([1, 2, 3]);
    const [toDelete, setToDelete] = useState(null); 

    function requestDelete(idx) {
        setToDelete(idx);
    }

    function handleDelete() {
        setItems(items => items.filter((_, i) => i !== toDelete));
        setToDelete(null);
    }

    function handleCancel() {
        setToDelete(null);
    }

    return (
        <>
            {items.map((item, idx) => (
                <Item key={item} showDialog={() => requestDelete(idx)} />
            ))}
            {toDelete !== null && (
                <div style={{position: 'fixed', top: 0, left: 0, width: '100vw', height: '100vh', background: 'rgba(0,0,0,0.3)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 1000}}>
                    <div style={{background: 'white', padding: 24, borderRadius: 8, boxShadow: '0 2px 8px rgba(0,0,0,0.2)'}}>
                        <p>Czy na pewno usunąć ten element?</p>
                        <button onClick={handleDelete} style={{marginRight: 8}}>Usuń</button>
                        <button onClick={handleCancel}>Anuluj</button>
                    </div>
                </div>
            )}
        </>
    );
};

export default App;
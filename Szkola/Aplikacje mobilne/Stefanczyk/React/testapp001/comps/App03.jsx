import { useActionState, useState } from 'react';
import Item from './Item03.jsx'

const App = () => {


 // visible - wartość do zmieniania za pomocą useState()
 // setVisible - funkcja dokonująca zmiany
 // true - początkowa wartość visible

    const [visible, setVisible] = useState(true)
    const[text, setText] = useState('aaa')
    const[value, setValue] = useState(1)

    return (
        <div id='container'>        
            <h2>USESTATE()</h2>
                <div className='app'>
                    <button onClick={() => setVisible(true)}>visible</button>
                    <button onClick={() => setVisible(false)}>invisible</button>
                    <Item visible={visible} />
                </div>
                <div className='app'>
                    <button onClick={() => setText('aaa')}>set to aaa</button>
                    <button onClick={() => setText('bbb')}>set to bbb</button>
                    <Item text={text} visible={'true'} />
                </div>
                <div className='app'>
                    <button onClick={() => setValue(5)}>set to 5</button>
                    <button onClick={() => setValue(10)}>set to 10</button>
                    <button onClick={() => setValue(value+1)}>add 1</button>     
                    <button onClick={() => setValue(value-1)}>sub 1</button>                    
                    <button onClick={() => setValue(value*value)}>power</button>                    

                    <Item visible={'true'} value={value}/>
                </div>
        </div>
    );
}

export default App
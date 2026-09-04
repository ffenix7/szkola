import React from "react";

const AddTaskForm = (props) =>{
    const options = props.options;

    const handleRange = (event) =>{
        changeDays(event.target.value)
    }

    const handleSubmit = (e) =>{
        e.preventDefault();
    }

    const[days,changeDays] = React.useState(0);
    return(
    <div id="AddTaskForm">
            <form onSubmit={handleSubmit}>
                <h3>Dodaj nowe zadanie</h3>
                <label>Wybierz projekt docelowy:</label><br></br>
                <select>
                    {options}
                </select><br></br>
                <label>Nazwa zadania:</label><br></br>
                <input></input><br></br>
                <label>Dni do końca:<p className="addtaskformp">Pozostało: {days} dni</p></label>
                <input type="range" max='20' min='-20' value={days} onChange={handleRange}></input><br></br>
                <button type="submit" id="AddTaskButton">Dodaj zadanie</button>
            </form>
    </div>
    )
}

export default AddTaskForm;
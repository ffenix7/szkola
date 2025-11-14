const AddProjectForm = () =>{

    const handleSubmit = (e) =>{
        e.preventDefault();
    }

    const newProject = (props) =>{
        const name = props.name
        return
    }

    return(
        <div id="AddProjectForm">
            <form onSubmit={handleSubmit}>
                <h3>Dodaj nowy projekt</h3>
                <label>Nazwa projektu:</label><br></br>
                <input></input><br></br>
                <button type="submit" id="AddProjectButton" onClick={newProject}>Utwórz projekt</button>
            </form>
        </div>
    )
}

export default AddProjectForm;
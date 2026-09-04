const ProjectRow = (props) => {
    const name = props.name
    let status = props.status
    const id = props.id
    const dni = props.dniDoTerminu
    console.log(props)
    let info = status



    if(status==="Do zrobienia" && dni < 0){
        info=`Opóźnione o: ${Math.abs(dni)} dni`
        status = "Opóźnione o"
    }
    else{
        info=`Do terminu: ${dni}`
        status="Do zrobienia"
    }

    let color = (status==="Do zrobienia") ? "green" : "red"
    console.log(color)
    if(dni==0){
        color = "yellow"
        info = "Termin: Dziś"
    }
    return (
        <div>
            <p>{name}</p>
            <p className={color}>{info}</p>
            <select>
                <option selected={status === "Do zrobienia"}>Do zrobienia</option>
                <option selected={status === "Ukończone"}>Ukończone</option>
            </select>
        </div>
    )
}

export default ProjectRow;
const Item = (props) =>{
    const {title, info} = props
    
    const showAll = () =>{
        alert("title " + title + "\ninfo " + info)
    }

    const showTitle = () =>{
        alert("title " + title)
    }

    return(
        <div className="item">
            <h1>{title}</h1>
            <h3>{info}</h3>
            <button onClick={showAll}>Show all props</button>
            <button onClick={showAll}>Show title</button>
        </div>
    )
}

export default Item
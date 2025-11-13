const Avatar = (props) =>{
    return(
        <div className='avatar'>
            <img src={props.icon} alt={props.name}></img>
            <h4>{props.name}</h4>
            <hr></hr>
            <p>'{props.title}'</p>
            <p className="tags">{props.tags}</p>
            <p className="hp">{props.hp}</p>
            <p className="speed">{props.speed}</p>
        </div>
    )
}

export default Avatar;
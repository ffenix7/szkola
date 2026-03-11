const Avatar = (props) =>{
    return(
        <div className='avatar'>
            <h2>{props.name}</h2>
            <p>{props.name}</p>
            <p>{props.title}</p>
            <img src={props.icon} alt={props.name}></img>
        </div>
    )
}

export default Avatar;
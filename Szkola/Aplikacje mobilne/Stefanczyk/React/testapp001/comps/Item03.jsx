const Item = (props) => {
    let {visible, text, value, bg} = props
    
    if (visible){
        visible = "block"
    }
    else{
        visible = "none"
    }

    if(!text && value){
        text = value
    }

    if (value==0){
        text = '0'
    }

    if(!text && !value){
        text = 'Item 01'
    }

    return (
        <div style={{display: visible}}>
            <h1>{text}</h1>
        </div> 
)
}

export default Item
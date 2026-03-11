const Item01 = () => {

    const showAlert = () =>{
        alert("test")
    }

    return(
        <>
            <div>
                <h2>Item01</h2>
                <button onClick={showAlert}>
                    show alert
                </button>
            </div>
        </>
    )
} 

export default Item01
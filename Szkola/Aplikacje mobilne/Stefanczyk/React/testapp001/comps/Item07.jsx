const Item = (props) => {
    const num = Math.random() * 1000;
    return (
        <div className="item">
            <h2>ITEM</h2>
            <p>{num}</p>
            <button onClick={props.showDialog}>Show dialog</button>
        </div>
    );
};

export default Item;
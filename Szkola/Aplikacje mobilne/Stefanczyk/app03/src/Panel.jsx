const Panel = (props) =>{
    const RoleFilter = props.role;
    const HpFilter = props.hp;
    const SetRoleFilter = props.setRole;
    const SetHpFilter = props.setHp;
    const ViewConfig = props.viewConfig;
    const SetViewConfig = props.setViewConfig;
    const ResultCount = props.resultCount;

    

    return(
        <div>
            <h2>Opcje filtrowania</h2>
            <div>
                <h3>1.Filtruj po roli</h3>
                <select>
                    <option value="all">Wszystkie</option>
                    <option value="tank">Tank</option>
                    <option value="healer">Healer</option>
                    <option value="dps">DPS</option>
                </select>
            </div>
            <div>
                <h3>2.Filtruj po hp</h3>
                <button type="radio" name="hp" value="all">Wszystkie</button>
                <button type="radio" name="hp" value="low">Niskie 0-550HP</button>
                <button type="radio" name="hp" value="medium">Średnie 550-600HP</button>
                <button type="radio" name="hp" value="high">Wysokie 600+</button>
            </div>
            <div>
                <h3>3.Konfiguracja widoku</h3>
                <button type="checkbox">Pokaż tytuł</button>
                <button type="checkbox">Pokaż role</button>
                <button type="checkbox">Pokaż HP</button>
                <button type="checkbox">Pokaż speed</button>
            </div>
            <div>
                <p>
                    Liczba wyników: {ResultCount}
                </p>
            </div>
        </div>
    )
}

export default Panel;
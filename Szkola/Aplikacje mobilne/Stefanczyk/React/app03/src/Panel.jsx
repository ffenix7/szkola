const Panel = (props) => {
    // Oczekiwane propsy:
    // role, hp, setRole, setHp, viewConfig, setViewConfig, resultCount
    const RoleFilter = props.role;
    const HpFilter = props.hp;
    const SetRoleFilter = props.setRole;
    const SetHpFilter = props.setHp;
    const ViewConfig = props.viewConfig || {};
    const SetViewConfig = props.setViewConfig;
    const ResultCount = props.resultCount;

    const onRoleChange = (e) => {
        SetRoleFilter(e.target.value);
    };

    const onHpChange = (e) => {
        SetHpFilter(e.target.value);
    };

    const toggleView = (key) => {
        SetViewConfig({ ...ViewConfig, [key]: !ViewConfig[key] });
    };

    return (
        <div>
            <h2>Opcje filtrowania</h2>
            <div>
                <h3>1. Filtruj po roli</h3>
                <select value={RoleFilter} onChange={onRoleChange}>
                    <option value="all">Wszystkie</option>
                    <option value="Tank">Tank</option>
                    <option value="Fighter">Fighter</option>``
                    <option value="Mage">Mage</option>
                    <option value="Assassin">Assassin</option>
                    <option value="Support">Support</option>
                </select>
            </div>
            <div>
                <h3>2. Filtruj po hp</h3>
                <label>
                    <input type="radio" name="hp" value="all" checked={HpFilter === 'all'} onChange={onHpChange} />
                    Wszystkie
                </label>
                <label>
                    <input type="radio" name="hp" value="low" checked={HpFilter === 'low'} onChange={onHpChange} />
                    Niskie 0-550HP
                </label>
                <label>
                    <input type="radio" name="hp" value="medium" checked={HpFilter === 'medium'} onChange={onHpChange} />
                    Średnie 550-600HP
                </label>
                <label>
                    <input type="radio" name="hp" value="high" checked={HpFilter === 'high'} onChange={onHpChange} />
                    Wysokie 600+
                </label>
            </div>
            <div>
                <h3>3. Konfiguracja widoku</h3>
                <label>
                    <input type="checkbox" checked={ViewConfig.showTitle} onChange={() => toggleView('showTitle')} /> Pokaż tytuł
                </label>
                <label>
                    <input type="checkbox" checked={ViewConfig.showRole} onChange={() => toggleView('showRole')} /> Pokaż role
                </label>
                <label>
                    <input type="checkbox" checked={ViewConfig.showHp} onChange={() => toggleView('showHp')} /> Pokaż HP
                </label>
                <label>
                    <input type="checkbox" checked={ViewConfig.showSpeed} onChange={() => toggleView('showSpeed')} /> Pokaż speed
                </label>
            </div>
            <div>
                <p>Liczba wyników: {ResultCount}</p>
            </div>
        </div>
    );
};

export default Panel;
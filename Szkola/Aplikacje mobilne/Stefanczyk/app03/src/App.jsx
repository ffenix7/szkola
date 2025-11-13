import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import json from './avatars.json'
import Panel from './Panel.jsx'
import Avatar from './Avatar.jsx'

function App() {
  const[RoleFilter, setRoleFilter] = useState('all');
  const[hpFilter, setHpFilter] = useState('all');
  const[viewConfig, setViewConfig] = useState({
    showTitle: true,
    showRole: true,
    showHp: true,
    showSpeed: true
  });

  const filtered = json.filter(avatar =>{
    let roleMatch = (RoleFilter === 'all' || avatar.tags.some(tag => tag === RoleFilter));
    let hpMatch = false;

    if(hpFilter === 'all'){
      hpMatch = true;
    } else if(hpFilter === 'low' && avatar.stats.hp >= 0 && avatar.stats.hp <= 550){
      hpMatch = true;
    } else if(hpFilter === 'medium' && avatar.stats.hp > 550 && avatar.stats.hp <= 600){
      hpMatch = true;
    } else if(hpFilter === 'high' && avatar.stats.hp > 600){
      hpMatch = true;
    }
  
    return roleMatch && hpMatch;
  })

  return (
    <div>
      <Panel
        role={RoleFilter}
        setRole={setRoleFilter}
        hp={hpFilter}
        setHp={setHpFilter}
        viewConfig={viewConfig}
        setViewConfig={setViewConfig}
        resultCount={filtered.length}
      />
      <div className='avatar-container'>
        {filtered.map((element) => {
          return (
            <Avatar
              key={element.id}
              name={element.name}
              title={element.title}
              icon={element.icon}
              tags={element.tags.join(', ')}
              hp={element.stats.hp}
              speed={element.stats.movespeed}
            />
          )
        })}
      </div>
    </div>
  )
}

export default App

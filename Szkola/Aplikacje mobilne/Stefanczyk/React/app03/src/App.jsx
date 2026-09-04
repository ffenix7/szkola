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

  const filterAvatars = (list, roleFilter, hpFilter) => {
    return list.filter(avatar => {
      const roleMatch = roleFilter === 'all' || avatar.tags.includes(roleFilter);

      let hpMatch = true;
      if (hpFilter === 'all') {
        hpMatch = true;
      } else if (hpFilter === 'low') {
        hpMatch = avatar.stats.hp >= 0 && avatar.stats.hp <= 550;
      } else if (hpFilter === 'medium') {
        hpMatch = avatar.stats.hp > 550 && avatar.stats.hp <= 600;
      } else if (hpFilter === 'high') {
        hpMatch = avatar.stats.hp > 600;
      }

      return roleMatch && hpMatch;
    });
}

  const filtered = filterAvatars(json, RoleFilter, hpFilter);
  console.log("git")
  return (
    <div>
      <Panel
        role={RoleFilter}
        hp={hpFilter}
        setRole={setRoleFilter}
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

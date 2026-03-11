import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import json from './avatars.json'
import Avatar from './Avatar.jsx'

const App = () => {
  const avatars = json;
  
  return(

    <div className="App">
      {avatars.map((avatar, index) => {
        return <Avatar key={index} name={avatar.name} title={avatar.title} icon={avatar.icon} />
      })}
    </div>
)

}
export default App

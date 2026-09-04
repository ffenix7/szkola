import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import AddProjectForm  from './AddProjectForm'
import AddTaskForm from './AddTaskForm'
import ProjectCard from './ProjectCard'
import json from './dane.json'

function App() {
  const [count, setCount] = useState(0)
  const [project, setProjects] = useState(0)

  const createNewProject = (props) =>{
    const name = props.name
    return(
      <ProjectCard key={index} id={element.id} name={element.name} tasks={element.tasks} />
    )
  }

  return (
    <>
      <h1>Sprawdzian - system zarządzania projektami</h1>
      <div id="main">
        <aside id='leftPanel'>
          <AddProjectForm newProject={createNewProject}/>
          <AddTaskForm options={json} />
        </aside>
        <aside>
          {json.map((element, index)=>{
            return <ProjectCard key={index} id={element.id} name={element.name} tasks={element.tasks} />
          })}
        </aside>
      </div>
    </>

  )
}

export default App

import json from './dane.json'
import TaskItem from './TaskItem'

const ProjectCard = (props) =>{
    const id = props.id
    const name = props.name
    const tasks = props.tasks
    const count = props.tasks.length
    console.log(count)
    return(
        <div className='ProjectCard'>
            <h2>{name}</h2>
            {tasks.map((element, index) =>{
                console.log(element)
                return <TaskItem key={index} name={element.name} status={element.status} id={element.id} dniDoTerminu={element.dniDoTerminu} />
            })}
        </div>
    )
}

export default ProjectCard;
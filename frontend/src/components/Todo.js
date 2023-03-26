import React from "react";


const TODOItem = ({todo, deleteTodo}) => {
    return (
        <tr>
            <td>{todo.project}</td>
            <td>{todo.text}</td>
            <td>{todo.created}</td>
            <td>{todo.author}</td>
            <td>{todo.is_active}</td>
            <td><button onClick={()=>deleteTodo(todo.id)} type='button'>Delete</button></td>
        </tr>
    )
}

const TODOList = ({todos, deleteTodo}) => {
    return (
        <table border="1">
            <tr>
                <th>Project</th>
                <th>Text</th>
                <th>Created</th>
                <th>Author</th>
                <th>Active</th>
                <th></th>
            </tr>
            {todos.map((todo) => <TODOItem todo={todo} deleteTodo={deleteTodo}/>)}
        </table>
    )
}
export default TODOList

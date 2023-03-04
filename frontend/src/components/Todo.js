import React from "react";


const TODOItem = ({todo}) => {
    return (
        <tr>
            <td>{todo.project.name}</td>
            <td>{todo.text}</td>
            <td>{todo.created}</td>
            <td>{todo.author}</td>
            <td>{todo.is_active}</td>

        </tr>
    )
}

const TODOList = ({todos}) => {
    return (
        <table border="1">
            <tr>
                <th>Project</th>
                <th>Text</th>
                <th>Created</th>
                <th>Author</th>
                <th>Active</th>
            </tr>
            {todos.map((todo) => <TODOItem todo={todo}/>)}
        </table>
    )
}
export default TODOList

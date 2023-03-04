import React from "react";


const ProjectItem = ({ project }) => {
    return (
        <tr>
            <td>{project.name}</td>
            <td>{project.authors}</td>
            <td>{project.repository}</td>

        </tr>
    )
}

const ProjectList = ({ projects }) => {
    return (
        <table border="1">
            <tr>
                <th>Name</th>
                <th>Authors</th>
                <th>Repository</th>
            </tr>
            {projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}
export default ProjectList

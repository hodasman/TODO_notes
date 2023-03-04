import React from 'react';
import logo from './logo.svg';
import axios from 'axios'
import { HashRouter, Route, BrowserRouter, Switch, Link } from 'react-router-dom'

// import Footer from './components/Footer.js'
// import Navbar from './components/Menu.js'
import UserList from './components/User.js'
import ProjectList from './components/Project.js'
import TODOList from './components/Todo.js'
import NotFound404 from './components/NotFound404.js'


const DOMAIN = 'http://127.0.0.1:8000/api/'
const get_url = (url => `${DOMAIN}${url}`)

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': [],
      'projects': [],
      'todos': []
    }
  }

  componentDidMount() {
    axios.get(get_url('users/')).then(response => {
      this.setState({ 'users': response.data.results })
    }).catch(error => console.log(error))

    axios.get(get_url('projects/')).then(response => {
      this.setState({ 'projects': response.data.results })
    }).catch(error => console.log(error))

    axios.get(get_url('todo/')).then(response => {
      this.setState({ 'todos': response.data.results })
    }).catch(error => console.log(error))
  }

  render() {
    return (
      <div className="App">
        <BrowserRouter>

          <nav>
            <ul>
              <li>
                <Link to='/'>Project</Link>
              </li>
              <li>
                <Link to='/users'>Users</Link>
              </li>
              <li>
                <Link to='/todos'>TODO</Link>
              </li>
            </ul>
          </nav>
          <Switch>
            <Route exact path='/' component={() => <ProjectList projects={this.state.projects} />} />
            <Route exact path='/users' component={() => <UserList users={this.state.users} />} />
            <Route exact path='/todos' component={() => <TODOList todos={this.state.todos} />} />

            <Route component={NotFound404} />
          </Switch>
        </BrowserRouter>
      </div>

    )
  }
}


export default App;
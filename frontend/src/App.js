import React from 'react';
import logo from './logo.svg';
import axios from 'axios'

import Footer from './components/Footer.js'
import Navbar from './components/Menu.js'
import Userlist from './components/User.js'


const DOMAIN = 'http://127.0.0.1:8000/api/'
const get_url = (url => `${DOMAIN}${url}`)

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'navbarItems': [
        {name: 'users', href: '/todo'},
      ],
      users: []
    }
  }

  componentDidMount() {
    axios.get(get_url('users')).then(response => {
      this.setState({users: response.data})
    }).catch(error => console.log(error))
  }

  render() {
    return (
      <div>
        <header>
          <Navbar navbarItems={this.state.navbarItems}/>
        </header>
        <div className='container'>
          <Userlist users={this.state.users}/>
        </div>
        <Footer/>
      </div>
    
    )
  }
}


export default App;
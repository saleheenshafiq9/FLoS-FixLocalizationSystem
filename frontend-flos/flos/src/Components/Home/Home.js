import React from 'react'
import './Home.css'


const Home = () => {
  return (
    <div>
        <nav class="navbar">
          <div class="container">
            <a class="navbar-brand" href="/">
                <img src="./logo.png" alt="Bootstrap" width="100" height="100"/>
            </a>
            <ul class="navbar-nav">
              <li class="nav-item">
                <a class="nav-link" aria-current="page" href="/about">About</a>
              </li>
            </ul>
          </div>
        </nav>
      <div className='container home-body'>
        <div class="row">
          <div className='col-6 app-title'>
            <b>FLoS: Fix <br></br>Localization System</b>
            <p className='app-desc'>The “Fix Localisation System” (FLoS) will be a web application that automates the testing process for localisation in a mobile application. It will handle localisation for both text and media content (audio, video & image).</p>
            <div className='row feature-list'>
              <div className='col-4'>
                <img src='./project.png' alt='project' width='50' height='50' id='feature-img'/>
                Project Management
              </div>
              <div className='col-4'>
                <img src='./report.png' alt='project' width='50' height='50' id='feature-img'/>
                Report Generation
              </div>
              <div className='col-4'>
                <img src='./fix.png' alt='project' width='50' height='50' id='feature-img'/>
                Localization Fix
              </div>
            </div>
          </div>
          <div className='col-6'>
            <div class="card shadow-sm">
              <b className='login-title'>Sign In</b>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Home

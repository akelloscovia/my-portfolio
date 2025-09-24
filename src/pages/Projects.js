import React from "react";
import "../App.css";

function Projects() {
  return (
    <div className="projects-page">
      <h1>My Projects</h1>

      <div className="projects-container">
        <div className="project-box">
          <p>
            <strong>Project 1:</strong></p>
             <p>Portfolio Website - A personal portfolio built with React
            showcasing my skills, projects, and experience.
          </p>
        </div>

        <div className="project-box">
          <p>
            <strong>Project 2:</strong> </p>
            <p>Task Manager App - A web application to manage daily
            tasks and deadlines using React and Firebase.
          </p>
        </div>

        <div className="project-box">
          <p>
           <strong> Project 3:</strong></p>
           <p> Weather App - A small app that fetches weather data from
            an API and displays it dynamically based on user location.
          </p>
        </div>

        <div className="project-box">
          <p>
           <strong>Project 4:</strong></p> 
           <p>Blog Platform - A simple blog where users can read and
            post articles, built with React and Node.js.
          </p>
        </div>
      </div>
    </div>
  );
}

export default Projects;

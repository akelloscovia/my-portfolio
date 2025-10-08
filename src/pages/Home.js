import React from "react";
import "../App.css"; // make sure the path is correct
import myPhoto from "../images/WhatsApp Image 2025-09-23 at 14.31.29_5dc3d42d.jpg"; // <-- add your image in src/assets and adjust the path
function Home() {
  return (
    <div className="home-page">
      {/* Left side image */}
      <div className="image-section">
        <img src={myPhoto} alt="Akello Scovia Emaru" className="side-image" />
      </div>

      {/* Right side content */}
      <div className="content-section">
        <h1>Welcome to My Portfolio</h1>
        <p>
          Hello, I am <strong>Akello Scovia Emaru</strong>, a Computer Science
          student at the Women's Institute of Technology and Information.
        </p>
        <p>
          I am passionate about technology, coding, and building solutions that
          can make life easier for people. This portfolio showcases my skills,
          projects, and journey in the tech world.
        </p>
      </div>
    </div>
  );
}

export default Home;

import React from "react";
import "../App.css";

function Contact() {
  return (
    <div className="center-page">
      <div className="yellow-box">
        <h1>Contact Me</h1>
        <p>
          Email:{" "}
          <a href="mailto:akelloscovia907@gmail.com">
            akelloscovia907@gmail.com
          </a>
        </p>
        <p>
          LinkedIn:{" "}
          <a
            href="https://linkedin.com/in/scovia"
            target="_blank"
            rel="noreferrer"
          >
            linkedin.com/Akello Scovia
          </a>
        </p>
        <p>
          Twitter:{" "}
          <a
            href="https://twitter.com/scovia"
            target="_blank"
            rel="noreferrer"
          >
            twitter.com/akelloscovia907
          </a>
        </p>
        <p>
          GitHub:{" "}
          <a
            href="https://github.com/akelloscovia"
            target="_blank"
            rel="noreferrer"
          >
            github.com/akelloscovia
          </a>
        </p>
      </div>
    </div>
  );
}

export default Contact;

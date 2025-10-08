import React from "react";
import "../App.css";
import { FaWhatsapp, FaPhoneAlt } from "react-icons/fa";

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
          <p>
        {/* WhatsApp */}
        <a
          href="https://wa.me/256780740749"
          target="_blank"
          rel="noopener noreferrer"
          className="whatsapp-link"
        ></a>
      <FaWhatsapp className="icon whatsapp" /> +256 780 740 749
        </p>
<p>
        {/* Direct Call */}
        <a href="tel:+256780740749" className="call-link">
          <FaPhoneAlt className="icon call" /> +256 780 740 749
        </a>
      </p>
      </div>
    </div>
  );
}

export default Contact;

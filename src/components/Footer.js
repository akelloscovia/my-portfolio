import "../App.css";


export default function Footer() {
  return (
    <footer>
      &copy; {new Date().getFullYear()} Akello Scovia Emaru
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
            linkedin.com Akello Scovia
          </a>
        </p>
        <p>
          Twitter:{" "}
          <a
            href="https://twitter.com @AkelloScov907"
            target="_blank"
            rel="noreferrer"
          >
            twitter.com @akelloscovia907
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
    </footer>
  );
}

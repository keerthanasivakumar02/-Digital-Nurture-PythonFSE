function Header(props) {
  return (
    <header>

      <h1>{props.siteName}</h1>

      <p>
        Enrolled Courses: {props.enrolledCount}
      </p>

      <nav>
        <a href="#">Home</a>
        <a href="#">Courses</a>
        <a href="#">Profile</a>
      </nav>

    </header>
  );
}

export default Header;
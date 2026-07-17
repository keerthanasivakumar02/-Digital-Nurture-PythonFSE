function CourseCard(props) {

  return (
    <div className="course-card">

      <h3>{props.name}</h3>

      <p><strong>Code:</strong> {props.code}</p>

      <p><strong>Credits:</strong> {props.credits}</p>

      <p><strong>Grade:</strong> {props.grade}</p>

      <button
        onClick={() =>
          props.onEnroll({
            id: props.id,
            name: props.name,
            code: props.code,
            credits: props.credits,
            grade: props.grade,
          })
        }
      >
        Enroll
      </button>

    </div>
  );

}

export default CourseCard;
import React from "react";
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <div className="container mt-5">
      <div className="jumbotron">
        <h1 className="display-4">Welcome to Blog Lyfe</h1>
        <p className="lead">
          We make all kinds of awesome blog about various topics.
        </p>
        <hr className="my-4" />
        <p>Click the button below to check out our awesome blog.</p>
        <Link className="btn btn-primary btn-lg" to="/blog" role="button">
          Check out our Blog
        </Link>
      </div>
    </div>
  );
};

export default Home;

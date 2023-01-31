import React from "react";
import './Home.css'

const Login = () => {
  return (
    <div>
      <div class="card shadow-sm">
        <b className="login-title">Sign In</b>
        <form>
          <div className="mb-3">
            <input
              type="email"
              className="form-control"
              placeholder="Email Address"
              style={{
                backgroundColor: "#038F8F",
                color: "#FDFFF7",
                width: "300px",
                margin: "auto"
              }}
            />
          </div>
          <div className="mb-3 inputs">
            <input
              type="password"
              className="form-control"
              placeholder="Password"
              style={{
                backgroundColor: "#038F8F",
                color: "#FDFFF7",
                width: "300px",
                margin: "auto"
              }}
            />
          </div>
          <div className="mb-3">
            <div className="custom-control custom-checkbox">
              <input
                type="checkbox"
                className="custom-control-input"
                id="customCheck1"
                style={{
                    backgroundColor: "#038F8F",
                    color: "#FDFFF7",
                    marginLeft: "115px",
                    marginRight: "10px"
                  }}
              />
              <label className="custom-control-label" htmlFor="customCheck1">
                Remember me
              </label>
            </div>
          </div>
          <div className="d-grid">
            <button type="submit" className="btn btn-primary">
              Submit
            </button>
          </div>
          <p className="forgot-password text-right">
            Forgot <a href="#">password?</a>
          </p>
        </form>
      </div>
    </div>
  );
};

export default Login;

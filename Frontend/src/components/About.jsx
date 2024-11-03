import React from "react";
import { motion } from "framer-motion";
import Katman from "../assets/img/katman.svg";

function About() {
  return (
    <>
      <motion.div
        initial={{ x: -100, opacity: 0 }}
        animate={{ x: 0, opacity: 1 }}
        transition={{ duration: 0.5 }}
        className="about_section"
      >
        <h3 className="about_staff">About us</h3>
        <motion.div
          initial={{ y: -100, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ duration: 0.5 }}
        >
          <div className="content_staff">
            <div className="content_staff1">
              <div className="left_side">
                <p>
                  TrackXpert Monitor is an innovative card management system
                  designed specifically for educational institutions. Our
                  platform streamlines various school operations, enhancing both
                  security and efficiency. With TrackXpert, students gain access
                  to a seamless experience that integrates their identification
                  and access needs into a single, smart card solution.
                </p>
              </div>
              <div className="right_side">
                <div className="rate_star">
                  <img src={Katman} alt="star staff" />
                  <p className="rate">Rate it</p>
                </div>
              </div>
            </div>
            <div className="conten_staff2">
              <div className="about_benefit">
                <p>Benefits for Schools and Students:</p>
                <ul>
                  <li>
                    <h5>Increased Efficiency:</h5> By automating processes like
                    attendance tracking and library management, TrackXpert
                    reduces administrative burdens, allowing staff to focus on
                    teaching and student engagement.
                  </li>
                  <li>
                    <h5>Improved Safety:</h5>The ability to monitor access
                    points enhances overall campus security. Parents can feel
                    confident knowing that their children are safe within school
                    grounds.
                  </li>
                  <li>
                    <h5>User-Friendly Interface:</h5>Both students and staff
                    will find the TrackXpert system intuitive and easy to use.
                    Our platform is designed with user experience in mind,
                    ensuring a smooth transition to digital management.
                  </li>
                  <li>
                    <h5>Data Insights:</h5>Schools can gain valuable insights
                    through data collected via the TrackXpert system. This
                    information helps in making informed decisions regarding
                    student engagement and resource allocation.
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </motion.div>
      </motion.div>
    </>
  );
}

export default About;

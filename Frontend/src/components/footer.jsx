import React from "react";
import { motion } from "framer-motion";
import {
  BsFillEnvelopeFill,
  BsFillGeoAltFill,
  BsFillPhoneFill,
  BsFacebook,
  BsInstagram,
  BsTwitterX,
  BsLinkedin,
} from "react-icons/bs";
import Button from "../components/Button";
import Logo from "../assets/img/logosvg.svg";

function footer() {
  return (
    <>
      <footer class="footer">
        <motion.div
          initial={{ x: -100, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          transition={{ duration: 0.5 }}
          class="container"
        >
          {/* <div className="footer_logo">
            <img src={Logo} alt="logon" />
          </div> */}
          <div class="footer-bottom">
          <div className="social_media_staff">
           <a href="#" class="social-link">
                  <BsFacebook />
                </a>
                <a href="#" class="social-link">
                  <BsInstagram />
                </a>
                <a href="#" class="social-link">
                  <BsTwitterX />
                </a>
                <a href="#" class="social-link">
                  <BsLinkedin />
                </a>
          </div>
            <p>
              &copy; {new Date().getFullYear()} TrackXpert Monitor. All rights
              reserved.
            </p>
          </div>
        </motion.div>
      </footer>
      
    </>
  );
}

export default footer;

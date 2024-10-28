import React from "react";
import { motion } from "framer-motion";
import Logo from "../assets/img/logosvg.svg";
import CarStaff from '../assets/img/card.svg';

function Jumbotron() {
  return (
    <>
    <div className="w-full main_staff">
      <div className="flex gap-1 bottom_staff">
        {/* Animate the right staff content */}
        <motion.div
          className="right_staff flex gap-2"
          initial={{ x: 100, opacity: 0 }} 
          animate={{ x: 0, opacity: 1 }} 
          transition={{ duration: 0.5 }} 
        >
          <div className="flex-1 gap-1 inner_staff">
            <h2>Welcome To</h2>
            <img src={Logo} alt="TrackXpert logo." />
          </div>
          <p>
            Introducing "Positions" - a beautiful and functional landing page
            designed specifically for digital marketing agencies. With its clean
            and modern design, Positives is the perfect template to showcase your agency's services and case studies to potential clients.
          </p>
          <a href="/auth/login/"><button className="btn_staff p-1 text-center">Get started</button></a>
        </motion.div>

        {/* Animate the card image */}
        <motion.div
          className="p-1 light_staff"
          initial={{ x: -100, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }} 
          transition={{ duration: 0.5 }} 
        >
          <img src={CarStaff} alt="card staff" className="w-full img_card" />
        </motion.div>
      </div>
    </div>
      <div className="divider"></div>
    </>
  );
}

export default Jumbotron;
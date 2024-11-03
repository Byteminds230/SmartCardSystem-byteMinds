import React from "react";
import { motion } from "framer-motion";
import Logo from "../assets/img/logosvg.svg";
import CarStaff from '../assets/img/card.svg';
import LeftDiv from '../assets/img/bgimg.svg'
import leftTop from '../assets/img/Ellipse.svg'


function Jumbotron() {
  return (
    <>
    <div className="w-full main_staff">
      <motion.div 
      initial={{x: -100, opacity:0}}
      animate={{x:0, opacity:1}}
      transition={{duration: 0.5}}
      className="background_images_card"
      >
          <div className="background_images">
            <div className="right_image">
            <img src={LeftDiv} alt="logo staff"  className='image1'/>
            </div>
          </div>
      </motion.div>
      <div className="flex gap-0 bottom_staff">
        <motion.div
          className="right_staff flex gap-2"
          initial={{ x: 100, opacity: 0 }} 
          animate={{ x: 0, opacity: 1 }} 
          transition={{ duration: 2 }} 
        >
          <div className="flex gap-0 inner_staff">
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
        {/* <motion.div
          className="p-1 light_staff"
          initial={{ x: -100, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }} 
          transition={{ duration: 0.5 }} 
        >
          <img src={CarStaff} alt="card staff" className="w-full img_card" />
        </motion.div>  */}
        <motion.div
      className="p-1 light_staff"
      initial={{ y:0}} 
      animate={{
        y: [0, -5, 0], 
      }}
      transition={{
        duration: 0.8, 
        ease: "easeOut",
        repeat: Infinity, 
        repeatType: "reverse",
      }}
      whileHover={{
        scale: 1, 
        y: [0, 1, 0], 
      }}
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

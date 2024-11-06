import React from 'react'
import '../assets/css/main.css';
import Navbar from '../components/Navbar';
import Jumbtron from '../components/Jumbtron';
import HowItworks from '../components/HowItworks';
import Whyimportant from '../components/whyImportant';


function Mainpage() {
   
  return (
   <>
    <section id='/nav_list'>
        <Navbar />
    </section>
    <section id='/jumbtron'>
      <Jumbtron />
    </section>
    <section id='/howitworks'>
    <HowItworks />
    </section>
    <section>
    <Whyimportant />
    </section>
   </>
  )
}

export default Mainpage
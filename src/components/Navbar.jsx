import React from 'react'
import '../assets/css/main.css';
import Logo from '../assets/img/logosvg.svg'


function Navbar() {
    const listNav = [
        {id:'1', name:'How it works', path:'#howitworks'},
        {id:'2',name:'About us', path:'#about'},
        {id:'3',name:'Contact', path:'#contact'},
        {id:'4',name:'Portfolio', path:'#portfolio'},
        {id:'5',name:'Documentation', path:'/documentation'},
    ]
  return (
    <>
    <nav className=' min-h-screen min-w-min flex-1 gap-1 bg-black'>
        <div className="p-1 right_logo">
            <a href="/"><img src={Logo} alt="the TrackXpert Logo" /></a>
        </div>
        <div className="p-1 nav_list">
           {listNav.map((item,id)=>(
            <ul key={id} >
                <a href={item.path}><li>{item.name}</li></a>
            </ul>
           ))}
        </div>
        <div className='flex gap-1'>
            <a href='/auth/login/'><button className='left_button'>Get in account</button></a>
        </div>
    </nav>
   </>
  )
}

export default Navbar
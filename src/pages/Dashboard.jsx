import React,{Suspense} from 'react'
import axios from 'axios'
import { useState,useEffect } from 'react'
import { Link,Outlet } from 'react-router-dom'
import {motion} from 'framer-motion'

function Dashboard() {
  const [users , setUsers] = useState([]);
  const [setting,setSetting] =useState('');
  useEffect(()=>{
    const fetchData = async()=>{
      try{
        const data = await axios.get("http://localhost:8000/users/")
        const res = await data.data;
        setUsers(res)
        console.log(res)
      }catch(error){
        console.error(error)
      }
    }
    fetchData()
  } ,[])
  
  const handleOnChange =()=>{

  }

return(
  <>
  <div className='flex gap-2'>
  <div className='flex gap-0'>
      <head>
        <nav>
          <div>
            <img src={users.profile} alt="this is the profile." />
          </div>
        </nav>
      </head>
      <aside className='bg-blue-700 p-1 h-[100vh] w-10/42 text-white font-bold bottom-3'>
      <ul className="menu bg-base-200 rounded-box">
  <li>
    <a className="tooltip tooltip-right" data-tip="Home">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        className="h-5 w-5"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor">
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="2"
          d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
      </svg>
    </a>
  </li>
  <li>
    <a className="tooltip tooltip-right bg-transparent" data-tip="Details">
      <Link to='/dashboard'>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        className="h-5 w-5"
        fill="none"
        viewBox="0 0 24 24"
        stroke="#128512">
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="2"
          d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
      </svg>
      </Link>
    </a>
  </li>
  <li>
    <a className="tooltip tooltip-right" data-tip="Stats">
      <Link to='/dashboard/settings'>
    
      <svg
        xmlns="http://www.w3.org/2000/svg"
        className="h-5 w-5"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor">
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="2"
          d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
      </svg>
      </Link>
    </a>
  </li>
</ul>
      </aside>
      <Suspense fallback={<p>loading..</p>}>
        <div className='flex-1 gap-1 bg-slate-400 p-3 w-full h-[20vh]'>{
          users.map((user , index)=>{
            return <div key={index} className='mr-5'>{user.name}</div>
      })
      }</div>
      </Suspense>
    </div>
    <Outlet/>
<motion.div
initial={{ opacity: 1, scale: 0.5, x:100 }}
animate={{ opacity: 2, scale: 1 }}
transition={{ duration: 0.5 }}
className='p-10 bg-gray-50'
>

  <p className='text-blue-900'>hello guys </p>
  <h4 className='text-blue-900'>this is the main page</h4>

</motion.div>
  </div>
  </>
)
}

export default Dashboard
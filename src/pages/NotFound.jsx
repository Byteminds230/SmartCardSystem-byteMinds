import React from 'react'
import { Link } from 'react-router-dom'

function NotFound() {
  return (
    <>
    <div className='bg-blue-600 w-full p-10 h-[60vh]'>
    <div className='text-center mt-24 font-bold text-[4.5vw] text-slate-900 '>Page Not Found 404</div>
    <p className='align-middle justify-center text-center mt-5 object-fill'>&#128512;</p>
    </div>
    <div className='mt-5 p-2 text-[1.5vw] text-center'>
      <Link to='/' className='max-sm:hover:text-blue-700'>
          go back to main menu
      </Link>
    </div>
    </>
    
  )
}

export default NotFound
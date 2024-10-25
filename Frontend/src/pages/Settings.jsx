import React from 'react'
import 'tailwindcss/tailwind.css';

function Settings() {
  return (
    <>
    <div className='flex gap-1 p-3 flex-row h-[10rem]'>
      <div className='w-[10rem] rounded-sm bg-gray-200  p-2 text-center'>
        <h2 className='text-2xl font-bold'>45<span>%</span></h2>
        <p className='text-[1vw] w-[9rem]'>this is to say the way</p>
      </div>
      <div className='w-[10rem] rounded-sm bg-gray-200 p-2 text-center'>
        <h2 className='text-2xl font-bold '>45<span>%</span></h2>
        <p className='text-[1vw] w-[9rem]'>this is to say the way</p>
      </div>
      <div className='w-[10rem] rounded-sm bg-gray-200 p-2 text-center justify-center '>
      <div className="radial-progress text-blue-900" style={{"--value":80}} role="progressbar">50%</div>
      </div>      
    </div>
    </>
  )
}

export default Settings
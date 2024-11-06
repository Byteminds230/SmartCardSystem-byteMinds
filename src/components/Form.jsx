import React, { useState } from 'react'

const Forms = () => {
    const [name, setName] = useState("")
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [email, setEmail] = useState("")
    const [address, setAddress] = useState("")
    const [error , setError] = useState("")

    const handleSubmit = (e) => {
        e.preventDefault()
        console.log(name.length)
       if(name.length < 20){
        let error_message = "username characters not enough"
        setError(error_message)
        setName("")
       }
}

  return (
    <div className='min-h-screen w-full bg-slate-00 flex items-center justify-center'>
        <div className='bg-white p-10 px-20 rounded-xl shadow-md'>
            <form action="" className='flex flex-col gap-y-3 items-center' onSubmit={handleSubmit} >
            <div className="head py-3">
                <h1 className='font font-bold text-6xl text-blue-600'>Form</h1>
            </div>
                <div className='flex flex-col gap-y-2 items-center justify-center'>
                <input type="text" className={`input bg-white border border-slate-400 ${error.length > 0  ? "border border-red-500" : ""}`}  placeholder='enter the name'  value={name} onChange={(e) => setName(e.target.value)}/>
                {
                    error.length > 0 && <p className='text-red-500 text-sm'>{error}</p>
                }
                <input type="text" className='input bg-white border border-slate-400'  placeholder='enter the username' value={username} onChange={(e) => setUsername(e.target.value)}/>
                <input type="password"  className='input bg-white border border-slate-400' placeholder='enter the password' value={password} onChange={(e) => setPassword(e.target.value)}/>
                <input type="text"  className='input bg-white border border-slate-400' placeholder='enter the email' value={email} onChange={(e) => setEmail(e.target.value)}/>
                <input type="text"  className='input bg-white border border-slate-400' placeholder='enter the address' value={address} onChange={(e) => setAddress(e.target.value)}/>
                </div>
                <div>
                    <button type="submit" className="btn btn-outline btn-primary w-full">Submit</button>
                </div>
            </form>
        </div>
    </div>
  )
}

export default Forms;
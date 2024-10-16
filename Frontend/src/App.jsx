import axios from 'axios'
import { useEffect, useState } from 'react'
const App = ()=>{
  const [users , setUsers] = useState([])
  useEffect(()=>{
    axios.get('http://localhost:8000/users/')
    .then((response)=>{
      setUsers(response.data)
    })
  } ,[])
  

return(
  <>
  <p className="text-blue-500">frank akunda mama we </p>
<<<<<<< HEAD
  <p className="md:text-center font-bold text-slate-900">sure se niko bimeze but riba aribyo much respect</p>
=======
  <p>{
    users.map((user , index)=>{
      return <p key={index}>{user.name}</p>
    })
    }</p>
>>>>>>> fc8b70a9706e4dfa40a3a6e03c7d1ee96864ee4d
  </>
)
}

export default App

// this is the basic sample to fetch the api is from the backend : by frank
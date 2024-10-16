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
  <p>{
    users.map((user , index)=>{
      return <p key={index}>{user.name}</p>
    })
    }</p>
  </>
)
}

export default App

// this is the basic sample to fetch the api is from the backend : by frank
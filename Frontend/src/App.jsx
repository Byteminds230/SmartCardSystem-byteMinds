import axios from 'axios'
import { useEffect, useState } from 'react'
const App = ()=>{
  const [users , setUsers] = useState([])
  useEffect(()=>{
    
    const fetchData = async()=>{
      try{
        const data = await axios.get('http://localhost:8000/users/')
        const res = await data.json();
        setUsers(res)
        console.log(res)
      }catch(error){
        console.error(error)
      }
    }
    fetchData()
  } ,[])
  

return(
  <>
  <p>Frank</p>
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
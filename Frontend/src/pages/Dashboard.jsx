// my_api_key='you_have_to_try'
// import React from 'react'
// function Dashboard() {
//   const [users , setUsers] = useState([])
//   useEffect(()=>{
//     const fetchData = async()=>{
//       try{
//         const data = await axios.get(`http://localhost:8000/users/?api_key{process.env.my_api_key}`)
//         const res = await data.json();
//         setUsers(res)
//         console.log(res)
//       }catch(error){
//         console.error(error)
//       }
//     }
//     fetchData()
//   } ,[])
  

// return(
//   <>
//   <p>{
//     users.map((user , index)=>{
//       return <p key={index}>{user.name}</p>
//     })
//     }</p>
//   </>
// )
// }

// export default Dashboard



import React from 'react'

function Dashboard() {
  return (
    <div className='text-slate-900 text-center'>Dashboard</div>
  )
}

export default Dashboard
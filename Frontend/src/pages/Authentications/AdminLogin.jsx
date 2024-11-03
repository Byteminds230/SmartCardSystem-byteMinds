// import React, { useEffect, useState } from 'react';

// function AdminLogin() {
//     const [data, setData] = useState([]);
//     const [isLoading, setIsLoading] = useState(true); // Set loading to true initially
//     const BASE_URL = 'http://127.0.0.1:8000';

//     useEffect(() => {
//         const fetchData = async () => {
//             try {
//                 const response = await fetch(`${BASE_URL}/users`); // Use Fetch API to get data
//                 if (!response.ok) {
//                     throw new Error('Network response was not ok');
//                 }
//                 const result = await response.json(); // Await the JSON parsing
//                 console.log(result); // Log the result
//                 setData(result); // Set the data state with the response data
//             } catch (e) {
//                 console.error('Fetch error:', e); // Log any errors
//             } finally {
//                 setIsLoading(false); // Set loading to false after fetching
//             }
//         };
//         fetchData();
//     }, []);

//     if (isLoading) {
//         return <p>Loading...</p>; // Display loading message
//     }

//     return (
//         <div>
//             {data.map((user,id) => (
//                 <h3 key={id}>{user.email}</h3> // Render user emails
//             ))}
//         </div>
//     );
// }

// export default AdminLogin;

// import React, { useEffect, useState } from "react";
// import { useContext,createContext } from "react";
// function AdminLogin() {
//   const [data, setData] = useState([]);
//   const [isLoading, setIsLoading] = useState(false); // Set loading to true initially
//   const [username, setUsername] = useState("");
//   const [password, setPassword] = useState("");
//   const [errorMessage, setErrorMessage] = useState("");
//   const BASE_URL = "http://localhost:8000";

//   // Function to handle login
//   const handleLogin = async (e) => {
//     e.preventDefault(); // Prevent default form submission
//     // Here you would typically send the username and password to your backend for validation.
//     // For this example, let's assume a simple check:
//     if (username === "admin" && password === "password") {
//       // Replace with real authentication logic
//       fetchData(); // Fetch user data if login is successful
//     } else {
//       setErrorMessage("Invalid username or password");
//     }
//   };

//   useEffect(() => {
//     // Function to fetch user data
//     const fetchData = async () => {
//       try {
//         const response = await fetch(`${BASE_URL}/users`, {
//           // Content_Type:'application/json',
//           // method:'POST',
//         }); // Use Fetch API to get data
//         if (!response.ok) {
//           throw new Error("Network response was not ok");
//         }
//         const result = await response.json();
//         console.log(result);
//         setData(result);

//         return () => clearTimeout(response,result)
//       } catch (e) {
//         console.error("Fetch error:", e);
//       } finally {
//         setIsLoading(false); // Set loading to false after fetching
//       }
//     };
//     fetchData();
//   }, []);

//   if (isLoading) {
//     return <p>Loading...</p>; // Display loading message
//   }

//   return (
//     <div>
//       <h2>Admin Login</h2>
//       {errorMessage && <p style={{ color: "red" }}>{errorMessage}</p>}{" "}
//       {/* Display error message */}
//       <form onSubmit={handleLogin}>
//         <div>
//           <label>Username:</label>
//           <input
//             type="text"
//             value={username}
//             onChange={(e) => setUsername(e.target.value)}
//             required
//           />
//         </div>
//         <div>
//           <label>Password:</label>
//           <input
//             type="password"
//             value={password}
//             onChange={(e) => setPassword(e.target.value)}
//             required
//           />
//         </div>
//         <button type="submit">Login</button>
//       </form>
//       {/* Render user emails after successful login */}
//       <div>
//         {data.map((user, index) => (
//             <>
//             <div key={index}>
//             <h3 >{user.email}</h3> 
//             <p>{user.username}</p>
//             </div>
             
//             </>
//         ))}
//       </div>
//     </div>
//   );
// }

// export default AdminLogin;

import React from 'react'
import { useState,useEffect,useContext } from 'react'
import {AuthContextProvider}   from './authContext'

const AdminLogin = () => {
    const theme =useContext(AuthContextProvider)
  return (
    <div>
      <h3>{`hello ${theme}`}</h3>
    </div>
  )
}

export default AdminLogin


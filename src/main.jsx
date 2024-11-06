import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './assets/css/main.css';
import "../src/index.css"
import { BrowserRouter } from 'react-router-dom';
// require('dotenv').config()

createRoot(document.getElementById('root')).render(
  // <StrictMode>
  <BrowserRouter>
    <App />
  </BrowserRouter>
  // </StrictMode>,
)

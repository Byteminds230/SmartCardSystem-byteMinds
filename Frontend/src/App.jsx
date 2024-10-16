import React,{lazy,Suspense} from 'react'
import {Router,Routes,Route} from 'react-router-dom'

// importation of the pages nested navigations
const Dashboard = lazy(()=> import('./pages/Dashboard'));
const Settings = lazy(()=> import('./pages/Settings'));
const NotFound = lazy(()=> import('./pages/NotFound'));

function App() {
  return (
    <>
    <Suspense fallback={<p>loading...</p>}>
      <Routes>
        <Route path='/' element={<Dashboard/>} />
        <Route path='/settings' element={<Settings/>} />
        <Route path='*' element={<NotFound/>} />
      </Routes>
    </Suspense>
    </>
  )
}

export default App
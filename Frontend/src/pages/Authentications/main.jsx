import React from 'react'
import AdminLogin from './AdminLogin'
import AuthContextProvider, { ThemeContext } from './authContext'

function main() {
  return (
    <AuthContextProvider>
        <AdminLogin/>
    </AuthContextProvider>
  )
}

export default main
import React, { useState } from "react";
import { createContext } from "react";

export const ThemeContext = createContext()
// to create te theme provider 
export const AuthContextProvider = ({children}) => {
  const [theme, setTheme] = useState("light");
  return (
    <ThemeContext.Provider value={{theme,setTheme}}>
        {children}
    </ThemeContext.Provider>
  );
};

export default AuthContextProvider;

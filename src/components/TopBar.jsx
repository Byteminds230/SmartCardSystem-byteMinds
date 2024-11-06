import React from "react";
import img from "../assets/img/download.jpg";
import { FaMagnifyingGlass } from "react-icons/fa6";

const name = "Jonathan";

const TopBar = () => {
  return (
    <div className="bg-white rounded-md shadow-md p-3">
      <div className="flex items-center justify-between">
        
        {/* Left Section */}
        <div className="flex items-center gap-5">
          <img src={img} alt="User profile" className="w-10 h-10 rounded-full" />
          <h1 className="text-xl font-semibold text-slate-700">
            Welcome back, <span className="text-green-600">{name}</span>
          </h1>
        </div>
        
        {/* Right Section */}
        <div className="hidden sm:flex items-center bg-slate-200 rounded-md px-3 py-2">
          <input
            type="text"
            className="bg-transparent outline-none pr-2 w-full text-slate-700"
            placeholder="Search here..."
          />
          <FaMagnifyingGlass className="text-xl text-slate-600" />
        </div>
      </div>
    </div>
  );
};

export default TopBar;

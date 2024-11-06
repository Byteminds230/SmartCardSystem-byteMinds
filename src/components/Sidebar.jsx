// src/components/Sidebar.jsx
import React, { useState } from 'react';
import logo from '../assets/img/logoImg.png';
import { FaAlignLeft, FaBuffer, FaFileCircleQuestion, FaLock } from 'react-icons/fa6';
import { LuPencilLine, LuWalletCards } from 'react-icons/lu';
import { IoDocumentsOutline } from 'react-icons/io5';
import { MdSecurity } from 'react-icons/md';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';

const data = [
  { id: 0, title: 'Dashboard', path: '/dashboard', icon: <FaBuffer className="text-2xl" /> },
  { id: 1, title: 'Registry', path: '/registry', icon: <LuPencilLine className="text-2xl" /> },
  { id: 2, title: 'Cards', path: '/cards', icon: <LuWalletCards className="text-2xl" /> },
  { id: 4, title: 'Reports', path: '/reports', icon: <IoDocumentsOutline className="text-2xl" /> },
  { id: 5, title: 'Security', path: '/security', icon: <MdSecurity className="text-2xl" /> }
];

const subData = [
  { id: 0, title: 'Help', path: '/help', icon: <FaFileCircleQuestion className="text-2xl text-blue-800" /> },
  { id: 1, title: 'Lock Monitor', path: '/lock', icon: <FaLock className="text-2xl text-red-800" /> }
];

const Sidebar = ({ isOpen, onToggleSidebar }) => {
  const [active, setActive] = useState('Dashboard');
  const [open, setOpen] = useState(isOpen);

  const toggleSidebar = () => {
    const newOpenState = !open;
    setOpen(newOpenState);
    onToggleSidebar(newOpenState); 
  };

  return (
    <motion.div
      className={`min-h-[90vh] shadow-lg bg-white rounded-lg flex flex-col justify-between ${open ? 'w-[240px]' : 'w-[75px]'}`}
      animate={{ width: open ? '280px' : '75px' }}
      transition={{ duration: 1.0, type: 'spring' }}
    >
      {/* Top Section */}
      <div className="px-3 flex flex-col gap-y-12">
        <div className="flex items-center justify-between px-2">
          {open && <img src={logo} alt="Logo" className="block" />}
          <FaAlignLeft
            className="text-xl cursor-pointer translate-x-2 mt-5 text-slate-700"
            onClick={toggleSidebar} 
          />
        </div>

        {/* Menu Items */}
        <div className="flex flex-col gap-y-3">
          {data.map((item) => (
            <Link to={item.path} key={item.id} onClick={() => setActive(item.title)}>
              <div className={`${open ? 'flex items-center space-x-1' : ''}`}>
                <div
                  className={`bg-green-700 bg-opacity-50 w-1 h-8 rounded-lg ${active === item.title ? 'block' : 'hidden'} ${!open && 'hidden'}`}
                ></div>
                <div
                  className={`flex items-center gap-3 p-3 rounded-md cursor-pointer transition-all flex-auto text-slate-700 ${
                    active === item.title ? 'bg-green-700 text-white' : 'bg-slate-100 hover:bg-slate-200 duration-200'
                  }`}
                >
                  <div className={`${active === item.title ? 'text-white' : 'text-slate-600'}`}>
                    {item.icon}
                  </div>
                  {open && <h1 className="text-xl font-semibold">{item.title}</h1>}
                </div>
              </div>
            </Link>
          ))}
        </div>
      </div>

      {/* Bottom Section */}
      <div className="px-3 flex flex-col gap-y-3 py-5">
        {subData.map((item) => (
          <Link to={item.path} key={item.id}>
            <div className="flex items-center gap-x-3 px-5 py-3 bg-slate-200 rounded-md">
              <div className={`${!open && '-translate-x-1'}`}>{item.icon}</div>
              {open && <h1 className="font-semibold text-xl text-slate-700">{item.title}</h1>}
            </div>
          </Link>
        ))}
      </div>
    </motion.div>
  );
};

export default Sidebar;

// src/pages/Index.jsx
import React, { useState } from 'react';
import Sidebar from '../components/Sidebar';
import TopBar from '../components/TopBar';

const Index = () => {
  const [open, setOpen] = useState(true);

  const handleToggleSidebar = (isOpen) => {
    setOpen(isOpen);
  };

  return (
    <div className='min-h-screen w-full bg-slate-200 p-5 flex gap-x-5'>
      <div>
        <Sidebar isOpen={open} onToggleSidebar={handleToggleSidebar} />
      </div>
      <div className={`w-full ${open ? 'hidden' : 'block'} md:block`}>
        <TopBar />
      </div>
    </div>
  );
};

export default Index;

import React from 'react';
import { motion } from 'framer-motion'; 
import  You  from '../assets/img/you.svg'; 
import  Vector  from '../assets/img/vector.svg'; 

function HowItworks() {
    const staff = [{ name: 'How it works' }];
    const howItWorksItems = [
        {
            id: '1',
            title: 'Click Google Integration',
            desc: 'Simply log into your Google account, then seamlessly integrate and mirror your planned meeting.',

        },
        {
            id: '2',
            title: 'Customization',
            desc: 'Customize your settings to fit your needs and preferences easily.',

        },
        {
            id: '3',
            title: 'Automation',
            desc: 'Set up automation features to save time and enhance productivity.',

        },
    ];

    return (
        <div className='p-1 howitwork_staff'>
            {staff.map((item, index) => (
                <h3 key={index}>{item.name}</h3>
            ))}

            <div className='main_staff_content p-1 flex'>
                {howItWorksItems.map((item) => (
                    <motion.div
                        className='flex staff_content'
                        key={item.id}
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.5 }}
                    >
                        <div className='relative card_staff'>
                            <img src={You} alt="" className='img_staff'/>
                            <div className='p-0 card_content'>
                                <h3>{item.title}</h3>
                                <p>{item.desc}</p>
                            </div>
                        </div>
                    </motion.div>
                ))}
            </div>
        </div>
    );
}

export default HowItworks;
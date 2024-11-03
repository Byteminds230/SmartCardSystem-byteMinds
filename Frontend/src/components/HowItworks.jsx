import React from 'react';
import { motion } from 'framer-motion'; 
import  You  from '../assets/img/you.svg'; 
import  Vector  from '../assets/img/vector.svg'; 

function HowItworks() {
    const staff = [{ name: 'How it works' }];
    const howItWorksItems = [
        {
            id: '1',
            title: 'Smart Access Control',
            desc: 'Students can easily enter school premises by tapping their cards at entry points. This not only speeds up the entry process but also enhances security by monitoring who enters and exits the school.',
            img: You
        },
        {
            id: '2',
            title: 'Enhanced Security',
            desc: 'With TrackXpert, schools can monitor access points effectively. The system logs entries and exits, allowing administrators to keep track of who is on campus at all times.',
            img: You,
        },
        {
            id: '3',
            title: 'Attendance Tracking',
            desc: 'Our system simplifies attendance management. Teachers can quickly check attendance using student cards, providing real-time data that helps in monitoring student participation.',
            img: Vector

        },
    ];

    return (
        <div className='p-1 howitwork_staff'>
            {staff.map((item, index) => (
                <h3 key={index} className='heading'>{item.name}</h3>
            ))}

            <div className='main_staff_content flex'>
                {howItWorksItems.map((item) => (
                    <motion.div
                        className='flex staff_content'
                        key={item.id}
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.5 }}
                    >
                        <div className='card_staff'>
                            <img src={item.img} alt="" className='img_staff'/>
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
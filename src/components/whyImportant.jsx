import React from 'react';
import { motion } from 'framer-motion'; 
import  You  from '../assets/img/you.svg'; 
import  Vector  from '../assets/img/vector.svg'; 

function whyImportant() {
    const staff = [{ name: 'Why is it important', desc1:"How many hours are you and your team wasting in meetings that aren’t adding to your productivity?", desc2:"In a 2017 survey of office workers by the Harvard Business Review, key findings brought to light how useless meetings can actually be." }];
    const cardContent = [
        {id:'1',name:'josue cyuzuzo', desc:'thank you for the main staff and the information you have given to us so that we can mange our school compound based on the card you have provided to us.'},
        {id:'2',name:'josue cyuzuzo', desc:'thank you for the main staff and the information you have given to us so that we can mange our school compound based on the card you have provided to us.'},
        {id:'3',name:'josue cyuzuzo', desc:'thank you for the main staff and the information you have given to us so that we can mange our school compound based on the card you have provided to us.'},
    ]
    return (
        <div className='p-1 why_staff'>
            {staff.map((item, index) => (
                <>
                <h3 key={index} className='heading'>{item.name}</h3>
                <div className='heading_subs'>
                <p className='sub_heading'>{item.desc1}</p>
                <p className='sub_heading1'>{item.desc2}</p>
                </div>
                </>
                
            ))}

            <div className='why_staff_content flex'>
                    {cardContent.map((main,id)=>(
                    <div className='why_card_control' key={id}>
                        <div className="card">
                            <h3 className='card_title'> {main.name}</h3>
                            <p className="card_desc">
                                {main.desc}
                            </p>
                            
                        </div>
                    </div>
                    ))}
            </div>
        </div>
    );
}

export default whyImportant;
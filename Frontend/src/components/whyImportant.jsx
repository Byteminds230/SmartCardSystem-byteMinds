import React from "react";
import { Swiper, SwiperSlide } from "swiper/react";
import { EffectCoverflow, Pagination,Autoplay } from "swiper/modules";
import "swiper/css";
import "swiper/css/effect-coverflow";
import "swiper/css/pagination";
import Button from "./Button";

function WhyImportant() {
    const staff = [{ name: 'Why is it important', desc1:"How many hours are you and your team wasting in meetings that aren’t adding to your productivity?", desc2:"In a 2017 survey of office workers by the Harvard Business Review, key findings brought to light how useless meetings can actually be." }];
    const staff1 = [{content:'Feeling like there aren’t enough hours in the day is a common problem faced by many leaders in this world.',conten1:'Try post meeting surveys now and avoid wasting time.'}];
  const quotes = [
    {
      id: 1,
      percentage: "62%",
      text: "TrackXpert Monitor has transformed the way we manage student access. The seamless integration of identification and access needs into one smart card solution has made our operations more efficient and convenient.",
      source: "— School Administrator",
    },
    {
      id: 2,
      percentage: "64%",
      text: "With TrackXpert, we have significantly improved campus security. The ability to monitor who enters and exits the school grounds provides peace of mind for both staff and parents.",
      source: "— Principal",
    },
    {
      id: 3,
      percentage: "71%",
      text: "The user-friendly interface of TrackXpert Monitor has made it easy for both students and staff to adapt to the new system. It’s intuitive and requires minimal training.",
      source: "— IT Coordinator",
    },
    {
      id: 4,
      percentage: "90%",
      text: "Real-Time Monitoring:TrackXpert allows us to monitor student attendance in real-time, which has streamlined our administrative processes and improved accountability.",
      source: "— Attendance Officer",
    },
    {
      id: 5,
      percentage: "95%",
      text: "Students love the convenience of using their cards for library access and entry into the school. It’s made their daily routines smoother and more organized.",
      source: "— Student Council President",
    },
    {
      id: 6,
      percentage: "80%",
      text: "Comprehensive Solution:TrackXpert Monitor is not just a card management system; it's a comprehensive solution that addresses multiple aspects of school operations, from security to resource management.",
      source: "— Educational Consultant",
    },
    {
      id: 7,
      percentage: "85%",
      text: "High Satisfaction Rate:Since implementing TrackXpert, we’ve seen a noticeable increase in satisfaction among both staff and students regarding campus safety and access control.",
      source: "— School Board Member",
    },
  ];

  return (
    <div className="why_important_container">
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
    </div>
      <Swiper
        effect={"coverflow"}
        grabCursor={true}
        centeredSlides={true}
        slidesPerView={"auto"}
        loop={true}
        autoplay={{
          delay: 3000,
          disableOnInteraction: false,
        }}
        coverflowEffect={{
          rotate: 0, 
          stretch: 1000,
          depth: 200,
          modifier: 1, 
          slideShadows: false,
        }}
        pagination={{ clickable: true }}
        modules={[EffectCoverflow, Pagination,Autoplay ]}
        className="mySwiper"
      >
        {quotes.map((quote) => (
          <SwiperSlide key={quote.id} className="quote_slide">
            <div className="quote_card">
              <blockquote className="quote_text">
                <span className="quote_percentage">{quote.percentage} </span>
                <span className="quote_body">{quote.text}</span>
              </blockquote>
              <p className="quote_source">SOURCE: {quote.source}</p>
            </div>
          </SwiperSlide>
        ))}
      </Swiper>
      <div className='p-1 why_staff'>
            {staff1.map((item) => (
                <>
                <div className='heading_subs' key={item}>
                <p className='sub_heading'>{item.content}</p>
                <h4 className="sub_para">{item.conten1}</h4>
                <a href="/auth/login">
                <Button
                  className='btn_staff1'
                  content='request Account'
                 />
                </a>
                
                </div>
                </>
                
            ))}
    </div>
    </div>
  );
}

export default WhyImportant;

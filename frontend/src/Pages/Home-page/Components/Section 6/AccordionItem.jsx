import React, { useRef } from "react";
import { ReactComponent as ArrowIcon } from "./Vector.svg";
import style from "./section6.module.scss";

// export const AccordionItem = ({ faqItem, onClick, isOpen }) => {
//   const itemRef = useRef(null);

//   return (
//     <li className="accordion-item">
//       <button className="accordion-header" onClick={() => onClick()}>
//         {faqItem.q}
//         <ArrowIcon className={`accordion-arrow ${isOpen ? "active" : ""}`} />
//       </button>
//       <div
//         className="accordion-collapse"
//         style={
//           isOpen ? { height: itemRef.current.scrollHeight } : { height: "0px" }
//         }
//       >
//         <div className="accordion-body" ref={itemRef}>
//           {faqItem.a}
//         </div>
//       </div>
//     </li>
//   );
// };

export const AccordionItem = ({ faqItem, onClick, isOpen }) => {
  const itemRef = useRef(null);

  return (
    <li className={style["accordion-item"]}>
      <button className={style["accordion-header"]} onClick={() => onClick()}>
        {faqItem.q}
        <ArrowIcon className={`${style["accordion-arrow"]} ${isOpen ? style["active"] : ""}`} />
      </button>
      <div
        className={style["accordion-collapse"]}
        style={
          isOpen ? { height: itemRef.current.scrollHeight } : { height: "0px" }
        }
      >
        <div className={style["accordion-body"]} ref={itemRef}>
          {faqItem.a}
        </div>
      </div>
    </li>
  );
};
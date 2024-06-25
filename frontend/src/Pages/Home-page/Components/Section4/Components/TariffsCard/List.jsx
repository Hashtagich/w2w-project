import './list.scss';
import React, { useState, useRef, useEffect } from 'react';

const List = () => {
    const [isOpen, setIsOpen] = useState(false);
    const dropdownRef = useRef(null);
  
    const handleToggle = () => {
      setIsOpen(!isOpen);
    };
  
    const handleClickOutside = (event) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsOpen(false);
      }
    };
  
    useEffect(() => {
      document.addEventListener('mousedown', handleClickOutside);
      return () => {
        document.removeEventListener('mousedown', handleClickOutside);
      };
    }, []);
  
    return (
      <div className="dropdown" ref={dropdownRef}>
        <button onClick={handleToggle} className="dropdown-toggle">
          О тарифе
        </button>
        <ul className={`dropdown-menu dropdown-menu-up ${isOpen ? 'dropdown-open' : ''}`}>
          <li>Доступ к сервису 12 месяцев</li>
          <li>Доступ к чату в Telegram</li>
          <li>Размещение Бренда в каталоге</li>
          <li>Расширенный доступ к личному <br />кабинету</li>
          <li>Моментальное оповещение о<br /> матчах</li>
          <li>Возможность посещать онлайн <br />и офлайн<br /> мероприятия W2W Match</li>
          <li>Статистика охватов бренда</li>
          <li>Помощь в подборе и создании <br />коллабораций</li>
        </ul>
      </div>
    );
}

export default List;



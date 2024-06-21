import React from 'react';
import style from '../../section4.module.scss';
import { tariffsInfo } from './constans';
import List from './List';

const Tariff = ({ info }) => {
  return (
    <div className={style.tariffsCard}>
      <h1>{info.title1}</h1>
      <h1>{info.title2}</h1>
      <p className={style.text1}>{info.text1}</p>
      <p className={style.text2}>{info.text2}</p>
      <p className={style.price}>{info.price}</p>
      <p className={style.text3}>{info.text3}</p>
      <button className={style.button1}>{info.button}</button>
      <List/>
    </div>
  );
}

const TariffCard = () => {
  return (
    <>
      {tariffsInfo.map((info) => (
        <Tariff key={info.code} info={info} />
      ))}
    </>
  );
}

export default TariffCard;

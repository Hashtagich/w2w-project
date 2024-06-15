import Section1 from './Components/Section 1/Section1';
import Section2 from './Components/Section 2/Section2';
import Section3 from './Components/Section 3/Section3';
import Section4 from './Components/Section 4/Section4';
import style1 from './sectors.module.scss'


const HomePage = () => {
    return (
        <div className={style1.allSectors}>
           <Section1/>
           <Section2/>
           <Section3/>
           <Section4/>
        </div>
    )
}

export default HomePage;
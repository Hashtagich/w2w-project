import Tariffs from './Components/Tariffs/Tariffs';
import Main from './Components/Main/Main';
import Section2 from './Components/Section 2/Section2';
import Section3 from './Components/Section 3/Section3';
import Accordion from './Components/Section 6/Section6';
import style1 from './sectors.module.scss';


const HomePage = () => {
    return (
        <div className={style1.allSectors}>
           <Main/>
           <Section2/>
           <Section3/>
           <Tariffs/>
           <Accordion/>
        </div>
    )
}

export default HomePage;
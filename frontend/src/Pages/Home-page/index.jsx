import Tariffs from './Components/Tariffs/Tariffs';
import Main from './Components/Main/main';
import Section3 from './Components/Section 3/Section3';
import style1 from './sectors.module.scss'


const HomePage = () => {
    return (
        <div className={style1.allSectors}>
           <Main/>
           <Section3/>
           <Tariffs/>
        </div>
    )
}

export default HomePage;
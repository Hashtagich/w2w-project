import React, { useState } from "react";
import { AccordionItem } from "./AccordionItem";
import style from "./section6.module.scss";

const faqList = [
    {
        q: "Что я получу, присоединившись к сервис-комьюнити?",
        a: "W2W Match это не только поиск брендов для коллаборации. W2W Match — это нетворкинг, закрытые online-встречи, эстетичные мероприятия и образовательные форматы, чаты, где обмениваются информацией, опытом и инсайтами. В проекте есть не только бренды, но и некоммерческие организации, медиа, эксперты и инфлюенсеры. А также партнёры в лице участников сервис-комьюнити, которые предоставляют скидки и спец. условия по различным товарам и услугам.",
    },
    {
        q: "Если я не смогу найти бренд для коллаборации?",
        a: "Такой ситуации априори не может произойти. Коллаборироваться можно с любым брендом из любой ниши и главный критерий выбора — это ваша релевантная аудитория. Например, если у вас магазин одежды для мам, а рядом находится кафе, куда тоже ходят мамы, то вы уже можете делать коллаборацию.",
    },
    {
        q: "Если для моего бизнеса не подойдет формат коллабораций?",
        a: "Коллаборации — это маркетинговый инструмент, который подходит всем,и уметь его использовать важно для продвижения и развития собственного бизнеса. Мы собрали большую подборку непримитивных коллабораций, чтобы показать, что коллаборации — это для всех. Получите нашу idea book colaboration и вдохновитесь на коллабу.",
    },
    {
        q: "Если у меня недостаточно знаний для создания коллаборации?",
        a: "Коллаборации по реализации могут быть как простыми, так и сложными. Сложность коллабы зависит только от ваших идей. Если сомневаетесь в своих силах, то у нас есть тариф с поддержкой, где мы помогаем подобрать бренд, придумать идею и реализовать ее. Помимо этого вы попадаете в сервис-комьюнити, где у вас будет чат с такими же предпринимателями, как и вы, у которых всегда можно попросить помощи.",
    },
    {
        q: "Сколько нужно денег, чтобы реализовать коллаборацию?",
        a: "Сама коллаборация — бесплатная.В этом и есть её суть, чтобы дать вам возможность взаимодействовать друг с другом.При этом вы разделяете затраты с партнёром на саму реализацию идеи.И реализация может быть бесплатная, например, вы делаете совместный рилс своими силами из реквизита, который нашли дома.Но также коллаба может быть и очень классно реализована, с каким нибудь продакшеном в студии или организацией мероприятия.",
    },
];

const Accordion = () => {
    const [openId, setId] = useState(null);

    return (
        <section className={style.container}>
            <h2 className={style.subtitle}>
                частые вопросы
            </h2>
            <ul className={style.accordion}>
                {faqList.map((faqItem, id) => {
                    return (
                        <AccordionItem
                            onClick={() => (id === openId ? setId(null) : setId(id))}
                            faqItem={faqItem}
                            isOpen={id === openId}
                            key={id}
                        />
                    );
                })}
            </ul>
        </section>
    );
};

export default Accordion;
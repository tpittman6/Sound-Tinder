import React, { useState } from 'react';
import TinderCard from 'react-tinder-card';
import './TinderCards.css';
function TinderCards() {
    const [people, setPeople] = useState([
        {
            name: "steve jobs",
            url: "https://m.media-amazon.com/images/M/MV5BMDdmMTBiNTYtMDIzNi00NGVlLWIzMDYtZTk3MTQ3NGQxZGEwXkEyXkFqcGdeQXVyMzMwOTU5MDk@._V1_.jpg"
        },
        {
            name: "Mark",
            url: "https://static.wikia.nocookie.net/batman/images/c/c0/Facepaint.png/revision/latest?cb=20200320213434"
        }
    ]);

    /*
    good implementation
    setPeople([...people,'sonny', 'qazi'])*/
    return (
        <div>
            <h1>Tinder Cards</h1>
            <div className="tinderCards_cardContainer">
                {people.map(person => (
                    <TinderCard
                        className="swipe"
                        key={person.name}
                        preventSwipe={['up', 'down']}

                    >
                        <div
                            style={{ backgroundImage: `url(${person.url})` }}
                            className="card">
                            <h3> {person.name}</h3>
                        </div>
                    </TinderCard>
                ))}
            </div>
        </div>
    )
}

export default TinderCards

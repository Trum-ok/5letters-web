import React from'react'
import Typewriter from 'typewriter-effect';
import Game from './components/word'
import ToggleTypewriter from './components/animationToggler'
import './App.css'

function App() {
  const [isTypewriterActive, setIsTypewriterActive] = React.useState(true);

  const toggleTypewriter = () => {
    setIsTypewriterActive((prevState) => {
      return !prevState;
    });
  };

  return (
    <>
      <div className='container'>
        <h1>
          {isTypewriterActive ? (
            <Typewriter
              onInit={(typewriter) => {
                typewriter.typeString("5 БУКВ")
                  .pauseFor(7000)
                  .deleteAll()
                  .pauseFor(1300)
                  .start();
              }}
              options={{
                autoStart: true,
                loop: true,
                strings: ['5 БУКВ', '5 LETTERS', '5文字'],
              }}
            />
          ) : (
            "5 БУКВ"
          )}
        </h1>
        <Game />
        < ToggleTypewriter toggleTypewriter={toggleTypewriter} isTypewriterActive={isTypewriterActive} styles={{position: 'fixed', right: '0', bottom: '0', zIndex: '9999', margin: '10px'}} />
      </div>
    </>
  )
}

export default App

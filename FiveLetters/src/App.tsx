import Typewriter from 'typewriter-effect';
import Game from './components/word'
import './App.css'

function App() {

  return (
    <>
      <div className='container'>
        <h1>
            <Typewriter 
            onInit={(typewriter) => {
                typewriter.typeString("5 БУКВ")
                .pauseFor(7000)
                .deleteAll()
                .pauseFor(1300)
                .start()
            }}
            options={{
                autoStart: true,
                loop: true,
                strings: ['5 БУКВ', '5 LETTERS', '5文字'],
            }}/>
        </h1>
        <Game />
      </div>
    </>
  )
}

export default App

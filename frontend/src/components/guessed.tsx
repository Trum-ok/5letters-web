import Confetti from 'react-confetti'
import { getWindowWidth, getWindowHeight } from './windowSize'

interface GuessedProps {
    word: string;
}

function Guessed({ word }: GuessedProps) {
  return (
    <>
    <Confetti
        width={getWindowWidth()-50}
        height={getWindowHeight()-50}
        tweenDuration={1000}
    />
    <h2 style={{ fontSize: '24px' }}>Угадано: <span style={{color: '#00a651'}}>{word}</span></h2>
    </>
  )
}

export default Guessed;
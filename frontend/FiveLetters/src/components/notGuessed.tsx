interface GuessedProps {
    word: string;
}

function notGuessed({ word }: GuessedProps) {
  return (
    <>
        <h2 style={{ fontSize: '24px' }}>Игра окончена!</h2>
        <p style={{ fontSize: '18px' }}>Загаданное слово: <span style={{color: '#ffdd2d'}}>{word}</span></p>
    </>
  )
}

export default notGuessed;
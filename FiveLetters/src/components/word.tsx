import React, { useState, ChangeEvent, useRef, useEffect } from 'react';
import enterIcon from '../assets/enter.svg';

interface WordInputProps {}

const WordInput: React.FC<WordInputProps> = () => {
  const inputRefs = useRef<Array<HTMLInputElement>>(Array(5).fill(null));
  const [inputValues, setInputValues] = useState<string[]>(['', '', '', '', '']);
  const [history, setHistory] = useState<{ word: string; isMatch: boolean }[]>([]);
  const [attempts, setAttempts] = useState<number>(6);
  const [targetWord, setTargetWord] = useState<string>('');
  const [isWordGuessed, setIsWordGuessed] = useState<boolean>(false);
  const [isGameOver, setIsGameOver] = useState<boolean>(false);

  useEffect(() => {
    // Fetch random word from the Flask server
    fetch("http://127.0.0.1:8080/get_random_word", {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
      mode: 'cors',
    })
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => setTargetWord(data.word))
      .catch(error => console.error("Error fetching random word:", error));
  }, []);

  const handleInputChange = (index: number, event: ChangeEvent<HTMLInputElement>) => {
    const newValue = event.target.value.toUpperCase().slice(0, 1);
    const newInputValues = [...inputValues];
    newInputValues[index] = newValue;
    setInputValues(newInputValues);

    // Переход к следующему полю
    if (newValue && index < inputRefs.current.length - 1) {
      inputRefs.current[index + 1]?.focus();
    }
  };

  const handleKeyDown = (index: number, event: React.KeyboardEvent<HTMLInputElement>) => {
    if (event.key === 'Backspace' && !inputValues[index] && index > 0) {
      inputRefs.current[index - 1]?.focus();
    }

    if (event.key === 'Enter') {
        handleSubmit();
      }
  };

  const handleSubmit = () => {
    const submittedWord = inputValues.join('');

    if (submittedWord.length !== 5) {
      alert('Пожалуйста, введите ровно 5 букв.');
      return;
    }

    const isMatch = checkMatch(submittedWord);

    setHistory([...history, { word: submittedWord, isMatch }]);
    setAttempts(attempts - 1);

    if (isMatch && submittedWord === targetWord) {
      // Если слово полностью угадано, скрываем элементы
      setIsWordGuessed(true);
    }

    if (attempts === 1) {
      setIsGameOver(true);
    }

    setInputValues(['', '', '', '', '']); // Сброс полей ввода после отправки
    inputRefs.current[0]?.focus(); // Фокус на первое поле ввода
  };

  const checkMatch = (submittedWord: string): boolean => {
    for (let i = 0; i < targetWord.length; i++) {
      if (submittedWord[i] && submittedWord[i] === targetWord[i]) {
        continue;
      } else {
        return false;
      }
    }
    return true;
  };

  const renderHighlightedWord = (word: string): React.ReactNode => {
    const elements: React.ReactNode[] = [];
    const wordMask = mask(word);
  
    for (let i = 0; i < word.length; i++) {
      const char = word[i];
      const maskChar = wordMask[i];
  
      elements.push(
        <span
          key={i}
          style={{
            color: getColorForChar(char, maskChar),
            fontWeight: 'bold',
          }}
        >
          {char}
        </span>
      );
    }
  
    return <div>{elements}</div>;
  };
  
  const getColorForChar = (char: string, maskChar: string): string => {
    if (maskChar === '0') {
      return 'grey';
    } else if (maskChar === '#') {
      return 'white';
    } else if (maskChar === char) {
      return '#ffdd2d';
    } else {
      // Handle other cases if needed
      return 'black';
    }
  };
  
  const mask = (word: string): string => {
    let wordMask = '';
  
    if (word === targetWord) {
      return word;
    }
  
    let localAnswer = targetWord;
  
    for (let i = 0; i < 5; i++) {
      if (word[i] === targetWord[i]) {
        wordMask += targetWord[i];
      } else if (word[i] && localAnswer.includes(word[i])) {
        wordMask += '#';
      } else {
        wordMask += '0';
      }
      localAnswer = localAnswer.replace(word[i], '');
    }
  
    return wordMask;
  };
  

  return (
    <div>
      {!isWordGuessed && !isGameOver && (
        <div style={{ display: 'flex', alignItems: 'center', marginBottom: '10px' }}>
          {inputValues.map((value, index) => (
            <input
              key={index}
              type="text"
              pattern='[а-яА-Я]+'
              value={value}
              onChange={(event) => handleInputChange(index, event)}
              onKeyDown={(event) => handleKeyDown(index, event)}
              maxLength={1}
              ref={(input) => (inputRefs.current[index] = input)}
              style={{
                marginRight: '5px',
                height: '50px',
                width: '50px',
                textAlign: 'center',
                borderRadius: '5px',
                boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
                border: 'none',
                outline: 'none',
              }}
              onFocus={() => {
                inputRefs.current[index].style.boxShadow = '0 0 2px 1px white';
              }}
              onBlur={() => {
                inputRefs.current[index].style.boxShadow = '0 2px 4px rgba(0, 0, 0, 0.1)';
              }}
            />
          ))}
          <button
            onClick={handleSubmit}
            disabled={attempts === 0}
            style={{
              width: '30px',
              height: '30px',
              borderRadius: '5px',
              padding: '0',
              backgroundColor: attempts === 0 ? 'grey' : '#ffdd2d',
              color: 'white',
              border: 'none',
              cursor: attempts === 0 ? 'not-allowed' : 'pointer',
              display: 'flex',
              alignItems: 'center',
              justifyItems: 'center',
            }}
          >
            <img
              src={enterIcon}
              style={{
                width: '20px',
                height: '20px',
              }}
            />
          </button>
        </div>
      )}
      {isWordGuessed && (
        <h2 style={{ fontSize: '24px' }}>Угадано: <span style={{color: '#00a651'}}>{targetWord}</span></h2>
      )}
      {isGameOver && (
        <div>
          <h2 style={{ fontSize: '24px' }}>Игра окончена!</h2>
          <p style={{ fontSize: '18px' }}>Загаданное слово: <span style={{color: '#ffdd2d'}}>{targetWord}</span></p>
        </div>
      )}
      <div>
        <h3>История попыток:</h3>
        {history.map((item, index) => (
          <div key={index}>{renderHighlightedWord(item.word, item.isMatch)}</div>
        ))}
      </div>
      <p>Попыток осталось: {attempts}</p>
    </div>
  );
};

export default WordInput;

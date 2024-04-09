import React, { useState, ChangeEvent, useRef, useEffect } from 'react';
import { fetchRandomWord } from './wordService';
import InputForm from './inputForm';
import SubmitButton from './submitButton';
import mask from './wordMask';
import Guessed from './guessed';
import NGuessed from './notGuessed';

interface WordInputProps {}

const WordInput: React.FC<WordInputProps> = () => {
  const inputRefs = useRef<Array<HTMLInputElement>>(Array(5).fill(null));
  const currentInputRef = useRef<HTMLInputElement>(null);
  const [inputValues, setInputValues] = useState<string[]>(['', '', '', '', '']);
  const [history, setHistory] = useState<{ word: string; isMatch: boolean }[]>([]);
  const [attempts, setAttempts] = useState<number>(6);
  const [targetWord, setTargetWord] = useState<string>('');
  const [isWordGuessed, setIsWordGuessed] = useState<boolean>(false);
  const [isGameOver, setIsGameOver] = useState<boolean>(false);

  useEffect(() => {
    fetchRandomWord().then(word => setTargetWord(word));
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
      setIsWordGuessed(true); // Если слово полностью угадано, скрываем элементы
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
    const wordMask = mask(word, targetWord);
  
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
      return 'black';
    }
  };

  return (
    <div>
      {!isWordGuessed && !isGameOver && (
        <div style={{ display: 'flex', alignItems: 'center', marginBottom: '10px' }}>
          {inputValues.map((value, index) => (< InputForm index={index} value={value} hIC={handleInputChange} hKD={handleKeyDown} iRefs={inputRefs} />))}
          < SubmitButton onClick={handleSubmit} attempts={attempts} />
        </div>
      )}
      {isWordGuessed && (<Guessed word={targetWord} />)}
      {isGameOver && (< NGuessed word={targetWord} />)}
      <div>
        <h3>История попыток:</h3>
        {history.map((item, index) => (
          <div key={index}>{renderHighlightedWord(item.word)}</div>
        ))}
      </div>
      <p>Попыток осталось: {attempts}</p>
    </div>
  );                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
};  

export default WordInput;
const mask = (word: string, targetWord: string): string => {
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

export default mask;
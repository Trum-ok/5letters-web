import axios from 'axios';

export async function fetchRandomWord() {
  try {
    const response = await axios.get<{ word: string }>('http://127.0.0.1:8080/get_random_word', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      }
    //   mode: 'cors',
    });
    return response.data.word;
  } catch (error) {
    console.error('Error fetching random word:', error);
    throw error;
  }
}
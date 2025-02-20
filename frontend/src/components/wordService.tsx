import axios from 'axios';

export async function fetchRandomWord() {
  try {
    const port = import.meta.env.VITE_BACK_PORT || 8081;
    const url = `http://127.0.0.1:${port}/get_random_word`;
    console.log(import.meta.env.VITE_APP_TITLE);
    console.log(port, url);
    const response = await axios.get<{ word: string }>(url, {
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
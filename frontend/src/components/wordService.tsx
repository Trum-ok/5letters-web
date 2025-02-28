import axios from 'axios';

export async function fetchRandomWord() {
  try {
    const port = window.env.VITE_BACK_PORT || 1212;
    const ip = window.env.VITE_BACK_IP || '127.0.0.1';
    const url = `https://${ip}:${port}/get_random_word`;
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
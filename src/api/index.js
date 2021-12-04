import axios from 'axios';

const http = axios.create({
  baseURL: process.env.BASE_API_URL || 'http://127.0.0.1:8000/api',
});

export const login = (data) => http.post('/auth/login/', data);

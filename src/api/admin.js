import axios from 'axios'

const http = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/admin',
})

export const getUsers = (query = {}) =>
  http.get('/users/', {
    params: query,
  })
export const getSubjects = () => http.get('/subjects/')

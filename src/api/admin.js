import axios from 'axios'

const http = axios.create({
  baseURL:
    process.env.VUE_APP_BASE_URL + '/api/admin' ||
    'http://127.0.0.1:8000/api/admin',
})

export const addUser = (data) => http.post('/users/', data)
export const getUsers = (query = {}) =>
  http.get('/users/', {
    params: query,
  })
export const getUser = (id) => http.get(`/users/${id}/`)
export const updateUser = (id, data) => http.patch(`/users/${id}/`, data)
export const getAvatarUploadUrl = (id, file_type) =>
  http.get(`/users/${id}/avatar/upload/`, {
    params: {
      file_type: file_type,
    },
  })

export const getSubjects = () => http.get('/subjects/')

export const localFileUpload = (location, data) =>
  http.put('/upload/random.txt/', data, {
    params: {
      location: location,
    },
  })

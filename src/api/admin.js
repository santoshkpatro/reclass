import axios from 'axios'

const http = axios.create({
  baseURL:
    process.env.VUE_APP_BASE_URL + '/admin' ||
    'http://127.0.0.1:8000/api/admin',
})

export const fileUpload = (filename, config = {}, formData) =>
  http.put(`/upload/${filename}/`, formData, config)

export const addUser = (data) => http.post('/users/', data)
export const getUsers = (query = {}) =>
  http.get('/users/', {
    params: query,
  })
export const getUser = (id) => http.get(`/users/${id}/`)
export const updateUser = (id, data) => http.patch(`/users/${id}/`, data)
// export const updateUserAvatar = (
//   id,
//   formData,
//   config = {
//     headers: {
//       'Content-Type': 'multipart/form-data',
//     },
//   }
// ) => http.put(`/users/${id}/avatar/`, formData, config)

export const getSubjects = () => http.get('/subjects/')

import axios from 'axios'

const http = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/admin',
})

// Users
export const getUsers = (query = {}, conf = {}) =>
  http.get(
    '/users',
    {
      params: query,
    },
    conf
  )
export const getUserDetail = (id) => http.get(`/users/${id}/`)
export const updateUser = (id, data) => http.patch(`/users/${id}/`, data)
export const addUser = (data) => http.post('/users/', data)

export const getSchedules = () => http.get('/schedules')

export const getSubjects = () => http.get('/subjects')

export const getAssignments = () => http.get('/assignments')

export const getSubmissions = () => http.get('/submissions')

export const getNotifications = () => http.get('/notifications')

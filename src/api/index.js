import axios from 'axios'

const http = axios.create({
  baseURL: process.env.VUE_APP_BASE_URL + '/api' || 'http://127.0.0.1:8000/api',
})

export const login = (data) => http.post('/auth/login/', data)

export const passwordReset = (data) => http.post('/auth/password_reset/', data)

export const passwordResetVerify = (token) =>
  http.get(`/auth/password_reset/verify/${token}/`)

export const passwordResetConfirm = (token, data) =>
  http.post(`/auth/password_reset/confirm/${token}/`, data)

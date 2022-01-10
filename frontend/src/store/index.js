import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    profile: null,
  },
  mutations: {
    SET_PROFILE(state, userData) {
      state.profile = userData
    },
    REMOVE_PROFILE(state) {
      state.profile = null
    },
  },
  actions: {
    login({ commit }, userData) {
      commit('SET_PROFILE', userData)
      axios.defaults.headers.common[
        'Authorization'
      ] = `Bearer ${userData.access_token}`
      localStorage.setItem('profile', JSON.stringify(userData))
    },
    logout({ commit }) {
      commit('REMOVE_PROFILE')
      localStorage.removeItem('profile')
      location.reload()
    },
  },
  modules: {},
  getters: {
    loggedIn(state) {
      return !!state.profile
    },

    role(state) {
      if (state.profile) {
        if (state.profile.is_admin) {
          return 'admin'
        } else {
          if (state.profile.is_instructor) {
            return 'instructor'
          } else {
            return 'student'
          }
        }
      } else {
        return 'user'
      }
    },
  },
})

import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    profile: null,
  },
  mutations: {
    setProfile(state, profileData) {
      state.profile = profileData;
      axios.defaults.headers.common[
        'Authorization'
      ] = `Bearer ${profileData.access_token}`;
      localStorage.setItem('profile', JSON.stringify(profileData));
    },
    removeProfile(state) {
      state.profile = null;
      localStorage.removeItem('profile');
      location.reload();
    },
  },
  actions: {},
  modules: {},
  getters: {
    loggedIn(state) {
      return !!state.profile;
    },
  },
});

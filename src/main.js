import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import axios from 'axios';
import Toast from 'vue-toastification';
// import 'bootstrap-icons/font/bootstrap-icons.css';
// import 'bootstrap';
// import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import 'vue-toastification/dist/index.css';

const options = {};

Vue.use(Toast, options);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
  created() {
    const userString = localStorage.getItem('profile');
    if (userString) {
      const userData = JSON.parse(userString);
      this.$store.commit('setProfile', userData);
    }
    axios.interceptors.response.use(
      (response) => response,
      (error) => {
        if (error.response.status === 401) {
          this.$commit.commit('removeProfile');
        }
        return Promise.reject(error);
      }
    );
  },
}).$mount('#app');

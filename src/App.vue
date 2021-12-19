<template>
  <div>
    <Navbar />
    <router-view />
  </div>
</template>

<script>
import Navbar from './common/Navbar.vue'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    Navbar,
  },
  created() {
    const userString = localStorage.getItem('profile')
    if (userString) {
      const userData = JSON.parse(userString)
      this.$store.dispatch('login', userData)
    }
    axios.interceptors.response.use(
      (response) => response,
      (error) => {
        if (error.response.status === 401) {
          this.$store.dispatch('logout')
        }
        return Promise.reject(error)
      }
    )
  },
}
</script>

<style></style>

<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
import axios from 'axios'

export default {
  created() {
    const userString = localStorage.getItem('profile')
    if (userString) {
      const userData = JSON.parse(userString)
      this.$store.commit('setProfile', userData)
    }
    axios.interceptors.response.use(
      (response) => response,
      (error) => {
        if (error.response.status === 401) {
          this.$commit.commit('removeProfile')
        }
        return Promise.reject(error)
      }
    )
  },
}
</script>

<style></style>

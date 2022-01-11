<template>
  <div class="flex h-screen">
    <div class="m-auto border px-7 py-7 rounded shadow-lg">
      <p class="text-center text-2xl">Login</p>
      <form @submit.prevent="handleLogin">
        <BaseInput
          label="Email"
          v-model="email"
          type="text"
          name="email"
          required="true"
        />
        <BaseInput
          label="Password"
          v-model="password"
          type="password"
          name="password"
          required="true"
        />
        <button
          class="w-full bg-indigo-500 py-2 rounded text-white hover:bg-indigo-600"
          type="submit"
        >
          Login
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import { login } from '@/api/index.js'

export default {
  name: 'Login',
  components: {},
  data() {
    return {
      isLoading: false,
      email: null,
      password: null,
      remember_me: null,
    }
  },
  methods: {
    handleLogin() {
      this.isLoading = true
      login({ email: this.email, password: this.password })
        .then(({ data }) => {
          this.$store.dispatch('login', data)
          this.$router.push({ name: 'Home' })
        })
        .catch((e) => {
          this.isLoading = false
          console.log(e)
        })
    },
  },
}
</script>

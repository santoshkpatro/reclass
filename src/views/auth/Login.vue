<template>
  <div class="container mt-3">
    <h1>Login</h1>
    <form class="col-4" @submit.prevent="handleLogin">
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
      <BaseCheckbox label="Remember me" v-model="remember_me" />
      <router-link :to="{ name: 'PasswordReset' }">Forgot Password</router-link>
      <div class="d-grid gap-2">
        <button
          class="btn btn-primary my-3"
          type="submit"
          :disabled="isLoading"
        >
          <span
            v-if="isLoading"
            class="spinner-border spinner-border-sm me-2"
            role="status"
            aria-hidden="true"
          ></span>
          <span>Login</span>
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import { login } from '@/api/index.js'

export default {
  name: 'Login',
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

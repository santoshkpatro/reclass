<template>
  <div v-if="isLoading">
    <div class="col-4 mt-3">
      <p class="placeholder-glow">
        <span class="placeholder col-12"></span>
      </p>

      <p class="placeholder-wave">
        <span class="placeholder col-12"></span>
      </p>
    </div>
  </div>
  <div class="container mt-3" v-else>
    <div v-if="isValid">
      <h3>Password Reset</h3>
      <div class="col-4">
        <form @submit.prevent="handleSubmit">
          <BaseInput
            label="Password"
            v-model="password"
            placeholder="Password"
            required="true"
            type="password"
          />
          <BaseInput
            label="Confirm Password"
            v-model="confirm_password"
            placeholder="Confirm Password"
            required="true"
            type="password"
          />
          <div class="d-grid gap-2 mt-3">
            <button class="btn btn-primary">
              <span>Reset Password</span>
            </button>
          </div>
        </form>
      </div>
    </div>
    <div v-else>
      <p>Expired</p>
    </div>
  </div>
</template>

<script>
import { passwordResetVerify, passwordResetConfirm } from '@/api'

export default {
  name: 'PasswordReset',
  props: ['token'],
  data() {
    return {
      password: null,
      confirm_password: null,
      isLoading: true,
      isValid: false,
    }
  },
  methods: {
    handleSubmit() {
      passwordResetConfirm(this.token, {
        password: this.password,
        confirm_password: this.confirm_password,
      })
        .then(({ data }) => {
          this.$router.push({ name: 'Login' })
        })
        .catch((e) => console.log(e))
    },
  },
  mounted() {
    passwordResetVerify(this.token)
      .then(({ data }) => {
        this.isValid = true
      })
      .catch((e) => {
        if (e.response.status === 401) {
          console.log('Token expired')
        }
      })
      .finally(() => (this.isLoading = false))
  },
}
</script>

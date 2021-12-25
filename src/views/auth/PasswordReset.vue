<template>
  <div class="container mt-3">
    <h3>Password Reset</h3>
    <div class="col-4">
      <form @submit.prevent="handleSubmit">
        <BaseInput
          label="Email Address"
          v-model="email"
          placeholder="Email Address"
          required="true"
        />
        <div class="d-grid gap-2 mt-3">
          <button class="btn btn-primary">
            <span>Send Password Reset Link</span>
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { passwordReset } from '@/api'

export default {
  name: 'PasswordReset',
  data() {
    return {
      email: null,
    }
  },
  methods: {
    handleSubmit() {
      passwordReset({ email: this.email })
        .then(({ data }) => {
          this.$router.push({ name: 'Home' })
        })
        .catch((e) => console.log(e))
    },
  },
}
</script>

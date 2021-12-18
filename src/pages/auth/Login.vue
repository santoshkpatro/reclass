<template>
  <div class="login">
    <Navbar />
    <div class="container">
      <div class="d-flex justify-content-center align-items-center">
        <form @submit.prevent="handleSubmit">
          <BaseInput
            label="Email"
            v-model="email"
            type="email"
            required="true"
            :message="emailMessage"
          />
          <BaseInput
            label="Password"
            v-model="password"
            type="password"
            required="true"
            :message="passwordMessage"
          />
          <BaseSelect :options="roles" label="Select Role" v-model="role" />
          <div class="d-grid gap-2">
            <button class="btn btn-primary mt-2" type="submit">Login</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from '../../components/Navbar.vue'
import BaseInput from '../../components/base/BaseInput.vue'
import BaseSelect from '../../components/base/BaseSelect.vue'
import { login } from '../../api/index.js'

export default {
  name: 'Login',
  components: {
    Navbar,
    BaseInput,
    BaseSelect,
  },
  data() {
    return {
      email: '',
      emailMessage: '',
      password: '',
      passwordMessage: '',
      roles: ['admin', 'teacher', 'student'],
      role: '',
    }
  },
  methods: {
    checkForm() {
      let errors = 0

      if (this.email === '') {
        this.emailMessage = 'Please enter email'
        errors += 1
      }

      if (
        !this.email
          .toLowerCase()
          .match(
            /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i
          )
      ) {
        this.emailMessage = 'Please enter a valid email'
        errors += 1
      }

      if (this.password === '') {
        this.passwordMessage = 'Please enter valid password'
        errors += 1
      }

      if (errors === 0) {
        return true
      } else {
        return false
      }
    },
    handleSubmit() {
      // console.log(this.email)
      // console.log(this.password)
      console.log(this.role)
      this.checkForm()

      login({
        email: this.email,
        password: this.password,
      })
        .then(({ data }) => {
          this.$store.commit('setProfile', data)
          if (!this.$route.query === {}) {
            this.$router.push(this.$route.query.redirect)
          }

          this.$router.push({ name: 'Home' })
        })
        .catch((e) => console.log(e))
    },
  },
}
</script>

<style scoped>
.card {
  border: none;
}
</style>

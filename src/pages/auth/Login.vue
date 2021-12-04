<template>
  <div class="login">
    <Navbar />
    <div
      class="d-flex justify-content-center align-items-center"
      style="height: 80vh"
    >
      <div class="card shadow-lg col-4">
        <div class="card-body p-4">
          <form @submit.prevent="handleSubmit">
            <h3 class="text-center">Login</h3>
            <BaseInput
              name="email"
              v-model="email"
              label="Email"
              :message="emailMessage"
              class="my-2"
            />
            <BaseInput
              name="password"
              v-model="password"
              label="Password"
              :message="passwordMessage"
              class="my-2"
            />
            <div class="d-grid gap-2">
              <button type="submit" class="btn btn-dark mt-3">Login</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
import BaseInput from '@/components/base/BaseInput.vue';
import { login } from '@/api/index.js';

export default {
  name: 'Login',
  components: {
    Navbar,
    BaseInput,
  },
  data() {
    return {
      email: '',
      emailMessage: '',
      password: '',
      passwordMessage: '',
    };
  },
  methods: {
    checkForm() {
      let errors = 0;

      if (this.email === '') {
        this.emailMessage = 'Please enter email';
        errors += 1;
      }

      if (
        !this.email
          .toLowerCase()
          .match(
            /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i
          )
      ) {
        this.emailMessage = 'Please enter a valid email';
        errors += 1;
      }

      if (this.password === '') {
        this.passwordMessage = 'Please enter password';
        errors += 1;
      }

      if (errors === 0) {
        return true;
      } else {
        return false;
      }
    },
    handleSubmit() {
      if (this.checkForm()) {
        login({
          email: this.email,
          password: this.password,
        })
          .then(({ data }) => {
            this.$store.commit('setProfile', data);
            if (!this.$route.query === {}) {
              this.$router.push(this.$route.query.redirect);
            }

            this.$router.push({ name: 'Home' });
          })
          .catch((e) => console.log(e));
      }
    },
  },
};
</script>

<style scoped>
.card {
  border: none;
}
</style>
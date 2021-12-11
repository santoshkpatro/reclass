<template>
  <div class="login">
    <Navbar />
    <div class="w-1/3 mx-auto">
      <form @submit.prevent="handleSubmit">
        <BaseInput v-model="email" name="email" label="Email" />
        <BaseInput
          v-model="password"
          name="password"
          label="Password"
          type="password"
        />
        <button class="btn-primary">Login</button>
      </form>
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
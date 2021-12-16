<template>
  <h2 class="my-6 text-2xl font-semibold text-gray-700 dark:text-gray-200">
    Add User
  </h2>
  <form @submit.prevent="handleSubmit">
    <BaseInput name="email" label="Email" v-model="user.email" />
    <BaseInput name="first_name" label="First Name" v-model="user.first_name" />
    <BaseInput
      name="password"
      label="Password"
      v-model="user.password"
      type="password"
    />
    <button
      class="btn-primary w-full flex justify-center my-2"
      v-if="isAdding"
      disabled
    >
      <RefreshIcon class="animate-spin h-5 w-5 text-gray-500" />
    </button>
    <button class="btn-primary my-2 w-full" type="submit" v-if="!isAdding">
      Add
    </button>
  </form>
</template>

<script>
import BaseInput from '../../../components/base/BaseInput.vue'
import { RefreshIcon } from '@heroicons/vue/solid'
import { addUser } from '../../../api/admin'

export default {
  name: 'UserAdd',
  components: {
    BaseInput,
    RefreshIcon,
  },
  data() {
    return {
      user: {
        email: '',
        password: '',
        first_name: '',
        last_name: '',
        phone: '',
      },
      isAdding: false,
    }
  },
  methods: {
    handleSubmit() {
      this.isAdding = true
      addUser(this.user)
        .then(({ data }) => {
          console.log(data)
          this.isAdding = false
        })
        .catch((e) => {
          console.log(e)
          this.isAdding = false
        })
    },
  },
}
</script>

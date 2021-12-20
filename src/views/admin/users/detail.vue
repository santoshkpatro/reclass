<template>
  <h1>User Detail {{ user_id }}</h1>
  <form v-if="user" @submit.prevent="updateUserDetails">
    <BaseInput label="Email" disabled :value="user.email" />
    <BaseInput label="First Name" v-model="user.first_name" />
    <BaseInput label="Last Name" v-model="user.last_name" />
    <BaseInput label="Phone" v-model="user.phone" />
    <p class="fw-bold mt-3">Roles</p>
    <BaseCheckbox
      label="Instructor?"
      v-model="user.is_instructor"
      class="my-2"
    />
    <BaseToggle label="Active?" v-model="user.is_active" class="my-2" />
    <BaseSelect label="Gender" v-model="user.gender" :options="gender" />
    <button
      class="btn btn-primary mt-3"
      type="submit"
      :disabled="isUpdateLoading"
    >
      <span
        v-if="isUpdateLoading"
        class="spinner-border spinner-border-sm me-2"
        role="status"
        aria-hidden="true"
      ></span>
      <span>Update</span>
    </button>
  </form>
</template>

<script>
import { getUser, updateUser } from '@/api/admin'
import BaseInput from '@/views/base/BaseInput.vue'
import BaseCheckbox from '@/views/base/BaseCheckbox.vue'
import BaseSelect from '@/views/base/BaseSelect.vue'
import BaseToggle from '@/views/base/BaseToggle.vue'

export default {
  name: 'AdminUserDetail',
  props: ['user_id'],
  data() {
    return {
      user: null,
      isUpdateLoading: false,
      gender: ['Male', 'Female'],
    }
  },
  methods: {
    loadUserDetail(user_id) {
      getUser(user_id)
        .then(({ data }) => {
          this.user = data
        })
        .catch((e) => {
          console.log(e)
        })
    },
    updateUserDetails() {
      this.isUpdateLoading = true
      setTimeout(() => {
        updateUser(this.user_id, this.user)
          .then(({ data }) => {
            this.user = data
            this.isUpdateLoading = false
          })
          .catch((e) => {
            console.log(e)
            this.isUpdateLoading = false
          })
      }, 3000)
    },
  },
  mounted() {
    this.loadUserDetail(this.user_id)
  },
  components: { BaseInput, BaseCheckbox, BaseSelect },
}
</script>

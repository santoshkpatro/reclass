<template>
  <button
    class="btn btn-primary"
    type="button"
    data-bs-toggle="offcanvas"
    data-bs-target="#offcanvasRight"
    aria-controls="offcanvasRight"
  >
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="16"
      height="16"
      fill="currentColor"
      class="bi bi-plus"
      viewBox="0 0 16 16"
    >
      <path
        d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"
      />
    </svg>
  </button>

  <div
    class="offcanvas offcanvas-end"
    tabindex="-1"
    id="offcanvasRight"
    aria-labelledby="offcanvasRightLabel"
  >
    <div class="offcanvas-header">
      <h5 id="offcanvasRightLabel">Add User</h5>
      <button
        type="button"
        class="btn-close text-reset"
        data-bs-dismiss="offcanvas"
        aria-label="Close"
      ></button>
    </div>
    <div class="offcanvas-body">
      <form @submit.prevent="addNewUser">
        <BaseInput
          label="Email"
          name="email"
          v-model="user.email"
          required="true"
        />
        <BaseInput
          label="First Name"
          name="first_name"
          v-model="user.first_name"
          required="true"
        />
        <BaseInput
          label="Password"
          name="password"
          type="password"
          v-model="user.password"
        />

        <div class="d-grid gap-2 my-3">
          <button class="btn btn-primary"><span> Add </span></button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { addUser } from '@/api/admin.js'

export default {
  emits: ['newUser'],
  data() {
    return {
      showMenu: false,
      user: {
        email: null,
        password: null,
        first_name: null,
        last_name: null,
        avatar: null,
        gender: null,
        phone: null,
        password_reset_required: false,
        is_active: true,
      },
    }
  },
  methods: {
    addNewUser() {
      //   console.log(this.user)
      addUser(this.user)
        .then(({ data }) => {
          console.log(data)
          this.$emit('newUser')
        })
        .catch((e) => {
          console.log(e)
        })
    },
  },
}
</script>

<style></style>

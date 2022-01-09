<template>
  <button
    class="btn btn-outline-success btn-sm"
    type="button"
    data-bs-toggle="offcanvas"
    data-bs-target="#offcanvasRight"
    aria-controls="offcanvasRight"
  >
    Add
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="20"
      height="20"
      fill="currentColor"
      class="bi bi-plus"
      viewBox="0 0 16 20"
    >
      <path
        d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"
      />
    </svg>
  </button>

  <div
    class="offcanvas offcanvas-end bg-dark"
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
          label="Last Name"
          name="last_name"
          v-model="user.last_name"
        />
        <BaseInput
          label="Password"
          name="password"
          type="password"
          v-model="user.password"
        />
        <BaseToggle
          label="Active"
          name="is_active"
          v-model="user.is_active"
          class="my-2"
        />
        <BaseToggle
          label="Password Reset"
          name="password_reset_required"
          v-model="user.password_reset_required"
          class="my-2"
        />
        <p class="fw-bold">Role</p>
        <BaseCheckbox
          label="Instructor?"
          name="is_instructor"
          v-model="user.is_instructor"
        />
        <div class="d-grid gap-2 my-3">
          <button class="btn btn-success btn-sm">
            <span
              class="spinner-border spinner-border-sm me-2"
              role="status"
              aria-hidden="true"
              v-if="isAdding"
            ></span>
            <span> Add </span>
          </button>
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
      isAdding: false,
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
        is_instructor: false,
      },
    }
  },
  methods: {
    addNewUser() {
      this.isAdding = true
      addUser(this.user)
        .then(({ data }) => {
          console.log(data)
          this.$emit('newUser')
        })
        .catch((e) => {
          console.log(e)
        })
        .finally(() => (this.isAdding = false))
    },
  },
}
</script>

<style></style>

<template>
  <h1>User Detail {{ user_id }}</h1>
  <div class="row">
    <div class="col-8">
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
    </div>
    <div class="col-4">
      <div class="text-center" v-if="user">
        <img :src="user.avatar" />
        <p>Change avatar?</p>
        <input
          type="file"
          class="form-control my-3"
          id="inputGroupFile04"
          aria-describedby="inputGroupFileAddon04"
          aria-label="Upload"
          @change="newAvatar = $event.target.files[0]"
        />
        <button
          class="btn btn-primary btn-sm"
          @click="userAvatarChange"
          :disabled="isAvatarUploading"
        >
          <span
            class="spinner-border spinner-border-sm me-2"
            role="status"
            aria-hidden="true"
            v-if="isAvatarUploading"
          ></span>
          <span v-if="isAvatarUploading"
            >{{ avatarUploadingProgress }}% Updating</span
          >
          <span v-if="!isAvatarUploading"> Update </span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { getUser, updateUser, updateUserAvatar } from '@/api/admin'
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
      newAvatar: null,
      gender: ['Male', 'Female'],
      isAvatarUploading: false,
      avatarUploadingProgress: 0,
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
    processAvatar(event) {
      this.newAvatar = event.target.files[0]
    },
    userAvatarChange() {
      this.isAvatarUploading = true
      let formData = new FormData()
      formData.append('file', this.newAvatar)
      updateUserAvatar(this.user_id, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        onUploadProgress: function (progressEvent) {
          this.avatarUploadingProgress = parseInt(
            Math.round((progressEvent.loaded / progressEvent.total) * 100)
          )
        }.bind(this),
      })
        .then(({ data }) => {
          this.isAvatarUploading = false
          this.user.avatar = data.avatar
          this.newAvatar = null
        })
        .catch((e) => {
          console.log(e)
        })
        .finally(() => {
          this.isAvatarUploading = false
        })
    },
  },
  mounted() {
    this.loadUserDetail(this.user_id)
  },
  components: { BaseInput, BaseCheckbox, BaseSelect },
}
</script>

<style>
img {
  border: solid 1px black;
  border-radius: 50%;
  height: 100px;
  width: 100px;
}
</style>

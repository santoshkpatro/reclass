<template>
  <div v-if="isLoading">
    <Placeholder />
  </div>
  <div v-else>
    <h1>User Detail {{ user_id }}</h1>
    <form v-if="user" @submit.prevent="updateUserDetails">
      <div class="row">
        <div class="col-8">
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
            class="btn btn-primary btn-sm"
            @click="userAvatarChange"
            :disabled="isAvatarUploading"
            type="submit"
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
          </div>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import { getUser, updateUser, updateUserAvatar } from '@/api/admin'
import Placeholder from './_placeholder.vue'

export default {
  name: 'AdminUserDetail',
  props: ['user_id'],
  components: {
    Placeholder,
  },
  data() {
    return {
      isLoading: true,
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
      if (this.newAvatar) {
        this.userAvatarChange()
      }

      updateUser(this.user_id, this.user)
        .then(({ data }) => {
          this.user = data
          this.isUpdateLoading = false
        })
        .catch((e) => {
          console.log(e)
          this.isUpdateLoading = false
        })
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
    try {
      this.loadUserDetail(this.user_id)
    } catch (e) {
      console.log(e)
    } finally {
      this.isLoading = false
    }
  },
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

<template>
  <div v-if="isLoading">
    <Placeholder />
  </div>
  <div v-else>
    <h1>User Detail {{ user_id }}</h1>

    <div class="row">
      <div class="col-8">
        <form @submit.prevent="updateUserDetail">
          <BaseInput
            label="Email"
            v-model="user.email"
            name="email"
            disabled="true"
          />
          <BaseInput
            label="First Name"
            v-model="user.first_name"
            name="first_name"
          />
          <BaseInput
            label="Last Name"
            v-model="user.last_name"
            name="last_name"
          />
          <BaseInput label="Phone" v-model="user.phone" name="phone" />
          <BaseSelect
            v-model="user.gender"
            :options="['Male', 'Female']"
            label="Gender"
          />
          <BaseToggle class="my-3" label="Active" v-model="user.is_active" />
          <BaseToggle
            class="my-3"
            label="Password Reset"
            v-model="user.password_reset_required"
          />
          <p class="fw-bold">Role</p>
          <BaseCheckbox label="Instructor" v-model="user.is_instructor" />
          <div class="d-grid gap-2 mt-3">
            <button
              class="btn btn-success btn-sm"
              :disabled="isUpdating"
              type="submit"
            >
              <span
                class="spinner-border spinner-border-sm me-2"
                role="status"
                aria-hidden="true"
                v-if="isUpdating"
              ></span>
              <span v-if="isUpdating">{{ uploadProgress }} %</span>
              <span>Update</span>
            </button>
          </div>
        </form>
      </div>
      <div class="col-4 text-center">
        <img :src="resource(user.avatar)" alt="NA" />
        <div class="image-upload">
          <label for="file-input">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="25"
              height="25"
              fill="currentColor"
              class="bi bi-pencil-square"
              viewBox="0 0 16 16"
            >
              <path
                d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"
              />
              <path
                fill-rule="evenodd"
                d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"
              />
            </svg>
          </label>
          <input
            id="file-input"
            type="file"
            @change="newUserAvatar = $event.target.files[0]"
          />
          <button
            class="btn btn-dark btn-sm"
            :disabled="!newUserAvatar"
            @click="updateUserAvatar"
          >
            Update
          </button>
        </div>
      </div>
    </div>
    <hr />
    <div class="mt-3">
      <div class="row">
        <div class="col-6">
          <h5>Enrolled Subjects</h5>
          <ul class="list-group">
            <li
              class="list-group-item"
              v-for="enrollment in user.enrolled"
              :key="enrollment.id"
            >
              {{ enrollment.subject.title }}
              <span class="badge bg-secondary">{{
                enrollment.subject.subject_code
              }}</span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import {
  getUser,
  updateUser,
  localFileUpload,
  getAvatarUploadUrl,
} from '@/api/admin'
import Placeholder from './_placeholder.vue'
import BaseSelect from '../../base/BaseSelect.vue'

export default {
  name: 'AdminUserDetail',
  components: {
    Placeholder,
    BaseSelect,
  },
  props: ['user_id'],
  data() {
    return {
      isLoading: true,
      user: null,
      isUpdating: false,
      uploadProgress: 0,
      newUserAvatar: null,
    }
  },
  methods: {
    resource(url) {
      return process.env.VUE_APP_MEDIA_URL + '/' + url
    },
    updateUserAvatar() {
      var file = this.newUserAvatar
      getAvatarUploadUrl(this.user_id, file.type)
        .then(({ data }) => {
          const resource_url = data.resource_url
          const upload_url = data.upload_url

          switch (process.env.NODE_ENV) {
            case 'production':
              var http = axios.create()
              delete http.defaults.headers.common['Authorization']
              http
                .put(upload_url, file)
                .then(({ data }) => {
                  this.user.avatar = resource_url

                  this.updateUserDetail()
                  this.newUserAvatar = null
                })
                .catch((e) => {
                  console.log(e)
                })
              break

            default:
              localFileUpload(resource_url, file)
                .then(({ data }) => {
                  this.user.avatar = resource_url

                  this.updateUserDetail()
                  this.newUserAvatar = null
                })
                .catch((e) => {
                  console.log(e)
                })
              break
          }
        })
        .catch((e) => {
          console.log(e)
        })
        .finally(() => {})
    },
    updateUserDetail() {
      this.isUpdating = true

      updateUser(this.user_id, this.user)
        .then(({ data }) => {
          this.user = data
        })
        .catch((e) => {
          console.log(e)
        })
        .finally(() => (this.isUpdating = false))

      // Check for presence new user avatar
      // if (!this.newUserAvatar) {
      //   this.updateUserInfo()

      //   this.isUpdating = false
      //   return
      // }

      // this.updateUserAvatar()
      // this.updateUserInfo()

      // this.isUpdating = true
      // if (this.newUserAvatar) {
      //   const extension = this.newUserAvatar.type.split('/')[1]
      //   const filename = `${uuidv4()}.${extension}`
      //   const location = 'avatars/'

      //   getUploadUrl(filename, { location: location })
      //     .then(({ data }) => {
      //       var file = this.newUserAvatar
      //       var http = axios.create()
      //       console.log(file.type)
      //       delete http.defaults.headers.common['Authorization']
      //       http
      //         .put(data, file, {
      //           headers: {
      //             'Content-Type': file.type,
      //           },
      //           onUploadProgress: function (progressEvent) {
      //             this.uploadProgress = parseInt(
      //               Math.round(
      //                 (progressEvent.loaded / progressEvent.total) * 100
      //               )
      //             )
      //           }.bind(this),
      //         })
      //         .then((res) => {
      //           this.user.avatar = location + filename
      //           updateUser(this.user_id, this.user)
      //             .then(({ data }) => {
      //               this.user = data
      //             })
      //             .catch((e) => {
      //               console.log(e)
      //             })

      //           this.isUpdating = false
      //         })
      //         .catch()
      //     })
      //     .catch((e) => console.log(e))
      // } else {
      //   updateUser(this.user_id, this.user)
      //     .then(({ data }) => {
      //       this.user = data
      //     })
      //     .catch((e) => {
      //       console.log(e)
      //     })
      //     .finally(() => (this.isUpdating = false))
      // }
    },
  },
  mounted() {
    getUser(this.user_id)
      .then(({ data }) => {
        this.user = data
      })
      .catch((e) => {
        console.log(e)
      })
      .finally(() => {
        this.isLoading = false
      })
  },
}
</script>

<style scoped>
img {
  border: solid 1px black;
  border-radius: 50%;
  height: 100px;
  width: 100px;
}

.image-upload > input {
  display: none;
}
</style>

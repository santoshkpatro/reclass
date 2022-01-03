<template>
  <div class="d-flex justify-content-between mb-2">
    <div class="d-flex align-items-center">
      <h3>Users</h3>
      <input
        class="form-control bg-transparent mx-2 text-white"
        type="search"
        placeholder="Search user"
        aria-label="Search"
        @input="handleSearch"
      />
      <BaseSelect
        :options="resultsPerPage"
        v-model="limit"
        @click="loadUsers()"
      />
    </div>
    <div>
      <UserAddForm @newUser="loadUsers" />
    </div>
  </div>
  <table class="table text-white">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Details</th>
        <th scope="col">Active?</th>
        <th scope="col">Created on</th>
        <th scope="col">Role</th>
        <th scope="col">Enrolled Subjects</th>
        <th scope="col">Action</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="user in list.users">
        <th scope="row">
          <input
            class="form-check-input"
            type="checkbox"
            id="checkboxNoLabel"
            value=""
          />
        </th>
        <td class="d-flex flex-column">
          <span>
            <router-link
              class="text-white"
              :to="{ name: 'AdminUserDetail', params: { user_id: user.id } }"
            >
              {{ user.first_name }} {{ user.last_name }}
            </router-link>
          </span>
          <span class="fw-light">
            {{ user.email }}
          </span>
        </td>
        <td>
          <div class="form-check form-switch">
            <input
              @click="updateUserStatus(user)"
              class="form-check-input"
              type="checkbox"
              role="switch"
              id="switch1"
              data-on="Yes"
              data-off="No"
              :checked="user.is_active"
            />
          </div>
        </td>
        <td>{{ formatDate(user.created_at) }}</td>
        <td>
          <span class="badge bg-dark" v-if="!user.is_instructor">student</span>
          <span class="badge bg-success" v-else>instructor</span>
        </td>
        <td>
          <span
            class="badge bg-primary me-1"
            type="button"
            v-for="enrollment in user.enrolled"
            :key="enrollment.id"
            data-bs-toggle="tooltip"
            data-bs-placement="top"
            :title="enrollment.subject.title"
            >{{ enrollment.subject.subject_code }}</span
          >
        </td>
        <td>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            class="bi bi-trash"
            viewBox="0 0 16 16"
          >
            <path
              d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"
            />
            <path
              fill-rule="evenodd"
              d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"
            />
          </svg>
        </td>
      </tr>
    </tbody>
  </table>
  <div class="d-flex justify-content-between">
    <button
      class="btn btn-sm btn-dark"
      :disabled="offset === 0"
      @click="handlePrevious"
    >
      Previous
    </button>
    <button
      class="btn btn-sm btn-dark"
      @click="handleNext"
      :disabled="limit + offset >= list.count"
    >
      Next
    </button>
  </div>
</template>

<script>
import UserAddForm from './_add.vue'
import axios from 'axios'
import _ from 'lodash'
import dayjs from 'dayjs'
import { getUsers, updateUser } from '@/api/admin'
import BaseSelect from '../../base/BaseSelect.vue'

getUsers
export default {
  name: 'AdminUsers',
  components: {
    UserAddForm,
    BaseSelect,
  },
  data() {
    return {
      list: {
        count: 0,
        users: [],
      },
      toast: null,
      limit: 20,
      offset: 0,
      cancelToken: undefined,
      search: null,
      resultsPerPage: [20, 50, 100],
    }
  },
  methods: {
    formatDate(date) {
      return new dayjs(date).format('DD-MM-YYYY')
    },
    resource_url(url) {
      return process.env.VUE_APP_MEDIA_URL + '/' + url
    },
    loadUsers(query = {}) {
      getUsers({
        ...query,
        limit: this.limit,
        offset: this.offset,
        search: this.search,
      })
        .then(({ data }) => {
          this.list.count = data.count
          this.list.users = data.results
        })
        .catch((e) => {
          console.log(e)
        })
    },
    updateUserStatus(user) {
      updateUser(user.id, { is_active: !user.is_active })
        .then(({ data }) => {
          console.log(data)
        })
        .catch((e) => {
          console.log(e)
        })
    },
    handleSearch: _.debounce(function (e) {
      if (typeof this.cancelToken != typeof undefined) {
        this.cancelToken.cancel('Cancelling previous request')
      }
      this.cancelToken = axios.CancelToken.source()

      this.offset = 0
      this.search = e.target.value
      this.loadUsers({ cancelToken: this.cancelToken.token })
    }, 500),
    handleNext() {
      this.offset = this.offset + this.limit
      this.loadUsers()
    },
    handlePrevious() {
      this.offset = this.offset - this.limit
      this.loadUsers()
    },
  },
  mounted() {
    this.loadUsers()
  },
}
</script>

<style scoped>
a {
  text-decoration: none;
  color: black;
}

a:hover {
  text-decoration: underline;
}

.table > tbody > tr > td {
  vertical-align: middle;
}
</style>

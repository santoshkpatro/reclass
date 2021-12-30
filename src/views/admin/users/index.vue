<template>
  <div class="d-flex justify-content-between mb-2">
    <div class="d-flex align-items-center">
      <h3>Users</h3>
      <input
        class="form-control ms-2"
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
  <table class="table">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Details</th>
        <th scope="col">Active?</th>
        <th scope="col">Created on</th>
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
</style>

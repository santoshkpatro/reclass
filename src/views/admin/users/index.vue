<template>
  <div class="d-flex justify-content-between mb-2">
    <h3>Users</h3>
    <div>
      <input
        class="form-control"
        type="search"
        placeholder="Search user"
        aria-label="Search"
        @input="handleSearch"
      />
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
            aria-label="..."
          />
        </th>
        <td class="d-flex flex-column">
          <span>
            <router-link
              :to="{ name: 'AdminUserDetail', params: { user_id: user.id } }"
            >
              {{ user.first_name }}
            </router-link>
          </span>
          <span class="fw-light">
            {{ user.email }}
          </span>
        </td>
        <td>
          <div class="form-check form-switch">
            <input
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
</template>

<script>
import axios from 'axios'
import _ from 'lodash'
import dayjs from 'dayjs'
import { getUsers } from '@/api/admin'

getUsers
export default {
  name: 'AdminUsers',
  data() {
    return {
      list: {
        count: 0,
        users: [],
      },
    }
  },
  methods: {
    formatDate(date) {
      return new dayjs(date).format('DD-MM-YYYY')
    },
    loadUsers(query = {}) {
      getUsers(query)
        .then(({ data }) => {
          this.list.count = data.count
          this.list.users = data.results
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
      this.loadUsers(
        { search: e.target.value },
        { cancelToken: this.cancelToken.token }
      )
    }, 500),
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

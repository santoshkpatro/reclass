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
      <!-- <BaseSelect
        :options="resultsPerPage"
        v-model="limit"
        @click="loadUsers()"
      /> -->
    </div>
    <div>
      <UserAddForm @newUser="loadUsers" />
    </div>
  </div>

  <!-- Users Table -->
  <List
    v-if="list.users"
    :users="list.users"
    @onUpdate="handleUpdate"
    @onDelete="handleDelete"
  />

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
import List from './_list.vue'
import axios from 'axios'
import _ from 'lodash'
import { getUsers, updateUser, deleteUser } from '@/api/admin'

getUsers
export default {
  name: 'AdminUsers',
  components: {
    UserAddForm,
    List,
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
    handleDelete(id) {
      deleteUser(id)
        .then(() => {
          this.list.users = this.list.users.filter((user) => user.id !== id)
        })
        .catch((e) => console.log(e))
    },
    handleUpdate(userId, newData) {
      console.log(userId)
      console.log(newData)
      updateUser(userId, newData)
        .then(({ data }) => {
          console.log(data)
        })
        .catch((e) => {
          console.log(e)
        })
    },
  },
  mounted() {
    this.loadUsers()
  },
}
</script>

<style scoped></style>

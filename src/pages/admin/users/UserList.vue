<template>
  <div>
    <div v-if="isLoading">
      <Placeholder />
    </div>

    <div class="flex flex-col">
      <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
          <div
            class="
              shadow
              overflow-hidden
              border-b border-gray-200
              sm:rounded-lg
            "
          >
            <table class="min-w-full divide-y divide-gray-200">
              <thead class="bg-gray-50">
                <tr>
                  <th
                    scope="col"
                    class="
                      px-6
                      py-3
                      text-left text-xs
                      font-medium
                      text-gray-500
                      uppercase
                      tracking-wider
                    "
                  >
                    Name
                  </th>
                  <th
                    scope="col"
                    class="
                      px-6
                      py-3
                      text-left text-xs
                      font-medium
                      text-gray-500
                      uppercase
                      tracking-wider
                    "
                  >
                    Phone
                  </th>
                  <th
                    scope="col"
                    class="
                      px-6
                      py-3
                      text-left text-xs
                      font-medium
                      text-gray-500
                      uppercase
                      tracking-wider
                    "
                  >
                    Status
                  </th>
                  <th
                    scope="col"
                    class="
                      px-6
                      py-3
                      text-left text-xs
                      font-medium
                      text-gray-500
                      uppercase
                      tracking-wider
                    "
                  >
                    Instructor
                  </th>
                  <th
                    scope="col"
                    class="
                      px-6
                      py-3
                      text-left text-xs
                      font-medium
                      text-gray-500
                      uppercase
                      tracking-wider
                    "
                  >
                    Created On
                  </th>
                  <th
                    scope="col"
                    class="
                      px-6
                      py-3
                      text-left text-xs
                      font-medium
                      text-gray-500
                      uppercase
                      tracking-wider
                    "
                  >
                    Last Login
                  </th>
                  <th
                    scope="col"
                    class="
                      px-6
                      py-3
                      text-left text-xs
                      font-medium
                      text-gray-500
                      uppercase
                      tracking-wider
                    "
                  >
                    Subjects
                  </th>
                  <th scope="col" class="relative px-6 py-3">
                    <span class="sr-only">Edit</span>
                  </th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="user in users" :key="user.id">
                  <td class="px-6 py-4 whitespace-nowrap">
                    <div class="flex items-center">
                      <div class="flex-shrink-0 h-10 w-10">
                        <img
                          class="h-10 w-10 rounded-full"
                          :src="user.avatar"
                          alt
                        />
                      </div>
                      <div class="ml-4">
                        <div class="text-sm font-medium text-gray-900">
                          {{ user.first_name }} {{ user.last_name }}
                        </div>
                        <div class="text-sm text-gray-500">
                          {{ user.email }}
                        </div>
                      </div>
                    </div>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <span class="text-sm" v-if="user.phone"
                      >+91-{{ user.phone }}</span
                    >
                    <span v-else class="text-sm text-gray-500">No phone</span>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <span
                      v-if="user.is_active === true"
                      class="
                        px-2
                        inline-flex
                        text-xs
                        leading-5
                        font-semibold
                        rounded-full
                        bg-green-100
                        text-green-800
                      "
                      >Active</span
                    >
                    <span
                      v-else
                      class="
                        px-2
                        inline-flex
                        text-xs
                        leading-5
                        font-semibold
                        rounded-full
                        bg-red-100
                        text-red-800
                      "
                      >Not Active</span
                    >
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <span
                      v-if="user.is_instructor === true"
                      class="
                        px-2
                        inline-flex
                        text-xs
                        leading-5
                        font-semibold
                        rounded-full
                        bg-purple-100
                        text-purple-800
                      "
                      >Yes</span
                    >
                    <span
                      v-else
                      class="
                        px-2
                        inline-flex
                        text-xs
                        leading-5
                        font-semibold
                        rounded-full
                        bg-gray-100
                        text-gray-800
                      "
                      >No</span
                    >
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {{ dateFormat(user.created_at) }}
                  </td>
                  <td
                    class="
                      px-6
                      py-4
                      whitespace-nowrap
                      text-sm text-gray-500
                      w-24
                    "
                  >
                    <span v-if="user.last_login">{{
                      dateFormat(user.last_login)
                    }}</span>
                    <span v-else>Not logged in yet</span>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <span
                      class="px-2 text-xs leading-5 font-semibold rounded-full"
                      :class="{
                        'bg-green-100 text-green-800': e.is_active === true,
                        'bg-red-100 text -red-800': e.is_active === false,
                      }"
                      v-for="e in user.enrolled"
                      :key="e.id"
                      >{{ e.subject.title }}</span
                    >
                  </td>
                  <td
                    class="
                      px-6
                      py-4
                      whitespace-nowrap
                      text-right text-sm
                      font-medium
                    "
                  >
                    <router-link
                      :to="{ name: 'UserDetail', params: { id: user.id } }"
                      class="text-indigo-600 hover:text-indigo-900"
                      >Edit</router-link
                    >
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import dayjs from 'dayjs'
import axios from 'axios'
import { getUsers, updateUser, addUser } from '../../../api/admin'
// import BaseInput from '../../../components/base/BaseInput';
import Placeholder from '../../../components/admin/users/Placeholder.vue'

export default {
  name: 'UserList',
  components: {
    Placeholder,
  },
  data() {
    return {
      isLoading: true,
      users: [],
      next: null,
      previous: null,
      cancelToken: undefined,
      searchUser: null,
      addButtonLoading: false,
      newUser: {
        email: '',
        first_name: '',
        last_name: '',
        password: '',
        gender: '',
        phone: '',
        is_active: true,
        password_reset_false: false,
        is_instructor: false,
      },
    }
  },
  mounted() {
    getUsers()
      .then(({ data }) => {
        this.users = data.results
        this.next = data.next
        this.previous = data.previous
        this.isLoading = false
      })
      .catch((e) => console.log(e))
  },
  methods: {
    dateFormat(value) {
      return new dayjs(value).format('DD-MM-YYYY')
    },
    handleNext() {
      this.isLoading = true

      axios
        .get(this.next)
        .then(({ data }) => {
          this.users = data.results
          this.next = data.next
          this.previous = data.previous

          this.isLoading = false
        })
        .catch((e) => {
          this.isLoading = false
        })
    },
    handlePrevious() {
      this.isLoading = true

      axios
        .get(this.previous)
        .then(({ data }) => {
          this.users = data.results
          this.next = data.next
          this.previous = data.previous

          this.isLoading = false
        })
        .catch((e) => {
          this.isLoading = false
        })
    },
    handleUpdate(user, data) {
      updateUser(user.id, data)
        .then(({ data }) => {
          // console.log(data);
          const userIndex = this.users.findIndex((e) => e.id === data.id)
          console.log(userIndex)
          this.users[userIndex] = data
        })
        .catch((e) => console.log('Error', e))
    },
    handleSearch: _.debounce(function (e) {
      if (typeof this.cancelToken != typeof undefined) {
        this.cancelToken.cancel('Cancelling previous request')
      }

      this.cancelToken = axios.CancelToken.source()

      getUsers(
        { search: e.target.value },
        { cancelToken: this.cancelToken.token }
      )
        .then(({ data }) => {
          this.users = data.results
        })
        .catch((e) => console.log(e))
    }, 500),
    addUser() {
      this.addButtonLoading = true

      addUser(this.newUser)
        .then(({ data }) => {
          this.addButtonLoading = false
          this.$toast('New user added successfully!')
        })
        .catch((e) => {
          console.log(e)
          this.addButtonLoading = false
        })
    },
  },
}
</script>
<style>
a {
  text-decoration: none;
  color: black;
}

a:hover {
  text-decoration: underline;
}

.avatar {
  border: 1.5px solid;
}

td {
  vertical-align: middle;
}

.bi {
  font-size: 45px;
}
.bi {
  font-size: 45px;
}
</style>

<template>
  <div>
    <div v-if="isLoading">
      <Placeholder />
    </div>
    <div class="mt-3" v-else>
      <div class="d-flex justify-content-between">
        <button
          class="btn btn-dark"
          data-bs-toggle="offcanvas"
          data-bs-target="#offcanvasRight"
          aria-controls="offcanvasRight"
        >
          Add User
        </button>
        <div>
          <div>
            <input
              class="form-control me-2"
              type="search"
              placeholder="Search"
              aria-label="Search"
              @keyup="handleSearch"
            />
          </div>
        </div>
      </div>
      <table class="table table-borderless table-hover mt-3">
        <thead>
          <tr>
            <th scope="col"></th>
            <th scope="col">Name</th>
            <th scope="col">Email</th>
            <th scope="col">Created On</th>
            <th scope="col">Active</th>
            <th scope="col">Password Reset</th>
            <th scope="col">Instructor</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in users" :key="user.id">
            <th scope="row">
              <img
                :src="user.avatar"
                class="rounded-circle avatar"
                height="45"
                width="45"
                :alt="user.first_name"
                v-if="user.avatar"
              />
              <i class="bi bi-person-circle" v-else></i>
            </th>
            <td>
              <router-link
                :to="{ name: 'UserDetail', params: { id: user.id } }"
              >
                <span>{{ user.first_name }} {{ user.last_name }}</span>
              </router-link>
            </td>
            <td>{{ user.email }}</td>
            <td>{{ user.created_at | format }}</td>
            <td>
              <div class="form-check form-switch">
                <input
                  class="form-check-input"
                  type="checkbox"
                  :checked="user.is_active"
                  @click="handleUpdate(user, { is_active: !user.is_active })"
                />
              </div>
            </td>
            <td>
              <div class="form-check form-switch">
                <input
                  class="form-check-input"
                  type="checkbox"
                  :checked="user.password_reset_required"
                  @click="
                    handleUpdate(user, {
                      password_reset_required: !user.password_reset_required,
                    })
                  "
                />
              </div>
            </td>
            <td>
              <div class="form-check form-switch">
                <input
                  class="form-check-input"
                  type="checkbox"
                  :checked="user.is_instructor"
                  @click="
                    handleUpdate(user, {
                      is_instructor: !user.is_instructor,
                    })
                  "
                />
              </div>
            </td>
          </tr>
        </tbody>
      </table>

      <!-- Pagination -->
      <div class="d-flex justify-content-between">
        <button
          class="btn btn-sm btn-outline-dark"
          :disabled="!previous"
          @click="handlePrevious"
        >
          Previous
        </button>
        <button
          class="btn btn-sm btn-outline-dark"
          :disabled="!next"
          @click="handleNext"
        >
          Next
        </button>
      </div>

      <!-- New User  -->
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
          <form @submit.prevent="addUser">
            <BaseInput
              name="email"
              placeholder="sample@ex.com"
              label="Email address"
              v-model="newUser.email"
            />
            <BaseInput
              name="first_name"
              label="First Name"
              v-model="newUser.first_name"
            />
            <BaseInput
              name="last_name"
              label="Last Name"
              v-model="newUser.last_name"
            />
            <BaseInput
              name="password"
              placeholder="******"
              label="Password"
              type="password"
              v-model="newUser.password"
            />

            <div class="d-grid gap-2 mt-3">
              <button class="btn btn-dark" :disabled="addButtonLoading">
                <span
                  v-if="addButtonLoading"
                  class="spinner-grow spinner-grow-sm"
                  role="status"
                  aria-hidden="true"
                ></span>
                <span v-if="addButtonLoading">Adding</span>
                <span v-if="!addButtonLoading">Add</span>
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash';
import dayjs from 'dayjs';
import axios from 'axios';
import { getUsers, updateUser, addUser } from '@/api/admin';
import BaseInput from '@/components/base/BaseInput';
import Placeholder from '@/components/admin/users/Placeholder.vue';

export default {
  name: 'UserList',
  components: {
    BaseInput,
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
    };
  },
  filters: {
    format: function (value) {
      return new dayjs(value).format('DD-MM-YYYY');
    },
  },
  mounted() {
    getUsers()
      .then(({ data }) => {
        this.users = data.results;
        this.next = data.next;
        this.previous = data.previous;
        this.isLoading = false;
      })
      .catch((e) => console.log(e));
  },
  methods: {
    handleNext() {
      this.isLoading = true;

      axios
        .get(this.next)
        .then(({ data }) => {
          this.users = data.results;
          this.next = data.next;
          this.previous = data.previous;

          this.isLoading = false;
        })
        .catch((e) => {
          this.isLoading = false;
        });
    },
    handlePrevious() {
      this.isLoading = true;

      axios
        .get(this.previous)
        .then(({ data }) => {
          this.users = data.results;
          this.next = data.next;
          this.previous = data.previous;

          this.isLoading = false;
        })
        .catch((e) => {
          this.isLoading = false;
        });
    },
    handleUpdate(user, data) {
      updateUser(user.id, data)
        .then(({ data }) => {
          // console.log(data);
          const userIndex = this.users.findIndex((e) => e.id === data.id);
          console.log(userIndex);
          this.users[userIndex] = data;
        })
        .catch((e) => console.log('Error', e));
    },
    handleSearch: _.debounce(function (e) {
      if (typeof this.cancelToken != typeof undefined) {
        this.cancelToken.cancel('Cancelling previous request');
      }

      this.cancelToken = axios.CancelToken.source();

      getUsers(
        { search: e.target.value },
        { cancelToken: this.cancelToken.token }
      )
        .then(({ data }) => {
          this.users = data.results;
        })
        .catch((e) => console.log(e));
    }, 500),
    addUser() {
      this.addButtonLoading = true;

      addUser(this.newUser)
        .then(({ data }) => {
          this.addButtonLoading = false;
          this.$toast('New user added successfully!');
        })
        .catch((e) => {
          console.log(e);
          this.addButtonLoading = false;
        });
    },
  },
};
</script>

<style scoped>
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
</style>
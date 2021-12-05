<template>
  <div class="mt-3">
    <div class="d-flex justify-content-between">
      <h3>Users</h3>
      <button class="btn btn-dark">Add new user</button>
    </div>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Sl</th>
          <th scope="col">Name</th>
          <th scope="col">Email</th>
          <th scope="col">Created On</th>
          <th scope="col">Status</th>
          <th scope="col">Password Reset</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(user, index) in users" :key="user.id">
          <th scope="row">{{ ++index }}</th>
          <td>{{ user.first_name }} {{ user.last_name }}</td>
          <td>{{ user.email }}</td>
          <td>{{ user.created_at }}</td>
          <td>
            <div class="form-check form-switch">
              <input
                class="form-check-input"
                type="checkbox"
                role="switch"
                :checked="user.is_active"
                @click="handleActiveUpdate(user)"
              />
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { getUsers, updateUser } from '@/api/admin';

export default {
  name: 'UserList',
  data() {
    return {
      isLoading: true,
      users: [],
    };
  },
  mounted() {
    getUsers()
      .then(({ data }) => {
        this.users = data.results;
        this.isLoading = false;
      })
      .catch((e) => console.log(e));
  },
  methods: {
    handleActiveUpdate(user) {
      updateUser(user.id, {
        is_active: !user.is_active,
      })
        .then((res) => console.log('Updated'))
        .catch((e) => console.log('Error'));
    },
  },
};
</script>

<style scoped>
</style>
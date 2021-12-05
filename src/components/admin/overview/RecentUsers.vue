<template>
  <div class="card border-2 border-dark">
    <div class="card-body">
      <div class="d-flex justify-content-between">
        <h5>Recent Users</h5>
        <p>
          <router-link :to="{ name: 'UserList' }">
            <span class="badge bg-dark">View All</span>
          </router-link>
        </p>
      </div>
      <ul class="list-group">
        <li class="list-group-item" v-for="user in users" :key="user.id">
          <router-link :to="{ name: 'UserDetail', params: { id: user.id } }">
            {{ user.email }} | {{ user.first_name }} {{ user.last_name }}
          </router-link>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  props: ['users'],
};
</script>

<style scoped>
a {
  text-decoration: none;
  color: black;
}

.list-group-item {
  border-left: none;
  border-right: none;
}

.list-group-item:hover {
  text-decoration: underline;
  cursor: pointer;
}

.blank {
  font-size: 16px;
}
</style>
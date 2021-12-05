<template>
  <div class="card border-2 border-dark">
    <div class="card-body">
      <h5>Recent Users</h5>
      <ul class="list-group">
        <li class="list-group-item" v-for="user in users" :key="user.id">
          {{ user.email }} | {{ user.first_name }} {{ user.last_name }}
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
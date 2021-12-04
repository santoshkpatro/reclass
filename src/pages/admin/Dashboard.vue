<template>
  <div>
    <div class="row">
      <div class="col-3">
        <Sidebar />
      </div>
      <div class="col-9">
        <h1>Hello</h1>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from '@/components/admin/Sidebar.vue';
import { getUsers } from '@/api/admin.js';

export default {
  name: 'AdminDashboard',
  components: {
    Sidebar,
  },
  data() {
    return {
      recentUsers: [],
      totalUsersCount: 0,
    };
  },
  mounted() {
    getUsers()
      .then(({ data }) => {
        this.recentUsers = data.results;
        this.totalUsersCount = data.count;
      })
      .catch((e) => console.log(e));
  },
};
</script>

<style>
</style>
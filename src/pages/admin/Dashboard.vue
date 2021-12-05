<template>
  <div>
    <div class="row">
      <div class="col-2">
        <Sidebar />
      </div>
      <div class="col-9">
        <Topbar />
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from '@/components/admin/Sidebar.vue';
import Topbar from '@/components/admin/Topbar.vue';

export default {
  name: 'AdminDashboard',
  components: {
    Sidebar,
    Topbar,
  },
  data() {
    return {
      recentUsers: [],
      totalUsersCount: 0,
    };
  },
};
</script>

<style>
</style>
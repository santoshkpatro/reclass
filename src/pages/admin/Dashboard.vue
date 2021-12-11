<template>
  <div class="flex flex-wrap">
    <div class="w-1/5">
      <Sidebar />
    </div>
    <div class="px-2">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Sidebar from '../../components/admin/Sidebar.vue';
import Topbar from '../../components/admin/Topbar.vue';

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

<style scoped>
</style>

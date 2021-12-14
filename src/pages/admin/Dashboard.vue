<template>
  <div class="flex h-screen bg-gray-50 dark:bg-gray-900">
      <!-- Desktop sidebar -->
      <Sidebar />

      <!-- main -->
      <div class="flex flex-col flex-1 w-full">
        <main class="h-full overflow-y-auto">
          <div class="container px-6 mx-auto grid">
            <router-view></router-view>
          </div>
        </main>
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
      isSideMenuOpen: false,
      recentUsers: [],
      totalUsersCount: 0,
    };
  },
};
</script>

<style scoped>
</style>

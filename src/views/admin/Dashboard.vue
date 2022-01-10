<template>
  <div class="flex flex-row">
    <Sidebar class="w-56 flex-shrink-0 mr-4" />
    <router-view></router-view>
  </div>
</template>

<script>
import Sidebar from './_sidebar.vue'

export default {
  name: 'AdminDashboard',
  components: {
    Sidebar,
  },
}
</script>

<style scoped></style>

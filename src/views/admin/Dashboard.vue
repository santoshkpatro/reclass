<template>
  <!-- component -->
  <div class="md:flex flex-col md:flex-row md:min-h-screen w-full">
    <Sidebar />
    <div>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Sidebar from './_sidebar.vue'

export default {
  name: 'AdminDashboard',
  data() {
    return {
      open: false,
    }
  },
  components: {
    Sidebar,
  },
  methods: {
    toggleMenu() {
      this.open = !this.open
    },
  },
}
</script>

<style scoped></style>

<template>
  <div class="container-fluid">
    <div class="row">
      <nav
        id="sidebar"
        class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse"
      >
        <!-- sidebar content goes in here -->
        <Sidebar />
      </nav>
      <main class="col-md-9 ml-sm-auto col-lg-10 px-md-4 py-4">
        <router-view></router-view>
      </main>
    </div>
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

<style scoped>
.sidebar {
  position: relative;
  top: 0;
  bottom: 0;
  left: 0;
  z-index: 100;
  /* padding: 90px 0 0; */
  /* box-shadow: inset -1px 0 0 rgba(0, 0, 0, 0.1); */
  z-index: 99;
  height: 100vh;
}

@media (max-width: 767.98px) {
  .sidebar {
    top: 11.5rem;
    padding: 0;
  }
}

.navbar {
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.1);
}

@media (min-width: 767.98px) {
  .navbar {
    top: 0;
    position: sticky;
    z-index: 999;
  }
}

.sidebar .nav-link {
  color: #333;
}

.sidebar .nav-link.active {
  color: #0d6efd;
}
</style>

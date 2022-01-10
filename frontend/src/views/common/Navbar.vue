<template>
  <nav class="navbar navbar-expand-lg navbar-light">
    <div class="container">
      <router-link class="navbar-brand text-white" :to="{ name: 'Home' }"
        >Reclass</router-link
      >
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link
              class="nav-link active text-white"
              aria-current="page"
              :to="url"
            >
              Dashboard
            </router-link>
          </li>
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle text-white"
              href="#"
              id="navbarDropdown"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              Action
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><hr class="dropdown-divider" /></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </li>
        </ul>
        <ul class="navbar-nav">
          <router-link
            class="btn btn-dark btn-sm"
            v-if="!loggedIn"
            :to="{ name: 'Login' }"
            >Login</router-link
          >
          <button
            class="btn btn-dark btn-sm"
            v-if="loggedIn"
            @click="$store.dispatch('logout')"
          >
            Logout
          </button>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Navbar',
  computed: {
    ...mapGetters(['loggedIn', 'role']),
    url: function () {
      return '/' + this.role
    },
  },
}
</script>

<style scoped>
.navbar {
  border-bottom: 1px solid;
  border-color: #2a2a2a;
}
</style>

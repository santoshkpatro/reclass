<template>
  <nav class="h-16 flex items-center bg-white filter drop-shadow sticky top-0">
    <div
      class="
        container container
        flex
        justify-between
        items-center
        mx-6
        sm:mx-auto
      "
    >
      <div class="text-2xl font-semibold">Reclass.</div>
      <ul class="flex align-items gap-x-2 sm:gap-x-6">
        <li><a href="">Home</a></li>
        <li><a href="">Dashboard</a></li>
        <li>
          <router-link to="/auth/login" class="btn-primary">Login</router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'Navbar',
  computed: {
    ...mapGetters(['loggedIn']),
  },
};
</script>

<style>
</style>
<template>
  <Navbar />
  <router-view></router-view>
</template>

<script>
import Navbar from '@/views/common/Navbar.vue'

export default {
  name: 'Auth',
  components: {
    Navbar,
  },
}
</script>

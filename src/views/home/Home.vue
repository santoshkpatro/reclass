<template>
  <Navbar />
  <router-view></router-view>
</template>

<script>
import Navbar from '@/views/common/Navbar'

export default {
  name: 'Home',
  components: {
    Navbar,
  },
}
</script>

<template>
  <Navbar />
  <div class="container mt-2">
    <h1>Welcome to Reclass</h1>
    <p>Classroom engagement platform</p>
  </div>
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

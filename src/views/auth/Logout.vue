<template></template>

<script>
import { mapGetters } from 'vuex'

export default {
  computed: {
    ...mapGetters(['loggedIn']),
  },
  created() {
    if (this.loggedIn) {
      this.$store.dispatch('logout')
    }
  },
}
</script>

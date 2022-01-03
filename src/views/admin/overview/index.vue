<template>
  <p class="text-xl">Overview</p>
  <!-- <Count title="Users" :count="users.count" class="col-3 my-3" /> -->
  <!-- <Count title="Subjects" :count="subjects.count" class="col-3 my-3" /> -->
</template>

<script>
import { getUsers, getSubjects } from '@/api/admin.js'
import Count from './_count.vue'

export default {
  name: 'AdminOverview',
  components: {
    Count,
  },
  data() {
    return {
      users: {
        count: 0,
        list: [],
      },
      subjects: {
        count: 0,
        list: [],
      },
    }
  },
  mounted() {
    getUsers().then(({ data }) => {
      this.users.count = data.count
      this.users.list = data.results
    })

    getSubjects().then(({ data }) => {
      this.subjects.count = data.count
      this.subjects.list = data.results
    })
  },
}
</script>

<template>
  <h3>Subjects</h3>
</template>

<script>
import { getSubjects } from '@/api/admin.js'

export default {
  name: 'AdminSubjects',
  data() {
    return {
      list: {
        count: 0,
        subjects: [],
      },
    }
  },
  mounted() {
    getSubjects()
      .then(({ data }) => {
        this.list.count = data.count
        this.list.subjects = data.results
      })
      .catch((e) => console.log(e))
  },
}
</script>

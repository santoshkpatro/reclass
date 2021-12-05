<template>
  <div>
    <h1>{{ id }}</h1>
  </div>
</template>

<script>
import { getUserDetail } from '@/api/admin.js';

export default {
  props: ['id'],
  data() {
    return {
      user: null,
    };
  },
  mounted() {
    getUserDetail(this.id)
      .then(({ data }) => console.log(data))
      .catch((e) => console.log(e));
  },
};
</script>

<style>
</style>
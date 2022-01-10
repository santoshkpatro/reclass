<template>
  <div class="card bg-dark">
    <div class="card-body">
      <h5>{{ title }}</h5>
      <h3>{{ count }}</h3>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
    },
    count: {
      type: Number,
      default: 0,
    },
  },
}
</script>

<style scoped>
.card {
  border-radius: 8px;
}
</style>

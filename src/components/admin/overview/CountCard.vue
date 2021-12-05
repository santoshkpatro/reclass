<template>
  <div class="card border-1 border-dark">
    <div class="card-body">
      <h5 class="text-center">{{ name }}</h5>
      <div class="count">
        <p class="text-center">{{ count }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    name: {
      type: String,
      required: true,
    },
    count: {
      type: Number,
      default: 0,
    },
  },
};
</script>

<style scoped>
.count {
  font-size: 2.5rem;
}

.card:hover {
  background: black;
  color: white;
}
</style>
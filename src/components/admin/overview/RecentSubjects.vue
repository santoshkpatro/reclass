<template>
  <div class="card border-2 border-dark">
    <div class="card-body">
      <h5>Recent Subjects</h5>
      <ul class="list-group">
        <li
          class="list-group-item"
          v-for="subject in subjects"
          :key="subject.id"
        >
          {{ subject.title }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  props: ['subjects'],
};
</script>

<style scoped>
.list-group-item {
  border-left: none;
  border-right: none;
}

.list-group-item:hover {
  text-decoration: underline;
  cursor: pointer;
}
</style>
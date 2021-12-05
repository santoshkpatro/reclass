<template>
  <div class="card border-2 border-dark">
    <div class="card-body">
      <h5>Recent Assignments</h5>
      <ul class="list-group">
        <li
          class="list-group-item"
          v-for="assignment in assignments"
          :key="assignment.id"
        >
          {{ assignment.title }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  props: ['assignments'],
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
<template>
  <label for="label" class="form-label fw-bolder" v-if="label">{{
    label
  }}</label>
  <input
    :placeholder="label"
    class="form-control bg-transparent text-white"
    :value="modelValue"
    v-bind="$attrs"
    @input="$emit('update:modelValue', $event.target.value)"
  />
</template>

<script>
export default {
  name: 'BaseInput',
  props: {
    label: {
      type: String,
      default: '',
    },
    modelValue: {
      type: [String, Number],
      default: '',
    },
  },
}
</script>

<style>
input {
  border: none;
}
</style>

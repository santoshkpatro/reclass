<template>
  <label class="form-label fw-bold" v-if="label">{{ label }}</label>
  <input
    v-bind="$attrs"
    class="form-control"
    :placeholder="label"
    :value="modelValue"
    @input="$emit('update:modelValue', $event.target.value)"
  />
  <div class="form-text" v-if="message">{{ message }}</div>
</template>

<script>
export default {
  name: 'BaseInput',
  props: {
    label: {
      type: String,
      default: '',
    },
    message: {
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

<style scoped></style>

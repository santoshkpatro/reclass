<template>
  <div class="form-check form-switch">
    <input
      type="checkbox"
      role="switch"
      :checked="modelValue"
      @change="$emit('update:modelValue', $event.target.checked)"
      class="form-check-input"
    />
    <label class="form-check-label" v-if="label">{{ label }}</label>
  </div>
</template>

<script>
export default {
  props: {
    label: {
      type: String,
      default: '',
    },
    modelValue: {
      type: Boolean,
      default: false,
    },
  },
}
</script>

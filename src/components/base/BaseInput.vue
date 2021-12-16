<template>
  <div class="base-input">
    <label for class="text-lg">{{ label }}</label>
    <input
      :type="type"
      :name="name"
      :value="modelValue"
      :placeholder="placeholder"
      @input="$emit('update:modelValue', $event.target.value)"
      class="input-field"
    />
    <div class="form-text">{{ message }}</div>
  </div>
</template>

<script>
export default {
  name: 'BaseInput',
  props: {
    label: {
      type: String,
      default: '',
    },
    name: {
      type: String,
      required: true,
    },
    type: {
      type: String,
      default: 'text',
    },
    message: {
      type: String,
      default: '',
    },
    modelValue: {
      type: [String, Number],
      default: '',
    },
    placeholder: {
      type: String,
      default: '',
    },
  },
}
</script>

<style scoped></style>

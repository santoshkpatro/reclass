<template>
  <div class="base-input">
    <label for class="text-lg">{{ label }}</label>
    <input
      :type="type"
      :name="name"
      :value="modelValue"
      :placeholder="placeholder"
      @input="updateValue"
      class="input-field"
    />
    <div class="form-text">{{ message }}</div>
  </div>
</template>

<script>
export default {
  name: 'BaseInput',
  emits: ['input'],
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
      default: ''
    },
    placeholder: {
      type: String,
      default: '',
    },
  },
  methods: {
    updateValue(e) {
      this.$emit('input', e.target.value);
    },
  },
};
</script>

<style scoped>
input {
  border: 1px solid;
  box-shadow: none;
}

input:focus {
  border: 1px solid;
  box-shadow: none;
}
</style>
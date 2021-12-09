<template>
  <div class="base-input">
    <label for="" class="">{{ label }}</label>
    <input
      :type="type"
      :name="name"
      :value="value"
      :placeholder="placeholder"
      @input="updateValue"
      class="border border-transparent"
    />
    <div class="form-text">
      {{ message }}
    </div>
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
    value: {
      type: [String, Number],
      required: true,
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
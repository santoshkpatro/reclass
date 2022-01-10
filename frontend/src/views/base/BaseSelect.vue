<template>
  <label class="form-label fw-bolder" v-if="label">{{ label }}</label>
  <select
    class="form-select bg-transparent"
    :value="modelValue"
    v-bind="{
      ...$attrs,
      onChange: ($event) => {
        $emit('update:modelValue', $event.target.value)
      },
    }"
  >
    <option class="bg-dark text-white" selected>Open this select menu</option>
    <option
      class="bg-dark text-white"
      v-for="option in options"
      :key="option"
      :value="option"
      :selected="option === modelValue"
    >
      {{ option }}
    </option>
  </select>
</template>

<script>
export default {
  props: {
    label: {
      type: String,
      default: '',
    },
    modelValue: {
      type: [String, Number],
      default: '',
    },
    options: {
      type: Array,
      required: true,
    },
  },
}
</script>

<template>
  <div class="relative mb-4">
    <label
      for="name"
      class="block text-sm font-medium text-gray-700"
      v-if="label"
      >{{ label }}</label
    >
    <input
      :placeholder="label"
      :value="modelValue"
      v-bind="$attrs"
      @input="$emit('update:modelValue', $event.target.value)"
      class="w-full bg-white rounded border border-gray-500 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
    />
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
    modelValue: {
      type: [String, Number],
      default: '',
    },
  },
}
</script>

<style></style>

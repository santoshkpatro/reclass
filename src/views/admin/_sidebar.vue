<template>
  <div class="pt-6 pb-2 px-2 h-screen flex flex-col bg-gray-100">
    <div class="px-3">
      <h6 class="text-lg font-semibold">Reclass</h6>
    </div>
    <div class="mt-3">
      <div class="mt-1 first:mt-0">
        <div class="px-2 py-2 flex flex-col rounded-lg cursor-pointer">
          <div
            class="ml-1 my-1 text-lg text-gray-900 hover:bg-white text-blue-500"
          >
            <UsersIcon class="h-5 w-5 text-blue-500 inline" />
            USERS
          </div>
          <div class="ml-1 my-1 text-lg text-gray-900 hover:bg-white">
            <BookOpenIcon class="h-5 w-5 text-blue-500 inline" />
            SUBJECTS
          </div>
          <div class="ml-1 my-1 text-lg text-gray-900 hover:bg-white">
            <AnnotationIcon class="h-5 w-5 text-blue-500 inline" />
            NOTIFICATIONS
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { UsersIcon, BookOpenIcon, AnnotationIcon } from '@heroicons/vue/solid'
export default {
  components: { UsersIcon, BookOpenIcon, AnnotationIcon },
}
</script>

<style></style>

<template>
  <nav class="border-b-2 border-indigo-500">
    <div class="max-w-6xl mx-auto px-4">
      <div class="flex justify-between">
        <div class="flex space-x-7">
          <div>
            <!-- Website Logo -->
            <!-- <a href="#" class="flex items-center py-4 px-2">
              <img src="logo.png" alt="Logo" class="h-8 w-8 mr-2" />
              <span class="font-semibold text-gray-500 text-lg"
                >Navigation</span
              >
            </a> -->
          </div>
          <!-- Primary Navbar items -->
          <div class="hidden md:flex items-center space-x-1">
            <a
              href=""
              class="py-4 px-2 text-gray-500 border-indigo-500 font-semibold"
              >Home</a
            >
            <a
              href=""
              class="py-4 px-2 text-gray-500 font-semibold hover:text-indigo-500 transition duration-300"
              >Services</a
            >
            <a
              href=""
              class="py-4 px-2 text-gray-500 font-semibold hover:text-indigo-500 transition duration-300"
              >About</a
            >
            <a
              href=""
              class="py-4 px-2 text-gray-500 font-semibold hover:text-indigo-500 transition duration-300"
              >Contact Us</a
            >
          </div>
        </div>
        <!-- Secondary Navbar items -->
        <div class="hidden md:flex items-center space-x-3">
          <a
            href=""
            class="py-2 px-2 font-medium text-gray-500 rounded hover:bg-indigo-500 hover:text-white transition duration-300"
            >Log In</a
          >
          <a
            href=""
            class="py-2 px-2 font-medium text-white bg-indigo-500 rounded hover:bg-indigo-400 transition duration-300"
            >Sign Up</a
          >
        </div>
        <!-- Mobile menu button -->
        <div class="md:hidden flex items-center">
          <button class="outline-none mobile-menu-button" @click="toggleMenu">
            <svg
              class="w-6 h-6 text-gray-500 hover:text-green-500"
              x-show="!showMenu"
              fill="none"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </button>
        </div>
      </div>
    </div>
    <!-- mobile menu -->
    <div class="mobile-menu" :class="{ hidden: toggle }">
      <ul class="">
        <li class="active">
          <a
            href="index.html"
            class="block text-sm px-2 py-4 text-white bg-indigo-500 font-semibold"
            >Home</a
          >
        </li>
        <li>
          <a
            href="#services"
            class="block text-sm px-2 py-4 hover:bg-indigo-500 transition duration-300"
            >Services</a
          >
        </li>
        <li>
          <a
            href="#about"
            class="block text-sm px-2 py-4 hover:bg-indigo-500 transition duration-300"
            >About</a
          >
        </li>
        <li>
          <a
            href="#contact"
            class="block text-sm px-2 py-4 hover:bg-indigo-500 transition duration-300"
            >Contact Us</a
          >
        </li>
      </ul>
    </div>
    <!-- <script>
				const btn = document.querySelector("button.mobile-menu-button");
				const menu = document.querySelector(".mobile-menu");

				btn.addEventListener("click", () => {
					menu.classList.toggle("hidden");
				});
			</script> -->
  </nav>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Navbar',
  data() {
    return {
      toggle: true,
    }
  },
  computed: {
    ...mapGetters(['loggedIn', 'role']),
    url: function () {
      return '/' + this.role
    },
  },
  methods: {
    toggleMenu() {
      this.toggle = !this.toggle
    },
  },
}
</script>

<style></style>

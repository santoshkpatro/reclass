<template>
  <div
    class="d-flex flex-column flex-shrink-0 p-3 bg-light"
    style="height: 100vh"
  >
    <a
      href="/"
      class="
        d-flex
        align-items-center
        mb-3 mb-md-0
        me-md-auto
        link-dark
        text-decoration-none
      "
    >
      <svg class="bi me-2" width="40" height="32">
        <use xlink:href="#bootstrap" />
      </svg>
      <span class="fs-4">ReClass</span>
    </a>
    <hr />
    <ul class="nav nav-pills flex-column mb-auto">
      <li>
        <router-link :to="{ name: 'AdminOverview' }" class="nav-link link-dark">
          <svg class="bi me-2" width="16" height="16">
            <use xlink:href="#speedometer2" />
          </svg>
          Overview
        </router-link>
      </li>
      <li>
        <router-link :to="{ name: 'UserList' }" class="nav-link link-dark">
          <svg class="bi me-2" width="16" height="16">
            <use xlink:href="#table" />
          </svg>
          Users
        </router-link>
      </li>
      <li>
        <a href="#" class="nav-link link-dark">
          <svg class="bi me-2" width="16" height="16">
            <use xlink:href="#grid" />
          </svg>
          Subjects
        </a>
      </li>
      <li>
        <a href="#" class="nav-link link-dark">
          <svg class="bi me-2" width="16" height="16">
            <use xlink:href="#people-circle" />
          </svg>
          Customers
        </a>
      </li>
    </ul>
    <hr />
    <div class="dropdown">
      <a
        href="#"
        class="
          d-flex
          align-items-center
          link-dark
          text-decoration-none
          dropdown-toggle
        "
        id="dropdownUser2"
        data-bs-toggle="dropdown"
        aria-expanded="false"
      >
        <img
          src="https://github.com/mdo.png"
          alt=""
          width="32"
          height="32"
          class="rounded-circle me-2"
        />
        <strong>mdo</strong>
      </a>
      <ul
        class="dropdown-menu text-small shadow"
        aria-labelledby="dropdownUser2"
      >
        <li><a class="dropdown-item" href="#">New project...</a></li>
        <li><a class="dropdown-item" href="#">Settings</a></li>
        <li><a class="dropdown-item" href="#">Profile</a></li>
        <li><hr class="dropdown-divider" /></li>
        <li><a class="dropdown-item" href="#">Sign out</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.dropdown-toggle {
  outline: 0;
}

.nav-flush .nav-link {
  border-radius: 0;
}

.btn-toggle {
  display: inline-flex;
  align-items: center;
  padding: 0.25rem 0.5rem;
  font-weight: 600;
  color: rgba(0, 0, 0, 0.65);
  background-color: transparent;
  border: 0;
}
.btn-toggle:hover,
.btn-toggle:focus {
  color: rgba(0, 0, 0, 0.85);
  background-color: #d2f4ea;
}

.btn-toggle::before {
  width: 1.25em;
  line-height: 0;
  content: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 16 16'%3e%3cpath fill='none' stroke='rgba%280,0,0,.5%29' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M5 14l6-6-6-6'/%3e%3c/svg%3e");
  transition: transform 0.35s ease;
  transform-origin: 0.5em 50%;
}

.btn-toggle[aria-expanded='true'] {
  color: rgba(0, 0, 0, 0.85);
}
.btn-toggle[aria-expanded='true']::before {
  transform: rotate(90deg);
}

.btn-toggle-nav a {
  display: inline-flex;
  padding: 0.1875rem 0.5rem;
  margin-top: 0.125rem;
  margin-left: 1.25rem;
  text-decoration: none;
}
.btn-toggle-nav a:hover,
.btn-toggle-nav a:focus {
  background-color: #d2f4ea;
}

.scrollarea {
  overflow-y: auto;
}
</style>
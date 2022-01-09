<template>
  <table class="table table-responsive table-borderless table-sm text-white">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Details</th>
        <th scope="col">Active?</th>
        <th scope="col">Created on</th>
        <th scope="col">Role</th>
        <th scope="col">Enrolled Subjects</th>
        <th scope="col">Action</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="user in users">
        <th scope="row">
          <input
            class="form-check-input"
            type="checkbox"
            id="checkboxNoLabel"
            value=""
          />
        </th>
        <td class="d-flex flex-column">
          <span>
            <router-link
              class="text-white"
              :to="{ name: 'AdminUserDetail', params: { user_id: user.id } }"
            >
              {{ user.first_name }} {{ user.last_name }}
            </router-link>
          </span>
          <span class="fw-light">
            {{ user.email }}
          </span>
        </td>
        <td>
          <div class="form-check form-switch">
            <input
              @click="
                $emit('onUpdate', user.id, { is_active: !user.is_active })
              "
              class="form-check-input bg-success"
              type="checkbox"
              role="switch"
              id="switch1"
              data-on="Yes"
              data-off="No"
              :checked="user.is_active"
            />
          </div>
        </td>
        <td>{{ formatDate(user.created_at) }}</td>
        <td>
          <span class="badge bg-dark" v-if="!user.is_instructor">student</span>
          <span class="badge bg-success" v-else>instructor</span>
        </td>
        <td>
          <span
            class="badge bg-success me-1"
            type="button"
            v-for="enrollment in user.enrolled"
            :key="enrollment.id"
            data-bs-toggle="tooltip"
            data-bs-placement="top"
            :title="enrollment.subject.title"
            >{{ enrollment.subject.subject_code }}</span
          >
        </td>
        <td>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            class="bi bi-trash"
            viewBox="0 0 16 16"
            @click="$emit('onDelete', user.id)"
          >
            <path
              d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"
            />
            <path
              fill-rule="evenodd"
              d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"
            />
          </svg>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import dayjs from 'dayjs'

export default {
  props: {
    users: {
      type: Array,
      required: true,
    },
  },
  emits: ['onUpdate', 'onDelete'],
  methods: {
    formatDate(date) {
      return new dayjs(date).format('DD-MM-YYYY')
    },
    resource_url(url) {
      return process.env.VUE_APP_MEDIA_URL + '/' + url
    },
  },
}
</script>

<style scoped>
a {
  text-decoration: none;
  color: black;
}

a:hover {
  text-decoration: underline;
}

.table > tbody > tr > td {
  vertical-align: middle;
}
</style>

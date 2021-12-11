<template>
  <div>
    <h2>Overview</h2>
    <div v-if="isLoading">
      <Placeholder />
    </div>
    <div v-else>
      <!-- Count Section -->
      <!-- <div class="row my-3">
        <div class="col-2">
          <CountCard name="Users" :count="users.count" />
        </div>
        <div class="col-2">
          <CountCard name="Notifications" :count="notifications.count" />
        </div>
        <div class="col-2">
          <CountCard name="Schedules" :count="schedules.count" />
        </div>
        <div class="col-2">
          <CountCard name="Subjects" :count="subjects.count" />
        </div>
        <div class="col-2">
          <CountCard name="Assignments" :count="assignments.count" />
        </div>
        <div class="col-2">
          <CountCard name="Submissions" :count="submissions.count" />
        </div>
      </div>-->

      <div class="flex flex-wrap -m-4 text-center">
        <div class="p-4 md:w-1/4 sm:w-1/2 w-full">
          <div class="border-2 border-gray-200 px-4 py-6 rounded-lg">
            <svg
              fill="none"
              stroke="currentColor"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              class="text-indigo-500 w-12 h-12 mb-3 inline-block"
              viewBox="0 0 24 24"
            >
              <path d="M8 17l4 4 4-4m-4-5v9" />
              <path d="M20.88 18.09A5 5 0 0018 9h-1.26A8 8 0 103 16.29" />
            </svg>
            <h2 class="title-font font-medium text-3xl text-gray-900">2.7K</h2>
            <p class="leading-relaxed">Downloads</p>
          </div>
        </div>
        <div class="p-4 md:w-1/4 sm:w-1/2 w-full">
          <div class="border-2 border-gray-200 px-4 py-6 rounded-lg">
            <svg
              fill="none"
              stroke="currentColor"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              class="text-indigo-500 w-12 h-12 mb-3 inline-block"
              viewBox="0 0 24 24"
            >
              <path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2" />
              <circle cx="9" cy="7" r="4" />
              <path d="M23 21v-2a4 4 0 00-3-3.87m-4-12a4 4 0 010 7.75" />
            </svg>
            <h2 class="title-font font-medium text-3xl text-gray-900">1.3K</h2>
            <p class="leading-relaxed">Users</p>
          </div>
        </div>
        <div class="p-4 md:w-1/4 sm:w-1/2 w-full">
          <div class="border-2 border-gray-200 px-4 py-6 rounded-lg">
            <svg
              fill="none"
              stroke="currentColor"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              class="text-indigo-500 w-12 h-12 mb-3 inline-block"
              viewBox="0 0 24 24"
            >
              <path d="M3 18v-6a9 9 0 0118 0v6" />
              <path
                d="M21 19a2 2 0 01-2 2h-1a2 2 0 01-2-2v-3a2 2 0 012-2h3zM3 19a2 2 0 002 2h1a2 2 0 002-2v-3a2 2 0 00-2-2H3z"
              />
            </svg>
            <h2 class="title-font font-medium text-3xl text-gray-900">74</h2>
            <p class="leading-relaxed">Files</p>
          </div>
        </div>
        <div class="p-4 md:w-1/4 sm:w-1/2 w-full">
          <div class="border-2 border-gray-200 px-4 py-6 rounded-lg">
            <svg
              fill="none"
              stroke="currentColor"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              class="text-indigo-500 w-12 h-12 mb-3 inline-block"
              viewBox="0 0 24 24"
            >
              <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
            </svg>
            <h2 class="title-font font-medium text-3xl text-gray-900">46</h2>
            <p class="leading-relaxed">Places</p>
          </div>
        </div>
      </div>

      <!-- Activity Section  -->
      <div class="activity my-3">
        <div class="row">
          <div class="col-9">
            <ActivityChart />
          </div>
          <div class="col-3">
            <div class="d-grid gap-2">
              <button class="btn btn-outline-dark">Add User</button>
              <button class="btn btn-outline-dark">Add Notification</button>
              <button class="btn btn-outline-dark">Add Schedule</button>
              <button class="btn btn-outline-dark">Add Subject</button>
            </div>
          </div>
        </div>
      </div>

      <!-- Recent Items Section -->
      <div class="row my-3">
        <div class="col-4">
          <RecentUsers :users="users.recent" />
        </div>
        <div class="col-4">
          <RecentSubjects :subjects="subjects.recent" />
        </div>
        <div class="col-4">
          <RecentAssignments :assignments="assignments.recent" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {
  getUsers,
  getSubjects,
  getAssignments,
  getSubmissions,
  getSchedules,
  getNotifications,
} from '../../api/admin.js';
import Placeholder from '../../components/admin/overview/Placeholder.vue';
import RecentUsers from '../../components/admin/overview/RecentUsers.vue';
import RecentSubjects from '../../components/admin/overview/RecentSubjects.vue';
import RecentAssignments from '../../components/admin/overview/RecentAssignments.vue';
import CountCard from '../../components/admin/overview/CountCard.vue';
import ActivityChart from '../../components/admin/overview/ActivityChart.vue';

export default {
  name: 'AdminOverview',
  components: {
    Placeholder,
    RecentUsers,
    RecentSubjects,
    RecentAssignments,
    CountCard,
    ActivityChart,
  },
  data() {
    return {
      isLoading: true,
      users: {
        count: 0,
        recent: [],
      },
      subjects: {
        count: 0,
        recent: [],
      },
      assignments: {
        count: 0,
        recent: [],
      },
      submissions: {
        count: 0,
        recent: [],
      },
      schedules: {
        count: 0,
        recent: [],
      },
      notifications: {
        count: 0,
        recent: [],
      },
    };
  },
  async mounted() {
    const userData = await getUsers({ limit: 10 });
    const subjectData = await getSubjects();
    const assignmentData = await getAssignments();
    const submissionData = await getSubmissions();
    const scheduleData = await getSchedules();
    const notificationsData = await getNotifications();

    this.users.count = userData.data.count;
    this.users.recent = userData.data.results;

    this.subjects.count = subjectData.data.count;
    this.subjects.recent = subjectData.data.results;

    this.assignments.count = assignmentData.data.count;
    this.assignments.recent = assignmentData.data.results;

    this.submissions.count = submissionData.data.count;
    this.submissions.recent = submissionData.data.count;

    this.schedules.count = scheduleData.data.count;
    this.schedules.recent = scheduleData.data.results;

    this.notifications.count = notificationsData.data.count;
    this.notifications.recent = notificationsData.data.results;

    this.isLoading = false;
  },
};
</script>

<style>
</style>
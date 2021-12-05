<template>
  <div>
    <h2>Overview</h2>
    <div v-if="isLoading">
      <Placeholder />
    </div>
    <div v-else>
      <!-- Count Section -->
      <div class="row my-3">
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
      </div>

      <!-- Activity Section  -->
      <div class="activity my-3">
        <div class="row">
          <div class="col-9">
            <h3>Activity Graph</h3>
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
} from '@/api/admin.js';
import Placeholder from '@/components/admin/overview/Placeholder.vue';
import RecentUsers from '@/components/admin/overview/RecentUsers.vue';
import RecentSubjects from '@/components/admin/overview/RecentSubjects.vue';
import RecentAssignments from '@/components/admin/overview/RecentAssignments.vue';
import CountCard from '@/components/admin/overview/CountCard.vue';

export default {
  name: 'AdminOverview',
  components: {
    Placeholder,
    RecentUsers,
    RecentSubjects,
    RecentAssignments,
    CountCard,
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
    const userData = await getUsers();
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
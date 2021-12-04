import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../pages/Home.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue'),
  },
  {
    path: '/auth/login',
    name: 'Login',
    component: () => import('../pages/auth/Login.vue'),
  },
  {
    path: '/student',
    name: 'StudentDashboard',
    component: () => import('../pages/student/Dashboard.vue'),
    meta: { requiresAuth: true },
  },
  {
    path: '/admin',
    name: 'AdminDashboard',
    component: () => import('../pages/admin/Dashboard.vue'),
    meta: { requiresAuth: true, requiresAdmin: true },
  },
  {
    path: '/unauthorized',
    name: 'Unauthorized',
    component: () => import('../pages/401.vue'),
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'Notfound',
    component: () => import('../pages/404.vue'),
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    // this route requires auth, check if logged in
    const profileData = localStorage.getItem('profile');

    // if not, redirect to login page.
    if (!profileData) {
      next({
        path: '/auth/login',
        query: { redirect: to.fullPath },
      });
    } else {
      // Checking for admin permission
      if (to.matched.some((record) => record.meta.requiresAdmin)) {
        const profile = JSON.parse(profileData);

        if (!profile.is_admin) {
          next({
            path: '/unauthorized',
          });
        }
      }

      next();
    }
  } else {
    next(); // make sure to always call next()!
  }
});

export default router;

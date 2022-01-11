import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/home/Home.vue'
import Auth from '../views/auth/Auth.vue'
import AdminDashboard from '../views/admin/Dashboard.vue'
import StudentDashboard from '../views/student/Dashboard.vue'
import homeRoutes from './home.js'
import authRoutes from './auth.js'
import adminRoutes from './admin.js'
import studentRoutes from './student.js'

const routes = [
  {
    path: '/auth',
    name: 'Auth',
    component: Auth,
    children: authRoutes,
  },
  {
    path: '/admin',
    name: 'AdminDashboard',
    component: AdminDashboard,
    meta: { requiresAuth: true, requiresAdmin: true },
    children: adminRoutes,
  },
  {
    path: '/student',
    name: 'StudentDashboard',
    component: StudentDashboard,
    meta: { requiresAuth: true },
    children: studentRoutes,
  },
  {
    path: '/',
    name: 'Home',
    component: Home,
    children: homeRoutes,
  },
  {
    path: '/unauthorized',
    name: 'Unauthorized',
    component: () => import('../views/401.vue'),
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'Notfound',
    component: () => import('../views/404.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    // this route requires auth, check if logged in
    const profileData = localStorage.getItem('profile')

    // if not, redirect to login page.
    if (!profileData) {
      next({
        path: '/auth/login',
        query: { redirect: to.fullPath },
      })
    } else {
      // Checking for admin permission
      if (to.matched.some((record) => record.meta.requiresAdmin)) {
        const profile = JSON.parse(profileData)

        if (!profile.is_admin) {
          next({
            path: '/unauthorized',
          })
        }
      }

      next()
    }
  } else {
    next() // make sure to always call next()!
  }
})

export default router

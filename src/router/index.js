import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import adminRoutes from './admin.js'

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
    component: () => import('../views/auth/Login.vue'),
  },
  {
    path: '/auth/password_reset',
    name: 'PasswordReset',
    component: () => import('../views/auth/PasswordReset.vue'),
  },
  {
    path: '/auth/password_reset/confirm/:token',
    name: 'PasswordResetConfirm',
    props: true,
    component: () => import('../views/auth/PasswordResetConfirm.vue'),
  },
  {
    path: '/admin',
    name: 'AdminDashboard',
    component: () => import('../views/admin/Dashboard.vue'),
    // components: {
    //   admin: () => import('../views/admin/Dashboard.vue'),
    // },
    meta: { requiresAuth: true, requiresAdmin: true },
    children: adminRoutes,
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

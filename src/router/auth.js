export default [
  {
    path: 'login',
    name: 'Login',
    component: () => import('../views/auth/Login.vue'),
  },
  {
    path: 'password_reset',
    name: 'PasswordReset',
    component: () => import('../views/auth/PasswordReset.vue'),
  },
  {
    path: 'password_reset/confirm/:token',
    name: 'PasswordResetConfirm',
    props: true,
    component: () => import('../views/auth/PasswordResetConfirm.vue'),
  },
  {
    path: '/auth/logout',
    name: 'Logout',
    props: true,
    component: () => import('../views/auth/Logout.vue'),
  },
]

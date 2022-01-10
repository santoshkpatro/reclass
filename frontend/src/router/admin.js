export default [
  {
    path: '',
    name: 'AdminOverview',
    component: () => import('../views/admin/overview'),
    meta: { requiresAuth: true, requiresAdmin: true },
  },
  {
    path: 'users',
    name: 'AdminUsers',
    component: () => import('../views/admin/users'),
    meta: { requiresAuth: true, requiresAdmin: true },
  },
  {
    path: 'users/:user_id',
    name: 'AdminUserDetail',
    component: () => import('../views/admin/users/detail.vue'),
    props: true,
    meta: { requiresAuth: true, requiresAdmin: true },
  },
  {
    path: 'subjects',
    name: 'AdminSubjects',
    component: () => import('../views/admin/subjects'),
    meta: { requiresAuth: true, requiresAdmin: true },
  },
]

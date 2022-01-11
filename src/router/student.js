export default [
  {
    path: '',
    name: 'StudentOverview',
    component: () => import('../views/student/overview'),
    meta: { requiresAuth: true },
  },
]

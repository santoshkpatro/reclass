export default [
  {
    path: '',
    name: 'Root',
    component: () => import('../views/home/Root.vue'),
  },
  {
    path: 'about',
    name: 'About',
    component: () => import('../views/home/About.vue'),
  },
]

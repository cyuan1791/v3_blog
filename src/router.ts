import { createRouter, createWebHistory } from 'vue-router';
import Home from './views/Home.vue';
import PostView from './views/PostView.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: Home
    },
    {
      path: '/post/:id',
      component: PostView
    }
  ],
  scrollBehavior() {
    return { top: 0 }; // Always scroll to top
  }
});

export default router;

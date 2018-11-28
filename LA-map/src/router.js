import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/cmap',
      name: 'cmap',
      component: () => import(/* webpackChunkName: "about" */ './components/Cmap.vue')
    },
    {
      path: '/bmap',
      name: 'bmap',
      component: () => import(/* webpackChunkName: "about" */ './components/Bmap.vue')
    },
    {
      path: '/amap',
      name: 'amap',
      component: () => import(/* webpackChunkName: "about" */ './components/Amap.vue')
    }
  ]
})

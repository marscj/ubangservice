import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

export const constantRoutes = [
  {
    path: '/redirect',
    component: Layout,
    hidden: true,
    children: [
      {
        path: '/redirect/:path*',
        component: () => import('@/views/redirect/index')
      }
    ]
  },
  {
    path: '/',
    component: () => import('@/views/index/index'),
    hidden: true
  },

  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },

  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  },

  {
    path: '/dashboard',
    component: Layout,
    redirect: '/dashboard/index',
    children: [{
      path: 'index',
      name: 'Dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: { title: 'Home', icon: 'dashboard', affix: true }
    }]
  },

  {
    path: '/booking',
    component: Layout,
    redirect: '/booking/all',
    name: 'Booking',
    meta: {
      title: 'Booking',
      icon: 'lock'
    },
    children: [
      {
        path: 'all',
        name: 'AllBooking',
        component: () => import('@/views/booking/all'),
        meta: { title: 'All Booking', noCache: true }
      },
      {
        path: 'month',
        name: 'MonthBooking',
        component: () => import('@/views/booking/month'),
        meta: { title: 'Month', noCache: true },
        hidden: true
      },
      {
        path: 'my',
        name: 'MyBooking',
        component: () => import('@/views/booking/my'),
        meta: { title: 'My Booking', noCache: true },
        hidden: true
      },
      {
        path: 'edit/:id(\\d+)',
        component: () => import('@/views/booking/edit'),
        name: 'EditBooking',
        meta: { title: 'Edit Booking', noCache: true },
        hidden: true
      },
      {
        path: 'create',
        component: () => import('@/views/booking/create'),
        name: 'CreateBooking',
        meta: { title: 'Add Booking' },
        hidden: true
      }
    ]
  }
]

export const asyncRoutes = [
  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router

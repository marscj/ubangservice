import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

export const constantRoutes = [

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
    redirect: '/booking/index',
    meta: {
      title: 'Booking',
      icon: 'lock'
    },
    children: [
      {
        path: 'index',
        name: 'Booking',
        component: () => import('@/views/booking/index'),
        meta: { title: 'Booking List', noCache: true }
      },
      {
        path: 'self',
        name: 'My Booking',
        component: () => import('@/views/booking/self'),
        meta: { title: 'My Booking', noCache: true }
      },
      {
        path: 'edit/:id(\\d+)',
        component: () => import('@/views/booking/edit'),
        name: 'EditBooking',
        meta: { title: 'Edit Booking', noCache: true, activeMenu: '/booking/list' },
        hidden: true
      },
      {
        path: 'create',
        component: () => import('@/views/booking/create'),
        name: 'CreateBooking',
        meta: { title: 'Create Booking', noCache: true, activeMenu: '/booking/list' },
        hidden: true
      }
    ]
  },

  {
    path: '/order',
    component: Layout,
    redirect: '/order/index',
    meta: {
      title: 'Order',
      icon: 'lock'
    },
    children: [
      {
        path: 'index',
        name: 'Order',
        component: () => import('@/views/order/index'),
        meta: { title: 'Order List', noCache: true }
      },
      {
        path: 'self',
        name: 'My Order',
        component: () => import('@/views/order/self'),
        meta: { title: 'My Order', noCache: true }
      }
    ]
  },

  {
    path: '/permission',
    component: Layout,
    redirect: '/permission/user',
    meta: {
      title: 'Authorization',
      icon: 'lock'
    },
    children: [{
      path: 'user',
      name: 'Users',
      component: () => import('@/views/user/index'),
      meta: { title: 'Users' }
    },
    {
      path: 'permission',
      name: 'Permission',
      component: () => import('@/views/permission/index'),
      meta: { title: 'Permission' }
    }]
  },

  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  }
]

/**
 * asyncRoutes
 * the routes that need to be dynamically loaded based on user roles
 */
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

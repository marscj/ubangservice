import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/user/login/',
    method: 'post',
    data
  })
}

export function getUsers(token) {
  return request({
    url: '/users/',
    method: 'get'
  })
}

export function getInfo(token) {
  return request({
    url: '/users/info/',
    method: 'get'
  })
}

export function logout() {
  return request({
    url: '/user/logout/',
    method: 'post'
  })
}

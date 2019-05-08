import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/user/login/',
    method: 'post',
    data
  })
}

export function getUsers(query) {
  return request({
    url: 'user/users/',
    method: 'get',
    params: query
  })
}

export function updateUser(id, data) {
  return request({
    url: `user/users/${id}/`,
    method: 'put',
    data
  })
}

export function getInfo(token) {
  return request({
    url: 'user/users/info/',
    method: 'get'
  })
}

export function logout() {
  return request({
    url: '/user/logout/',
    method: 'post'
  })
}

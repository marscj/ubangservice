import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/login/',
    method: 'post',
    data
  })
}

export function getUsers(query) {
  return request({
    url: '/users/',
    method: 'get',
    params: query
  })
}

export function updateUser(id, data) {
  return request({
    url: `/users/${id}/`,
    method: 'put',
    data
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
    url: '/logout/',
    method: 'post'
  })
}

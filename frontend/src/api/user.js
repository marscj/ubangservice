import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/api/login/',
    method: 'post',
    data
  })
}

export function getUsers(query) {
  return request({
    url: 'api/users/',
    method: 'get',
    params: query
  })
}

export function updateUser(id, data) {
  return request({
    url: `api/users/${id}/`,
    method: 'put',
    data
  })
}

export function getInfo(token) {
  return request({
    url: 'api/users/info/',
    method: 'get'
  })
}

export function logout() {
  return request({
    url: '/api/logout/',
    method: 'post'
  })
}

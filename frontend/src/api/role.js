import request from '@/utils/request'

export function getRoles(query) {
  return request({
    url: '/roles/',
    method: 'get',
    params: query
  })
}

export function getRole(pk) {
  return request({
    url: `/roles/${pk}/`,
    method: 'get'
  })
}

export function updateRole(pk, data) {
  return request({
    url: `/roles/${pk}/`,
    method: 'put',
    data
  })
}

export function createRole(data) {
  return request({
    url: 'api/roles/',
    method: 'post',
    data
  })
}

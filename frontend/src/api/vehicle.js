import request from '@/utils/request'

export function getVehicles(query) {
  return request({
    url: '/vehicles/',
    method: 'get',
    params: query
  })
}

export function getVehicle(pk) {
  return request({
    url: `/vehicles/${pk}/`,
    method: 'get'
  })
}

export function getModels(query) {
  return request({
    url: '/models/',
    method: 'get',
    params: query
  })
}

import request from '@/utils/request'

export function getVehicles(query) {
  return request({
    url: 'api/vehicles/',
    method: 'get',
    params: query
  })
}

export function getVehicle(pk) {
  return request({
    url: `api/vehicles/${pk}/`,
    method: 'get'
  })
}

export function getModels(query) {
  return request({
    url: 'api/models/',
    method: 'get',
    params: query
  })
}

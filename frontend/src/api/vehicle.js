import request from '@/utils/request'

export function getVehicles(query) {
  return request({
    url: 'vehicle/vehicles/',
    method: 'get',
    params: query
  })
}

export function getVehicle(pk) {
  return request({
    url: `vehicle/vehicles/${pk}/`,
    method: 'get'
  })
}

export function getModels(query) {
  return request({
    url: 'vehicle/models/',
    method: 'get',
    params: query
  })
}

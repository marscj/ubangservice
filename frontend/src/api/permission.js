import request from '@/utils/request'

export function getPermissions() {
  return request({
    url: 'api/permissions/',
    method: 'get'
  })
}

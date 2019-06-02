import request from '@/utils/request'

export function getPermissions() {
  return request({
    url: 'permission/permissions/',
    method: 'get'
  })
}

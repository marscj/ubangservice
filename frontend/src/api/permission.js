import request from '@/utils/request'

export function getPermissions() {
  return request({
    url: '/permissions/',
    method: 'get'
  })
}

import request from '@/utils/request'

export function getBookings(query) {
  return request({
    url: 'booking/bookings/',
    method: 'get',
    params: query
  })
}

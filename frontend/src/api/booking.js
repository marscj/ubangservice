import request from '@/utils/request'

export function getBookings(query) {
  return request({
    url: 'booking/bookings/',
    method: 'get',
    params: query
  })
}

export function getBooking(pk) {
  return request({
    url: `booking/bookings/${pk}/`,
    method: 'get'
  })
}

export function updateBooking(pk, data) {
  return request({
    url: `booking/bookings/${pk}/`,
    method: 'put',
    data
  })
}

export function createBooking(data) {
  return request({
    url: 'booking/bookings/',
    method: 'post',
    data
  })
}

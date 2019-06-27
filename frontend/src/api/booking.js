import request from '@/utils/request'

export function getBookings(query) {
  return request({
    url: 'api/bookings/',
    method: 'get',
    params: query
  })
}

export function getDashboard(query) {
  return request({
    url: 'api/bookings/dashboard/',
    method: 'get',
    params: query
  })
}

export function getBooking(pk) {
  return request({
    url: `api/bookings/${pk}/`,
    method: 'get'
  })
}

export function updateBooking(pk, data) {
  return request({
    url: `api/bookings/${pk}/`,
    method: 'put',
    data
  })
}

export function createBooking(data) {
  return request({
    url: 'api/bookings/',
    method: 'post',
    data
  })
}

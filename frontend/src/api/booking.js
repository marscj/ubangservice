import request from '@/utils/request'

export function getBookings(query) {
  return request({
    url: '/bookings/',
    method: 'get',
    params: query
  })
}

export function getDashboard(query) {
  return request({
    url: '/bookings/dashboard/',
    method: 'get',
    params: query
  })
}

export function getBooking(pk) {
  return request({
    url: `/bookings/${pk}/`,
    method: 'get'
  })
}

export function updateBooking(pk, data) {
  return request({
    url: `/bookings/${pk}/`,
    method: 'put',
    data
  })
}

export function createBooking(data) {
  return request({
    url: '/bookings/',
    method: 'post',
    data
  })
}

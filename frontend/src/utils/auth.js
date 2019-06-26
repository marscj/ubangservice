import Cookies from 'js-cookie'

const TokenKey = 'jwt_auth_token'

export function getToken() {
  console.log('get token', Cookies.get(TokenKey))
  return Cookies.get(TokenKey)
}

export function setToken(token) {
  return Cookies.set(TokenKey, token)
}

export function removeToken() {
  return Cookies.remove(TokenKey)
}

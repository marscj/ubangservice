
export function objectPop(obj, key) {
  var result = obj[key]
  console.log(result)
  if (!delete obj[key]) {
    throw new Error()
  }
  console.log(result)
  return result
}

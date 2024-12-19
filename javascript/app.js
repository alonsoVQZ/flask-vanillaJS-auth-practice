const apiUrl = '?'

async function login(){
  const response =  await fetch(`${apiUrl}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({})
  })
  return respose
} 

async function register(){
  const response =  await fetch(`${apiUrl}/auth/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({})
  })
  return response
} 

async function logout(){
  const response =  await fetch(`${apiUrl}/auth/logout`, {
    method: 'POST'
  })
  return response
}

async function me(){
  const response =  await fetch(`${apiUrl}/users/me`, {
    method: 'GET'
  })
  return response
} 


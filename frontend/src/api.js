import axios from 'axios'


const API_URL_BASE = 'http://127.0.0.1:5000/api/v1/'
const API_URL_EVENTS = API_URL_BASE + 'events/'
const API_URL_THEMES = API_URL_BASE + 'themes/'
const API_URL_CITIES = API_URL_BASE + 'cities/'

const getConfig = () => {
	const identity = JSON.parse(localStorage.getItem('identity'))
	if (!identity) {
		return null
	}
	return  {
		headers: {
			'Authorization': 'Bearer ' + identity['access_token']
		}
	}
}

export const me = async () => {
	return await axios.get(API_URL_BASE + 'auth/me', getConfig()).then(res => {
        return  res.data
    }).catch(() => false)
}

export const login = (login, password) => {
	return axios.post(API_URL_BASE + 'auth/login', {login, password}).then(response => {
		return response.data
	}).catch(e => null)
}

export const register = (login, email, password) => {
	return axios.post(API_URL_BASE + 'auth/register', {login, email, password}).then(response => {
		return response.data
	})
}

export const get_events = async () => {
	return await axios.get(API_URL_EVENTS, getConfig()).then(response => {
		const data = JSON.parse(response.data)
		return  data
	})
}

export const get_themes = async () => {
	return await axios.get(API_URL_THEMES, getConfig()).then(response => {
		const data = response.data.map(item => JSON.parse(item))
		return  data
	})
}

export const get_cities = async () => {
	return await axios.get(API_URL_CITIES, getConfig()).then(response => {
		const data = response.data
		return  data
	})
}

export const create_event = async (data) => {
	return await axios.post(API_URL_EVENTS, data, getConfig()).then(response => {
		const data = response.data
		return  data
	})
}

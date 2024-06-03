import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/dj-rest-auth'; // Ваш API URL

export const register = async (email, password1, password2) => {
    try {
        const response = await axios.post(`${API_URL}/registration/`, {
            email,
            password1,
            password2,
        });
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
};

export const login = async (email, password) => {
    try {
        const response = await axios.post(`${API_URL}/login/`, {
            email,
            password,
        });
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
};

export const logout = async () => {
    try {
        const response = await axios.post(`${API_URL}/logout/`);
        return response.data;
    } catch (error) {
        throw error.response.data;
    }
};

import axios from "axios";

const api = axios.create({
    baseURL: "https://advanced-ai-medical-platform-1.onrender.com/"
});

export default api;
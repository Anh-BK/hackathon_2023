import axios from "axios";

const axiosClient = axios.create({
  baseURL: "http://0.0.0.0:8002/api/v1",
  headers: {
    "Content-Type": "application/json",
  },
});

// Add a response interceptor
axiosClient.interceptors.response.use(
  (response) =>
    // Any status code that lie within the range of 2xx cause this function to trigger
    // Do something with response data
    response.data,
  (error) =>
    // Any status codes that falls outside the range of 2xx cause this function to trigger
    // Do something with response error
    Promise.reject(error)
);

export default axiosClient;

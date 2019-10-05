import axios from "axios";

class AxiosClient {
  async get(url) {
    var serverResponse = { hasError: false, data: null };
    await axiosInstance()
      .get(url)
      .then(response => {
        if (response.status == StatusOk) {
          serverResponse.data = response.data;
        } else {
          serverResponse.hasError = true;
          serverResponse.data = response.data.Message;
        }
      })
      .catch(function(error) {
        console.log(error);
        serverResponse.hasError = true;
        serverResponse.data = "Connection Error";
        return serverResponse;
      });
    return serverResponse;
  }
  post(url, data) {
    var serverResponse = { hasError: false, data: null };
    axiosInstance()
      .post(url, data)
      .then(response => {
        if (response.status == StatusOk) {
          serverResponse.data = response.data;
        } else {
          serverResponse.hasError = true;
          serverResponse.data = response.data.Message;
        }
      })
      .catch(function(error) {
        console.log(error);
        serverResponse.hasError = true;
        serverResponse.data = "Connection Error";
        return serverResponse;
      });
    return serverResponse;
  }
  put(url, data) {
    var serverResponse = { hasError: false, data: null };
    axiosInstance()
      .put(url, data)
      .then(response => {
        if (response.status == StatusOk) {
          serverResponse.data = response.data;
        } else {
          serverResponse.hasError = true;
          serverResponse.data = response.data.Message;
        }
      })
      .catch(function(error) {
        console.log(error);
        serverResponse.hasError = true;
        serverResponse.data = "Connection Error";
        return serverResponse;
      });
    return serverResponse;
  }
  delete(url) {
    var serverResponse = { hasError: false, data: null };
    axiosInstance()
      .delete(url)
      .then(response => {
        if (response.status == StatusOk) {
          serverResponse.data = response.data;
        } else {
          serverResponse.hasError = true;
          serverResponse.data = response.data.Message;
        }
      })
      .catch(function(error) {
        console.log(error);
        serverResponse.hasError = true;
        serverResponse.data = "Connection Error";
        return serverResponse;
      });
    return serverResponse;
  }
  patch(url, data) {
    var serverResponse = { hasError: false, data: null };
    axiosInstance()
      .patch(url, data)
      .then(response => {
        if (response.status == StatusOk) {
          serverResponse.data = response.data;
        } else {
          serverResponse.hasError = true;
          serverResponse.data = response.data.Message;
        }
      })
      .catch(function(error) {
        console.log(error);
        serverResponse.hasError = true;
        serverResponse.data = "Connection Error";
        return serverResponse;
      });
    return serverResponse;
  }
}

const axiosInstance = () => {
  // Create instance
  let instance = axios.create();

  instance.defaults.crossdomain = true;
  /* instance.defaults.validateStatus = function() {
    return true;
  }; */

  return instance;
};

const StatusOk = 200;

export const axiosClient = new AxiosClient();

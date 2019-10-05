import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

var apiserver = {
  url: "http://localhost:8000/api/",
  endpoints: {
    addresses: "addresses/",
    users: "users/",
    customers: "customers/",
    appointments: "appointments/",
    vehicles: "vehicles/",
    employees: "employees/",
    taskforces: "taskforces/"
  }
};

export const store = new Vuex.Store({
  state: {},
  getters: {
    addresses: () => apiserver.url + apiserver.endpoints.addresses,
    users: () => apiserver.url + apiserver.endpoints.users,
    customers: () => apiserver.url + apiserver.endpoints.customers,
    appointments: () => apiserver.url + apiserver.endpoints.appointments,
    vehicles: () => apiserver.url + apiserver.endpoints.vehicles,
    employees: () => apiserver.url + apiserver.endpoints.employees,
    taskforces: () => apiserver.url + apiserver.endpoints.taskforces
  }
});

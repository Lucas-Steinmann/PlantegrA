import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    apiserver: {
      url: "http://localhost:8000/api/",
      endpoints: {
        addresses: "addresses/",
        users: "users/",
        customers: "customers/",
        appointments: "appointments/",
        vehicles: "vehicles/",
        employees: "employees/"
      }
    }
  },
  getters: {
    addresses: state => {
      return state.apiserver.url + state.apiserver.endpoints.addresses;
    },
    users: state => {
      return state.apiserver.url + state.apiserver.endpoints.users;
    },
    customers: state => {
      return state.apiserver.url + state.apiserver.endpoints.customers;
    },
    appointments: state => {
      return state.apiserver.url + state.apiserver.endpoints.appointments;
    },
    vehicles: state => {
      return state.apiserver.url + state.apiserver.endpoints.vehicles;
    },
    employees: state => {
      return state.apiserver.url + state.apiserver.endpoints.employees;
    }
  }
});

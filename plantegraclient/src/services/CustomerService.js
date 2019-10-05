import { axiosClient } from "../plugins/axiosClient";
import { store } from "../store";

class CustomerService {
  async getAll() {
    return await axiosClient.get(store.getters.customers);
  }
  async getById(id) {
    return await axiosClient.get(store.getters.customers + id);
  }
}

export const customerService = new CustomerService();

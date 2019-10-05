import { axiosClient } from "../plugins/axiosClient";
import { store } from "../store";

class AddressService {
  async getAll() {
    return await axiosClient.get(store.getters.addresses);
  }
  async getById(id) {
    return await axiosClient.get(store.getters.addresses + id);
  }
}

export const addressService = new AddressService();

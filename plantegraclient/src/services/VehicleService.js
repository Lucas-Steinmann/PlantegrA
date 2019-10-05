import { axiosClient } from "../plugins/axiosClient";
import { store } from "../store";

class VehicleService {
  async getAll() {
    return await axiosClient.get(store.getters.vehicles);
  }
  async getById(id) {
    return await axiosClient.get(store.getters.vehicles + id);
  }
}

export const vehicleService = new VehicleService();

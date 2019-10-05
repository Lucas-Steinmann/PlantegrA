import { axiosClient } from "../plugins/axiosClient";
import { store } from "../store";

class AppointmentService {
  async getAll() {
    return await axiosClient.get(store.getters.appointments);
  }
  async getById(id) {
    return await axiosClient.get(store.getters.appointments + id);
  }
}

export const appointmentService = new AppointmentService();

import { axiosClient } from "../plugins/axiosClient";
import { store } from "../store";

class EmployeeService {
  async getAll() {
    return await axiosClient.get(store.getters.employees);
  }
  async getById(id) {
    return await axiosClient.get(store.getters.employees + id);
  }
}

export const employeeService = new EmployeeService();

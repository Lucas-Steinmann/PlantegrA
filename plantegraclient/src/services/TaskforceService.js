import { axiosClient } from "../plugins/axiosClient";
import { store } from "../store";
import moment from "moment";

class TaskforceService {
  async getAll() {
    return await axiosClient.get(store.getters.taskforces);
  }
  async getById(id) {
    return await axiosClient.get(store.getters.taskforces + id);
  }
  async getByDate(date) {
    var dateString = moment(date.toString()).format("YYYY-MM-DD");
    return await axiosClient.get(
      store.getters.taskforces + "?working_day=" + dateString
    );
  }
}

export const taskforceService = new TaskforceService();

class CalcService {
  getMonday(date) {
    date = new Date(date);
    var day = date.getDay();
    var diff = date.getDate() - day + (day == 0 ? -6 : 1); // adjust when day is sunday
    return new Date(date.setDate(diff));
  }
  getDaysOfCurrentWeek() {
    var ret = [];
    ret.push(this.getMonday(new Date()));
    var monday = this.getMonday(new Date());
    for (let i = 0; i < 5; i++) {
      ret.push(new Date(monday.setDate(monday.getDate() + 1)));
    }
    return ret;
  }
}

export const calcService = new CalcService();

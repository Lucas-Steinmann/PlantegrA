class CalcService {
  getMonday(date) {
    var day = date.getDay();
    var diff = date.getDate() - day + (day == 0 ? -6 : 1); // adjust when day is sunday
    return new Date(date.setDate(diff));
  }
  getDaysOfCurrentWeek() {
    var ret = [];
    //var monday = this.getMonday(new Date());
    //Debug week
    var monday = new Date(Date.parse("21 Oct 2019"));
    for (let i = 0; i < 6; i++) {
      var weekday = new Date();
      ret.push(new Date(weekday.setDate(monday.getDate() + i)));
    }
    return ret;
  }
}

export const calcService = new CalcService();

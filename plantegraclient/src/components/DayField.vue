<template>
  <div v-if="date" class="DayField">
    <div class="date">
      <h3>{{ date.getDay() | weekDayText }}</h3>
      <span>{{ date | formatDate }}</span>

    </div>
    <Weather />
  </div>
</template>

<script>
import Weather from "../components/Weather";
import moment from "moment";

export default {
  components: {
    Weather
  },
  filters: {
    weekDayText(day) {
      if (day == 0) {
        return "Sonntag";
      } else if (day == 1) {
        return "Montag";
      } else if (day == 2) {
        return "Dienstag";
      } else if (day == 3) {
        return "Mittwoch";
      } else if (day == 4) {
        return "Donnerstag";
      } else if (day == 5) {
        return "Freitag";
      } else if (day == 6) {
        return "Samstag";
      } else {
        ("Urlaub");
      }
    },
    formatDate(date) {
      if (date) {
        return moment(date.toString()).format("DD.MM.YYYY");
      }
    }
  },
  props: {
    date: Date
  },
  data: () => ({
    //
  })
};
</script>

<style scoped>
  h3 {
    text-align: center;
  }
  .date {
    text-align: center;
  }
</style>

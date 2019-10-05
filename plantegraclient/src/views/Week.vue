<template>
  <div>
    <DayRow v-for="day in weekDays" :key="day.getDay()" :date="day" />
  </div>
</template>

<script>
import DayRow from "../components/DayRow";
import { calcService } from "../services";

export default {
  components: {
    DayRow
  },
  data: () => ({
    weekDays: []
  }),
  created() {
    this.weekDays = calcService.getDaysOfCurrentWeek();
  }
};
</script>

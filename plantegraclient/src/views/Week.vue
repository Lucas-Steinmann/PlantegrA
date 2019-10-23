<template>
  <div class="week-wrapper d-flex flex-column justify-space-around align-content-stretch">
    <DayRow class="dayrow" v-for="day in weekDays" :key="day.getDay()" :date="day" />
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

<style scoped>
  .dayrow {
      margin-top: 0;
  }
  .week-wrapper{
    height: 100%;
    width: 100%;
  }
</style>

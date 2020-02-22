<template>
  <div>
    <v-row style="height: 100%">
      <v-col sm="2">
        <DayField :date="date" />
      </v-col>
      <v-col v-for="taskforce in taskforces" :key="taskforce.id">
        <TaskForceCard :taskforce="taskforce" />
      </v-col>
      <v-col>
        <VacationCard :employeesOnVacation="employeesOnVacation" />
      </v-col>
    </v-row>
    <v-divider></v-divider>
  </div>

</template>

<script>
import DayField from "../components/DayField";
import TaskForceCard from "../components/TaskForceCard";
import VacationCard from "../components/VacationCard";
import { taskforceService, employeeService } from "../services";

export default {
  components: {
    DayField,
    TaskForceCard,
    VacationCard
  },
  props: {
    date: Date
  },
  data: () => ({
    taskforces: [],
    employeesOnVacation: []
  }),
  created() {
    taskforceService.getByDate(this.date).then(response => {
      if (response.hasError === false) {
        this.taskforces = response.data;
        employeeService.getAll().then(responseEmployee => {
      if (responseEmployee.hasError === false) {
        this.employeesOnVacation = responseEmployee.data;
        this.taskforces.forEach(taskforce => {
          taskforce.members.forEach(taskForceMember => {
            console.log(taskForceMember);
            var index = 0;
            this.employeesOnVacation.forEach(employee => {
              if (employee.id === taskForceMember) {
                this.employeesOnVacation.splice(index, 1);
                return;
              }
              index++;
            })
          });
        });
      }
    });
      }
    });

  }
};
</script>

<style scoped>
  .dayrow {
  }
  .week-wrapper{
    height: 100%;
  }
</style>

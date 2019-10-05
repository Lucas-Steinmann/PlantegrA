<template>
  <div>
    <v-row>
      <v-col sm="2">
        <DayField :date="date" />
      </v-col>
      <v-col v-for="taskforce in taskforces" :key="taskforce.id">
        <TaskForceCard :taskforce="taskforce" />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import DayField from "../components/DayField";
import TaskForceCard from "../components/TaskForceCard";
import { taskforceService } from "../services";

export default {
  components: {
    DayField,
    TaskForceCard
  },
  props: {
    date: Date
  },
  data: () => ({
    taskforces: []
  }),
  created() {
    taskforceService.getByDate(this.date).then(response => {
      if (response.hasError === false) {
        this.taskforces = response.data;
      }
    });
  }
};
</script>

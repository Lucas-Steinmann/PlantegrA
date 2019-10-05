<template>
  <div>
    <v-row>
      <v-col>
        <DayField />
      </v-col>
      <v-col v-for="taskforce in taskforces" :key="taskforce.id">
          <TaskForceCard/>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import DayField from "../components/DayField";
import TaskForceCard from "../components/TaskForceCard";

export default {
  components: {
    DayField,
    TaskForceCard
  },
  data: () => ({
    taskforces: []
  })
};
</script>

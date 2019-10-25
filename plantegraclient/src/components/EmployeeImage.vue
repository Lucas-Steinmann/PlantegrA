<template>
  <v-row class="nomargin">
    <v-avatar size="36px">
      <img v-if="employee.profile_image != null" :src="employee.profile_image" alt="X" />
      <img v-else :src="profile_default_image" alt="X" />
    </v-avatar>
  </v-row>
</template>

<script>
import { employeeService } from "../services";

export default {
  data: () => ({
    employee: {},
    //TODO: change hardcoded path to dynamic?
    profile_default_image: "http://localhost:8000/media/profile-default.jpg"
  }),
  props: {
    employeeid: Number
  },
  mounted() {
    employeeService.getById(this.employeeid).then(response => {
      if (response.hasError === false) {
        this.employee = response.data;
      }
    });
  }
};
</script>

<style scoped>
.nomargin {
  margin: 0px;
}
</style>

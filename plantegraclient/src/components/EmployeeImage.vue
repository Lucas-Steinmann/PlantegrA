<template>
  <v-row class="nomargin">
    <v-avatar size="36px">
      <img :src="employee.profile_image" alt="X" />
    </v-avatar>
  </v-row>
</template>

<script>
import { employeeService } from "../services";

export default {
  data: () => ({
    employee: {}
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

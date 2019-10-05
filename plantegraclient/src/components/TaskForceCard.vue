<template>
  <v-card class="taskforce">
    {{ taskforce.working_day }}
    <v-row dense class="nomargin">
      <v-col class="members">
        <EmployeeImage
          v-for="memberid in taskforce.members"
          :key="memberid"
          :employeeid="memberid"
        />
      </v-col>
      <v-col>
        <p>{{ vehicle }}</p>
        <v-row dense v-for="appointment in appointments" :key="appointment.id">
          {{ appointment.description }}
        </v-row>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import EmployeeImage from "../components/EmployeeImage";
import { vehicleService, appointmentService } from "../services";

export default {
  components: {
    EmployeeImage
  },
  props: {
    taskforce: Object
  },
  data: () => ({
    vehicle: "",
    appointments: []
  }),
  methods: {
    GetVehiclePlate(vehicleid) {
      if (vehicleid) {
        vehicleService.getById(vehicleid).then(response => {
          if (response.hasError === false) {
            this.vehicle = response.data.plate_number;
          }
        });
      }
    },
    GetAppointments(appointmentids) {
      appointmentids.forEach(id => {
        appointmentService.getById(id).then(response => {
          if (response.hasError === false) {
            this.appointments.push(response.data);
          }
        });
      });
    }
  },
  mounted() {
    this.GetVehiclePlate(this.taskforce.vehicle);
    this.GetAppointments(this.taskforce.appointments);
  }
};
</script>

<style scoped>
.taskforce {
  max-width: 400px;
}
.nomargin {
  margin: 0px;
}
</style>

<template>
  <v-card class="taskforce" color="accent" dark>
    <v-row dense class="nomargin">
      <v-col class="members" cols="3">
        <div class="d-flex align-content-start flex-wrap">
          <EmployeeImage
            v-for="memberid in taskforce.members"
            :key="memberid"
            :employeeid="memberid"
          />
        </div>
      </v-col>
      <v-col>
        <p>{{ vehicle }}</p>
        <v-row dense v-for="appointment in appointments" :key="appointment.id">
          <v-row>
            <v-col>{{ appointment.customer.name }}</v-col>
            <v-col>{{ appointment.description }}</v-col>
          </v-row>
        </v-row>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import EmployeeImage from "../components/EmployeeImage";
import {
  vehicleService,
  appointmentService,
  addressService,
  customerService
} from "../services";

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
            var appointment = response.data;
            appointment.address = null;
            appointment.customer = null;
            if (appointment.location) {
              addressService.getById(appointment.location).then(response => {
                if (response.hasError === false) {
                  appointment.address = response.data;
                  customerService
                    .getById(appointment.address.customer)
                    .then(response => {
                      if (response.hasError === false) {
                        appointment.customer = response.data;
                      }
                    });
                }
              });
            }
            this.appointments.push(appointment);
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

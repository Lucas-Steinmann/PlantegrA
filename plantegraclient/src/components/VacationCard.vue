<template>
    <v-card class="vacationcard">
        Urlaub
        <v-col class="members">
            <EmployeeImage
                    v-for="employee in employeesOnVacation"
                    :key="employee.id"
                    :employeeid="employee.id"
            />
        </v-col>
    </v-card>
</template>

<script>
    import EmployeeImage from "../components/EmployeeImage";
    export default {
        components: {
            EmployeeImage
        },
        props: {
          employeesOnVacation : Array
        },
        name: "VacationCard"
    }
</script>

<style scoped>

    .vacationcard {
        max-width: 400px;
        width: 100px;
        height: 100px;
        background-color: red;
    }
    .nomargin {
        margin: 0px;
    }
</style>

<template>
    <v-card color="secondary" dark class="vacationcard">
        Urlaub
        <div class="d-flex align-content-start flex-wrap">
            <EmployeeImage
                    v-for="employee in employeesOnVacation"
                    :key="employee.id"
                    :employeeid="employee.id"
            />
        </div>
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
    }
    .nomargin {
        margin: 0px;
    }
</style>

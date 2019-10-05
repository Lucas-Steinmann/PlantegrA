<template>
  <div class="DayField">
    <span>Montag</span>
    <v-divider></v-divider>
    <Weather/>
  </div>
</template>

<script>
import Weather from "../components/Weather";

export default {
  components:{
    Weather
  },
  data: () => ({
    //
  })
};
</script>

<style scoped>
.DayField{
  max-width: 150px;
}
</style>
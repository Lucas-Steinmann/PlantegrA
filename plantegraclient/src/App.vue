<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title class="headline">
        <span>PlantegrA</span>
      </v-toolbar-title>
    </v-app-bar>

    <v-content>
      <router-view />
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "App",
  data: () => ({
    //
  })
};
</script>

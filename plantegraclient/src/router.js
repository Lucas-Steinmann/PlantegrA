import Vue from "vue";
import Router from "vue-router";
import Week from "./views/Week.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "week",
      component: Week
    }
  ]
});

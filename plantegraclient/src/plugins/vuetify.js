import Vue from "vue";
import Vuetify from "vuetify";
import "vuetify/dist/vuetify.min.css";
import de from "vuetify/es5/locale/de";

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    options: {
      customProperties: true
    },
    themes: {
      light: {
        primary: "#8c54d0",
        secondary: "#19b092",
        accent: "#3498db",
        error: "#ed3624",
        success: "#4CAF50",
        warning: "#fa9d00"
      }
    }
  },
  lang: {
    locales: { de },
    current: "de"
  },
  icons: {
    iconfont: "mdi"
  }
});

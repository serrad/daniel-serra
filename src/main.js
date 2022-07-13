import Vue from 'vue'
import * as VueGoogleMaps from "vue2-google-maps"
import vmodal from 'vue-js-modal'

Vue.use(vmodal)
Vue.config.productionTip = false
Vue.use(VueGoogleMaps, {
  load: {
    key: "AIzaSyBhby6uhgAVS-oYwYxLuzgl9BKLV0pGJHU",
    libraries: "places"
  }
});
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from "axios";

axios.defaults.baseURL = 'http://127.0.0.1:8000'


/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faUser, faUserDoctor, faHouseMedical, faHospitalUser, faHospital, faCalendarCheck, faHouse,
  faBuilding, faUsers } from "@fortawesome/free-solid-svg-icons"

/* add icons to the library */
library.add(faUser, faUserDoctor, faHouseMedical, faHospitalUser, faHospital, faCalendarCheck, faHouse, faBuilding, faUsers)

const app = createApp(App).use(store)

app.use(router, axios)

app.component('font-awesome-icon', FontAwesomeIcon).mount('#app')

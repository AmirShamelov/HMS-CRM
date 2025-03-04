import { createRouter, createWebHistory } from 'vue-router'
import store from "../store"

import HomeView from '../views/HomeView.vue'
import SignUp from "@/views/SignUp.vue"
import LogIn from "@/views/LogIn.vue"
import Dashboard from "@/views/dasnboard/Dashboard.vue"
import MyAccount from "@/views/dasnboard/MyAccount.vue"
import Departments from "@/views/departments/Departments.vue"
import Department from "@/views/departments/Department.vue"
import Appointments from "@/views/appointments/Appointments.vue"
import Appointment from "@/views/appointments/Appointment.vue"
import Patients from "@/views/patients/Patients.vue"
import Patient from "@/views/patients/Patient.vue"
import PatientConclusion from "@/views/patients/PatientConclusion.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/sign-up',
      name: 'SignUp',
      component: SignUp,
    },
    {
      path: '/log-in',
      name: 'LogIn',
      component: LogIn,
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard,
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/dashboard/my-account',
      name: 'MyAccount',
      component: MyAccount,
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/departments',
      name: 'Departments',
      component: Departments,
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/departments/:id',
      name: 'Department',
      component: Department,
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/appointments',
      name: 'Appointments',
      component: Appointments,
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/appointments/:id',
      name: 'Appointment',
      component: Appointment,
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/patients',
      name: 'Patients',
      component: Patients,
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/patients/:id',
      name: 'Patient',
      component: Patient,
      meta: {
        requireLogin: true
      }
    },
    {
      path: '/patients/:id/conclusion',
      name: 'PatientConclusion',
      component: PatientConclusion,
      meta: {
        requireLogin: true
      }
    },
  ],
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/log-in')
  } else {
    next()
  }
})

export default router

<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12 is-offset-5">
                <h1 class="title">Записи</h1>
            </div>
            <div class="column is-12 is-offset-1-desktop">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Врач</th>
                            <th>Дата</th>
                            <th>Время</th>
                            <th>Детали записи</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr
                            v-for="appointment in appointments"
                            v-bind:key="appointment.id">
                                <td>{{ appointment.doctor.first_name }} {{ appointment.doctor.last_name }}</td>
                                <td>{{ appointment.date }}</td>
                                <td>{{ appointment.time }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>


<script>
import axios from "axios";

export default {
    name: "Appointments",
    data() {
        return {
            appointments: []
        }
    },
    mounted() {
        this.getAppointments()
    },
    methods: {
        async getAppointments() {
            this.$store.commit('setIsLoading', true)

            axios
                .get('/api/v1/appointments/')
                .then(response => {
                    this.appointments = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>


<style scoped>

</style>
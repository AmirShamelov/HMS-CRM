<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12 is-offset-3">
                <h1 class="title">Записи</h1>
            </div>
            <div class="column is-12 is-offset-left">
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
                        <td>{{ getTimeLabel(appointment.time) }}</td>
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
        },
        getTimeLabel(timeValue) {
            const timeOptions = [
                {value: 1, label: '9:00-9:30'},
                {value: 2, label: '9:30-10:00'},
                {value: 3, label: '10:00-10:30'},
                {value: 4, label: '10:30-11:00'},
                {value: 5, label: '11:00-11:30'},
                {value: 6, label: '11:30-12:00'},
                {value: 7, label: '12:00-12:30'},
                {value: 8, label: '12:30-13:00'},
                {value: 9, label: '14:30-15:00'},
                {value: 10, label: '15:00-15:30'},
                {value: 11, label: '15:30-16:00'},
                {value: 12, label: '16:00-16:30'},
                {value: 13, label: '16:30-17:00'},
                {value: 14, label: '17:00-17:30'},
                {value: 15, label: '17:30-18:00'},
            ];
            const time = timeOptions.find(option => option.value === timeValue);
            return time ? time.label : 'Неизвестное время';
        },
    }
}
</script>


<style scoped>
.is-offset-left {
    margin-left: -100px;
}
</style>
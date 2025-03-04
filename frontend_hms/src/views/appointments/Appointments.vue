<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12 is-offset-3">
                <h1 class="title">Записи</h1>
            </div>
            <div class="column is-12 is-offset-left">
                <h2 class="subtitle">Активные записи</h2>
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
                        v-for="appointment in activeAppointments"
                        v-bind:key="appointment.id">
                        <td>{{ appointment.doctor.first_name }} {{ appointment.doctor.last_name }}</td>
                        <td>{{ appointment.date }}</td>
                        <td>{{ getTimeLabel(appointment.time) }}</td>
                        <td>
                            <router-link :to="{ name: 'Appointment', params: { id: appointment.id }}">Перейти к записи</router-link>
                        </td>
                    </tr>
                    </tbody>
                </table>

                <h2 class="subtitle">Неактивные записи</h2>
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
                        v-for="appointment in inactiveAppointments"
                        v-bind:key="appointment.id"
                        class="has-text-grey"
                    >
                        <td class="has-text-grey">{{ appointment.doctor.first_name }} {{ appointment.doctor.last_name }}</td>
                        <td class="has-text-grey">{{ appointment.date }}</td>
                        <td class="has-text-grey">{{ getTimeLabel(appointment.time) }}</td>
                        <td>
                            <router-link :to="{ name: 'Appointment', params: { id: appointment.id }}" class="has-text-grey">Перейти к записи</router-link>
                        </td>
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
            appointments: [],
            activeAppointments: [],
            inactiveAppointments: [],
        }
    },
    mounted() {
        this.getAppointments()
    },
    methods: {
        async getAppointments() {
            this.$store.commit('setIsLoading', true)

            await axios
                .get('/api/v1/appointments/')
                .then(response => {
                    this.appointments = response.data
                    this.filterAppointments()
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },
        getTimeLabel(timeValue) {
            const timeOptions = [
                {value: 1, label: '09:00'},
                {value: 2, label: '09:30'},
                {value: 3, label: '10:00'},
                {value: 4, label: '10:30'},
                {value: 5, label: '11:00'},
                {value: 6, label: '11:30'},
                {value: 7, label: '12:00'},
                {value: 8, label: '12:30'},
                {value: 9, label: '14:30'},
                {value: 10, label: '15:00'},
                {value: 11, label: '15:30'},
                {value: 12, label: '16:00'},
                {value: 13, label: '16:30'},
                {value: 14, label: '17:00'},
                {value: 15, label: '17:30'},
            ];
            const time = timeOptions.find(option => option.value === timeValue);
            return time ? time.label : 'Неизвестное время';
        },
        getDateTime(appointment) {
            const date = appointment.date
            const timeLabel = this.getTimeLabel(appointment.time);
            return new Date(`${date}T${timeLabel}:00`)
        },
        filterAppointments() {
            const now = new Date();

            this.activeAppointments = this.appointments.filter(appointment => {
                const appointmentDateTime = this.getDateTime(appointment);
                return appointmentDateTime > now
            });

            this.inactiveAppointments = this.appointments.filter(appointment => {
                const appointmentDateTime = this.getDateTime(appointment);
                return appointmentDateTime <= now
            });

        }
    }
}
</script>


<style scoped>
.is-offset-left {
    margin-left: -100px;
}

.has-text-grey {
    color: #999;
}

</style>
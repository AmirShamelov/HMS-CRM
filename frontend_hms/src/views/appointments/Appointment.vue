<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <template v-if="appointment.doctor">
                    <h1 class="title">Запись к врачу {{ appointment.doctor.first_name }} {{
                            appointment.doctor.last_name
                        }}</h1>
                </template>
            </div>

            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Детали записи</h2>
                    <p><strong>Имя: </strong>{{ appointment.patient_name }}</p>
                    <p><strong>ИИН пациента: </strong>{{ appointment.patient_iin }}</p>
                    <p><strong>Дата: </strong>{{ appointment.date }}</p>
                    <p><strong>Время записи: </strong>{{ getTimeLabel(appointment.time) }}</p>
                    <template v-if="appointment.comment">
                        <p><strong>Описание: </strong>{{ appointment.comment }}</p>
                    </template>
                </div>

                <div class="box">
                    <h2 class="subtitle">Заключение врача</h2>
                    <template v-if="appointment.conclusion">
                        <p><strong>Заключение: </strong>{{ appointment.conclusion }}</p>
                        <p><strong>Лечение: </strong>{{ appointment.treatment }}</p>
                    </template>

                    <template v-else>
                        <p>Врач еще не добавил заключение...</p>
                    </template>
                </div>
            </div>


        </div>
    </div>
</template>

<script>
import axios from "axios"

export default {
    name: "Appointment",
    data() {
        return {
            appointment: {}
        }
    },
    mounted() {
        this.getAppointment()
    },
    methods: {
        async getAppointment() {
            this.$store.commit('setIsLoading', true)

            const appointmentID = this.$route.params.id

            await axios
                .get(`/api/v1/appointments/${appointmentID}/`)
                .then(response => {
                    this.appointment = response.data
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

</style>
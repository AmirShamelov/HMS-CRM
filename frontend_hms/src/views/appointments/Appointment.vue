<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <template v-if="appointment.doctor">
                    <h1 class="title">
                        <font-awesome-icon class="sidebar-icon" icon="fa-solid fa-calendar-check"/>
                        Запись к врачу {{ appointment.doctor.full_name }}
                    </h1>
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

                <div class="buttons">
                    <button class="button is-danger" @click="openAppointmentModal">Отменить запись</button>
                </div>

                <div v-if="isModalOpen" class="modal-overlay">
                    <div class="modal-content">
                        <h3>Вы уверены что хотите отменить запись?</h3>
                        <div class="buttons">
                            <button type="submit" class="button is-success" @click="deleteAppointment">Да</button>
                            <button type="button" class="button is-danger" @click="closeAppointmentModal">Нет</button>
                        </div>
                    </div>
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
            appointment: {},
            isModalOpen: false,
        }
    },
    mounted() {
        this.getAppointment()
    },
    methods: {
        async deleteAppointment() {
            this.$store.commit('setIsLoading', true)

            const appointmentID = this.$route.params.id

            await axios
                .post(`/api/v1/appointments/delete_appointment/${appointmentID}/`)
                .then(response => {
                    console.log(response.data)

                    this.$router.push('/appointments')
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },
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
        openAppointmentModal() {
            this.isModalOpen = true;
        },
        closeAppointmentModal() {
            this.isModalOpen = false;
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

.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
}

.modal-content {
    background-color: white;
    padding: 20px;
    border-radius: 5px;
    width: 400px;
    max-width: 90%;
}

.modal-content h3 {
    margin-top: 0;
    margin-bottom: 15px;
}

</style>
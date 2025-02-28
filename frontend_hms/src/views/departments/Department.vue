<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12 is-offset-3">
                <h1 class="title">{{ department.title }}</h1>
            </div>

            <div class="column is-12 is-offset-left">
                <table class="table is-fullwidth">
                    <thead>
                    <tr>
                        <th>ИИН врача</th>
                        <th>Имя Фамилия</th>
                        <th>Запись</th>
                    </tr>
                    </thead>

                    <tbody>
                    <tr
                        v-for="doctor in department.doctors"
                        :key="doctor.id" :value="doctor.id"
                    >
                        <td>{{ doctor.username }}</td>
                        <td>{{ doctor.first_name }} {{ doctor.last_name }}</td>

                        <td @click="openAppointmentModal(doctor)" class="appointment-cell">
                            Записаться на прием
                        </td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <div v-if="isModalOpen" class="modal-overlay">
            <div class="modal-content">
                <h3>Запись на прием к {{ selectedDoctor.first_name }} {{ selectedDoctor.last_name }}</h3>
                <form @submit.prevent="submitAppointmentForm">
                    <div class="field">
                        <label>Ваше имя</label>
                        <input type="text" v-model="appointmentForm.patient_name" required/>
                    </div>
                    <div class="field">
                        <label>Ваш ИИН</label>
                        <input type="text" v-model="appointmentForm.patient_iin" pattern="\d{12}"
                               title="ИИН должен состоять из 12 цифр" required/>
                    </div>
                    <div class="field">
                        <label>Дата приема</label>
                        <select v-model="appointmentForm.date" @change="loadAvailableTimes" required>
                            <option value="" selected>Выберите дату</option>
                            <option v-for="date in availableDates" :key="date" :value="date">
                                {{ date }}
                            </option>
                        </select>
                    </div>
                    <div class="field">
                        <label>Время приема</label>
                        <select v-model="appointmentForm.time" :disabled="!appointmentForm.date">
                            <option value="" selected>Выберите время</option>
                            <option v-for="time in availableTimes" :key="time.value" :value="time.value">
                                {{ time.label }}
                            </option>
                        </select>
                    </div>
                    <div class="field">
                        <label>Комментарий</label>
                        <textarea v-model="appointmentForm.comment"></textarea>
                    </div>
                    <div class="modal-buttons">
                        <button type="submit" class="button is-success">Отправить</button>
                        <button type="button" @click="closeAppointmentModal" class="cancel-button">
                            Отмена
                        </button>
                    </div>
                </form>
            </div>
        </div>
        <div class="column is-12 is-offset-3">
            <router-link to="/departments" class="back-link">Назад к списку отделений</router-link>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "Department",
    data() {
        return {
            department: {
                doctors: []
            },
            isModalOpen: false,
            selectedDoctor: null,
            appointmentForm: {
                patient_name: '',
                patient_iin: '',
                date: '',
                time: 1,
                comment: '',
            },
            availableTimes: [],
            availableDates: [],
        }
    },
    mounted() {
        this.getDepartment()
    },
    methods: {
        async getDepartment() {
            this.$store.commit('setIsLoading', true)

            const DepartmentID = this.$route.params.id

            await axios
                .get(`/api/v1/departments/${DepartmentID}/`)
                .then(response => {
                    this.department = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },
        openAppointmentModal(doctor) {
            this.selectedDoctor = doctor;
            this.isModalOpen = true;
            this.loadAvailableDates()
        },
        closeAppointmentModal() {
            this.isModalOpen = false;  // Закрываем модальное окно
            this.selectedDoctor = null;  // Сбрасываем выбранного врача
            this.resetAppointmentForm();
        },
        resetAppointmentForm() {
            this.appointmentForm = {
                patient_name: '',
                patient_iin: '',
                date: '',
                time: 1,
                comment: '',
            };
            this.availableTimes = [];
            this.availableDates = [];
        },
        async loadAvailableDates() {
            this.$store.commit('setIsLoading', true)

            if (this.selectedDoctor) {
                await axios
                    .get(`/api/v1/appointments/available_dates/?doctor_id=${this.selectedDoctor.id}`)
                    .then(response => {
                        this.availableDates = response.data
                    })
                    .catch(error => {
                        console.log(error)
                        this.availableDates = [];
                    })
            }
            this.$store.commit('setIsLoading', false)
        },
        async loadAvailableTimes() {
            this.$store.commit('setIsLoading', true)

            if (this.selectedDoctor && this.appointmentForm.date) {
                await axios
                    .get(`/api/v1/appointments/available_times/?doctor_id=${this.selectedDoctor.id}&date=${this.appointmentForm.date}`)
                    .then(response => {
                        this.availableTimes = response.data.map(time => ({
                            value: time[0],
                            label: time[1],
                        }))
                    })
                    .catch(error => {
                        console.log(error)
                        this.availableTimes = [];
                    })
            }

            this.$store.commit('setIsLoading', false)
        },
        async submitAppointmentForm() {
            this.$store.commit('setIsLoading', true)

            const appointment = {
                department: this.department.id,
                doctor_id: this.selectedDoctor.id,
                ...this.appointmentForm,
            }

            await axios
                .post('/api/v1/appointments/', appointment)
                .then(response => {
                    console.log(response)

                    this.$router.push('/appointments')
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },
    }
}
</script>


<style scoped>
.is-offset-left {
    margin-left: -100px;
}

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
}

.field {
    margin-bottom: 15px;
}

.field label {
    display: block;
    margin-bottom: 5px;
}

.field input,
.field textarea {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.modal-buttons {
    display: flex;
    justify-content: space-between;
}

.submit-button {
    background-color: #42b983;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
}

.submit-button:hover {
    background-color: #369c6e;
}

.cancel-button {
    background-color: #ff3860;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
}

.cancel-button:hover {
    background-color: #e03157;
}

.appointment-cell {
    color: #369c6e;
    cursor: pointer;
}

.appointment-cell:hover {
    text-decoration: underline;
}
</style>
<template>
    <div class="container">
        <div class="column is-12">
            <h1 class="title">Наши врачи</h1>

            <form @submit.prevent="getDoctors">
                <div class="field has-addons">
                    <div class="control">
                        <input type="text" placeholder="Введите фамилию врача или отделение" class="input" v-model="query">
                    </div>
                    <div class="control">
                        <button class="button is-success" @click="search">Найти</button>
                    </div>
                </div>
            </form>
        </div>

        <div class="columns is-multiline">
            <div
                v-for="doctor in doctors"
                :key="doctor.id"
                class="column is-4"
            >
                <div class="card">
                    <div class="card-image">
                        <figure class="image mb-4">
                            <img
                                v-bind:src="doctor.get_image"
                                :alt="doctor.full_name"
                                loading="lazy"
                            />
                        </figure>
                    </div>
                    <div class="card-content">
                        <div class="media">
                            <div class="media-content">
                                <p class="title is-4">{{ doctor.full_name }}</p>
                                <hr>
                                <p class="subtitle is-5">{{ doctor.position }}</p>
                            </div>
                        </div>
                        <div class="content">
                            <p><strong>Образование:</strong> {{ doctor.education }}</p>
                            <p><strong>Отделение:</strong> {{ doctor.department.title }}</p>
                        </div>
                        <div class="buttons">
                            <button @click="openAppointmentModal(doctor)" class="button is-success">
                                Записатья на прием
                            </button>

                            <router-link :to="{ name: 'Doctor', params: {id: doctor.id}}"
                                         class="button is-info">Профиль
                            </router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="buttons">
            <button class="button is-light" @click="goToPreviousPage()" v-if="showPreviousButton">Назад</button>
            <button class="button is-light" @click="goToNextPage()" v-if="showNextButton">Вперед</button>
        </div>

        <div v-if="isModalOpen" class="modal-overlay">
            <div class="modal-content">
                <h3>Запись на прием к {{ selectedDoctor.full_name }}</h3>
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
    </div>
</template>


<script>
import axios from "axios";

export default {
    name: "Doctors",
    data() {
        return {
            doctors: [],
            showNextButton: false,
            showPreviousButton: false,
            currentPage: 1,
            query: '',
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
        this.getDoctors()
    },
    methods: {
        async getDoctors() {
            this.$store.commit('setIsLoading', true)

            this.showNextButton = false
            this.showPreviousButton = false

            await axios
                .get(`/api/v1/doctors/?page=${this.currentPage}&search=${this.query}`)
                .then(response => {
                    this.doctors = response.data.results

                    if (response.data.next) {
                        this.showNextButton = true
                    }

                    if (response.data.previous) {
                        this.showPreviousButton = true
                    }
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
            this.isModalOpen = false;
            this.selectedDoctor = null;
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
                department: this.selectedDoctor.department.id,
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

        goToNextPage() {
            this.currentPage += 1
            this.getDoctors()
        },
        goToPreviousPage() {
            this.currentPage -= 1
            this.getDoctors()
        },

        search() {
            this.currentPage = 1;
            this.getDoctors()
        },

    }
}
</script>


<style scoped>

.container {
    padding: 20px;
}

.title {
    text-align: center;
    margin-bottom: 30px;
}

.card {
    height: 100%;
    display: flex;
    flex-direction: column;
}

.card-content {
    flex-grow: 1;
}

.image.mb-4 {
    height: 500px;
    overflow: hidden;
}

.image.mb-4 img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center;
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


</style>
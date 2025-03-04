<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Запись № {{ patient.id }}</h1>
            </div>

            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Детали записи</h2>
                    <p><strong>Имя: </strong>{{ patient.patient_name }}</p>
                    <p><strong>ИИН пациента: </strong>{{ patient.patient_iin }}</p>
                    <p><strong>Дата: </strong>{{ patient.date }}</p>
                    <p><strong>Время записи: </strong>{{ getTimeLabel(patient.time) }}</p>
                    <template v-if="patient.comment">
                        <p><strong>Описание: </strong>{{ patient.comment }}</p>
                    </template>
                </div>

                <div class="buttons">
                    <router-link :to="{ name: 'PatientConclusion', params: { id: patient.id }}" class="button is-light">
                        Перейти к заключению
                    </router-link>
                </div>
            </div>

            <div class="box">
                <h2 class="subtitle">Заключение доктора</h2>
                <template v-if="patient.conclusion">
                    <p><strong>Заключение: </strong>{{ patient.conclusion }}</p>
                </template>

                <template v-if="patient.treatment">
                    <p><strong>Лечение: </strong>{{ patient.treatment }}</p>
                </template>
            </div>
        </div>
    </div>
</template>


<script>
import axios from "axios";

export default {
    name: "Patient",
    data() {
        return {
            patient: {}
        }
    },
    mounted() {
        this.getPatient()
    },
    methods: {
        async getPatient() {
            this.$store.commit('setIsLoading', true)

            const patientID = this.$route.params.id

            await axios
                .get(`/api/v1/patients/${patientID}/`)
                .then(response => {
                    this.patient = response.data
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
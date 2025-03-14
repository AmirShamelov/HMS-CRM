<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12 is-offset-3">
                <h1 class="title">Записи пациентов</h1>

                <form @submit.prevent="getPatients">
                    <div class="field has-addons">
                        <div class="control">
                            <input type="text" class="input" v-model="query">
                        </div>
                        <div class="control">
                            <button class="button is-success" @click="search">Найти</button>
                        </div>
                    </div>
                </form>
            </div>
            <div class="column is-12 is-offset-left">
                <table class="table is-fullwidth">
                    <thead>
                    <tr>
                        <th>Пациент</th>
                        <th>Дата</th>
                        <th>Время</th>
                        <th>Детали записи</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr
                        v-for="patient in patients"
                        v-bind:key="patient.id">
                        <td>{{ patient.patient_name }}</td>
                        <td>{{ patient.date }}</td>
                        <td>{{ getTimeLabel(patient.time) }}</td>
                        <td>
                            <router-link :to="{ name: 'Patient', params: { id: patient.id }}">Перейти к записи</router-link>
                        </td>
                    </tr>
                    </tbody>
                </table>
                <div class="buttons">
                    <button class="button is-light" @click="goToPreviousPage()" v-if="showPreviousButton">Назад</button>
                    <button class="button is-light" @click="goToNextPage()" v-if="showNextButton">Вперед</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "Patients",
    data() {
        return {
            patients: [],
            showNextButton: false,
            showPreviousButton: false,
            currentPage: 1,
            query: '',
        }
    },
    mounted() {
        this.getPatients()
    },
    methods: {
        goToNextPage() {
            this.currentPage += 1
            this.getPatients()
        },

        goToPreviousPage() {
            this.currentPage -= 1
            this.getPatients()
        },

        async getPatients() {
            this.$store.commit('setIsLoading', true)

            this.showNextButton = false
            this.showPreviousButton = false

            await axios
                .get(`/api/v1/patients/?page=${this.currentPage}&search=${this.query}`)
                .then(response => {
                    this.patients = response.data.results

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
        search() {
            this.currentPage = 1;
            this.getPatients()
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
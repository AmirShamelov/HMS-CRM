<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Пациент {{ patient.patient_name }}</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Заключение</label>
                        <div class="control">
                            <input type="text" class="input" v-model="patient.conclusion">
                        </div>
                    </div>

                    <div class="field">
                        <label>Лечение</label>
                        <div class="control">
                            <textarea class="textarea" v-model="patient.treatment"></textarea>
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Сохранить</button>
                        </div>
                    </div>

                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

export default {
    name: "PatientConclusion",
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
        async submitForm() {
            this.$store.commit('setIsLoading', true)

            const patientID = this.$route.params.id

            axios
                .patch(`/api/v1/patients/${patientID}/`, this.patient)
                .then(response => {
                    toast({
                        message: 'Заключение добавлено',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })

                    this.$router.push(`/patients/${patientID}`)
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
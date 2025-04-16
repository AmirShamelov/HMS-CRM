<template>
    <template v-if="$store.state.department.title">
        <div class="container">
            <div class="columns is-multiline">
                <div class="column is-12">
                    <h1 class="title">Медицинский статус {{ user.id }}</h1>
                </div>

                <div class="column is-12">
                    <form @submit.prevent="submitForm">
                        <div class="field">
                            <label>Группа крови</label>
                            <div class="control">
                                <div class="select">
                                    <select v-model="user.blood">
                                        <option value="" selected>Выберите группу крови</option>
                                        <option
                                            v-for="option in bloodTypes"
                                            :key="option.value"
                                            :value="option.value"
                                        >
                                            {{ option.label }}
                                        </option>
                                    </select>
                                </div>
                            </div>
                        </div>

                        <div class="field">
                            <label>Аллергия</label>
                            <div class="control">
                                <textarea class="textarea" v-model="user.allergies"></textarea>
                            </div>
                        </div>

                        <div class="field">
                            <label>Хроническое заболевание</label>
                            <div class="control">
                                <textarea class="textarea" v-model="user.chronic_disease"></textarea>
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
</template>

<script>
import axios from "axios";
import {toast} from "bulma-toast";

export default {
    name: "PatientMedicalStatus",
    data() {
        return {
            user: {

            },
            bloodTypes: [
                {value: 1, label: '0-'},
                {value: 2, label: '0+'},
                {value: 3, label: 'A-'},
                {value: 4, label: 'A+'},
                {value: 5, label: 'B-'},
                {value: 6, label: 'B+'},
                {value: 7, label: 'AB-'},
                {value: 8, label: 'AB+'},
            ]
        }
    },
    mounted() {
      this.getUsers()
    },
    methods: {
        async getUsers() {
            this.$store.commit('setIsLoading', true)

            const UserID = this.$route.params.id

            await axios
                .get(`/api/v1/user/${UserID}/`)
                .then(response => {
                    this.user = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },
        async submitForm() {
            this.$store.commit('setIsLoading', true)

            const UserID = this.$route.params.id

            axios
                .patch(`/api/v1/user/${UserID}/`, this.user)
                .then(response => {
                    toast({
                        message: 'Изменен медицинский статус',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })

                    this.$router.go(-1)
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
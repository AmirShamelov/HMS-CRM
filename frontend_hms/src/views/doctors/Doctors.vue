<template>
    <div class="container">
        <div class="column is-12 is-offset-left">
            <h1 class="title">Наши врачи</h1>

            <form @submit.prevent="getDoctors">
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

        <div class="columns is-multiline is-offset-left">
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
                            <router-link :to="{ name: 'Department', params: {id: doctor.department.id}}"
                                         class="button is-success">Записаться на прием
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
        }
    },
    mounted() {
        this.getDoctors()
    },
    methods: {
        goToNextPage() {
            this.currentPage += 1
            this.getDoctors()
        },
        goToPreviousPage() {
            this.currentPage -= 1
            this.getDoctors()
        },
        async getDoctors() {
            this.$store.commit('setIsLoading', true)

            this.showNextButton = false
            this.showPreviousButton = false

            await axios
                .get(`/api/v1/doctors/?page=${this.currentPage}&search=${this.query}`)
                .then(response => {
                    console.log(response.data)
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
        search() {
          this.currentPage = 1;
          this.getDoctors()
        },
    }
}
</script>


<style scoped>
.is-offset-left {
    margin-left: -100px;
}

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

.image img {
    object-fit: cover;
    width: 100%;
    height: auto;
}

</style>
<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12 is-offset-3">
                <h1 class="title">Отделения</h1>
            </div>
            <div class="column is-12 is-offset-left">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Отделение</th>
                            <th>Депаратамент</th>
                            <th>Врачи</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr
                            v-for="department in departments"
                            v-bind:key="department.id">
                                <td>{{ department.title }}</td>
                                <td>{{ department.sub_title }}</td>
                                <td>
                                    <router-link :to="{ name: 'Department', params: { id: department.id }}">Выбрать врача</router-link>
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
    name: "Departments",
    data() {
        return {
            departments: []
        }
    },
    mounted() {
        this.getDepartments()
    },
    methods: {
        async getDepartments() {
            this.$store.commit('setIsLoading', true)

            axios
                .get('/api/v1/departments/')
                .then(response => {
                    this.departments = response.data
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
.is-offset-left {
  margin-left: -100px;
}
</style>
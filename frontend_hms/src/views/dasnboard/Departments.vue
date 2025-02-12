<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12 is-offset-5">
                <h1 class="title">Departments</h1>
            </div>
            <div class="column is-12 is-offset-1">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Department</th>
                            <th>Sub title</th>
                            <th>Link</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr
                            v-for="department in departments"
                            v-bind:key="department.id">
                                <td>{{ department.title }}</td>
                                <td>{{ department.sub_title }}</td>
                                <td>{{ department.link }}</td>
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
                .get('/api/v1/departments')
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

</style>
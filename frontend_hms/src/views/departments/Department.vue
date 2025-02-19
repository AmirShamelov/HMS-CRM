<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12 is-offset-5">
                <h1 class="title">{{ department.title }}</h1>
            </div>

            <div class="column is-12 is-offset-1-desktop">
                <h2 class="subtitle">Врачи</h2>

                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>ИИН врача</th>
                            <th>Имя</th>
                            <th>Прием</th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr
                            v-for="doctor in department.doctors"
                            :key="doctor.id"
                        >
                            <td>{{ doctor.username }}</td>
                            <td>{{ doctor.first_name}} {{ doctor.last_name }}</td>
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
    name: "Department",
    data () {
        return {
            department: {
                doctors: [
                ]
            }
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
        }
    }
}
</script>


<style scoped>

</style>
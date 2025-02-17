<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12 is-offset-6">
                <h1 class="title">{{ department.title }}</h1>
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
            department: {}
        }
    },
    mounted() {
        this.getDepartment()
    },
    methods: {
        async getDepartment() {
            this.$store.commit('setIsLoading', true)

            const DepartmentID = this.$route.params.id

            axios
                .get(`/api/v1/departments/${DepartmentID}`)
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
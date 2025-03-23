<template>
    <div class="departments">
        <h1 class="departments-title">Наши отделения</h1>
        <form @submit.prevent="getDepartments">
            <div class="field has-addons">
                <div class="control">
                    <input type="text" class="input" v-model="query">
                </div>
                <div class="control">
                    <button class="button is-success">Найти</button>
                </div>
            </div>
        </form>
        <hr>
        <div class="column is-11">
            <div class="departments-grid">
                <div
                    v-for="department in departments"
                    :key="department.id"
                    class="department-card"
                    @click = "goToDepartment(department.id)"
                >
                    <font-awesome-icon :icon="department.link" class="department-icon"/>
                    <h2 class="department-name">{{ department.title }}</h2>
                    <p class="department-description">{{ department.sub_title }}</p>
                </div>
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
            departments: [],
            query: '',
        }
    },
    mounted() {
        this.getDepartments()
    },
    methods: {
        async getDepartments() {
            this.$store.commit('setIsLoading', true)

            await axios
                .get(`/api/v1/departments/?search=${this.query}`)
                .then(response => {
                    this.departments = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },
        goToDepartment(id) {
            this.$router.push({name: 'Department', params: { id } })
        }
    }
}
</script>


<style scoped>

hr {
    background-color: darkgray;
}

.departments {
    padding: 20px;
    text-align: center;
    min-height: 100vh;
}

.departments-title {
    font-size: 2.5rem;
    margin-bottom: 40px;
}

.departments-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    padding: 0 20px;
}

.department-card {
    background-color: white;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    cursor: pointer;
}

.department-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.department-icon {
    font-size: 2.5rem;
    color: #1e90ff;
    margin-bottom: 15px;
}

.department-name {
    font-size: 1.5rem;
    color: #2c3e50;
    margin-bottom: 10px;
}

.department-description {
    font-size: 1rem;
    color: #666;
    line-height: 1.5;
}

</style>
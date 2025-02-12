<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Вход по ИИН</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>ИИН</label>
                        <div class="control">
                            <input type="text" name="iin" class="input" v-model="username" pattern="\d{12}" title="ИИН должен состоять из 12 цифр">
                        </div>
                    </div>
                    <div class="field">
                        <label>Пароль</label>
                        <div class="control">
                            <input type="password" name="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Войти</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'LogIn',
        data() {
            return {
                username: '',
                password: '',
                errors: []
            }
        },
        methods: {
            async submitForm() {
                this.$store.commit('setIsLoading', true)

                axios.defaults.headers.common['Authorization'] = ''
                localStorage.removeItem('token')
                const formData = {
                    username: this.username,
                    password: this.password
                }
                await axios
                    .post('/api/v1/token/login/', formData)
                    .then(response => {
                        const token = response.data.auth_token
                        this.$store.commit('setToken', token)
                        axios.defaults.headers.common['Authorization'] = 'Token ' + token
                        localStorage.setItem('token', token)
                        this.$router.push('/dashboard/my-account')
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again!')
                        }
                    })
                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>
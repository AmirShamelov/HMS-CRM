<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Регистрация</h1>

                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>ИИН</label>
                        <div class="control">
                            <input type="text" name="iin" class="input" v-model="username" pattern="\d{12}" title="ИИН должен состоять из 12 цифр">
                        </div>
                    </div>
                    <div class="field">
                        <label>Имя</label>
                        <div class="control">
                            <input type="text" name="first_name" class="input" v-model="first_name">
                        </div>
                    </div>
                    <div class="field">
                        <label>Фамилия</label>
                        <div class="control">
                            <input type="text" name="last_name" class="input" v-model="last_name">
                        </div>
                    </div>
                    <div class="field">
                        <label>Пароль</label>
                        <div class="control">
                            <input type="password" name="password1" class="input" v-model="password1">
                        </div>
                    </div>
                    <div class="field">
                        <label>Повторите пароль</label>
                        <div class="control">
                            <input type="password" name="password2" class="input" v-model="password2">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Подтвердить</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    import {toast} from 'bulma-toast'

    export default {
        name: 'SignUp',
        data() {
            return {
                username: '',
                first_name: '',
                last_name: '',
                password1: '',
                password2: '',
                errors: []
            }
        },
        methods: {
            submitForm() {
                this.errors = []
                if (this.username === '') {
                    this.errors.push('The username is missing')
                }
                if (this.first_name === '') {
                    this.errors.push('The first_name is missing')
                }
                if (this.last_name === '') {
                    this.errors.push('The last_name is missing')
                }
                if (this.password1 === '') {
                    this.errors.push('The password is too short')
                }
                if (this.password1 !== this.password2) {
                    this.errors.push('The password are not matching')
                }
                if (!this.errors.length) {
                    const formData = {
                        username: this.username,
                        password: this.password1,
                        first_name: this.first_name,
                        last_name: this.last_name
                    }
                    axios
                        .post('/api/v1/users/', formData)
                        .then(response => {
                            toast({
                                message: 'Account was created, please log in',
                                type: 'is-success',
                                dismissible: true,
                                pauseOnHover: true,
                                duration: 2000,
                                position: 'bottom-right',
                            })
                            this.$router.push('/log-in')
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
                }
            }
        }
    }
</script>
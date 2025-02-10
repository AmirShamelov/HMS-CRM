<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Регистрация</h1>

                <form>
                    <div class="field">
                        <label>ИИН</label>
                        <div class="control">
                            <input type="text" name="iin" class="input" pattern="\d{12}" title="ИИН должен состоять из 12 цифр">
                        </div>
                    </div>
                    <div class="field">
                        <label>Имя</label>
                        <div class="control">
                            <input type="text" name="first_name" class="input">
                        </div>
                    </div>
                    <div class="field">
                        <label>Фамилия</label>
                        <div class="control">
                            <input type="text" name="last_name" class="input">
                        </div>
                    </div>
                    <div class="field">
                        <label>Дата рождения</label>
                        <div class="control">
                            <input type="date" name="birth_date" class="input">
                        </div>
                    </div>
                    <div class="field">
                        <label>Пароль</label>
                        <div class="control">
                            <input type="password" name="password1" class="input">
                        </div>
                    </div>
                    <div class="field">
                        <label>Повторите пароль</label>
                        <div class="control">
                            <input type="password" name="password2" class="input">
                        </div>
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
    export default {
        name: 'SignUp'
    }
</script>
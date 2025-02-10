<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Вход по ИИН</h1>

                <form>
                    <div class="field">
                        <label>ИИН</label>
                        <div class="control">
                            <input type="text" name="iin" class="input" pattern="\d{12}" title="ИИН должен состоять из 12 цифр">
                        </div>
                    </div>
                    <div class="field">
                        <label>Пароль</label>
                        <div class="control">
                            <input type="password" name="password" class="input">
                        </div>
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
    export default {
        name: 'LogIn'
    }
</script>
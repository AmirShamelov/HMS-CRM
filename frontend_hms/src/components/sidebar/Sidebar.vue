<template>
    <template v-if="$store.state.isAuthenticated">
        <div class="sidebar">
            <hr>
            <h2 class="sidebar-title">Меню</h2>
            <ul class="sidebar-menu">
                <li class="sidebar-item">
                    <router-link to="/" class="sidebar-link">Главная</router-link>
                </li>
                <li class="sidebar-item">
                    <router-link to="/departments" class="sidebar-link">Департаменты</router-link>
                </li>
                <li class="sidebar-item">
                    <router-link to="/doctors" class="sidebar-link">Врачи</router-link>
                </li>
                <li class="sidebar-item">
                    <router-link to="/appointments" class="sidebar-link">Записи</router-link>
                </li>
                <li class="sidebar-item">
                    <router-link to="/profile" class="sidebar-link">Профиль</router-link>
                </li>
            </ul>
        </div>
    </template>
</template>

<script>
export default {
    name: 'Sidebar'
}
</script>

<style scoped>
.sidebar {
    width: 200px; /* Ширина Sidebar */
    background-color: #2c3e50;
    color: white;
    padding: 20px;
    height: 100vh;
    position: fixed; /* Фиксированное положение */
    top: 0;
    left: 0;
}

.sidebar-title {
    font-size: 1.5rem;
    margin-bottom: 20px;
    text-align: center;
}

.sidebar-menu {
    list-style: none;
    padding: 0;
}

.sidebar-item {
    margin-bottom: 15px;
}

.sidebar-link {
    color: white;
    text-decoration: none;
    font-size: 1.1rem;
    display: block;
    padding: 10px;
    border-radius: 5px;
    transition: background-color 0.3s ease;
}

.sidebar-link:hover {
    background-color: #34495e;
}

.router-link-active {
    background-color: #34495e;
    font-weight: bold;
}
</style>
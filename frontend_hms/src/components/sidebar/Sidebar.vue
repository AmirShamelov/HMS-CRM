<template>
    <template v-if="$store.state.isAuthenticated">
        <div class="app-container">
            <div class="sidebar">
                <h2 class="sidebar-title">Меню</h2>
                <ul class="sidebar-menu">
                    <li class="sidebar-item">
                        <router-link to="/" class="sidebar-link">
                            <font-awesome-icon class="sidebar-icon" icon="fa-solid fa-house"/>
                            <span class="sidebar-text">Главная</span>
                        </router-link>
                    </li>
                    <li class="sidebar-item">
                        <router-link to="/departments" class="sidebar-link">
                            <font-awesome-icon class="sidebar-icon" icon="fa-solid fa-building"/>
                            <span class="sidebar-text">Департаменты</span>
                        </router-link>
                    </li>
                    <template v-if="$store.state.department.title">
                        <li class="sidebar-item">
                            <router-link to="/patients" class="sidebar-link">
                                <font-awesome-icon class="sidebar-icon" icon="fa-solid fa-users"/>
                                <span class="sidebar-text">Пациенты</span>
                            </router-link>
                        </li>
                    </template>
                    <li class="sidebar-item">
                        <router-link to="/appointments" class="sidebar-link">
                            <font-awesome-icon class="sidebar-icon" icon="fa-solid fa-calendar-check"/>
                            <span class="sidebar-text">Записи</span>
                        </router-link>
                    </li>
                    <li class="sidebar-item">
                        <router-link to="/doctors" class="sidebar-link">
                            <font-awesome-icon class="sidebar-icon" icon="fa-solid fa-user-doctor"/>
                            <span class="sidebar-text">Врачи</span>
                        </router-link>
                    </li>
                </ul>
            </div>

            <div class="main-content">
                <Router-view/>
            </div>
        </div>
    </template>
</template>

<script>
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";

export default {
    name: 'Sidebar',
    components: {FontAwesomeIcon}
}
</script>

<style scoped>
.app-container {
    display: flex;
    min-height: 100vh;
}

.sidebar {
    width: 250px; /* Фиксированная ширина Sidebar */
    background-color: #2c3e50;
    color: white;
    padding: 20px;
    height: 100vh;
    position: sticky;
    top: 0;
}

.main-content {
    flex-grow: 1; /* Основная часть занимает оставшееся пространство */
    padding: 20px;
    margin-left: 50px; /* Отступ, равный ширине Sidebar */
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

.sidebar-icon {
    margin-right: 10px; /* Отступ справа от иконки */
    font-size: 18px; /* Размер иконки */
}

.sidebar-text {
    flex-grow: 1;
    text-align: left;
    font-size: 16px;
}
</style>
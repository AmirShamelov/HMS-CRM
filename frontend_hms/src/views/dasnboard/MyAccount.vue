<template>
    <div class="profile-container">
        <div class="profile-header">
            <h1>Мой профиль</h1>
            <div class="header-decoration"></div>
        </div>

        <div class="profile-card">
            <div class="profile-avatar">
                <font-awesome-icon icon="fa-solid fa-user" class="avatar-icon"/>
            </div>

            <div class="profile-info">
                <div class="info-section">
                    <h2>Основная информация</h2>
                    <div class="info-grid">
                        <div class="info-item">
                            <span class="info-label">ФИО:</span>
                            <span class="info-value">{{ user.first_name }} {{ user.last_name }}</span>
                        </div>
                        <div class="info-item">
                            <span class="info-label">ИИН:</span>
                            <span class="info-value">{{ user.username }}</span>
                        </div>
                        <div class="info-item">
                            <span class="info-label">Дата рождения:</span>
                            <span class="info-value">{{ user.profile.birth_date || 'Не указан' }}</span>
                        </div>
                    </div>
                </div>

                <div class="info-section">
                    <h2>Контактные данные</h2>
                    <div class="info-grid">
                        <div class="info-item">
                            <span class="info-label">Телефон:</span>
                            <span class="info-value">{{ user.profile.phone || 'Не указан' }}</span>
                        </div>
                        <div class="info-item">
                            <span class="info-label">Адрес:</span>
                            <span class="info-value">{{ user.profile.address || 'Не указан' }}</span>
                        </div>
                    </div>
                </div>

                <div class="info-section">
                    <h2>Медицинская информация</h2>
                    <div class="info-grid">
                        <div class="info-item">
                            <span class="info-label">Группа крови:</span>
                            <span class="info-value">{{ bloodType(user.profile.blood) || 'Не указан' }}</span>
                        </div>
                        <div class="info-item">
                            <span class="info-label">Аллергия:</span>
                            <span class="info-value">{{ user.profile.allergies || 'Не указан' }}</span>
                        </div>
                        <div class="info-item">
                            <span class="info-label">Хроническое заболевание:</span>
                            <span class="info-value">{{ user.profile.chronic_disease || 'Не указан' }}</span>
                        </div>
                    </div>
                </div>
            </div>

            <h3>Чтобы изменить информацию, обращайтесь к админу или врачу</h3>
            <hr>

            <button @click="logout()" class="button is-danger">
                Выйти из аккаунта
            </button>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'MyAccount',
    data() {
        return {
            user: {
                profile: []
            }
        }
    },
    mounted() {
        this.getUserProfile()
    },
    methods: {
        async getUserProfile() {
            this.$store.commit('setIsLoading', true)

            await axios
                .get('/api/v1/my_profile/')
                .then(response => {
                    this.user = response.data[0]
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },
        bloodType(bloodValue) {
            const bloodTypes = [
                {value: 1, label: '0-'},
                {value: 2, label: '0+'},
                {value: 3, label: 'A-'},
                {value: 4, label: 'A+'},
                {value: 5, label: 'B-'},
                {value: 6, label: 'B+'},
                {value: 7, label: 'AB-'},
                {value: 8, label: 'AB+'},
            ];
            const blood = bloodTypes.find(option => option.value === bloodValue);
            return blood ? blood.label : '-';
        },
        async logout() {
            await axios
                .post('/api/v1/token/logout/')
                .then(response => {
                    console.log('Logged out')
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })

            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('token')
            localStorage.removeItem('username')
            localStorage.removeItem('userid')
            this.$store.commit('removeToken')
            this.$router.push('/')
        },
    }
}
</script>


<style scoped>

hr {
    background: #1e90ff;
}

.profile-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: aliceblue;
    border-radius: 12px;
}

.profile-header {
    text-align: center;
    margin-bottom: 2rem;
}

.profile-header h1 {
    font-size: 2.2rem;
    color: #2c3e50;
    margin-bottom: 0.5rem;
}

.header-decoration {
    width: 80px;
    height: 4px;
    background: #1e90ff;
    margin: 0 auto;
    border-radius: 2px;
}

.profile-card {
    background: white;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    padding: 2rem;
    position: relative;
}

.profile-avatar {
    width: 100px;
    height: 100px;
    background: #f0f8ff;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 1.5rem;
    border: 3px solid #1e90ff;
}

.avatar-icon {
    font-size: 2.5rem;
    color: #1e90ff;
}

.info-section {
    margin-bottom: 2rem;
}

.info-section h2 {
    color: #1e90ff;
    font-size: 1.3rem;
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid #e0e0e0;
}

.info-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
}

.info-item {
    display: flex;
    flex-direction: column;
}

.info-label {
    font-weight: 600;
    color: #555;
    margin-bottom: 0.3rem;
    font-size: 0.9rem;
}

.info-value {
    font-size: 1.1rem;
    color: #333;
    padding: 0.5rem;
    background: #f9f9f9;
    border-radius: 6px;
    min-height: 40px;
    display: flex;
    align-items: center;
}
</style>
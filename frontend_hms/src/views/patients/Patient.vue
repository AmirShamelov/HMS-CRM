<template>
    <div class="appointment-container">
        <!-- Шапка с заголовком и декоративными элементами -->
        <div class="appointment-header">
            <h1 class="appointment-title">Запись #{{ patient.id }}</h1>
            <div class="divider"></div>
        </div>

        <!-- Основное содержимое в двух колонках -->
        <div class="appointment-content">
            <!-- Левая колонка - информация о пациенте -->
            <div class="patient-info-section">
                <div class="info-card">
                    <div class="card-header">
                        <h2>
                            <font-awesome-icon icon="fa-solid fa-user"/>
                            Основные данные
                        </h2>
                    </div>
                    <div class="card-body">
                        <div class="info-row">
                            <span class="info-label">ФИО пациента:</span>
                            <span class="info-value">{{ patient.patient_name }}</span>
                        </div>
                        <div class="info-row">
                            <span class="info-label">ИИН:</span>
                            <span class="info-value">{{ patient.patient_iin }}</span>
                        </div>
                        <div class="info-row">
                            <span class="info-label">Дата рождения:</span>
                            <span class="info-value">{{ patient.created_by.profile.birth_date }}</span>
                        </div>
                        <div class="info-row">
                            <span class="info-label">Дата приема:</span>
                            <span class="info-value">{{ patient.date }}</span>
                        </div>
                        <div class="info-row">
                            <span class="info-label">Время:</span>
                            <span class="info-value">{{ getTimeLabel(patient.time) }}</span>
                        </div>
                        <div v-if="patient.comment" class="info-row">
                            <span class="info-label">Жалобы:</span>
                            <span class="info-value">{{ patient.comment }}</span>
                        </div>
                    </div>
                </div>

                <!-- Кнопки действий -->
                <div class="action-buttons">
                    <router-link
                        :to="{ name: 'PatientConclusion', params: { id: patient.id }}"
                        class="action-btn primary">
                        <font-awesome-icon icon="fa-solid fa-file-medical"/>
                        Перейти к заключению
                    </router-link>

                    <button class="action-btn secondary">
                        <font-awesome-icon icon="fa-solid fa-print"/>
                        Распечатать
                    </button>
                </div>
            </div>

            <!-- Правая колонка - медицинская информация -->
            <div class="medical-info-section">
                <div class="info-card medical-card">
                    <div class="card-header">
                        <h2>
                            <font-awesome-icon icon="fa-solid fa-file-waveform"/>
                            Медицинские данные
                        </h2>
                    </div>
                    <div class="card-body">
                        <template v-if="patient.conclusion">
                            <div class="info-row">
                                <span class="info-label">Диагноз:</span>
                                <span class="info-value medical-value">{{ patient.conclusion }}</span>
                            </div>
                        </template>

                        <template v-if="patient.treatment">
                            <div class="info-row">
                                <span class="info-label">Назначения:</span>
                                <span class="info-value medical-value">{{ patient.treatment }}</span>
                            </div>
                        </template>

                        <div v-if="!patient.conclusion" class="empty-state">
                            <font-awesome-icon icon="fa-solid fa-file-circle-plus" class="empty-icon"/>
                            <p>Заключение не заполнено</p>
                        </div>
                    </div>
                </div>

                <div class="info-card medical-card">
                    <div class="card-header">
                        <h2>
                            <font-awesome-icon icon="fa-solid fa-heart-pulse"/>
                            Медицинский статус пациента
                        </h2>
                    </div>
                    <div class="card-body">
                        <div class="info-row">
                            <span class="info-label">Группа крови:</span>
                            <span class="info-value">{{ bloodType(patient.created_by.profile.blood) }}</span>
                        </div>

                        <div class="info-row">
                            <span class="info-label">Аллергии:</span>
                            <span class="info-value">{{ patient.created_by.profile.allergies || 'Не указан' }}</span>
                        </div>

                        <div class="info-row">
                            <span class="info-label">Хроническое:</span>
                            <span class="info-value">{{ patient.created_by.profile.chronic_disease || 'Не указан' }}</span>
                        </div>
                    </div>
                </div>

                <div class="action-buttons">
                    <router-link
                        :to="{ name: 'PatientMedicalStatus', params: { id: patient.created_by.profile.id }}"
                        class="action-btn primary">
                        Изменить данные
                    </router-link>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import axios from "axios";

export default {
    name: "Patient",
    data() {
        return {
            patient: {
                created_by: {
                    profile: []
                }
            }
        }
    },
    mounted() {
        this.getPatient()
    },
    methods: {
        async getPatient() {
            this.$store.commit('setIsLoading', true)

            const patientID = this.$route.params.id

            await axios
                .get(`/api/v1/patients/${patientID}/`)
                .then(response => {
                    this.patient = response.data
                    console.log(this.patient)
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },
        getTimeLabel(timeValue) {
            const timeOptions = [
                {value: 1, label: '9:00-9:30'},
                {value: 2, label: '9:30-10:00'},
                {value: 3, label: '10:00-10:30'},
                {value: 4, label: '10:30-11:00'},
                {value: 5, label: '11:00-11:30'},
                {value: 6, label: '11:30-12:00'},
                {value: 7, label: '12:00-12:30'},
                {value: 8, label: '12:30-13:00'},
                {value: 9, label: '14:30-15:00'},
                {value: 10, label: '15:00-15:30'},
                {value: 11, label: '15:30-16:00'},
                {value: 12, label: '16:00-16:30'},
                {value: 13, label: '16:30-17:00'},
                {value: 14, label: '17:00-17:30'},
                {value: 15, label: '17:30-18:00'},
            ];
            const time = timeOptions.find(option => option.value === timeValue);
            return time ? time.label : 'Неизвестное время';
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
    }
}
</script>


<style scoped>

.appointment-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
    font-family: 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
}

.appointment-header {
    margin-bottom: 2.5rem;
    text-align: center;
}

.appointment-title {
    font-size: 2.2rem;
    color: #2c3e50;
    font-weight: 600;
    margin-bottom: 1rem;
}

.divider {
    width: 80px;
    height: 4px;
    background: #1e90ff;
    margin: 0 auto;
    border-radius: 2px;
}

.appointment-content {
    display: grid;
    grid-template-columns: 1fr 1.5fr;
    gap: 2rem;
}

.info-card {
    background: white;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
    margin-bottom: 1.5rem;
    overflow: hidden;
    transition: transform 0.3s ease;
}


.card-header {
    background: #1e90ff;
    color: white;
    padding: 1.2rem 1.5rem;
}

.card-header h2 {
    font-size: 1.2rem;
    font-weight: 600;
    margin: 0;
    display: flex;
    align-items: center;
    gap: 0.8rem;
}

.card-body {
    padding: 1.5rem;
}

.info-row {
    display: flex;
    margin-bottom: 1rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid #f0f0f0;
}

.info-row:last-child {
    border-bottom: none;
    margin-bottom: 0;
    padding-bottom: 0;
}

.info-label {
    font-weight: 600;
    color: #555;
    min-width: 150px;
    font-size: 0.95rem;
}

.info-value {
    color: #333;
    flex: 1;
}

.medical-value {
    background: #f8f9fe;
    padding: 0.8rem;
    border-radius: 6px;
    border-left: 3px solid #4a6cf7;
}

.action-buttons {
    display: flex;
    gap: 1rem;
    margin-top: 1.5rem;
}

.action-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    padding: 0.8rem 1.5rem;
    border-radius: 8px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
    border: none;
}

.action-btn.primary {
    background: #1e90ff;
    color: white;
}

.action-btn.secondary {
    background: white;
    color: #1e90ff;
    border: 1px solid #1e90ff;
}

.action-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(74, 108, 247, 0.2);
}

.empty-state {
    text-align: center;
    padding: 2rem;
    color: #888;
}

.empty-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    color: #d0d0d0;
}

</style>
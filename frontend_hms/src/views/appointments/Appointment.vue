<template>
    <div class="appointment-page">
        <!-- Шапка с заголовком -->
        <div class="appointment-header">
            <template v-if="appointment.doctor">
                <h1 class="appointment-title">
                    <font-awesome-icon icon="fa-solid fa-calendar-check" class="header-icon"/>
                    Запись к врачу {{ appointment.doctor.full_name }}
                </h1>
                <div class="header-divider"></div>
            </template>
        </div>

        <!-- Основное содержимое -->
        <div class="appointment-content">
            <!-- Левая колонка - информация о записи -->
            <div class="appointment-details">
                <div class="detail-card">
                    <div class="card-header">
                        <font-awesome-icon icon="fa-solid fa-clipboard-list" class="card-icon"/>
                        <h2>Детали записи</h2>
                    </div>
                    <div class="card-body">
                        <div class="detail-row">
                            <span class="detail-label">Пациент:</span>
                            <span class="detail-value">{{ appointment.patient_name }}</span>
                        </div>
                        <div class="detail-row">
                            <span class="detail-label">ИИН:</span>
                            <span class="detail-value">{{ appointment.patient_iin }}</span>
                        </div>
                        <div class="detail-row">
                            <span class="detail-label">Дата приема:</span>
                            <span class="detail-value">{{ appointment.date }}</span>
                        </div>
                        <div class="detail-row">
                            <span class="detail-label">Время:</span>
                            <span class="detail-value">{{ getTimeLabel(appointment.time) }}</span>
                        </div>
                        <template v-if="appointment.comment">
                            <div class="detail-row">
                                <span class="detail-label">Жалобы:</span>
                                <span class="detail-value">{{ appointment.comment }}</span>
                            </div>
                        </template>
                    </div>
                </div>

                <!-- Кнопка отмены -->
                <button class="cancel-btn" @click="openAppointmentModal">
                    <font-awesome-icon icon="fa-solid fa-calendar-xmark"/>
                    Отменить запись
                </button>
            </div>

            <!-- Правая колонка - медицинское заключение -->
            <div class="medical-info">
                <div class="medical-card">
                    <div class="card-header">
                        <font-awesome-icon icon="fa-solid fa-file-medical" class="card-icon"/>
                        <h2>Заключение врача</h2>
                    </div>
                    <div class="card-body">
                        <template v-if="appointment.conclusion">
                            <div class="medical-row">
                                <span class="medical-label">Диагноз:</span>
                                <span class="medical-value">{{ appointment.conclusion }}</span>
                            </div>
                            <div class="medical-row">
                                <span class="medical-label">Назначения:</span>
                                <span class="medical-value">{{ appointment.treatment }}</span>
                            </div>
                        </template>
                        <template v-else>
                            <div class="empty-state">
                                <font-awesome-icon icon="fa-solid fa-hourglass-half" class="empty-icon"/>
                                <p>Врач еще не добавил заключение</p>
                            </div>
                        </template>
                    </div>
                </div>
            </div>
        </div>

        <!-- Модальное окно подтверждения отмены -->
        <div v-if="isModalOpen" class="modal">
            <div class="modal-container">
                <div class="modal-header">
                    <h3>Подтверждение отмены записи</h3>
                    <button class="modal-close" @click="closeAppointmentModal">
                        <font-awesome-icon icon="fa-solid fa-xmark"/>
                    </button>
                </div>
                <div class="modal-body">
                    <p>Вы уверены, что хотите отменить запись на {{ appointment.date }} в
                        {{ getTimeLabel(appointment.time) }}?</p>
                </div>
                <div class="modal-footer">
                    <button class="modal-btn confirm" @click="deleteAppointment">
                        Да, отменить
                    </button>
                    <button class="modal-btn cancel" @click="closeAppointmentModal">
                        Нет, оставить
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios"

export default {
    name: "Appointment",
    data() {
        return {
            appointment: {},
            isModalOpen: false,
        }
    },
    mounted() {
        this.getAppointment()
    },
    methods: {
        async deleteAppointment() {
            this.$store.commit('setIsLoading', true)

            const appointmentID = this.$route.params.id

            await axios
                .post(`/api/v1/appointments/delete_appointment/${appointmentID}/`)
                .then(response => {
                    console.log(response.data)

                    this.$router.push('/appointments')
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },
        async getAppointment() {
            this.$store.commit('setIsLoading', true)

            const appointmentID = this.$route.params.id

            await axios
                .get(`/api/v1/appointments/${appointmentID}/`)
                .then(response => {
                    this.appointment = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },
        openAppointmentModal() {
            this.isModalOpen = true;
        },
        closeAppointmentModal() {
            this.isModalOpen = false;
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
    }
}
</script>


<style scoped>

.appointment-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
  font-family: 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
}

/* Шапка */
.appointment-header {
  text-align: center;
  margin-bottom: 3rem;
}

.appointment-title {
  font-size: 2.2rem;
  color: #2c3e50;
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
}

.header-icon {
  color: #4a6cf7;
  font-size: 1.8rem;
}

.header-divider {
  width: 100px;
  height: 4px;
  background: #1e90ff;
  margin: 1rem auto 0;
  border-radius: 2px;
}

/* Основное содержимое */
.appointment-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}

/* Карточки */
.detail-card,
.medical-card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  overflow: hidden;
  margin-bottom: 1.5rem;
}

.card-header {
  background: #1e90ff;
  color: white;
  padding: 1.2rem 1.5rem;
  display: flex;
  align-items: center;
  gap: 0.8rem;
}

.card-header h2 {
  font-size: 1.3rem;
  font-weight: 500;
  margin: 0;
}

.card-icon {
  font-size: 1.2rem;
}

.card-body {
  padding: 1.5rem;
}

/* Строки с информацией */
.detail-row,
.medical-row {
  display: flex;
  margin-bottom: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #f0f0f0;
}

.detail-row:last-child,
.medical-row:last-child {
  border-bottom: none;
  margin-bottom: 0;
  padding-bottom: 0;
}

.detail-label {
  font-weight: 600;
  color: #555;
  min-width: 130px;
  font-size: 0.95rem;
}

.detail-value {
  color: #333;
  flex: 1;
}

.medical-label {
  font-weight: 600;
  color: #4a6cf7;
  min-width: 100px;
}

.medical-value {
  flex: 1;
  background: #f8f9fe;
  padding: 0.8rem;
  border-radius: 6px;
  border-left: 3px solid #4a6cf7;
}

/* Состояние пустого заключения */
.empty-state {
  text-align: center;
  padding: 2rem;
  color: #888;
}

.empty-icon {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #d0d0d0;
}

/* Кнопка отмены */
.cancel-btn {
  background: #ff4757;
  color: white;
  border: none;
  padding: 0.8rem 1.5rem;
  border-radius: 8px;
  font-weight: 500;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  transition: all 0.3s ease;
  width: 100%;
  justify-content: center;
}

.cancel-btn:hover {
  background: #e8413d;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 71, 87, 0.3);
}

/* Модальное окно */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-container {
  background: white;
  border-radius: 12px;
  width: 100%;
  max-width: 500px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.modal-header {
  padding: 1.5rem;
  background: #f8f9fe;
  border-bottom: 1px solid #eee;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.modal-header h3 {
  margin: 0;
  color: #2c3e50;
}

.modal-close {
  background: none;
  border: none;
  font-size: 1.2rem;
  cursor: pointer;
  color: #888;
}

.modal-body {
  padding: 2rem 1.5rem;
  text-align: center;
}

.modal-footer {
  padding: 1rem 1.5rem;
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
  border-top: 1px solid #eee;
}

.modal-btn {
  padding: 0.7rem 1.5rem;
  border-radius: 8px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
}

.modal-btn.confirm {
  background: #ff4757;
  color: white;
  border: none;
}

.modal-btn.cancel {
  background: white;
  color: #4a6cf7;
  border: 1px solid #4a6cf7;
}

.modal-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

</style>
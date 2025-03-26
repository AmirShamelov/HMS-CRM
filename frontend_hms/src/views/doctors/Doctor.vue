<template>
    <div class="doctor-profile">
        <div class="profile-header">
            <div class="profile-image">
                <img :src="doctor.get_image" :alt="doctor.full_name" class="doctor-photo">
            </div>
            <div class="profile-info">
                <h1 class="doctor-name">{{ doctor.full_name }}</h1>
                <h2 class="doctor-position">{{ doctor.position }}</h2>
                <p class="doctor-department">
                    {{ doctor.department.title }}
                </p>
            </div>
        </div>

        <div class="profile-details">
            <div class="detail-section">
                <h3>
                    <font-awesome-icon icon="fa-solid fa-graduation-cap"/>
                    Образование
                </h3>
                <p>{{ doctor.education }}</p>
            </div>

            <div class="detail-section">
                <h3>
                    <font-awesome-icon icon="fa-solid fa-file-lines"/>
                    Описание
                </h3>
                <p v-if="doctor.description">{{ doctor.description }}</p>
                <p v-else>Врач еще не добавил описание...</p>
            </div>

            <div class="contact-section">
                <h3>
                    <font-awesome-icon icon="fa-solid fa-address-card"/>
                    Контакты
                </h3>
                <div class="contact-info">
                    <p>
                        <font-awesome-icon icon="fa-solid fa-envelope"/>
                        <a :href="'mailto:' + doctor.email">{{ doctor.email }}</a>
                    </p>
                    <p>
                        <font-awesome-icon icon="fa-solid fa-phone"/>
                        <a :href="'tel:' + doctor.phone">{{ doctor.phone }}</a>
                    </p>
                </div>
            </div>


            <div class="reviews-section">
                <h3>
                    <font-awesome-icon icon="fa-solid fa-comment-dots"/>
                    Отзывы
                </h3>

                <!-- Форма добавления отзыва -->
                <div class="add-review">
                    <button @click="openReviewModal" class="submit-review-btn">Оставить отзыв</button>
                </div>


                <div>
                    <div v-if="reviews.length === 0" class="no-reviews">
                        Пока нет отзывов. Будьте первым!
                    </div>

                    <div v-for="review in reviews" :key="review.id" class="review-item">
                        <div class="review-header">
                            <span class="review-author">{{ review.first_name }}</span>
                            <span class="review-date">{{ formDate(review.created_at) }}</span>
                        </div>
                        <div class="review-text">{{ review.review }}</div>
                    </div>
                </div>

            </div>
        </div>

        <div v-if="isModalOpen" class="modal-overlay">
            <div class="modal-content">
                <h3>Отзыв на врача {{ doctor.full_name }} </h3>
                <form @submit.prevent="submitReviewForm">
                    <div class="field">
                        <label>Ваше имя</label>
                        <input type="text" v-model="reviewForm.first_name" required/>
                    </div>
                    <div class="field">
                        <label>Ваша фамилия</label>
                        <input type="text" v-model="reviewForm.last_name" required/>
                    </div>
                    <div class="field">
                        <label>Номер телефона</label>
                        <input type="text" v-model="reviewForm.phone_number" required/>
                    </div>
                    <div class="field">
                        <label>Дата приема</label>
                        <input type="date" v-model="reviewForm.date" required/>
                    </div>
                    <div class="field">
                        <label>Отзыв</label>
                        <textarea v-model="reviewForm.review" required></textarea>
                    </div>
                    <div class="modal-buttons">
                        <button type="submit" class="button is-success">Отправить</button>
                        <button type="button" @click="closeReviewModal" class="cancel-button">
                            Отмена
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "Doctor",
    data() {
        return {
            doctor: {
                department: []
            },
            reviews: {},
            isModalOpen: false,
            reviewForm: {
                first_name: '',
                last_name: '',
                phone_number: '',
                date: '',
                review: '',
            },
        }
    },
    mounted() {
        this.getDoctor()
        this.getReviews()
    },
    methods: {
        async getDoctor() {
            this.$store.commit('setIsLoading', true)

            const DoctorID = this.$route.params.id

            await axios
                .get(`/api/v1/doctors/${DoctorID}/`)
                .then(response => {
                    this.doctor = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },

        async getReviews() {
            this.$store.commit('setIsLoading', true)

            const DoctorID = this.$route.params.id

            await axios
                .get(`/api/v1/reviews/?doctor_id=${DoctorID}`)
                .then(response => {
                    console.log(response)

                    this.reviews = response.data
                })
                .catch(error => {
                    console.log(error)
                })


            this.$store.commit('setIsLoading', false)
        },

        openReviewModal() {
            this.isModalOpen = true;
        },
        closeReviewModal() {
            this.isModalOpen = false;
            this.resetReviewForm();
        },
        resetReviewForm() {
            this.reviewForm = {
                first_name: '',
                last_name: '',
                phone_number: '',
                date: '',
                review: '',
            }
        },

        async submitReviewForm() {
            this.$store.commit('setIsLoading', true)

            const DoctorID = this.$route.params.id

            const review = {
                doctor_id: DoctorID,
                ...this.reviewForm
            }

            await axios
                .post('/api/v1/reviews/', review)
                .then(response => {
                    console.log(response)

                    location.reload()
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },
        formDate(dateString) {
            const options = { year: 'numeric', month: 'long', day: 'numeric' };
            return new Date(dateString).toLocaleDateString('ru-RU', options);
        },
    }
}
</script>


<style scoped>
/* Стили для профиля */
.doctor-profile {
    max-width: 1200px;
    margin: 0 auto;
    padding: 30px;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}

.profile-header {
    display: flex;
    align-items: center;
    margin-bottom: 30px;
    padding-bottom: 20px;
    border-bottom: 1px solid #eee;
}

.profile-image {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    overflow: hidden;
    margin-right: 40px;
    border: 5px solid #f0f8ff;
}

.doctor-photo {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.profile-info {
    flex: 1;
}

.doctor-name {
    font-size: 2rem;
    color: #2c3e50;
    margin-bottom: 5px;
}

.doctor-position {
    font-size: 1.3rem;
    color: #1e90ff;
    margin-bottom: 10px;
    font-weight: normal;
}

.doctor-department {
    font-size: 1.1rem;
    color: #7f8c8d;
}

.detail-section, .contact-section {
    margin-bottom: 25px;
}

.detail-section h3, .contact-section h3 {
    color: #2c3e50;
    margin-bottom: 15px;
    font-size: 1.3rem;
    display: flex;
    align-items: center;
}

.detail-section h3 svg, .contact-section h3 svg {
    margin-right: 10px;
    color: #1e90ff;
}

.contact-info p {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
}

.contact-info svg {
    margin-right: 10px;
    color: #7f8c8d;
    width: 20px;
}

.contact-info a {
    color: #3498db;
    text-decoration: none;
}

.contact-info a:hover {
    text-decoration: underline;
}

/* Стили для отзывов */

.reviews-section {
    margin-top: 40px;
    padding-top: 30px;
    border-top: 1px solid #eee;
}

.reviews-section h3 {
    color: #2c3e50;
    font-size: 1.5rem;
    margin-bottom: 25px;
    display: flex;
    align-items: center;
}

.reviews-section h3 svg {
    margin-right: 12px;
    color: #1e90ff;
    width: 20px;
}

/* Форма добавления отзыва */
.add-review {
    background-color: #f9fafb;
    padding: 25px;
    border-radius: 8px;
    margin-bottom: 30px;
    border: 1px solid #eaecef;
}


.rating-select label {
    margin-right: 15px;
    color: #2c3e50;
    font-weight: 500;
}

.rating-select select {
    padding: 8px 12px;
    border-radius: 6px;
    border: 1px solid #ddd;
    background-color: white;
    font-size: 1rem;
}

.submit-review-btn {
    background-color: #1e90ff;
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 6px;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.3s;
}

.submit-review-btn:hover {
    background-color: #187bcd;
    transform: translateY(-1px);
}

/* Стили для списка отзывов */
.review-item {
    background-color: white;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    border: 1px solid #eee;
    transition: transform 0.3s, box-shadow 0.3s;
}

.review-item:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.review-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 12px;
}

.review-author {
    font-weight: 600;
    color: #2c3e50;
    font-size: 1.1rem;
}


.review-date {
    color: #7f8c8d;
    font-size: 0.9rem;
    font-style: italic;
}

.review-text {
    color: #34495e;
    line-height: 1.6;
    margin-top: 10px;
}

/* Состояния */
.no-reviews {
    text-align: center;
    padding: 40px;
    color: #7f8c8d;
    font-size: 1.1rem;
    background-color: #f9fafb;
    border-radius: 8px;
}

/* Стили для модального окна */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  backdrop-filter: blur(3px);
}

.modal-content {
  background-color: white;
  border-radius: 12px;
  width: 100%;
  max-width: 500px;
  padding: 30px;
  box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
  animation: modalFadeIn 0.3s ease-out;
}

.modal-content h3 {
  color: #2c3e50;
  font-size: 1.5rem;
  margin-bottom: 25px;
  text-align: center;
  padding-bottom: 15px;
  border-bottom: 1px solid #eee;
}

/* Стили для формы */
.form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.field {
  display: flex;
  flex-direction: column;
}

.field label {
  color: #2c3e50;
  margin-bottom: 8px;
  font-weight: 500;
  font-size: 0.95rem;
}

.field input,
.field textarea {
  padding: 12px 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 1rem;
  transition: all 0.3s;
}

.field input:focus,
.field textarea:focus {
  outline: none;
  border-color: #1e90ff;
  box-shadow: 0 0 0 3px rgba(30, 144, 255, 0.1);
}

.field textarea {
  min-height: 120px;
  resize: vertical;
}

/* Стили для кнопок */
.modal-buttons {
  display: flex;
  justify-content: flex-end;
  gap: 15px;
  margin-top: 20px;
}

.button.is-success {
  background-color: #1e90ff;
  color: white;
  border: none;
  padding: 12px 25px;
  border-radius: 8px;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s;
}

.button.is-success:hover {
  background-color: #187bcd;
  transform: translateY(-1px);
}

.cancel-button {
  background-color: #f5f5f5;
  color: #2c3e50;
  border: none;
  padding: 12px 25px;
  border-radius: 8px;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s;
}

.cancel-button:hover {
  background-color: #e0e0e0;
}

</style>
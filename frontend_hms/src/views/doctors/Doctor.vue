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
                    <font-awesome-icon :icon="doctor.department.link" class="department-icon"/>
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
                <p>{{ doctor.description }}</p>
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
            }
        }
    },
    mounted() {
        this.getDoctor()
    },
    methods: {
        async getDoctor() {
            this.$store.commit('setIsLoading', true)

            const DoctorID = this.$route.params.id

            await axios
                .get(`/api/v1/doctors/${DoctorID}/`)
                .then(response => {
                    console.log(response)

                    this.doctor = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>


<style scoped>

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


</style>
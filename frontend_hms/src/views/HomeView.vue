<template>
  <div class="home">
    <!-- Заголовок и приветствие -->
    <div class="hero-section">
      <h1 class="hero-title">Добро пожаловать в наш медицинский центр</h1>
      <p class="hero-subtitle">Ваше здоровье — наш приоритет. Мы предоставляем лучшую медицинскую помощь.</p>
    </div>

    <div class="cta-buttons">
      <router-link to="/appointments" class="cta-button">
        <font-awesome-icon icon="fa-solid fa-calendar-check" />
        <span>Записи</span>
      </router-link>
      <router-link to="/doctors" class="cta-button">
        <font-awesome-icon icon="fa-solid fa-user-doctor" />
        <span>Врачи</span>
      </router-link>
    </div>

    <div class="info-section">
      <p>Свяжитесь с нами для получения дополнительной информации или записи на прием.</p>
    </div>
  </div>
</template>

<script>
export default {
name: "HomeView"
}
</script>


<style scoped>

.home {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #6a11cb, #2575fc);
  color: white;
  text-align: center;
  padding: 20px;
}

.hero-section {
  margin-bottom: 40px;
}

.hero-title {
  font-size: 3rem;
  font-weight: bold;
  margin-bottom: 20px;
}

.hero-subtitle {
  font-size: 1.5rem;
  opacity: 0.9;
}

.cta-buttons {
  display: flex;
  gap: 20px;
  margin-bottom: 40px;
}

.cta-button {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 15px 30px;
  background-color: rgba(255, 255, 255, 0.1);
  border: 2px solid white;
  border-radius: 50px;
  color: white;
  text-decoration: none;
  font-size: 1.2rem;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.cta-button:hover {
  background-color: rgba(255, 255, 255, 0.2);
  transform: translateY(-5px);
}

.info-section {
  max-width: 600px;
  font-size: 1.1rem;
  opacity: 0.8;
}

</style>
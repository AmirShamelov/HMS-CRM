<template>
    <div>
        <Navbar />

        <section class="section">
            <Router-view />
        </section>
    </div>

</template>

<script>
import axios from "axios"

import Navbar from "@/components/layout/Navbar.vue"

export default {
    name: 'App',
    components: {
        Navbar
    },
    beforeCreate() {
        this.$store.commit('initializeHospital')

        if (this.$store.state.token) {
            axios.defaults.headers.common['Authorization'] = "Token " + this.$store.state.token
        } else {
            axios.defaults.headers.common['Authorization'] = ""
        }
    }
}

</script>


<style lang="css">
@import "../node_modules/bulma";

</style>

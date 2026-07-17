<template>

  <Header />

  <h2>Course Details</h2>

  <p>Course ID: {{ route.params.id }}</p>

  <button @click="enrollCourse">
    Enroll
  </button>

</template>

<script setup>

import { useRoute, useRouter } from 'vue-router'
import Header from '../components/Header.vue'

const route = useRoute()
const router = useRouter()

function enrollCourse() {

  alert("Course Enrolled!")

  router.push('/profile')

}

</script>

<style scoped>

</style>
<template>

  <Header />

  <h2>Student Profile</h2>

  <h3>Enrolled Courses</h3>

  <div v-if="store.enrolledCourses.length === 0">
    No courses enrolled.
  </div>

  <ul v-else>

    <li
      v-for="course in store.enrolledCourses"
      :key="course.id"
    >

      {{ course.name }} ({{ course.credits }} Credits)

      <button @click="store.unenroll(course.id)">
        Remove
      </button>

    </li>

  </ul>

  <h3>Total Credits : {{ store.totalCredits }}</h3>

</template>

<script setup>

import Header from '../components/Header.vue'
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()

</script>

<style scoped>

ul{
  padding-left:20px;
}

li{
  margin-bottom:10px;
}

button{
  margin-left:10px;
}

</style>
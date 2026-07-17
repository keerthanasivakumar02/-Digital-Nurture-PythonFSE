<template>

  <Header />

  <h2>Courses</h2>

  <input
    type="text"
    placeholder="Search courses..."
    v-model="searchTerm"
  />

  <br><br>

  <CourseCard
    v-for="course in filteredCourses"
    :key="course.id"
    :name="course.name"
    :code="course.code"
    :credits="course.credits"
    :grade="course.grade"
    @enroll="store.enroll(course)"
  />

</template>

<script setup>

import { ref, computed, onMounted } from 'vue'

import Header from '../components/Header.vue'
import CourseCard from '../components/CourseCard.vue'
import { useEnrollmentStore } from '../stores/enrollment'

const searchTerm = ref("")

const store = useEnrollmentStore()

const courses = ref([])

onMounted(() => {

  courses.value = [

    {
      id: 1,
      name: "Data Structures",
      code: "CS101",
      credits: 4,
      grade: "A"
    },

    {
      id: 2,
      name: "Database Systems",
      code: "CS102",
      credits: 3,
      grade: "A+"
    },

    {
      id: 3,
      name: "Operating Systems",
      code: "CS103",
      credits: 4,
      grade: "B+"
    },

    {
      id: 4,
      name: "Computer Networks",
      code: "CS104",
      credits: 3,
      grade: "A"
    },

    {
      id: 5,
      name: "Web Development",
      code: "CS105",
      credits: 4,
      grade: "A+"
    }

  ]

})

const filteredCourses = computed(() => {

  return courses.value.filter(course =>

    course.name
      .toLowerCase()
      .includes(searchTerm.value.toLowerCase())

  )

})

</script>

<style scoped>

</style>
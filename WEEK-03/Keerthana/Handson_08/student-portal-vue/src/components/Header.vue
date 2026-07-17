<template>

  <header>

    <h1>Student Portal</h1>

    <nav>

      <RouterLink to="/">Home</RouterLink> |

      <RouterLink to="/courses">Courses</RouterLink> |

      <RouterLink to="/profile">Profile</RouterLink>

    </nav>

    <p>
      Enrolled Courses: {{ store.enrolledCourses.length }}
    </p>

    <hr>

  </header>

</template>

<script setup>

import { RouterLink } from 'vue-router'
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()

</script>

<style scoped>

header{
  margin-bottom:20px;
}

nav{
  margin-bottom:10px;
}

</style>
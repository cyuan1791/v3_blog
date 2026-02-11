<script setup lang="ts">
defineProps<{
  id: number;
  title: string;
  date: string;
  author: string;
  image: string;
  summary: string;
}>();
</script>

<template>
  <div class="col-lg-4 col-md-6 col-12 mb-4">
    <div class="card h-100 blog-card">
      <img :src="image" class="card-img-top" :alt="title">
      <div class="card-body d-flex flex-column">
        <h5 class="card-title">{{ title }}</h5>
        <p class="text-muted small mb-2">
          By {{ author }} on {{ new Date(date).toLocaleDateString() }}
        </p>
        <p class="card-text card-summary">{{ summary }}</p>
        <router-link
          :to="'/post/' + title.replace(/\s+/g, '-').replace(/[^a-zA-Z0-9-_]/g, '')"
          class="btn btn-outline-primary btn-sm mt-auto"
        >
          Read More
        </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped>
.blog-card {
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.blog-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}

.blog-card .card-img-top {
  height: 200px;
  object-fit: cover;
}

.blog-card .card-title {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-summary {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>

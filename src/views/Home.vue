<script setup lang="ts">
import { ref, computed } from 'vue';
import BlogPost from '../components/BlogPost.vue';

let myWindow = window as any;
let postData = JSON.parse(atob(myWindow.asoneData));
let posts: any = { posts: postData }

const searchQuery = ref('');

const filteredPosts = computed(() => {
  const query = searchQuery.value.toLowerCase().trim();
  if (!query) return posts.posts;
  return posts.posts.filter((post: any) =>
    post.title?.toLowerCase().includes(query) ||
    post.author?.toLowerCase().includes(query) ||
    post.summary?.toLowerCase().includes(query)
  );
});
</script>

<template>
  <div class="container mt-4">
    <div class="mb-3">
      <input
        v-model="searchQuery"
        type="text"
        class="form-control"
        placeholder="Search posts..."
      />
    </div>
    <div class="row">
        <BlogPost
          v-for="post in filteredPosts"
          :key="post.id"
          v-bind="post"
        />
    </div>
    <div v-if="filteredPosts.length === 0" class="text-center text-muted mt-4">
      No posts found.
    </div>
  </div>
</template>

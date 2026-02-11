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
  <div>
    <div class="hero-section text-center text-white py-5 mb-4">
      <div class="container">
        <h1 class="hero-title mb-2">The Blog</h1>
        <p class="hero-subtitle mb-4">Stories, insights, and ideas</p>
        <div class="row justify-content-center">
          <div class="col-lg-6 col-md-8">
            <div class="input-group search-bar">
              <div class="input-group-prepend">
                <span class="input-group-text bg-white border-right-0">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#999" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="11" cy="11" r="8"/>
                    <line x1="21" y1="21" x2="16.65" y2="16.65"/>
                  </svg>
                </span>
              </div>
              <input
                v-model="searchQuery"
                type="text"
                class="form-control border-left-0"
                placeholder="Search posts..."
              />
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="row">
        <BlogPost
          v-for="post in filteredPosts"
          :key="post.id"
          v-bind="post"
        />
      </div>
      <div v-if="filteredPosts.length === 0" class="text-center mt-5 mb-5">
        <p class="h5 text-muted">No posts found</p>
        <p class="text-muted">Try a different search term or clear the search bar</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.hero-section {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.hero-title {
  font-size: 2.5rem;
  font-weight: 700;
  letter-spacing: -0.5px;
}

.hero-subtitle {
  font-size: 1.15rem;
  opacity: 0.9;
}

.search-bar .input-group-text {
  border-radius: 50px 0 0 50px;
  border-color: #ced4da;
  display: flex;
  align-items: center;
  height: 100%;
}

.search-bar .form-control {
  border-radius: 0 50px 50px 0;
  border-color: #ced4da;
}

.search-bar .form-control:focus {
  box-shadow: none;
  border-color: #ced4da;
}
</style>

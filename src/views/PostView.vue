<script setup lang="ts">
import { computed } from "vue";
import { useRoute } from "vue-router";

let myWindow = window as any;

let postData = JSON.parse(atob(myWindow.asoneData));
let posts = { posts: postData };

const route = useRoute();
const post = computed(() => {
  for (var d in posts.posts) {
    //console.log(this.posts[d])
    if (
      posts.posts[d]["title"]
        .replace(/\s+/g, "-")
        .replace(/[^a-zA-Z0-9-_]/g, "") == route.params.id
    ) {
      return posts.posts[d];
    }
  }

  // @ts-ignore
  //return posts.posts.find(p => p.id === Number(route.params.id));
});
</script>

<template>
  <div class="container mt-4" v-if="post">
    <div class="row">
      <div class="col-12">
        <div class="d-flex p-4">
          <div class="m-auto">
            <router-link to="/" class="btn btn-secondary"
              >Back to Posts</router-link
            >
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <img :src="post.image" class="img-fluid mb-4" :alt="post.title" />
      </div>
      <div class="col-md-8">
        <h1>Ttile {{ post.title }}</h1>
        <p class="text-muted">
          By {{ post.author }} on {{ new Date(post.date).toLocaleDateString() }}
        </p>
        <div class="content mt-4" v-html="post.content">
        </div>
      </div>
      <div class="col-12">
        <div class="d-flex w-100 h-100">
          <div class="m-auto">
            <router-link to="/" class="btn btn-secondary mt-4"
              >Back to Posts</router-link
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

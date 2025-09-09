<template>
  <!-- use vue3 and bootstrap 4 to create a blogpost. The post data is read from a json file. The main page display the title, data, author, image, summary and a read more link to read the content
  -->

  <router-view v-slot="slotProps">
    <transition name="fade" mode="out-in">
      <component  :is="slotProps.Component"></component>
    </transition>
  </router-view>
</template>
<style lang="css">

.fade-enter-from,
.fade-button-leave-to {
  opacity: 0;
}   
      
.fade-enter-active {
  transition: opacity 0.3s ease-out;
}   
      
.fade-leave-active {
  transition: opacity 0.3s ease-in;
}   
    
.fade-enter-to,
.fade-leave-from {
  opacity: 1;
}     
</style>

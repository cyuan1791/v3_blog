import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

let myWindow = window as any;

const app = createApp(App);
app.use(router);
app.mount('#'+myWindow.asoneId)

/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Components
import App from "./App.vue";

// Composables
import { createApp } from "vue";

// Plugins
import { registerPlugins } from "@/plugins";

// Pinia

import { createPinia } from "pinia";

const pinia = createPinia();

const app = createApp(App);

registerPlugins(app);

app.use(pinia);
app.mount("#app");

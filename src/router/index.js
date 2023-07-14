// Composables
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    component: () => import("@/layouts/default/HomeView.vue"),
    children: [
      {
        path: "",
        name: "Home",
        component: () =>
          import(/* webpackChunkName: "home" */ "@/views/Home.vue"),
      },
      {
        path: "/endereco",
        name: "Endereco",
        component: () =>
          import(/* webpackChunkName: "home" */ "@/views/Endereco.vue"),
      },
      {
        path: "/dadoscomprador",
        name: "DadosComprador",
        component: () =>
          import(/* webpackChunkName: "home" */ "@/views/DadosComprador.vue"),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

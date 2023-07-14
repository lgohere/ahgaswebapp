<template>
  <carrinho-view style="z-index: 3" />
  <v-app style="z-index: 1">
    <default-bar style="z-index: 2" />
    <default-view style="z-index: 1" />
  </v-app>
</template>

<script setup>
import DefaultBar from "./AppBar.vue";
import DefaultView from "./View.vue";
import CarrinhoView from "@/components/CarrinhoView.vue";
</script>

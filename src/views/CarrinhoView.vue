<template>
  <div class="d-flex justify-end">
    <v-container
      :style="{ display: mostrar ? 'flex' : 'none' }"
      class="fill-height d-flex justify-start align-start mx-0"
      style="
        max-width: 80%;
        position: fixed;
        z-index: 2;
        padding-top: 25%;
        border-radius: 20px 0px 0px 20px;
        border: 1px solid rgba(0, 0, 0, 0.185);
        background-color: rgba(233, 233, 233, 0.98);
      "
    >
      <v-btn @click="mostrar = false">Ocultar Carrinho</v-btn>
      <v-container class="d-flex mx-0 pa-0">
        <v-row class="d-flex flex-column">
          <v-col class="border d-flex align-center mb-3 justify-center">
            Aqui ficará o item.
          </v-col>
        </v-row>
      </v-container>
    </v-container>
  </div>
</template>

<script setup>
import { ref } from "vue";

const mostrar = ref(true); // Inicialmente o carrinho está visível
</script>

<style></style>

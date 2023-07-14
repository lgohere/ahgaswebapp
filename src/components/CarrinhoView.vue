<template>
  <div class="d-flex justify-end">
    <div id="carrinho" class="slide-cart" ref="carrinhoRef" v-show="carrinho">
      <v-container>
        <v-row>
          <v-col cols="12" class="my-0 py-0 d-flex justify-end align-start px-0"
            ><v-btn elevation="0" style="background: none"
              ><v-icon @click="fecharCarrinho" color="white" size="x-large"
                >mdi-close-circle</v-icon
              ></v-btn
            ></v-col
          >
        </v-row>
      </v-container>
      <v-container class="bg-blue border my-0">
        <v-row>
          <v-col cols="12" class="d-flex flex-row justify-center">
            <v-col cols="1">
              <h4 class="text-center font-weight-regular">1</h4>
            </v-col>
            <v-col cols="8" class="text-start">
              <h4 class="font-weight-regular">Gás de Cozinha 13kg</h4>
              <h5 class="font-weight-regular">Recarga</h5>
            </v-col>
            <v-col
              cols="3"
              class="d-flex justify-start align-center flex-column"
            >
              <h4 class="font-weight-regular">R$110,00</h4>
            </v-col>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<style>
#carrinho {
  width: 85%;
  height: 100%;
  background-color: rgba(133, 133, 133, 0.99);
  position: fixed;
  z-index: 3;
  color: rgb(0, 0, 0);
  padding-top: 5%;
}

.slide-cart {
  -webkit-animation: slide-cart 0.5s cubic-bezier(0, 0, 0.58, 1) both;
  animation: slide-cart 0.5s cubic-bezier(0, 0, 0.58, 1) both;
}

@-webkit-keyframes slide-cart {
  0% {
    -webkit-transform: translateX(1000px);
    transform: translateX(1000px);
    opacity: 0;
  }
  100% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes slide-cart {
  0% {
    -webkit-transform: translateX(1000px);
    transform: translateX(1000px);
    opacity: 0;
  }
  100% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
    opacity: 1;
  }
}
</style>

<script setup>
import { ref, onMounted, onUnmounted, computed } from "vue";
import { useProductStore } from "@/store/ProductStore";

let productStore = useProductStore();
let carrinho = computed(() => productStore.carrinho); // reage ao estado do carrinho na store

let fecharCarrinho = () => {
  productStore.toggleCarrinho();
};

let fecharCarrinhoForaDoDiv = (event) => {
  if (!this.$refs.carrinhoRef.contains(event.target)) {
    productStore.toggleCarrinho();
  }
};

onMounted(() => {
  document.addEventListener("click", fecharCarrinhoForaDoDiv);
});

onUnmounted(() => {
  document.removeEventListener("click", fecharCarrinhoForaDoDiv);
});
</script>

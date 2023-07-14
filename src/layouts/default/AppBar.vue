<template>
  <v-app-bar
    id="app-bar"
    :elevation="3"
    rounded
    :style="{ backgroundColor: `rgba(255, 255, 255, ${opacity})` }"
  >
    <template v-slot>
      <v-container fluid>
        <row class="d-flex justify-center">
          <v-col cols="2" class="d-flex justify-center px-0">
            <v-btn
              v-if="$route.path != '/'"
              id="voltar"
              size="x-large"
              @click="voltarRota"
            >
              <v-icon>mdi-arrow-left</v-icon>
            </v-btn>
          </v-col>
          <v-col class="d-flex justify-center" cols="8">
            <div class="d-flex">
              <v-img src="@/assets/logo.png" alt="logo" width="120"></v-img>
            </div>
          </v-col>
          <v-col cols="2" class="px-0 d-flex justify-center">
            <v-btn size="x-large" @click="toggleCarrinho">
              <v-badge content="0" color="primary">
                <v-icon>mdi-cart-outline</v-icon>
              </v-badge>
            </v-btn>
          </v-col>
        </row>
      </v-container>
    </template>
  </v-app-bar>
</template>

<style scoped>
#app-bar {
  position: relative;
}

#app-bar::before {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-color: rgba(255, 255, 255, 0.9);
  z-index: -1;
  transition: opacity 0.1s ease;
}

#app-bar .v-app-bar__content {
  position: relative;
  z-index: 1;
}

#app-bar.scrolled::before {
  filter: blur(5px);
}
</style>

<script setup>
import { ref, onMounted, onUnmounted } from "vue";
import { useProductStore } from "@/store/ProductStore";

const productStore = useProductStore();

const toggleCarrinho = () => {
  productStore.toggleCarrinho();
};

let opacity = ref(1); // Inicialmente o v-app-bar é totalmente opaco

const handleScroll = () => {
  let scrolled = window.scrollY / 300;
  opacity.value = scrolled > 1 ? 0.5 : 1 - scrolled;

  let appBarElement = document.getElementById("app-bar");
  if (scrolled > 1) {
    appBarElement.classList.add("scrolled");
  } else {
    appBarElement.classList.remove("scrolled");
  }
};

onMounted(() => {
  window.addEventListener("scroll", handleScroll);
});

onUnmounted(() => {
  window.removeEventListener("scroll", handleScroll);
});

const voltarRota = () => {
  window.history.go(-1);
};
</script>

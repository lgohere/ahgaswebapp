<template>
  <!-- <CarrinhoView /> -->

  <v-container fluid class="h-100 py-0 px-0" style="max-width: 800px">
    <v-container class="d-flex flex-column align-start" fluid>
      <h3 class="font-weight-bold">Escolha seu produto:</h3>
      <h5 class="font-weight-regular pb-4">
        Clique em <span class="font-weight-bold">"+"</span> para adiciona-lo ao
        carrinho.
      </h5>

      <v-container fluid class="bg-white pa-0">
        <v-row class="bg-white fill-height">
          <v-col
            v-for="(product, index) in products"
            :key="index"
            cols="12"
            class="mx-0 px-0 mb-0 pb-0"
          >
            <v-sheet elevation="3" class="d-flex align-center flex-row">
              <v-col
                class="max-width-100 d-flex align-center justify-center"
                cols="2"
              >
                <v-col class="d-flex max-width-100">
                  <v-img
                    max-width="80"
                    :src="product.image"
                    :alt="product.title"
                    width="40"
                  ></v-img>
                </v-col>
              </v-col>
              <v-col class="py-0 d-flex align-center" cols="6">
                <v-col elevation="1">
                  <h3 class="font-weight-bold">
                    {{ product.title }}
                  </h3>
                  <h5 class="font-weight-regular">
                    {{ product.desc }}
                  </h5>

                  <v-chip-group column multiple>
                    <v-chip
                      v-if="product.title !== 'Assistência Técnica'"
                      filter
                      variant="outlined"
                      class="px-2"
                      color="primary"
                      v-model="product.vasilhame"
                    >
                      Vasilhame
                    </v-chip>
                  </v-chip-group>
                </v-col>
              </v-col>
              <v-col
                class="d-flex flex-column align-center justify-center"
                cols="4"
              >
                <CapturaLocalizacao />

                <v-btn
                  size="small"
                  class="d-flex justify-center align-center justify-center"
                  icon="mdi-plus"
                  color="primary"
                  @click="snackbar = true"
                ></v-btn>

                <h4 class="pt-3 font-weight-bold text-primary">
                  R$ {{ product.price }}
                </h4>
              </v-col>
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-container>
  </v-container>
  <router-link style="text-decoration: none" to="/endereco">
    <ProsseguirBotao />
  </router-link>
</template>

<script setup>
import ProsseguirBotao from "@/components/ProsseguirBotao.vue";

const products = [
  {
    id: "p13",
    image: "/p13.png",
    title: "P-13",
    desc: "Gás GLP 13kg",
    price: "110,00",
    vasilhame: false,
  },
  {
    id: "p20",
    image: "/p20.png",
    title: "P-20",
    desc: "Gás GLP 20kg",
    price: "250,00",
    vasilhame: false,
  },
  {
    id: "p45",
    image: "/p45.png",
    title: "P-45",
    desc: "Gás GLP 45kg",
    price: "450,00",
    vasilhame: false,
  },
  {
    id: "assistencia",
    image: "/assistencia.png",
    title: "Assistência Técnica",
    price: "50,00",
  },
];
</script>
<script>
import { onMounted } from "vue";
import { useProductStore } from "@/store/ProductStore";

export default {
  setup() {
    const productStore = useProductStore();

    onMounted(async () => {
      await productStore.fill();
    });

    return {
      products: productStore.products,
    };
  },
};
</script>

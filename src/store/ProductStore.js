import { defineStore } from "pinia";

// aqui vai o .json com a array de produtos e todas as outras requisições necessárias.

import axios from "axios";

export const useProductStore = defineStore("ProductStore", {
  //state- the central part of the whole store.
  //the reason the store exists to begin with.

  state: () => {
    return {
      products: [],
    };
  },

  //actions
  actions: {
    fill() {
      axios
        .get("http://localhost:8000/get_products")
        .then((response) => {
          this.products = response.data;
        })
        .catch((error) => {
          console.error("Erro ao buscar produtos:", error);
        });
    },
  },

  //getters
});

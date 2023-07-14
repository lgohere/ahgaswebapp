import { defineStore } from "pinia";

// aqui vai o .json com a array de produtos e todas as outras requisições necessárias.

export const useProductStore = defineStore("ProductStore", {
  state: () => ({
    carrinho: false,
    products: ["aqui deve estar todos os produtos da api."],
  }),
  actions: {
    async fill() {
      const response = await fetch(
        "https://livefrontapp-api.gasdelivery.com.br/product",
        {
          method: "GET",
          headers: {
            "gd-group-hash": "99b97d48ff2976e48105748d0e02f148",
            "Content-Type": "application/json",
            // Include other headers as needed
          },
          // You can include other parameters as needed
        }
      );

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const data = await response.json();

      this.products = data.products;
    },
    toggleCarrinho() {
      // Isso irá inverter o valor de carrinho.
      // Se carrinho for true, ficará false, e vice-versa.
      this.carrinho = !this.carrinho;
    },
  },
});

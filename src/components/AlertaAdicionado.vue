<template>
  <v-snackbar
    id="snackbar"
    v-model="snackbar"
    :timeout="1500"
    type="success"
    color="success"
    width="100%"
    top
    >{{ adicionado }}
  </v-snackbar>
</template>

<script>
export default {
  data: () => ({
    snackbar: false,
    adicionado: `Item adicionado ao carrinho TESTANDOO!!`,
  }),
};
</script>

<style></style>

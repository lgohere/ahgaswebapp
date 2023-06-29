<template>
  <v-container class="sticky-button">
    <v-row class="d-flex justify-center fill-height">
      <v-col
        cols="12"
        class="d-flex align-center fill-height ma-0 pa-0 justify-center"
        lg="8"
      >
        <v-btn
          class="fill-height pa-4 ma-0 d-flex w-100"
          color="primary"
          size="x-large"
        >
          <v-text
            v-text="
              $route.path !== '/dadoscomprador'
                ? 'Prosseguir'
                : 'Finalizar Pedido'
            "
          ></v-text>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script></script>

<style scoped>
.sticky-button {
  position: sticky;
  bottom: 0;
}
</style>

<template>
  <v-container fluid class="pa-1 fill-height px-0">
    <v-card max-width="760" class="px-0 fill-height mx-auto" elevation="0">
      <v-layout class="fill-height px-0">
        <v-main class="mx-0 px-0">
          <v-container class="d-flex flex-column align-start -">
            <h3 class="font-weight-bold">Insira o endereço para entrega:</h3>

            <v-container fluid class="bg-white pa-0">
              <v-row class="bg-white" dense>
                <v-col class="ma-0 pb-0">
                  <v-form v-model="valid">
                    <v-container class="d-flex px-0" fluid>
                      <v-layout class="d-flex flex-column">
                        <v-row>
                          <v-col class="pb-0">
                            <v-text-field
                              v-model="firstname"
                              :rules="nameRules"
                              label="Endereço"
                              required
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-layout>
                    </v-container>
                  </v-form>
                </v-col>
              </v-row>
              <!-- detalhamento-endereço start -->
              <v-container class="px-0">
                <v-row>
                  <v-col cols="6" class="py-1">
                    <v-text-field
                      v-model="lastname"
                      :rules="nameRules"
                      label="Numero"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col cols="6" class="py-1">
                    <v-text-field
                      v-model="lastname"
                      :rules="nameRules"
                      label="Complemento"
                      required
                    ></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="6" class="py-1">
                    <v-text-field
                      v-model="lastname"
                      :rules="nameRules"
                      label="Bairro"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col cols="6" class="py-1">
                    <v-text-field
                      v-model="lastname"
                      :rules="nameRules"
                      label="CEP"
                      required
                    ></v-text-field>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col cols="6" class="py-1">
                    <v-text-field
                      v-model="lastname"
                      :rules="nameRules"
                      label="Numero"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col cols="6" class="py-1">
                    <v-text-field
                      v-model="lastname"
                      :rules="nameRules"
                      label="Complemento"
                      required
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-container>

              <!-- detalhamento-endereço end -->

              <!-- -->

              <!-- GeoLocator -->
              <v-row>
                <v-col class="d-flex align-center mb-5" cols="12">
                  <v-col cols="9">
                    <h5 class="font-weight-regular">
                      Clique no botão ao lado para capturar seu endereço atual.
                    </h5>
                  </v-col>

                  <v-col cols="4">
                    <v-btn
                      size="large"
                      elevation="3"
                      class="d-flex justify-center align-center"
                      icon="mdi-plus"
                      @click="toggleGeolocator"
                    >
                      <v-img
                        src="location_pin.png"
                        alt="logo"
                        width="20"
                      ></v-img>
                    </v-btn>
                  </v-col>
                </v-col>
              </v-row>
            </v-container>
          </v-container>
        </v-main>
      </v-layout>
    </v-card>
  </v-container>
  <router-link style="text-decoration: none" to="/dadoscomprador">
    <ProsseguirBotao />
  </router-link>
</template>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease, height 0.3s ease;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
  height: 0;
}
</style>

<script>
export default {
  data: () => ({
    amenities: [1, 4],
    neighborhoods: [1],
    geolocator: false,
    pinlocator: false,
  }),
  methods: {
    toggleGeolocator() {
      this.geolocator = !this.geolocator;
      this.pinlocator = !this.pinlocator;
    },
  },
};
</script>

<script setup>
import ProsseguirBotao from "@/components/ProsseguirBotao.vue";
</script>

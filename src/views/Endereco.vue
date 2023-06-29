<template>
  <v-container fluid class="ma-0 pa-0">
    <v-card max-width="760" class="fill-height mx-auto" elevation="0">
      <v-layout class="fill-height">
        <v-main>
          <v-container fluid>
            <h3 class="font-weight-bold my-2">
              Insira o endereço para entrega:
            </h3>

            <v-container fluid class="bg-white pa-0">
              <v-row class="bg-white" dense>
                <v-col class="ma-0 pb-0">
                  <v-text-field label="Endereço" single-line outlined>
                  </v-text-field>
                </v-col>
              </v-row>

              <!-- detalhamento-endereço start -->
              <v-expand-transition>
                <v-container v-show="geolocator" fluid class="ma-0 pa-0">
                  <v-row>
                    <v-col cols="12" class="d-flex mx-0 px-0">
                      <v-col cols="6" class="py-0">
                        <v-text-field label="Numero" single-line outlined>
                        </v-text-field>
                      </v-col>
                      <v-col cols="6" class="py-0">
                        <v-text-field label="Complemento" single-line outlined>
                        </v-text-field>
                      </v-col>
                    </v-col>
                  </v-row>

                  <v-row>
                    <v-col cols="12" class="d-flex ma-0 pa-0">
                      <v-col cols="6" class="py-0">
                        <v-text-field label="Bairro" single-line outlined>
                        </v-text-field>
                      </v-col>
                      <v-col cols="6" class="py-0">
                        <v-text-field label="CEP" single-line outlined>
                        </v-text-field>
                      </v-col>
                    </v-col>
                  </v-row>

                  <v-row>
                    <v-col cols="12" class="d-flex ma-0 pa-0">
                      <v-col cols="6" class="py-0">
                        <v-text-field label="Cidade" single-line outlined>
                        </v-text-field>
                      </v-col>
                      <v-col cols="6" class="py-0">
                        <v-text-field label="Estado" single-line outlined>
                        </v-text-field>
                      </v-col>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col class="d-flex justify-center text-center">
                      <h5 class="font-weight-regular">
                        Confirme os dados acima e clique em prosseguir.
                      </h5>
                    </v-col>
                  </v-row>
                </v-container>
              </v-expand-transition>
              <!-- detalhamento-endereço end -->

              <!-- -->

              <!-- GeoLocator -->
              <v-row v-show="!geolocator">
                <v-col class="d-flex align-center mb-5" cols="12">
                  <v-col cols="9">
                    <h5 class="font-weight-regular">
                      Clique no botão ao lado para capturar seu endereço atual.
                    </h5>
                  </v-col>

                  <v-col cols="3">
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

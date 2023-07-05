<template>
  <v-container fluid class="h-100 py-0" style="max-width: 800px">
    <v-layout class="">
      <v-main class="">
        <v-container class="d-flex flex-column align-start px-0">
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
                            id="endereco"
                            name="endereco"
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
                    v-model="delivery.number"
                    :rules="nameRules"
                    label="Numero"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="6" class="py-1">
                  <v-text-field
                    v-model="delivery.complement"
                    :rules="nameRules"
                    label="Complemento"
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="6" class="py-1">
                  <v-text-field
                    v-model="delivery.neighborhood"
                    :rules="nameRules"
                    label="Bairro"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="6" class="py-1">
                  <v-text-field
                    v-model="delivery.cep"
                    :rules="nameRules"
                    label="CEP"
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

                <v-col cols="3">
                  <CapturarLocalizacao />
                  <!-- <v-btn
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
                    </v-btn> -->
                </v-col>
              </v-col>
            </v-row>
          </v-container>
        </v-container>
      </v-main>
    </v-layout>
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
import { onMounted, ref } from "vue";
import CapturarLocalizacao from "@/components/CapturarLocalizacao.vue";
import ProsseguirBotao from "@/components/ProsseguirBotao.vue";

export default {
  components: {
    CapturarLocalizacao,
    ProsseguirBotao,
  },
  data: () => ({
    amenities: [1, 4],
    neighborhoods: [1],
    geolocator: false,
    pinlocator: false,
    delivery: {
      number: "",
      complement: "",
      neighborhood: "",
      cep: "",
      lat: "",
      lng: "",
    },
  }),
  mounted() {
    this.initAutocomplete();
  },
  methods: {
    initAutocomplete() {
      let input = document.querySelector("#endereco");
      let autocomplete = new google.maps.places.Autocomplete(input, {
        componentRestrictions: { country: ["br"] },
        fields: ["address_components", "geometry"],
        types: ["address"],
      });

      let fillInAddress = () => {
        const place = autocomplete.getPlace();

        for (const component of place.address_components) {
          const componentType = component.types[0];

          switch (componentType) {
            case "street_number":
              this.delivery.number = component.long_name;
              break;
            case "route":
              this.delivery.address = component.long_name;
              break;
            case "sublocality_level_1": // Aqui está a alteração. É onde o bairro é especificado.
              this.delivery.neighborhood = component.long_name;
              break;
            case "postal_code":
              this.delivery.cep = component.long_name;
              break;
            case "locality":
              this.delivery.city = component.long_name;
              break;
            case "administrative_area_level_1":
              this.delivery.state = component.long_name;
              break;
            case "country":
              this.delivery.country = component.long_name;
              break;
          }
        }

        if (place.geometry && place.geometry.location) {
          this.delivery.lat = place.geometry.location.lat();
          this.delivery.lng = place.geometry.location.lng();
        }
      };

      autocomplete.addListener("place_changed", fillInAddress);
    },
    toggleGeolocator() {
      this.geolocator = !this.geolocator;
      this.pinlocator = !this.pinlocator;
    },
  },
};
</script>

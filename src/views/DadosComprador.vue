<template>
  <v-container fluid class="h-100 py-0" style="max-width: 800px">
    <v-layout class="fill-height px-0">
      <v-main class="mx-auto px-0">
        <v-container fluid class="d-flex px-0 flex-column align-start">
          <h3 class="font-weight-bold">Insira os dados do comprador:</h3>

          <v-container fluid class="bg-white pa-0">
            <v-row class="bg-white" dense>
              <v-col class="ma-0 px-0">
                <v-form v-model="valid">
                  <v-container class="d-flex px-0 pb-1" fluid>
                    <v-layout class="d-flex flex-column">
                      <v-text-field
                        v-model="firstname"
                        :rules="nameRules"
                        label="Nome"
                        required
                      ></v-text-field>
                      <v-text-field
                        v-model="lastname"
                        :rules="nameRules"
                        :counter="11"
                        label="Telefone"
                        required
                      ></v-text-field>
                      <v-select
                        v-model="select"
                        :items="items"
                        :rules="[(v) => !!v || 'Campo obrigatório']"
                        label="Forma de Pagamento"
                        required
                      ></v-select>
                    </v-layout>
                  </v-container>
                </v-form>
              </v-col>
            </v-row>
          </v-container>
          <v-container fluid class="pb-5 mx-0">
            <v-row>
              <v-col class="d-flex text-center justify-center" cols="1">
                <v-icon color="primary" class="mb-4" size="x-large"
                  >mdi-map-marker</v-icon
                >
              </v-col>
              <v-col cols="6">
                <v-text class="font-weight-bold"> Entregar em: </v-text>
                <br />
                <span style="font-size: small">
                  <v-text> Oswaldo Cruz </v-text>
                  <br />
                  <v-text> 429 , APT 85 </v-text>
                  <br />
                  <v-text> Boqueirão , 11045101 </v-text>
                  <br />
                  <v-text> Santos , SP </v-text>
                </span>
              </v-col>
              <v-col
                class="d-flex flex-column align-end justify-start"
                cols="5"
              >
                <v-icon class="mb-4" size="x-large"
                  >mdi-calendar-outline</v-icon
                >

                <span style="font-size: small">
                  <v-text> 06/06/2023</v-text>
                  <br />
                  <v-text class="d-flex justify-end"> 12:00</v-text>
                </span>
              </v-col>
            </v-row>
          </v-container>
          <hr />
          <v-container
            fluid
            class="my-2"
            style="
              border: 1px solid grey;
              border-left: none;
              border-right: none;
            "
          >
            <v-row class="font-weight-medium" style="font-size: small">
              <v-col cols="2"> 1</v-col>
              <v-col class="d-flex justify-center"> P-13 (Recarga)</v-col>
              <v-col class="d-flex justify-end"> R$ 110.00</v-col>
            </v-row>
          </v-container>
          <v-text
            class="font-weight-medium"
            color="grey"
            style="font-size: small"
          >
            Por: Revenda Teste Ltda.
          </v-text>
          <br />
          <v-container fluid class="px-0 pb-0">
            <v-text class="d-flex justify-end font-weight-bold">
              Total: R$ 110,00
            </v-text>
          </v-container>
        </v-container>
      </v-main>
    </v-layout>
  </v-container>
  <ProsseguirBotao />
</template>

<script setup>
import ProsseguirBotao from "@/components/ProsseguirBotao.vue";
</script>

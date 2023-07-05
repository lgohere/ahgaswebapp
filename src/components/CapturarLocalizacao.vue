<template>
  <div>
    <v-btn @click="getGeoLocation">
      <v-icon>mdi-crosshairs-gps</v-icon>
    </v-btn>
  </div>
</template>

<script></script>

<!-- <script>
export default {
  data() {
    return {
      position: {},
      addressDetails: {},
    };
  },
  methods: {
    getGeoLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(this.showPosition);
      } else {
        console.error("Geolocation is not supported by this browser.");
      }
    },
    showPosition(position) {
      this.position = position;
      this.getAddressDetails();
    },
    async getAddressDetails() {
      let lat = this.position.coords.latitude;
      let lon = this.position.coords.longitude;

      // replace "YOUR_API_KEY" with your actual Google Maps API key
      let res = await fetch(
        `https://maps.googleapis.com/maps/api/geocode/json?latlng=${lat},${lon}&key=AIzaSyDXWZt8O3y0lYSDresa8iAy14bvEumbYDc`
      );
      let data = await res.json();

      // the details of the address will be in data.results[0]
      this.addressDetails = data.results[0];

      this.$emit("updateLocation", this.addressDetails);
    },
  },
};
</script> -->

<template>
  <router-view />
</template>

<script setup>
//

import { useProductStore } from "@/store/ProductStore";
useProductStore();
</script>

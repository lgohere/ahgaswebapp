<template>
  <div class="vue-modal">
    <div class="vue-modal-innes">
      <div class="vue-modaal-content">
        <slot />
        <v-btn @click="$emit('close')">Close</v-btn>
      </div>
    </div>
  </div>
</template>

<script></script>

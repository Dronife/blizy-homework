<script setup lang="ts">
import BrandsTable from '~/components/BrandsTable.vue'
import { useBrands } from '~/composables/useBrands'

const { brands, pending, error } = useBrands()
</script>

<template>
  <BrandsTable v-if="!pending && !error" :items="brands" />
  <div v-else class="p-6 text-center">
    <span v-if="pending">Loading…</span>
    <span v-else class="text-red-600">{{ error.message }}</span>
  </div>
</template>
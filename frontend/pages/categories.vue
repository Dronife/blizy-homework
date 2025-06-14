<script setup lang="ts">
import CategoriesTable from '~/components/CategoriesTable.vue'
import { useCategories } from '~/composables/useCategories'

const { categories, pending, error } = useCategories()
</script>

<template>
  <CategoriesTable v-if="!pending && !error" :items="categories" />
  <div v-else class="p-6 text-center">
    <span v-if="pending">Loading…</span>
    <span v-else class="text-red-600">{{ error.message }}</span>
  </div>
</template>
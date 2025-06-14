<script setup lang="ts">
import { ref } from 'vue'
import ModelsTable from '~/components/ModelsTable.vue'
import { useModels } from '~/composables/useModels'

// reactive controls
const search   = ref('')
const orderAsc = ref(true)
const page     = ref(1)

const { models, totalPages, pending, error } = useModels(search, orderAsc, page)

function toggleOrder() {
  orderAsc.value = !orderAsc.value
  page.value = 1
}
function prev() { if (page.value > 1) page.value-- }
function next() { if (page.value < totalPages.value) page.value++ }
</script>

<template>
  <ModelsTable
      v-if="!pending && !error"
      :items="models"
      :page="page"
      :total-pages="totalPages"
      :order-asc="orderAsc"
      @update:search="val => { search = val; page = 1 }"
      @toggle-order="toggleOrder"
      @page-prev="prev"
      @page-next="next"
  />

  <div v-else class="p-6 text-center">
    <span v-if="pending">Loading…</span>
    <span v-else class="text-red-600">{{ error.message }}</span>
  </div>
</template>
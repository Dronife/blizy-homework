<script setup lang="ts">
import { ref } from 'vue'
import BrandsTable from '~/components/BrandsTable.vue'
import { useBrands } from '~/composables/useBrands'

const search = ref('')
const orderAsc = ref(true)
const page = ref(1)

const { brands, totalPages, pending, error } = useBrands(search, orderAsc, page)

function toggleOrder () {
  orderAsc.value = !orderAsc.value
  page.value = 1
}
function prev () { if (page.value > 1) page.value-- }
function next () { if (page.value < totalPages.value) page.value++ }
</script>

<template>
  <BrandsTable
      v-if="!pending && !error"
      :items="brands"
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
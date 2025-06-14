<script setup lang="ts">
import { ref, computed } from 'vue'
import ProductsTable from '~/components/ProductsTable.vue'
import { useProducts } from '~/composables/useProducts'
import type { OrderField } from '~/composables/useProducts'
import { useFetch } from '#imports'

// filters
const search      = ref('')
const grade       = ref('')
const brand       = ref('')
const priceMin    = ref('')
const priceMax    = ref('')
const storageMin  = ref('')
const storageMax  = ref('')

const orderBy  = ref<OrderField>('price')
const orderAsc = ref(true)
const page     = ref(1)

// fetch brands for dropdown
const { data: brandData } = useFetch('http://localhost:8000/api/brands?order[name]=asc')
const brandOptions = computed(() => (brandData.value?.member ?? []).map((b: any) => b.name))

const gradeOptions = ['A+', 'A', 'AB', 'B', 'C', 'D']

const { products, totalPages, pending, error } = useProducts(
    search, grade, brand, priceMin, priceMax, storageMin, storageMax, orderBy, orderAsc, page
)

function changeSort(field: OrderField) {
  if (orderBy.value === field) {
    orderAsc.value = !orderAsc.value
  } else {
    orderBy.value = field
    orderAsc.value = true
  }
  page.value = 1
}
function prev() { if (page.value > 1) page.value-- }
function next() { if (page.value < totalPages.value) page.value++ }
</script>

<template>
  <ProductsTable
      v-if="!pending && !error"
      :items="products"
      :page="page"
      :total-pages="totalPages"
      :order-by="orderBy"
      :order-asc="orderAsc"

      :search-term="search"
      :selected-grade="grade"
      :selected-brand="brand"
      :price-min="priceMin"
      :price-max="priceMax"
      :storage-min="storageMin"
      :storage-max="storageMax"

      :grade-options="gradeOptions"
      :brand-options="brandOptions"

      @update:search="val => { search = val; page = 1 }"
      @update:grade="val => { grade = val; page = 1 }"
      @update:brand="val => { brand = val; page = 1 }"
      @update:priceMin="val => { priceMin = val; page = 1 }"
      @update:priceMax="val => { priceMax = val; page = 1 }"
      @update:storageMin="val => { storageMin = val; page = 1 }"
      @update:storageMax="val => { storageMax = val; page = 1 }"

      @sort="changeSort"
      @page-prev="prev"
      @page-next="next"
  />

  <div v-else class="p-6 text-center">
    <span v-if="pending">Loading…</span>
    <span v-else class="text-red-600">{{ error.message }}</span>
  </div>
</template>
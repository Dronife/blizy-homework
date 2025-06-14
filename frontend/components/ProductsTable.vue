<template>
  <div class="bg-white rounded-xl shadow p-4">
    <!-- filter bar -->
    <div class="grid gap-3 mb-4 md:grid-cols-6 md:items-end">
      <!-- search -->
      <div class="md:col-span-2 flex flex-col">
        <label class="text-xs mb-1">Search (model)</label>
        <input
            v-model="internalSearch"
            class="border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring focus:border-blue-500"
        />
      </div>
      <!-- grade -->
      <div class="flex flex-col">
        <label class="text-xs mb-1">Grade</label>
        <select v-model="internalGrade" class="border border-gray-300 rounded-md px-3 py-2">
          <option value="">All</option>
          <option v-for="g in gradeOptions" :key="g" :value="g">{{ g }}</option>
        </select>
      </div>
      <!-- brand -->
      <div class="flex flex-col">
        <label class="text-xs mb-1">Brand</label>
        <select v-model="internalBrand" class="border border-gray-300 rounded-md px-3 py-2">
          <option value="">All</option>
          <option v-for="b in brandOptions" :key="b" :value="b">{{ b }}</option>
        </select>
      </div>
      <!-- price range -->
      <div class="flex flex-col">
        <label class="text-xs mb-1">Price € from</label>
        <input v-model="internalPriceMin" type="number" min="0" step="0.01" class="border rounded-md px-3 py-2"/>
      </div>
      <div class="flex flex-col">
        <label class="text-xs mb-1">Price € to</label>
        <input v-model="internalPriceMax" type="number" min="0" step="0.01" class="border rounded-md px-3 py-2"/>
      </div>
      <!-- storage range -->
      <div class="flex flex-col">
        <label class="text-xs mb-1">Storage GB from</label>
        <input v-model="internalStorageMin" type="number" min="0" step="1" class="border rounded-md px-3 py-2"/>
      </div>
      <div class="flex flex-col">
        <label class="text-xs mb-1">Storage GB to</label>
        <input v-model="internalStorageMax" type="number" min="0" step="1" class="border rounded-md px-3 py-2"/>
      </div>
    </div>

    <!-- table -->
    <div class="overflow-x-auto">
      <table class="min-w-full text-sm text-left">
        <thead class="border-b bg-gray-50 text-xs uppercase tracking-wide text-gray-600">
        <tr>
          <th class="px-3 py-2">ID</th>
          <th class="px-3 py-2 cursor-pointer select-none" @click="sort('brand')">
            Brand <span v-if="orderBy==='brand'">{{ orderAsc ? '↑' : '↓' }}</span>
          </th>
          <th class="px-3 py-2 cursor-pointer select-none" @click="sort('category')">
            Category <span v-if="orderBy==='category'">{{ orderAsc ? '↑' : '↓' }}</span>
          </th>
          <th class="px-3 py-2 cursor-pointer select-none" @click="sort('model')">
            Model <span v-if="orderBy==='model'">{{ orderAsc ? '↑' : '↓' }}</span>
          </th>
          <th class="px-3 py-2">Grade</th>
          <th class="px-3 py-2">Storage</th>
          <th class="px-3 py-2 cursor-pointer select-none" @click="sort('price')">
            Price <span v-if="orderBy==='price'">{{ orderAsc ? '↑' : '↓' }}</span>
          </th>
          <th class="px-3 py-2">Color</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="p in items" :key="p.id" class="border-b hover:bg-gray-50">
          <td class="px-3 py-2">{{ p.id }}</td>
          <td class="px-3 py-2 capitalize">{{ p.category.brand.name }}</td>
          <td class="px-3 py-2 capitalize">{{ p.category.name }}</td>
          <td class="px-3 py-2">{{ p.model.name }}</td>
          <td class="px-3 py-2">{{ p.grade }}</td>
          <td class="px-3 py-2">{{ p.storage }} GB</td>
          <td class="px-3 py-2">€ {{ p.price.toFixed(2) }}</td>
          <td class="px-3 py-2">{{ p.color }}</td>
        </tr>
        <tr v-if="items.length === 0">
          <td colspan="8" class="px-3 py-4 text-center text-gray-500">No results</td>
        </tr>
        </tbody>
      </table>
    </div>
    <div class="flex justify-between items-center mt-4">
      <button @click="emit('page-prev')" :disabled="page===1"
              class="px-3 py-1 rounded border text-sm disabled:opacity-40">Prev
      </button>
      <span class="text-sm">Page {{ page }} / {{ totalPages }}</span>
      <button @click="emit('page-next')" :disabled="page===totalPages"
              class="px-3 py-1 rounded border text-sm disabled:opacity-40">Next
      </button>
    </div>
    <!-- (table markup unchanged from previous version) -->
  </div>
</template>

<script setup lang="ts">
import {ref, watch} from 'vue'
import type {OrderField} from '~/composables/useProducts'

interface ProductItem {
  id: number
  category: { name: string; brand: { name: string } }
  model: { name: string }
  grade: string
  storage: number
  price: number
  color: string
}

const props = defineProps<{
  items: ProductItem[]
  page: number
  totalPages: number
  orderBy: OrderField
  orderAsc: boolean
  // current filters
  searchTerm: string
  selectedGrade: string
  selectedBrand: string
  priceMin: string
  priceMax: string
  storageMin: string
  storageMax: string
  // options arrays
  gradeOptions: string[]
  brandOptions: string[]
}>()

const emit = defineEmits<{
  (e: 'update:search', val: string): void
  (e: 'update:grade', val: string): void
  (e: 'update:brand', val: string): void
  (e: 'update:priceMin', val: string): void
  (e: 'update:priceMax', val: string): void
  (e: 'update:storageMin', val: string): void
  (e: 'update:storageMax', val: string): void
  (e: 'sort', field: OrderField): void
  (e: 'page-prev'): void
  (e: 'page-next'): void
}>()

function sort(field: OrderField) {
  emit('sort', field)
}

// ----- two‑way bindings -----
const internalSearch = ref(props.searchTerm)
const internalGrade = ref(props.selectedGrade)
const internalBrand = ref(props.selectedBrand)
const internalPriceMin = ref(props.priceMin)
const internalPriceMax = ref(props.priceMax)
const internalStorageMin = ref(props.storageMin)
const internalStorageMax = ref(props.storageMax)

watch(() => props.searchTerm, v => {
  if (v !== internalSearch.value) internalSearch.value = v
})
watch(() => props.selectedGrade, v => {
  internalGrade.value = v
})
watch(() => props.selectedBrand, v => {
  internalBrand.value = v
})
watch(() => props.priceMin, v => {
  internalPriceMin.value = v
})
watch(() => props.priceMax, v => {
  internalPriceMax.value = v
})
watch(() => props.storageMin, v => {
  internalStorageMin.value = v
})
watch(() => props.storageMax, v => {
  internalStorageMax.value = v
})

const deb = (fn: () => void) => {
  clearTimeout((deb as any)._t);
  (deb as any)._t = setTimeout(fn, 400)
}

watch(internalSearch, v => deb(() => emit('update:search', v.trim())))
watch(internalGrade, v => emit('update:grade', v))
watch(internalBrand, v => emit('update:brand', v))
watch(internalPriceMin, v => deb(() => emit('update:priceMin', v)))
watch(internalPriceMax, v => deb(() => emit('update:priceMax', v)))
watch(internalStorageMin, v => deb(() => emit('update:storageMin', v)))
watch(internalStorageMax, v => deb(() => emit('update:storageMax', v)))
</script>
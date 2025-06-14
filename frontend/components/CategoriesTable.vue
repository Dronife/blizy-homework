<template>
  <div class="bg-white rounded-xl shadow p-4">
    <!-- header / search -->
    <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 mb-4">
      <h2 class="text-lg font-semibold">All categories</h2>
      <input
          v-model="internalSearch"
          placeholder="Search by category name…"
          class="border border-gray-300 rounded-md px-3 py-2 w-full sm:w-72 focus:outline-none focus:ring focus:border-blue-500"
      />
    </div>

    <!-- table -->
    <div class="overflow-x-auto">
      <table class="min-w-full text-sm text-left">
        <thead class="border-b bg-gray-50 text-xs uppercase tracking-wide text-gray-600">
        <tr>
          <th class="px-3 py-2">ID</th>
          <th class="px-3 py-2 cursor-pointer select-none" @click="emit('toggle-order')">
            Name <span>{{ orderAsc ? '↑' : '↓' }}</span>
          </th>
          <th class="px-3 py-2">Brand</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="c in items" :key="c.id" class="border-b hover:bg-gray-50">
          <td class="px-3 py-2">{{ c.id }}</td>
          <td class="px-3 py-2 whitespace-nowrap">{{ c.name }}</td>
          <td class="px-3 py-2 capitalize">{{ c.brand.name }}</td>
        </tr>
        <tr v-if="items.length === 0">
          <td colspan="3" class="px-3 py-4 text-center text-gray-500">No results</td>
        </tr>
        </tbody>
      </table>
    </div>

    <!-- pagination -->
    <div class="flex justify-between items-center mt-4">
      <button @click="emit('page-prev')" :disabled="page===1" class="px-3 py-1 rounded border text-sm disabled:opacity-40">Prev</button>
      <span class="text-sm">Page {{ page }} / {{ totalPages }}</span>
      <button @click="emit('page-next')" :disabled="page===totalPages" class="px-3 py-1 rounded border text-sm disabled:opacity-40">Next</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'

type CatItem = { id: number; name: string; brand: { name: string } }

const props = defineProps<{
  items: CatItem[]
  page: number
  totalPages: number
  orderAsc: boolean
}>()

const emit = defineEmits<{
  (e: 'update:search', val: string): void
  (e: 'toggle-order'): void
  (e: 'page-prev'): void
  (e: 'page-next'): void
}>()

const internalSearch = ref('')
watch(internalSearch, (v) => {
  clearTimeout((internalSearch as any)._t)
  ;(internalSearch as any)._t = setTimeout(() => emit('update:search', v.trim()), 400)
})
</script>
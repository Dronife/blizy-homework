<template>
  <div class="bg-white rounded-xl shadow p-4">
    <!-- header / search -->
    <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 mb-4">
      <h2 class="text-lg font-semibold">All brands</h2>
      <input
          v-model="search"
          placeholder="Search..."
          class="border border-gray-300 rounded-md px-3 py-2 w-full sm:w-64 focus:outline-none focus:ring focus:border-blue-500"
      />
    </div>

    <!-- table -->
    <div class="overflow-x-auto">
      <table class="min-w-full text-sm text-left">
        <thead class="border-b bg-gray-50 text-xs uppercase tracking-wide text-gray-600">
        <tr>
          <th class="px-3 py-2 cursor-pointer select-none" @click="setSort('id')">
            ID <span v-if="sortKey==='id'">{{ sortAsc ? '↑' : '↓' }}</span>
          </th>
          <th class="px-3 py-2 cursor-pointer select-none" @click="setSort('name')">
            Name <span v-if="sortKey==='name'">{{ sortAsc ? '↑' : '↓' }}</span>
          </th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="b in paginated" :key="b.id" class="border-b hover:bg-gray-50">
          <td class="px-3 py-2">{{ b.id }}</td>
          <td class="px-3 py-2 capitalize">{{ b.name }}</td>
        </tr>
        <tr v-if="paginated.length === 0">
          <td colspan="2" class="px-3 py-4 text-center text-gray-500">No results</td>
        </tr>
        </tbody>
      </table>
    </div>

    <!-- pagination -->
    <div class="flex justify-between items-center mt-4">
      <button @click="prev" :disabled="page===1" class="px-3 py-1 rounded border text-sm disabled:opacity-40">Prev</button>
      <span class="text-sm">Page {{ page }} / {{ totalPages }}</span>
      <button @click="next" :disabled="page===totalPages" class="px-3 py-1 rounded border text-sm disabled:opacity-40">Next</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'

const props = defineProps<{
  items: Array<{ id: number; name: string }>
}>()

const search = ref('')
const sortKey = ref<'id'|'name'>('id')
const sortAsc = ref(true)
const page = ref(1)
const perPage = 10

function setSort(key: 'id'|'name') {
  if (sortKey.value === key) sortAsc.value = !sortAsc.value
  else { sortKey.value = key; sortAsc.value = true }
  page.value = 1
}
const prev = () => page.value > 1 && page.value--
const next = () => page.value < totalPages.value && page.value++

const filtered = computed(() => {
  const term = search.value.toLowerCase()
  return props.items.filter(b =>
      b.name.toLowerCase().includes(term) ||
      b.id.toString().includes(term)
  )
})

const sorted = computed(() => {
  return [...filtered.value].sort((a, b) => {
    const aVal = a[sortKey.value]
    const bVal = b[sortKey.value]
    if (aVal < bVal) return sortAsc.value ? -1 : 1
    if (aVal > bVal) return sortAsc.value ? 1 : -1
    return 0
  })
})
const totalPages = computed(() => Math.ceil(sorted.value.length / perPage))
const paginated = computed(() => sorted.value.slice((page.value-1)*perPage, page.value*perPage))
watch(() => props.items, () => { page.value = 1 })
</script>
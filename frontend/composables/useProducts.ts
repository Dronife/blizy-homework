import { computed } from 'vue'
import type { Ref } from 'vue'
import { useFetch, useRuntimeConfig } from '#imports'

export type OrderField = 'price' | 'model' | 'category' | 'brand'

export function useProducts (
    search: Ref<string>,
    grade: Ref<string>,
    brand: Ref<string>,
    priceMin: Ref<string>,
    priceMax: Ref<string>,
    storageMin: Ref<string>,
    storageMax: Ref<string>,
    orderBy: Ref<OrderField>,
    orderAsc: Ref<boolean>,
    page: Ref<number>
) {
    const { public: { apiBase = 'http://localhost:8000/api' } } = useRuntimeConfig()
    const itemsPerPage = 10

    const url = computed(() => {
        const qs = new URLSearchParams()

        // --- text search ---
        if (search.value.trim()) {
            qs.append('model.name', search.value.trim())
        }

        // --- exact & ipartial filters ---
        if (grade.value) qs.append('grade', grade.value)
        if (brand.value) qs.append('category.brand.name', brand.value)

        // --- range filters ---
        if (priceMin.value) qs.append('price[gte]', priceMin.value)
        if (priceMax.value) qs.append('price[lte]', priceMax.value)
        if (storageMin.value) qs.append('storage[gte]', storageMin.value)
        if (storageMax.value) qs.append('storage[lte]', storageMax.value)

        // --- ordering ---
        const fieldMap: Record<OrderField, string> = {
            price: 'price',
            model: 'model.name',
            category: 'category.name',
            brand: 'category.brand.name'
        }
        qs.append(`order[${fieldMap[orderBy.value]}]`, orderAsc.value ? 'asc' : 'desc')

        qs.append('page', String(page.value))
        qs.append('itemsPerPage', String(itemsPerPage))
        return `${apiBase}/products?${qs.toString()}`
    })

    const { data, pending, error } = useFetch(url)

    const products   = computed(() => data.value?.member ?? [])
    const totalItems = computed(() => data.value?.totalItems ?? 0)
    const totalPages = computed(() => Math.max(1, Math.ceil(totalItems.value / itemsPerPage)))

    return { products, totalPages, pending, error }
}
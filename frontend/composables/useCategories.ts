import { computed } from 'vue'
import type { Ref } from 'vue'
import {ITEMS_PER_PAGE, useFetch, useRuntimeConfig} from '#imports'

/**
 * Reactive list of categories using API‑Platform filters:
 *   ‑ `name` ipartial (search)
 *   ‑ `order[name]` asc|desc (sort by name)
 *   ‑ `page` + `itemsPerPage` (pagination)
 */
export function useCategories (
    search: Ref<string>,
    orderAsc: Ref<boolean>,
    page: Ref<number>
) {
    const { public: { apiBase = 'http://localhost:8000/api' } } = useRuntimeConfig()

    const url = computed(() => {
        const qs = new URLSearchParams()
        if (search.value.trim()) qs.append('name', search.value.trim())
        qs.append('order[name]', orderAsc.value ? 'asc' : 'desc')
        qs.append('page', String(page.value))
        qs.append('itemsPerPage', String(ITEMS_PER_PAGE))
        return `${apiBase}/categories?${qs.toString()}`
    })

    const { data, pending, error } = useFetch(url)

    const categories  = computed(() => data.value?.member ?? [])
    const totalItems  = computed(() => data.value?.totalItems ?? 0)
    const totalPages  = computed(() => Math.max(1, Math.ceil(totalItems.value / ITEMS_PER_PAGE)))

    return { categories, totalPages, pending, error }
}
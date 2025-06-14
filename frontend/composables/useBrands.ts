import { computed } from 'vue'
import type { Ref } from 'vue'
import {ITEMS_PER_PAGE, useFetch, useRuntimeConfig} from '#imports'

/**
 * Reactive list of brands using API‑Platform filters:
 *   ‑ `name` ipartial (search)
 *   ‑ `order[name]` asc|desc (sort)
 *   ‑ `page` + `itemsPerPage` (pagination)
 */
export function useBrands (
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
        return `${apiBase}/brands?${qs.toString()}`
    })

    const { data, pending, error } = useFetch(url)

    const brands      = computed(() => data.value?.member ?? [])
    const totalItems  = computed(() => data.value?.totalItems ?? 0)
    const totalPages  = computed(() => Math.max(1, Math.ceil(totalItems.value / ITEMS_PER_PAGE)))

    return { brands, totalPages, pending, error }
}
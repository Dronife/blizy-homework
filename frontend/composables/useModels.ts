import {computed} from 'vue'
import type {Ref} from 'vue'
import {useFetch, useRuntimeConfig} from '#imports'
import {ITEMS_PER_PAGE} from "./config";

/**
 * Reactive, server‑side filtered list of models.
 * @param search   reactive search term (ipartial on Model.name)
 * @param orderAsc reactive sort order for name (true → asc / false → desc)
 * @param page     reactive page (1‑based)
 */
export function useModels(
    search: Ref<string>,
    orderAsc: Ref<boolean>,
    page: Ref<number>
) {
    const {public: {apiBase = 'http://localhost:8000/api'}} = useRuntimeConfig()

    /* build URL whenever params change */
    const url = computed(() => {
        const qs = new URLSearchParams()
        if (search.value.trim()) qs.append('name', search.value.trim())
        qs.append('order[name]', orderAsc.value ? 'asc' : 'desc')
        qs.append('page', String(page.value))
        qs.append('itemsPerPage', String(ITEMS_PER_PAGE))
        return `${apiBase}/models?${qs.toString()}`
    })

    // useFetch re‑fires automatically when url.value changes
    const {data, pending, error} = useFetch(url)

    const models = computed(() => data.value?.member ?? [])
    const totalItems = computed(() => data.value?.totalItems ?? 0)
    const totalPages = computed(() => Math.max(1, Math.ceil(totalItems.value / ITEMS_PER_PAGE)))

    return {models, totalPages, pending, error}
}
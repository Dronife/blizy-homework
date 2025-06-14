import { computed } from 'vue'
import { useFetch, useRuntimeConfig } from '#imports'

export function useCategories () {
    // default to local dev backend
    const { public: { apiBase = 'http://localhost:8000/api' } } = useRuntimeConfig()

    // fetch once; Nuxt handles SSR + client re‑use
    const { data, pending, error } = useFetch(`${apiBase}/categories?order[name]=asc`)

    // API returns { member: [...] }
    const categories = computed(() => data.value?.member ?? [])

    return { categories, pending, error }
}
import { computed } from 'vue'
import { useFetch, useRuntimeConfig } from '#imports'

export function useBrands () {
    const { public: { apiBase = 'http://localhost:8000/api' } } = useRuntimeConfig()
    const { data, pending, error } = useFetch(`${apiBase}/brands?order[name]=asc`)
    const brands = computed(() => data.value?.member ?? [])
    return { brands, pending, error }
}
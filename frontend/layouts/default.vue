<template>
  <div class="min-h-screen flex flex-col bg-gray-100 text-gray-900">
    <!-- --- header --- -->
    <header class="bg-white shadow">
      <div class="container mx-auto px-4 py-4 flex items-center justify-between">
        <NuxtLink to="/" class="text-xl font-semibold">MyShop Admin</NuxtLink>
        <nav class="flex gap-6 text-sm font-medium">
          <NuxtLink to="/categories" active-class="text-blue-600" class="hover:text-blue-600">Categories</NuxtLink>
          <NuxtLink to="/brands" active-class="text-blue-600" class="hover:text-blue-600">Brands</NuxtLink>
          <NuxtLink to="/models" active-class="text-blue-600" class="hover:text-blue-600">Models</NuxtLink>
          <!-- add more links here later -->
        </nav>
      </div>
    </header>

    <!-- --- page content --- -->
    <main class="flex-1 container mx-auto px-4 py-6">
      <slot />
    </main>

    <!-- --- footer --- -->
    <footer class="bg-white border-t">
      <div class="container mx-auto px-4 py-4 text-xs text-gray-500">
        © {{ new Date().getFullYear() }} MyShop
      </div>
    </footer>
  </div>
</template>
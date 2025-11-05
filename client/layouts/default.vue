<template>
  <div>
    <nav
      style="
        display: flex;
        gap: 1rem;
        padding: 1rem;
        border-bottom: 1px solid #ddd;
      "
    >
      <NuxtLink to="/">Home</NuxtLink>
      <NuxtLink to="/users">Users</NuxtLink>
    </nav>
    <slot />
  </div>
</template>

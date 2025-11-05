<template>
  <div style="max-width: 720px; margin: 2rem auto; padding: 1rem">
    <h1>Users</h1>
    <section style="margin-top: 1rem">
      <h3>Create User</h3>
      <UserForm @submit="handleCreate" />
      <p v-if="error" style="color: crimson">{{ error }}</p>
    </section>

    <section style="margin-top: 2rem">
      <h3>Existing Users</h3>
      <ul>
        <li v-for="u in users" :key="u.id">{{ u.id }} — {{ u.email }}</li>
      </ul>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import UserForm from "@/components/UserForm.vue";

type User = { id: number | string; email: string };

const { getUsers, createUser } = useApi();

const users = ref<User[]>([]);
const error = ref<string>("");

async function loadUsers() {
  try {
    users.value = (await getUsers()) as User[];
  } catch (e) {
    error.value = "Failed to load users";
    users.value = [];
  }
}

async function handleCreate(email: string) {
  try {
    await createUser(email);
    await loadUsers();
  } catch (e) {
    error.value = "Failed to create user";
  }
}

onMounted(loadUsers);
</script>

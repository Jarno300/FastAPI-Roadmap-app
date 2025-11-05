<!-- Removed duplicate script setup and unused import -->

<template>
  <div
    :style="boxStyle"
    style="max-width: 720px; margin: 2rem auto; padding: 1rem"
  >
    <h1>Nuxt + FastAPI skeleton</h1>
    <section style="margin-top: 1rem">
      <h3>Health</h3>
      <div>
        <button @click="checkHealth">Check FastAPI health</button>
        <span v-if="health" style="margin-left: 0.5rem"
          >{{ health.status }} (db: {{ health.db }})</span
        >
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import { BackgroundColor, TextColor } from "@/utils/colors";

type User = { id: number | string; email: string };
type Health = { status: string; db: boolean };

const { health: apiHealth, getUsers, createUser } = useApi();

const health = ref<Health | null>(null);
const error = ref<string>("");

const boxStyle = {
  backgroundColor: BackgroundColor.red900,
  color: TextColor.primary,
};

async function checkHealth() {
  try {
    health.value = (await apiHealth()) as Health;
  } catch (e) {
    health.value = { status: "down", db: false };
    error.value = "Backend not reachable";
  }
}

onMounted(async () => {
  await Promise.all([checkHealth()]);
});
</script>

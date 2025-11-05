<template>
  <form @submit.prevent="onSubmit">
    <input
      v-model="localEmail"
      type="email"
      placeholder="email@example.com"
      required
    />
    <button type="submit">Create</button>
  </form>
</template>

<script setup lang="ts">
import { ref } from "vue";

const emit = defineEmits<{
  (e: "submit", email: string): void;
}>();

const localEmail = ref<string>("");

function onSubmit() {
  if (!localEmail.value) return;
  emit("submit", localEmail.value);
  localEmail.value = "";
}
</script>

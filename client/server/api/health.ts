import { defineEventHandler } from "h3";
export default defineEventHandler(async () => {
  // Simple Nuxt server route for liveness
  return { status: "ok" };
});

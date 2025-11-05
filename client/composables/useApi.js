export const useApi = () => {
  const config = useRuntimeConfig();
  const baseUrl = config.public.apiBase;
  return {
    async health() {
      return await $fetch(`${baseUrl}/health`);
    },
    async getUsers() {
      return await $fetch(`${baseUrl}/users`);
    },
    async createUser(email) {
      return await $fetch(`${baseUrl}/users`, {
        method: 'POST',
        body: { email }
      });
    }
  };
};

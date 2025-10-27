import { BASE_URL } from "~/config/constants";

export const useApi = () => {
  const baseUrl = BASE_URL;
  return {
    async getRoadmaps() {
      return await $fetch(`${baseUrl}/api/roadmaps`);
    },
  };
};

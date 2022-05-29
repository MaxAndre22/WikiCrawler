<template>
  <q-layout view="lHh Lpr lFf" class="bg-primary">
    <div className="Logo" position="top" class="flex flex-center" padding>
      <q-btn
        icon="img:/icons/wikipedialogo.png"
        size="70px"
        flat
        round
        dense
        @click="$router.replace('/')"
      />
      <h1 style="color: white; font-family: 'Inter', sans-serif">
        WikiCrawler
      </h1>
    </div>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "MainLayout",

  setup() {
    return {};
  },
});
</script>

<style></style>

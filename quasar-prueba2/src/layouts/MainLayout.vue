<template>
  <q-layout view="lHh Lpr lFf" class="bg-primary">
    <div className="Logo" position="top" class="flex flex-center" padding>
      <q-img
        src="~/assets/wikipedialogo.png"
        style="width: 150px; height: 150px; margin-right:2%;"
      />
      <h1 style="color:white; font-family: 'Inter', sans-serif;">WikiCrawler</h1>
    </div>
    
    <q-page-container >
      <router-view/>
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'MainLayout',

  setup () {
    return {}
  }
})
</script>

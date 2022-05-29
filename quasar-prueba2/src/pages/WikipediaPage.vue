<template>
  <q-page>
    <h1 class="flex flex-center" style="margin-top: -2%;"> "{{keyword}}" </h1>

    <q-list classname="data" class="bg-secondary" style="min-height: 100vh;">
      <q-item-label header> Pages: </q-item-label>
      <a href="https://www.w3schools.com"> PAGE NAME FROM RESULTS</a>
    </q-list>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'
import { useRouter } from 'vue-router'

// Results = pages that the word appears
export default defineComponent({
  name: 'WikipediaPage',

  setup(){
    const router = useRouter()

    return {
      keyword: router.currentRoute.value.params.keyword
    }
  }
  
})
</script>

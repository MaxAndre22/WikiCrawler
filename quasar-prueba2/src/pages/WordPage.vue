<template>
  <q-page>
    <h1 class="flex flex-center" style="margin-top: -2%;"> "{{keyword}}" </h1>

    <div classname="data" class="bg-secondary" style="min-height: 100vh;padding: 12px;">
      <ul style="list-style-type: none;">
        <li><a href="https://www.w3schools.com"> PAGE NAME FROM RESULTS</a></li>
        <li><a href="https://www.w3schools.com"> PAGE NAME FROM RESULTS</a></li>
        <li><a href="https://www.w3schools.com"> PAGE NAME FROM RESULTS</a></li>
        <li><a href="https://www.w3schools.com"> PAGE NAME FROM RESULTS</a></li>        
        <li><a href="https://www.w3schools.com"> PAGE NAME FROM RESULTS</a></li>        
        <li><a href="https://www.w3schools.com"> PAGE NAME FROM RESULTS</a></li>        
        <li><a href="https://www.w3schools.com"> PAGE NAME FROM RESULTS</a></li>        
        <li><a href="https://www.w3schools.com"> PAGE NAME FROM RESULTS</a></li>        
        <li><a href="https://www.w3schools.com"> PAGE NAME FROM RESULTS</a></li>        
        <li><a href="https://www.w3schools.com"> PAGE NAME FROM RESULTS</a></li>        
        <li><a href="https://www.w3schools.com"> PAGE NAME FROM RESULTS</a></li>        
        <li><a href="https://www.w3schools.com"> PAGE NAME FROM RESULTS</a></li>        
        <li><a href="https://www.w3schools.com"> PAGE NAME FROM RESULTS</a></li>
      </ul>
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'
import { useRouter } from 'vue-router'

// Results = pages that the word appears
export default defineComponent({
  name: 'WordPage',

  setup(){
    const router = useRouter()

    return {
      keyword: router.currentRoute.value.params.keyword
    }
  }
  
})
</script>

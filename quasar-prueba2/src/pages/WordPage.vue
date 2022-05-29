<template>
  <q-page>
    <h1 class="flex flex-center text-white" style="margin-top: -2%;"> "{{keyword}}" </h1>

    <div classname="data" class="bg-secondary" style="min-height: 100vh;padding: 12px;">
      <ul style="list-style-type: none;">
        <li><router-link :to="{ name: 'wiki', params: { keyword: keyword, page:var1 } }"> {{var1}}</router-link></li>
        <li><router-link :to="{ name: 'wiki', params: { keyword: keyword, page:var2 } }"> {{var2}}</router-link></li>
        <li><router-link :to="{ name: 'wiki', params: { keyword: keyword, page:var3 } }"> {{var3}}</router-link></li>
      </ul>
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'
import { useRouter } from 'vue-router'

//const resultsNamePages = //Lista de nombres de paginas que son respuesta --> Dinamico

// Results = pages that the word appears
export default defineComponent({
  name: 'WordPage',

  setup(){
    const router = useRouter()

    return {
      var1: "Sinfonia N1", var2: "Shrek (musical)", var3: "Minecraft (game)",
      keyword: router.currentRoute.value.params.keyword
    }
  }
  
})
</script>

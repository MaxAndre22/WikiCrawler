<template>
  <q-page>
    <h2 class="flex flex-center text-white" style="margin-top: -2%;"> Artículo: "{{page}}" </h2>
    <h2 class="flex flex-center text-white" style="margin-top: -2%;"> Palabra: "{{keyword}}" </h2>

    <div classname="data" class="bg-secondary" style="margin-top: -2%; min-height: 100vh;">
      <h5 class="text-center" style="padding-top: 2%;">
        Cantidad de veces que aparece la(s) palabra(s) en el texto: {{var1}}
      </h5>
      <h5 class="text-center">
        Porcentaje de la palabra en el título: {{var2}}%
      </h5>
      <h5 class="text-center">
        Porcentaje de la palabra en el texto: {{var3}}%
      </h5>
      <h5 class="text-center">
        Tags en donde aparece y porcentaje: H1: {{varH1}}% ...
      </h5>
    </div>
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
      keyword: router.currentRoute.value.params.keyword,
      page: router.currentRoute.value.params.page,

      var1: 10, var2: 5, var3: 12, varH1: 40
    }
  }
  
})
</script>

<template>
  <q-page>
    <h1 class="flex flex-center text-white" style="margin-top: -2%;"> "{{keyword}}" </h1>

    <div classname="data" class="bg-secondary" style="min-height: 100vh;padding: 12px;">
      <ul style="list-style-type: none;">
        <li v-for="item in pages" :key="item._id">
          <router-link :to="{ name: 'wiki', params: { keyword: keyword, page:item.name } }"> {{item.name}}</router-link>
        </li>
      </ul>
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'
import { useRouter } from 'vue-router'

export default defineComponent({
  name: 'WordPage',

  data(){
    return{
      pages: [
        { name: 'Aguanish River' },
        { name: 'Triple 9' },
        { name: 'Chrysoprasis guerrerensis' },
        { name: 'Super Auto Pets' },
        { name: 'Angelo Altieri' },
        { name: 'Sugarloaf massacre' },
        { name: 'Trinity College School' },
        { name: 'Mortimer J. Adler' },
        { name: 'Frielendorf' },
        { name: 'Lucian Itu' },
        { name: 'Gilgit River' },
        { name: 'Cengiz Coşkun' },
        { name: 'Juan Sebastián Gamboa' },
        { name: 'XD' }
      ]
    }
  },

  setup(){
    const router = useRouter()

    return {
      var1: "Sinfonia N1", var2: "Shrek (musical)", var3: "Minecraft (game)",
      keyword: router.currentRoute.value.params.keyword
    }
  }
})
</script>

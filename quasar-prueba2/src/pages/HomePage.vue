<template>
  <q-page>
    <q-form classname="Search" class="flex flex-center" style="margin-top: -2%;"
      @submit="onSubmit"
    >
      <q-input 
        style="min-width: 45%;" 
        bg-color="white"
        color="primary"
        v-model="words" 
        placeholder="Ingrese una o varias palabras."
      />
      
      <q-btn
        flat
        dense
        type="submit"
        icon="search"
        aria-label="search"
        size=25px
        color="white"
      />

    </q-form>
    
  </q-page>
</template>

<script>
import { defineComponent, ref } from 'vue'

export default defineComponent({
  name: 'HomePage',

  setup(){

    const words = ref(null)

    return{ 
      words,
      onSubmit(){
        console.log(words.value) 
      }
    }
  }
})
</script>

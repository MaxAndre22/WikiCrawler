<template>
  <q-page>
    <q-form
      classname="Search"
      class="flex flex-center"
      style="margin-top: -2%"
      @submit="onSubmit"
    >
      <q-input
        style="min-width: 45%"
        bg-color="white"
        color="black"
        v-model="words"
        placeholder="Ingrese una o varias palabras."
        :rules="[(val) => (val && val.length > 0) || 'Por favor escriba algo']"
      />

      <q-btn
        flat
        dense
        type="submit"
        icon="search"
        aria-label="search"
        size="25px"
        color="white"
      />
    </q-form>

    <div classname="data" class="bg-secondary" style="min-height: 100vh">
      <h5 class="text-center">
        Hay un promedio de {{ varA }} títulos por página.
      </h5>
      <h5 class="text-center">
        Usando Stemming hay un promedio de {{ varB1 }} palabras distintas por
        página, {{ varB2 }} por títulos y {{ varB3 }} por subtítulos.
      </h5>
      <h5 class="text-center">
        En promedio un {{ varC1 }}% de las referencias tienen links y
        {{ varC2 }}% de estos links están activos.
      </h5>
      <h5 class="text-center">
        Cada referencia se usa aproximadamente {{ varD }} veces en el texto.
      </h5>
      <h5 class="text-center">Un {{ varE }}% de las imágenes tienen Alt.</h5>
      <h5 class="text-center">Las palabras más comunes son: {{ varF }}.</h5>
    </div>
  </q-page>
</template>

<script>
import { defineComponent, ref } from "vue";
import { useRouter } from "vue-router";

export default defineComponent({
  name: "HomePage",

  setup() {
    const words = ref(null);
    const router = useRouter();

    return {
      words,

      //Vue lifecycle hooks beforecreate()
      varA: 10,
      varB1: 150,
      varB2: 7,
      varB3: 4,
      varC1: 40,
      varC2: 70,
      varD: 2,
      varE: 27,
      varF: "'What', 'The', 'A', 'An' y 'Another'",

      onSubmit() {
        //console.log(words.value)
        router.push({ name: "word", params: { keyword: words.value } });
      },
    };
  },
});
</script>

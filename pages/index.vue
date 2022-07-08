<script>
import Exemple from '../components/exemple.vue'
import Map from '../components/map.vue'
export default {
  name: "IndexPage",
  components:{
    'app':Exemple,
    'carte':Map
  },
  data () {
    return {
      restos: []
    }
  },
    mounted(){
    this.fetchAll();
  },
  methods: {
    async fetchAll() {
      this.restos = await this.$axios.$get('http://localhost:8000');
    },
  }
}
</script>

<template>
    <div>
      <br><h1 class='text-xl' style="text-align:center"><strong>Carte et liste de mes restaurants préférés</strong></h1><br>
    <carte :locations="restos"></carte>
    <app @changed="fetchAll()"></app>
    </div>
</template>
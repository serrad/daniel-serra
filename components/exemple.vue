<template>
  <div class="container mx-auto mt-8">
    
    <form action="#">
      <div class="mb-6">
          <label for="title" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300" >Nom du restaurant (requis)</label>
          <input v-model="fields.title" type="text" id="title" name="title" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
      </div>
      <div class="mb-6">
          <label for="description" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Description (requise)</label>
          <input v-model="fields.description" type="text" id="description" name="description" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
      </div>
      <div class="mb-6">
          <label for="address" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Adresse</label>
          
      <gmap-autocomplete
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" id="address" name="address"  :value="description" @place_changed="setPlace">
        <template v-slot:default="slotProps">
          <FormulateInput
            name='direccion_1'
            label="Direccion Uno"
            ref="input"
            v-on:listener="slotProps.listeners"
            v-on:attrs="slotProps.attrs"
          >
        </FormulateInput>
      </template>
      </gmap-autocomplete>
      </div>
      <div class="mb-6">
          <label for="phone" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Téléphone</label>
          <input v-model="fields.phone" type="text" id="phone" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="+41 21 111 11 11">
      </div>
      <button @click="create()" type="button" class="text-white bg-green-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Ajouter</button>
      <br><br>
      <p v-if="errorsCreate.length">
        <b>Veuillez corriger les erreurs :</b>
        <ul>
          <li v-for="error in errorsCreate">{{ error }}</li>
        </ul>
      </p>
    </form>
    <br><br>
    <ul>
      <li v-for="resto in restos" :key="resto.id"><br>{{ parentMessage }} : {{ resto.title }}<br>  {{ resto.description }}<br>  {{ resto.address }}<br>  {{ resto.phone }}<br><br>
      <button @click="show(resto)" type="button" class="text-white bg-yellow-500 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Modifier</button>
      <br><br>
      <button @click="del(resto.id)" type="button" class="text-white bg-red-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Supprimer</button>
      <br><br><br>
      </li>
    </ul>

    <modal v-if="resto" name="modification" :width="600" :height="600" :adaptive="true">
      <form action="#" class="p-8">      
        <div class="mb-6">
            <label for="title" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Nom du restaurant (requis)</label>
            <input v-model="resto.title" type="text" id="title" name="title" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required>
        </div>
        <div class="mb-6">
            <label for="description" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Description (requise)</label>
            <input v-model="resto.description" type="text" id="description" name="description" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
        </div>
        <div class="mb-6">
            <label for="address" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Adresse</label>
             <gmap-autocomplete
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" id="address" name="address"  :value="description" @place_changed="setPlace">
                <template v-slot:default="slotProps">
                  <FormulateInput
                    name='direccion_1'
                    label="Direccion Uno"
                    ref="input"
                    v-on:listener="slotProps.listeners"
                    v-on:attrs="slotProps.attrs"
                  >
                </FormulateInput>
              </template>
      </gmap-autocomplete>
        </div>
        <div class="mb-6">
            <label for="phone" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Téléphone</label>
            <input v-model="resto.phone" type="text" id="phone" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="+41 21 111 11 11">
        </div>
        <button @click="update(resto.id)" type="button" class="text-white bg-yellow-500 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Mettre à jour</button>
        <br><br>
        <p v-if="errorsUpdate.length">
          <b>Veuillez corriger les erreurs :</b>
          <ul>
            <li v-for="error in errorsUpdate">{{ error }}</li>
          </ul>
        </p>
      </form>
    </modal>
  </div>
</template>

<script>
export default {
  data(){
    return {
      errorsCreate: [],
      errorsUpdate: [],
      parentMessage: 'Nom',
      restos: [],
      resto: null,
      fields: {
        title: '',
        description: '',
        address: '',
        phone: '',
        latitude: '0.0',
        longitude: '0.0'
      },
    }
  },
  mounted(){
    this.fetchAll();
  },
  methods: {
    
  setPlace(place) {
    this.place = place;
  },
  setFields(){
      if(this.place){
        this.fields.latitude = this.place.geometry.location.lat();
        this.fields.longitude = this.place.geometry.location.lng();
        this.fields.address = this.place.formatted_address;
      }
  },
    updateFields(){
      if(this.place){
        this.resto.latitude = this.place.geometry.location.lat();
        this.resto.longitude = this.place.geometry.location.lng();
        this.resto.address = this.place.formatted_address;
      }
  },
  setDescription(description) {
      this.description = description;
  },
    checkFormCreate: function (e) {
      this.errorsCreate = [];
      if (this.fields.title && this.fields.description) {
        return true;
      }
      if (!this.fields.title) {
        this.errorsCreate.push('Nom requis');
      }
      if (!this.fields.description) {
        this.errorsCreate.push('Description requise');
      }
    },
    checkFormUpdate: function (e) {
      this.errorsUpdate = [];
      if (this.resto.title && this.resto.description) {
        return true;
      }
      if (!this.resto.title) {
        this.errorsUpdate.push('Nom requis');
      }
      if (!this.resto.description) {
        this.errorsUpdate.push('Description requise');
      }
    },
    async fetchAll() {
      this.restos = await this.$axios.$get('http://localhost:8000');
    },
    async create() {
      if (this.checkFormCreate()) {
        this.setFields();
        await this.$axios.post('http://localhost:8000/items', this.fields)
          .then(function( response ){
              this.fetchAll();
              this.dataChange();
              this.fields = {
                title: '',
                description: '',
                address: '',
                phone: '',
                latitude: '0.0',
                longitude: '0.0'
              }
          }.bind(this));
          
      }
    },
    async del(id) {
      await this.$axios.delete('http://localhost:8000/items/' + id)
        .then(function( response ){
            this.fetchAll();
            this.dataChange();
        }.bind(this));
    },
    async update(id) {
      if (this.checkFormUpdate()) {
        this.updateFields();
        await this.$axios.put('http://localhost:8000/items/'+ id, this.resto)
          .then(function( response ){
              this.fetchAll();
              this.dataChange();
              this.resto = null;
              this.hide();
          }.bind(this));
      }
    },

    show (resto) {
            this.resto = resto;
            this.$modal.show('modification');
            this.errorsCreate = [];
    },
    hide () {
            this.$modal.hide('modification');
    },
    dataChange() {
      this.$emit('changed');
    }
  }
}
</script>
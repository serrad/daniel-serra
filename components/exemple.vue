<template>
  <div class="container mx-auto mt-8">
    
    <!-- Formulaire d'ajout de restaurants -->
    <form action="#">
      <div class="mb-6">
          <label for="title" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300" >Nom du restaurant (requis)</label>
          <input v-model="fields.title" type="text" id="title" name="title" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
      </div>
      <div class="mb-6">
          <label for="description" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Description</label>
          <input v-model="fields.description" type="text" id="description" name="description" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
      </div>
      <div class="mb-6">
          <label for="phone" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Téléphone</label>
          <input v-model="fields.phone" type="text" id="phone" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="+41 21 111 11 11">
      </div>
      <div class="mb-6">
          <label for="address" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Adresse</label>
      <!-- Autocomplete de l'adresse saisie -->
      <gmap-autocomplete class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" id="address" name="address"  :value="description" @place_changed="setPlace">
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
      <button @click="create()" type="button" class="text-white bg-green-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Ajouter</button>
      <br><br>
      <!-- Affichage des erreurs de saisie requise -->
      <p v-if="errorsCreate.length">
        <b style="color:#FF0000">Veuillez corriger les erreurs suivantes :</b>
        <ul>
          <li v-for="error in errorsCreate">{{ error }}</li>
        </ul>
      </p>
    </form>
    <br><br>
    <!-- Affichage de la liste de mes restaurants -->
    <ul>
      <li v-for="resto in restos" :key="resto.id"><br>{{ parentMessage }} : {{ resto.title }}<br> Description : {{ resto.description }}<br>  Tél. : {{ resto.phone }}<br> Adresse : {{ resto.address }}<br><br>
      <button @click="show(resto)" type="button" class="text-white bg-yellow-500 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Modifier</button>
      <br><br>
      <button @click="del(resto.id)" type="button" class="text-white bg-red-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Supprimer</button>
      <br><br><br>
      </li>
    </ul>

    <!-- Fenêtre modale de modification avec formulaire -->
    <modal v-if="resto" name="modification" :width="600" :height="600" :adaptive="true">
      <form action="#" class="p-8">      
        <div class="mb-6">
            <label for="title" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Nom du restaurant (requis)</label>
            <input v-model="resto.title" type="text" id="title" name="title" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required>
        </div>
        <div class="mb-6">
            <label for="description" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Description</label>
            <input v-model="resto.description" type="text" id="description" name="description" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
        </div>
        <div class="mb-6">
            <label for="phone" class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300">Téléphone</label>
            <input v-model="resto.phone" type="text" id="phone" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="+41 21 111 11 11">
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
        <button @click="update(resto.id)" type="button" class="text-white bg-yellow-500 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Mettre à jour</button>
        <br><br>
        <!-- Affichage des erreurs de saisie requise -->
        <p v-if="errorsUpdate.length">
          <b style="color:#FF0000">Veuillez corriger les erreurs suivantes :</b>
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
  // Au démarrage de l'application
  mounted(){
    this.fetchAll();
  },
  // Méthodes
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
    // Gestion des erreurs de saisie requise lors de la création d'un restaurant
    checkFormCreate: function (e) {
        this.errorsCreate = [];
        if (this.fields.title) {
          return true;
        }
        if (!this.fields.title) {
          this.errorsCreate.push('Nom requis');
        }
    },
    // Gestion des erreurs de saisie requise lors de la modification d'un restaurant
    checkFormUpdate: function (e) {
        this.errorsUpdate = [];
        if (this.resto.title) {
          return true;
        }
        if (!this.resto.title) {
          this.errorsUpdate.push('Nom requis');
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
    // Nouvel affichage de la page lors d'une suppression
    async del(id) {
        await this.$axios.delete('http://localhost:8000/items/' + id)
          .then(function( response ){
              this.fetchAll();
              this.dataChange();
          }.bind(this));
    },
    // Nouvel affichage de la page lors d'une modification
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
    // Fait apparaître la fenêtre modale - Appelé lors d'une modification
    show (resto) {
              this.resto = resto;
              this.$modal.show('modification');
              this.errorsCreate = [];
    },
    // Fait disparaître la fenêtre modale
    hide () {
              this.$modal.hide('modification');
    },
    dataChange() {
        this.$emit('changed');
    }
  }
}
</script>
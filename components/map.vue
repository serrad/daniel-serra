<script>

export default {
  name: "map",
  props: {
    locations:{
      type: Array,
      default: []
    }
  },
  data () {
    return {
          center: {
            lat: 46.5196535,
            lng: 6.6322734
          },
          infoWindowPos: null,
          infoWinOpen: false,
          currentMidx: null,

          infoOptions: {
        	content: '',
            pixelOffset: {
              width: 0,
              height: -35
            }
          },
          locations: this.locations
    }
  },

  methods: {
    toggleInfoWindow: function(marker, idx) {
            this.infoWindowPos = marker.position;
            this.infoOptions.content = marker.infoText;

            //check if its the same marker that was selected if yes toggle
            if (this.currentMidx == idx) {
              this.infoWinOpen = !this.infoWinOpen;
            }
            //if different marker set infowindow to open and reset current marker index
            else {
              this.infoWinOpen = true;
              this.currentMidx = idx;
            }
      },   
  }
}
</script>

<template>
    <div>
    <gmap-map
      :center="center"
      :zoom="10"
      style="width:100%;  height: 555px;">
      
      <gmap-marker
        :key="index"
        v-for="(m,i) in locations"
        :position="m.position"
        :clickable="true"
        :icon="markerIcon"
        @click="toggleInfoWindow(m,i)">
      ></gmap-marker>

      <gmap-info-window :options="infoOptions" :position="infoWindowPos" :opened="infoWinOpen" @closeclick="infoWinOpen=false">
      </gmap-info-window>
    </gmap-map>
    </div>
</template>
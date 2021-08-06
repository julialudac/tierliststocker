<template>
  <select name="tierlist" id="" v-model="selectedName">
    <option v-for="(name, index) in tierlistNames" :key="index" :value="name">{{name}}</option>
  </select>
</template>

<script>
export default {
  name: 'TierlistSelection',
  props: {
    tierlistNames: Array
  },
  data() {
    return {
      selectedName: ''
    }
  },
  created() {
    this.selectedName = this.tierlistNames[0];
  },
  watch: {
    // at the creation of the component tierlistNames can be undefined so selectedName too.
    tierlistNames: function() {
      this.selectedName = this.tierlistNames[0];
    }
  }
}
</script>
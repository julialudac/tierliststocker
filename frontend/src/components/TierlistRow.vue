<template>
  <tr>
      <th :style="`background-color:${tierAndElements.headColor}`">{{ tierAndElements.rank }}</th>
      <TierlistCell :elements="tierAndElements.elements" @new-item-submitted="submitNewItem" @delete-item="deleteItem"/>
  </tr>
</template>

<script>
import TierlistCell from '../components/TierlistCell.vue'

export default {
  name: 'TierlistRow',
  props: {
    tierAndElements : Object
  },
  components : {
    TierlistCell
  },
  methods: {
    submitNewItem(val) {
      this.$emit('new-item-submitted', {rank: this.tierAndElements.rank, item: val});
    },
    deleteItem(val) {
      this.$emit('delete-item', {rank: this.tierAndElements.rank, item: val});
    }
  }
}
</script>

<style scoped>
tr {
  border: 1px solid;
}
</style>
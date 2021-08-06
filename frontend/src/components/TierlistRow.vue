<template>
  <tr>
      <th :style="`background-color:${tierAndItsElements.headColor}`">{{ tierAndItsElements.rank }}</th>
      <TierlistCell :elements="tierAndItsElements.elements" @new-item-submitted="submitNewItem" @delete-item="deleteItem"/>
  </tr>
</template>

<script>
import TierlistCell from '../components/TierlistCell.vue'

export default {
  name: 'TierlistRow',
  props: {
    tierAndItsElements: Object,
    allTierlistElements: Array
  },
  components : {
    TierlistCell
  },
  methods: {
    submitNewItem(val) {
      this.$emit('new-item-submitted', {rank: this.tierAndItsElements.rank, item: val});
    },
    deleteItem(val) {
      this.$emit('delete-item', {rank: this.tierAndItsElements.rank, item: val});
    }
  }
}
</script>

<style scoped>
tr {
  border: 1px solid;
}
</style>
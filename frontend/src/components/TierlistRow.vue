<template>
  <tr>
      <th :style="`background-color:${tierAndElements.headColor}`">{{ tierAndElements.rank }}</th>
      <TierlistCell :elements="tierAndElements.elements"/>
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
  }
}
</script>

<style scoped>
tr {
  border: 1px solid;
}
</style>
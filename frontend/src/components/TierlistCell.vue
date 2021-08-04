<template>
  <td @dblclick="toggleAddMode">
    <button v-for="(el, index) in elements" :key="index">
      {{ el }} | x
    </button>
    <span v-show="addMode"><input type="text" /><button class="ok">Ok!</button></span>
  </td>
</template>

<script>
export default {
  name: 'TierlistCell',
  props: {
    elements: Array
  },
  data() {
    return {
      addMode: false
    }
  },
  methods: {
    toggleAddMode(event) {
      if (event.target.__vnode.type == 'td') {
        this.addMode=!this.addMode;
      }
    }
  }
}
</script>

<style scoped>
td {
  border: 1px solid;
}
.ok {
  background-color: lightgreen;
}
</style>
<template>
  <td @dblclick="toggleAddModeByClick">
    <button v-for="(el, index) in elements" :key="index" @click="askDeleteElement">
      {{ el }} | <span>x</span> 
    </button>
    <form @submit="submitNewItem" style="display:inline-block">
      <span v-show="addMode"><input type="text" v-model="inputVal"/><button type='submit' class="ok">Ok!</button></span>
    </form>
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
      addMode: Boolean,
      inputVal: String
    }
  },
  created() {
    this.addMode = false;
    this.inputVal = '';
  },
  methods: {
    toggleAddModeByClick(event) {
      if (event.target.__vnode.type == 'td') {
        this.addMode=!this.addMode;
      }
    },
    submitNewItem(e) {
      e.preventDefault();
      if (this.inputVal != '') {
        this.$emit('new-item-submitted', this.inputVal);
        this.addMode=!this.addMode;
        this.inputVal = '';
      } else {
        alert('Please enter something!');
      }
    },
    askDeleteElement(event) {
      if (event.target.__vnode.type == 'span') {
        let item = event.target.parentNode.textContent;
        item = item.substring(0, item.length-4);
        if (confirm(`Are you sure you want to delete item "${item}"?`)) {
          this.$emit('delete-item', item);
        } 
      }
    }
  }
}
</script>

<style scoped>
td {
  border: 1px solid;
}
td:hover {
  background-color: #ddffff;
}
.ok {
  background-color: lightgreen;
}
</style>
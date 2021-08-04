<template>
  <div>
    <h1>This is your tierlist table</h1>
    <TierlistTable/>
  </div>
</template>

<script>
import TierlistTable from './components/TierlistTable.vue'

export default {
  name: 'App',
  components: {
    // HelloWorld
    TierlistTable
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

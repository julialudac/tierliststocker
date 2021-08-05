<template>
  <div>
    <h1>This is your tierlist table</h1>
    <p>Switch tierlist: 
      <select name="tierlist" id="" v-model="selectedName">
        <option v-for="(name, index) in tierlistNames" :key="index" :value="name">{{name}}</option>
      </select>
    </p>
    <TierlistTable :tierlistName="selectedName"/>
  </div>
</template>

<script>
import TierlistTable from './components/TierlistTable.vue'

export default {
  name: 'App',
  data() {
    return {
      tierlistNames: [],
      selectedName: ""
    }
  },
  components: {
    // HelloWorld
    TierlistTable
  },
  async created() {
    const tierlists = await this.fetchTierlists();
    this.tierlistNames = tierlists.map(tierlist => tierlist.name);
    this.selectedName = this.tierlistNames[0];
  },
  methods: {
    async fetchTierlists() {
      const res = await fetch('http://localhost:3000/tierlists');
      return res.json();
    },
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

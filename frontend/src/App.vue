<template>
  <div>
    <h1>This is your tierlist table</h1>
    <p>Switch tierlist: 
      <select name="tierlist" id="" v-model="selectedName">
        <option v-for="(name, index) in tierlistNames" :key="index" :value="name">{{name}}</option>
      </select>
    </p>
    <TierlistTable :tierlistName="selectedName"/>
    <form @submit="addTierlist">
      <input type="text" v-model="tierlistToAdd"/>
      <button type="submit">New tierlist</button>
    </form>
  </div>
</template>

<script>
import TierlistTable from './components/TierlistTable.vue'

export default {
  name: 'App',
  data() {
    return {
      tierlistNames: [],
      selectedName: '',
      tierlistToAdd: ''
    }
  },
  components: {
    // HelloWorld
    TierlistTable
  },
  created() {
    this.refresh();
  },
  methods: {
    async fetchTierlists() {
      const res = await fetch('http://localhost:3000/tierlists');
      return res.json();
    },
    async refresh() {
      const tierlists = await this.fetchTierlists();
      this.tierlistNames = tierlists.map(tierlist => tierlist.name);
      this.selectedName = this.tierlistNames[0];
    },
    addTierlist(e) {
      e.preventDefault();
      if (this.tierlistNames.some(name => name == this.tierlistToAdd)) {
        alert(`Tierlist ${this.tierlistToAdd} already exits.`);
        return;
      }
      try {
          const tiers = ['S', 'A', 'B', 'C', 'D', 'E', 'F'];
          let emptyContent = {}
          for (let tier of tiers) {
            emptyContent[tier] = [];
          }
          fetch('http://localhost:3000/tierlists', {
            method: "POST",
            headers: {'Content-type': 'application/json'},
            body: JSON.stringify({name: this.tierlistToAdd, content: emptyContent})
          });
          alert(`Successfully added new tierlist ${this.tierlistToAdd}!`);
          this.refresh();
      } catch(e) {
        console.log(`Error adding new tierlist: ${e.message}`);
      }
    }
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

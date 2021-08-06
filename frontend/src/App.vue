<template>
  <div>
    <h1>This is your tierlist table</h1>
    <p>Switch tierlist: 
      <TierlistSelection :tierlistNames="tierlistNames" v-model="selectedName" />
    </p>
    <TierlistTable :tierlistName="selectedName"/>
    <form @submit="addTierlist">
      <input type="text" v-model="tierlistToAdd"/>
      <button type="submit">New tierlist</button>
    </form>
    <form @submit="deleteTierlist">
      <TierlistSelection :tierlistNames="tierlistNames" v-model="tierlistToDelete" />
      <button type="submit">Delete tierlist (!!!)</button>
    </form>
  </div>
</template>

<script>
import TierlistTable from './components/TierlistTable.vue'
import TierlistSelection from './components/TierlistSelection.vue'

export default {
  name: 'App',
  data() {
    return {
      tierlistNames: [],
      selectedName: '',
      tierlistToAdd: '',
      tierlistToDelete: ''
    }
  },
  components: {
    TierlistTable,
    TierlistSelection
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
          this.tierlistToAdd = '';
          this.refresh();
      } catch(e) {
        console.log(`Error adding new tierlist: ${e.message}`);
      }
    },
    async deleteTierlist(e) {
      e.preventDefault();
      if (confirm(`Are you really sure you want to delete tierlist ${this.tierlistToDelete}?`)) {
        try {
          const tierlists = await this.fetchTierlists();
          const toDelete = tierlists.find(tierlist => tierlist.name == this.tierlistToDelete);
          fetch(`http://localhost:3000/tierlists/${toDelete.id}`, {
            method: "DELETE",
          });
          alert(`Successfully deleted tierlist ${this.tierlistToDelete}!`);
          this.refresh();
      } catch(e) {
        console.log(`Error deleting tierlist: ${e.message}`);
      }
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

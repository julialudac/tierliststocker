<template>
  <div>
    <table v-show="elementRanks.length > 0">
    <tbody>
      <TierlistRow v-for="(tierAndElements, rIndex) in elementRanks" 
                  :key="rIndex" 
                  :tierAndElements="tierAndElements"
                  @new-item-submitted="addNewItem"
                  @delete-item="deleteItem"              
      />
    </tbody>
  </table>
  <p v-show="elementRanks.length == 0">Please wait. Your tierlist is coming soon...</p>
  </div>
</template>

<script>
import TierlistRow from '../components/TierlistRow'

export default {
  name: 'TierlistTable',
  components: {
    TierlistRow
  },
  props: {
    tierlistName: String
  },
  watch: {
    tierlistName: function(newVal, oldVal) {
      console.log(`Switch tierlist from ${oldVal} to ${newVal}`);
      this.refresh();
    }
  },
  data() {
    return {
      elementRanks: []
    }
  },
  created() {
    this.refresh();
  },
  methods: {
    async refresh() {
      // this.tierlistName can be empty at this time, because the parent feeds a value that is not yet filled (async operations are culprit!)
      if (this.tierlistName == '') {
        console.log('There is no selected tierlist table. We just have to wait for the value to be loaded.');
      } else {
        this.elementRanks = await this.getCurrentTierlistElements();
      }
    },
    async fetchTierlistFromDB() { 
      const res = await fetch('http://localhost:3000/tierlists');
      let tierlistsFromDB = await res.json();
      const tierlistFromDB = tierlistsFromDB.find(val => val.name == this.tierlistName);
      return tierlistFromDB;
    },
    async getCurrentTierlistElements() {
      // remember that in the DB tierlists are stored in a list as an object with an id, a name and its actual content
      return this.dbDataToVueData((await this.fetchTierlistFromDB()).content);
    },
    // format the fetched data so it can be v-for-ed
    dbDataToVueData(dbData) {
      const rankColor = {
        S: 'red',
        A: 'orange',
        B: 'yellow',
        C: 'lightgreen',
        D: 'lightblue',
        E: 'purple',
        F: 'magenta'
      };
      return Object.keys(dbData).map(rank => {
        return { 
          rank: rank,
          elements: dbData[rank],
          headColor: rankColor[rank] 
        }
      });
    },
    async addNewItem(itemWithRank) {
      console.log(`New item to be added of rank ${itemWithRank.rank}: ${itemWithRank.item}`);
      let tierlist = await this.fetchTierlistFromDB();
      tierlist['content'][itemWithRank.rank].push(itemWithRank.item);
      try {
        await fetch(`http://localhost:3000/tierlists/${tierlist.id}`, {
          method: 'PUT',
          headers: {'Content-type': 'application/json'},
          body: JSON.stringify(tierlist)
        });
        this.elementRanks = this.dbDataToVueData(tierlist.content);
      } catch(e) {
        console.log('Error adding item:', e);
      }
    },
    async deleteItem(itemWithRank) {
      console.log(`Item to delete of rank ${itemWithRank.rank}: ${itemWithRank.item}`);
      let tierlist = await this.fetchTierlistFromDB();
      tierlist['content'][itemWithRank.rank] = tierlist['content'][itemWithRank.rank].filter(item => item != itemWithRank.item);
      try {
        await fetch(`http://localhost:3000/tierlists/${tierlist.id}`, {
          method: 'PUT',
          headers: {'Content-type': 'application/json'},
          body: JSON.stringify(tierlist)
        });
        this.elementRanks = this.dbDataToVueData(tierlist.content);
      } catch(e) {
        console.log('Error deleting item:', e);
      }
    }
  }
}
</script>

<style scoped>
table {
  width: 80%;
  border-collapse: collapse;
}
.ok {
  background-color: lightgreen;
}
</style>
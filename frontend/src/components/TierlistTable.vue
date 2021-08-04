<template>
  <table>
    <tbody>
      <TierlistRow v-for="(tierAndElements, rIndex) in elementRanks" 
                  :key="rIndex" 
                  :tierAndElements="tierAndElements"
                  @new-item-submitted="addNewItem"
                  @delete-item="deleteItem"              
      />
    </tbody>
  </table>
</template>

<script>
import TierlistRow from '../components/TierlistRow'

export default {
  name: 'TierlistTable',
  components: {
    TierlistRow
  },
  data() {
    return {
      elementRanks: []
    }
  },
  async created() {
    this.elementRanks = await this.getCurrentTierlistElements();
  },
  methods: {
    async fetchDBElements() {
      const res = await fetch('http://localhost:3000/rankAndElements');
      const dbData = await res.json();
      return dbData;
    },
    async getCurrentTierlistElements() {
      return this.dbDataToVueData(await this.fetchDBElements());
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
    async addNewItem(rankAndItem) {
      console.log(`New item to be added of rank ${rankAndItem.rank}: ${rankAndItem.item}`);
      const dbData = await this.fetchDBElements();
      dbData[rankAndItem.rank].push(rankAndItem.item);
      try {
        await fetch('http://localhost:3000/rankAndElements', {
          method: 'PUT',
          headers: {'Content-type': 'application/json'},
          body: JSON.stringify(dbData)
        });
        this.elementRanks = this.dbDataToVueData(dbData);
      } catch(e) {
        console.log('Error adding item:', e);
      }
    },
    async deleteItem(itemWithRank) {
      console.log(`Item to delete of rank ${itemWithRank.rank}: ${itemWithRank.item}`);
      const dbData = await this.fetchDBElements();
      dbData[itemWithRank.rank] = dbData[itemWithRank.rank].filter(item => item != itemWithRank.item);
      try {
        await fetch('http://localhost:3000/rankAndElements', {
          method: 'PUT',
          headers: {'Content-type': 'application/json'},
          body: JSON.stringify(dbData)
        });
        this.elementRanks = this.dbDataToVueData(dbData);
      } catch(e) {
        console.log('Error removing item:', e);
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
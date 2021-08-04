<template>
  <table>
    <tbody>
      <TierlistRow v-for="(tierAndElements, rIndex) in elementRanks" :key="rIndex" :tierAndElements="tierAndElements"/>
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
    this.elementRanks = await this.fetchTierListElements();
  },
  methods: {
    async fetchTierListElements() {
      const res = await fetch('http://localhost:3000/rankAndElements');
      const dbData = await res.json();
      return this.dbDataToVueData(dbData);
    },
    // format the fetched data so it can be v-for-ed
    dbDataToVueData(dbData) {
      console.log(`dbData: ${JSON.stringify(dbData)}`);
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
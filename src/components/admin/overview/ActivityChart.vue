<template>
  <canvas ref="myGraph" id="myChart" height="150"></canvas>
</template>

<script>
export default {
  data() {
    return {
      myChart: {},
    };
  },
  methods: {
    async loadData() {
      try {
        const labels = ['January', 'February', 'March', 'April', 'May', 'June'];
        const data = {
          labels: labels,
          datasets: [
            {
              label: 'My First dataset',
              backgroundColor: 'rgb(0, 0, 0)',
              borderColor: 'rgb(0, 0, 0)',
              data: [0, 10, 5, 2, 20, 30, 45],
            },
          ],
        };

        const config = {
          type: 'line',
          data: data,
          options: {},
        };

        this.myChart = new Chart(this.$refs.myGraph, config);
      } catch (e) {
        console.log(e);
      }
    },
  },
  mounted() {
    this.loadData();
  },
};
</script>

<style>
</style>
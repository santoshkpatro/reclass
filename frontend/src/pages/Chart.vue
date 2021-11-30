<template>
    <div>
        <div>Hey there</div>
        <div ref="chart"></div>
    </div>
</template>

<script>
import { Chart } from 'frappe-charts/dist/frappe-charts.min.esm'
export default {
    data() {
        return {
            data: {},
            chart: null,
        }
    },
    mounted() {
        this.data = {
            labels: [
                '12am-3am',
                '3am-6pm',
                '6am-9am',
                '9am-12am',
                '12pm-3pm',
                '3pm-6pm',
                '6pm-9pm',
                '9am-12am',
            ],
            datasets: [
                {
                    name: 'Some Data',
                    type: 'bar',
                    values: [25, 40, 30, 35, 8, 52, 17, -4],
                },
                {
                    name: 'Another Set',
                    type: 'line',
                    values: [25, 50, -10, 15, 18, 32, 27, 14],
                },
            ],
        }
        this.chart = new Chart(this.$refs.chart, {
            // or a DOM element,
            // new Chart() in case of ES6 module with above usage
            title: 'My Awesome Chart',
            data: this.data,
            type: 'axis-mixed', // or 'bar', 'line', 'scatter', 'pie', 'percentage'
            height: 250,
            colors: ['#7cd6fd', '#743ee2'],
        })
    },
}
</script>

<style></style>

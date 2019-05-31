<template>
  <div>
    <el-tabs v-model="activeTabName">
      <el-tab-pane label="All Booking" name="all" lazy></el-tab-pane>
      <el-tab-pane label="Jan Booking" name="month" lazy></el-tab-pane>
      <el-tab-pane label="My Booking" name="my" lazy></el-tab-pane>
    </el-tabs>
    <component v-bind:is="activeTabName" :tabName="activeTabName"></component>
  </div>
</template>

<script>
import all from './BookingList'
import month from './BookingList'
import my from './BookingList'

export default {
  components: { all, month, my },
  data() {
    return {
      activeTabName: 'all',
      all: 'all',
      month: 'month',
      my: 'my'
    };
  },
  methods: {
  },
}
</script>
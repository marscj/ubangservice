<template>
  <div>
    <el-tabs v-model="activeTabName">
      <el-tab-pane label="All Booking" name="all" lazy></el-tab-pane>
      <!-- <el-tab-pane :label="monthTitle" name="month" lazy></el-tab-pane> -->
      <el-tab-pane label="My Booking" name="my" lazy></el-tab-pane>
      <el-tab-pane label="Users" name="user" lazy></el-tab-pane>
      <el-tab-pane label="Vehicle" name="vehicle" lazy></el-tab-pane>
      <el-tab-pane label="Guide" name="guide" lazy></el-tab-pane>
      <!-- <el-tab-pane label="Roles" name="role" lazy></el-tab-pane> -->
    </el-tabs>
    <component v-bind:is="activeTabName" :tabName="activeTabName" :query="get_queryset()"></component>
  </div>
</template>

<script>
import all from './BookingList'
import month from './BookingList'
import my from './BookingList'
import user from './UserList'
import role from './RoleList'
import vehicle from './VehicleList';
import guide from './GuideList'

export default {
  components: { all, my, user, vehicle, guide },
  data() {
    return {
      activeTabName: 'all',
      all: 'all',
      month: 'month',
      my: 'my',
      user: 'user',
      role: 'role',
      vehicle: 'vehicle',
      guide: 'guide',
      monthTitle: this.$moment().format('MMM') + ' Booking'
    };
  },
  methods: {
    get_queryset: function() {
      switch(this.activeTabName) {
        case 'all':
          return {
            page: 1,
            limit: 20,
            search: '',
            start_time: '',
            end_time: '',
            status: '',
            create_by: undefined
          }
        case 'month':
          return {
            page: 1,
            limit: 20,
            search: '',
            status: '',
            create_by: undefined,
            start_time: this.$moment().startOf('month').format(),
            end_time: this.$moment().endOf('month').format()
          }
        case 'my':
          return {
            page: 1,
            limit: 20,
            search: '',
            start_time: '',
            end_time: '',
            status: '',
            creator_by: this.$store.getters.user.id
          }
        case 'user':
          return {
            page: 1,
            limit: 20,
            search: undefined,
            company: this.$store.getters.user.company.id
          }
      }
    }
  },
}
</script>
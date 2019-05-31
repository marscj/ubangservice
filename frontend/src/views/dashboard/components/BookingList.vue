<template>
  <el-table :data="list" style="width: 100%;padding-top: 15px; margin-left:8px;">
    <el-table-column label="Booking_No" min-width="200">
      <template slot-scope="scope">
        {{ scope.row.bookingId }}
      </template>
    </el-table-column>
    <el-table-column label="Creator" width="200px" align="center">
      <template slot-scope="scope">
        {{ scope.row.create_by.name || scope.row.create_by.username }}
      </template>
    </el-table-column>
    <el-table-column label="Vehicle" width="200px" align="center">
      <template slot-scope="scope">
        {{ scope.row.vehicle.traffic_plate_no }}
      </template>
    </el-table-column>
    <el-table-column label="Status" width="120px" align="center">
      <template slot-scope="{row}">
        <el-tag :type="row.status | statusFilter">
          {{ row.status }}
        </el-tag>
      </template>
    </el-table-column> 
  </el-table>
</template>

<script>
import { getDashboard } from '@/api/booking'

export default {
  filters: {
    statusFilter(status) {
      const statusMap = {
        Created: 'success',
        Cancel: 'danger',
        Process: 'warning',
        Complete: 'primary'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      list: null
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      getDashboard().then(response => {
        this.list = response.data
      })
    }
  }
}
</script>

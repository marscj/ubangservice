<template>
    <div>
      <div class="filter-container">
        <el-input v-model="query.search" placeholder="" style="width: 240px" class="filter-item" @keyup.enter.native="handleFilter" />
        <el-button type="primary" @click="loadVehicles" class="filter-item">Search</el-button>
      </div>
      <el-table
        :key="tableKey"
        v-loading="vehicleLoading"
        :data="vehicleList"
        border 
        stripe
        fit
        highlight-current-row
        style="width: 100%;"
      >
        <el-table-column label="Traffic Number" align="center" min-width="120px">
          <template slot-scope="{row}">
            <span>{{ row.traffic_plate_no }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Brand" align="center" width="120px">
          <template slot-scope="{row}">
            <span>{{ row.model.brand.name }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Model" align="center" min-width="120px">
          <template slot-scope="{row}">
            <span>{{ row.model.name }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Year" align="center" width="120px">
          <template slot-scope="{row}">
            <span>{{ row.model.year }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Type" align="center" width="120px">
          <template slot-scope="{row}">
            <span>{{ row.model.type }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Category" align="center" min-width="120px">
          <template slot-scope="{row}">
            <span>{{ row.model.category }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Passengers" align="center" width="120px">
          <template slot-scope="{row}">
            <span>{{ row.model.passengers }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Average Score" width="130px" align="center">
          <template slot-scope="{row}">
            <span>{{ row.avg_score }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Total Score" width="130px" align="center">
          <template slot-scope="{row}">
            <span>{{ row.total_score }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Active" width="130px" align="center">
          <template slot-scope="{row}">
            <el-checkbox v-model="row.is_actived" disabled></el-checkbox>
          </template>
        </el-table-column>
      </el-table>
      <pagination v-show="total>0" :total="total" :page.sync="query.page" :limit.sync="query.limit" @pagination="loadVehicles" />
    </div>
</template>

<script>

import { getModels, getVehicles } from '@/api/vehicle'
import Pagination from '@/components/Pagination'

export default {
  components: { Pagination },
  data() {
    return {
      tableKey: 0,
      total: 0,
      query: {
        model: undefined,
        limit: 20,
        page: 1,
        search: undefined
      },
      vehicleList: [],
      modelLoading: false,
      vehicleLoading: false,
    }
  },
  created() {
    this.loadVehicles()
  },
  methods: {
    loadVehicles() {
      this.vehicleLoading = true
      this.vehicleList = []
      getVehicles(this.query).then(response => {
        this.vehicleList = response.data.items
        this.total = response.data.total
        this.vehicleLoading = false
      }).catch(error => {
        this.vehicleLoading = false
      })
    },
    handleFilter() {
      this.query.page = 1
      this.vehicleList = []
      this.loadVehicles()
    }
  },
}
</script>

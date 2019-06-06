<template>
    <div>
      <div class="filter-container">
        <el-select 
          v-model="query.model"
          reserve-keyword 
          clearable
          :loading="modelLoading"
          placeholder="Vehicle Model"
          @change="loadVehicles"
          class="filter-item">
          <el-option
            v-for="item in modelOptions"
            :key="item.id"
            :label="item.name"
            :value="item.id">
          </el-option>
        </el-select>
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
        <el-table-column label="Brand" align="center" width="120px">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectVechicleHandle(row)">{{ row.model.brand.name }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Model" align="center" width="160px">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectVechicleHandle(row)">{{ row.model.name }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Year" align="center" width="120px">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectVechicleHandle(row)">{{ row.model.year }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Type" align="center" width="120px">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectVechicleHandle(row)">{{ row.model.type }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Category" align="center" width="120px">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectVechicleHandle(row)">{{ row.model.category }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Passengers" align="center" width="120px">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectVechicleHandle(row)">{{ row.model.passengers }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Average Score" width="130px" align="center">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectVechicleHandle(row)">{{ row.avg_score }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Total Score" width="130px" align="center">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectVechicleHandle(row)">{{ row.total_score }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Traffic Number" align="center" min-width="120px">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectVechicleHandle(row)">{{ row.traffic_plate_no }}</span>
          </template>
        </el-table-column>
      </el-table>
    </div>
</template>

<script>

import { getModels, getVehicles } from '@/api/vehicle'

export default {
  data() {
    return {
      tableKey: 0,
      query: {
        model: undefined,
        is_actived: true
      },
      modelOptions: [],
      vehicleList: [],
      modelLoading: false,
      vehicleLoading: false,
    }
  },
  created() {
    this.loadModel()
  },
  methods: {
    loadModel() {
      if(this.modelOptions.length === 0){
        this.modelLoading = true
        getModels().then(response => {
          this.modelLoading = false
          this.modelOptions = response.data
        }).catch(err => {
          this.modelLoading = false
        })
      }
    },
    loadVehicles() {
      this.vehicleLoading = true
      this.vehicleList = []
      getVehicles(this.query).then(response => {
        this.vehicleList = response.data
        this.vehicleLoading = false
      }).catch(error => {
        this.vehicleLoading = false
      })
    },
  },
}
</script>

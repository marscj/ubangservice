<template>
  <div>
    <div class="filter-container">
      <el-button type="primary" @click="loadGuides" class="filter-item">Refresh</el-button>
    </div>
    <el-table :data="list"
    :key="tableKey"
    v-loading="loading"
    border 
    stripe
    fit
    highlight-current-row
    style="width: 100%;"
    >
    <el-table-column label="UserName" align="center" width="180px">
        <template slot-scope="{row}">
        <span class="link-type" @click="selectGuideHandle(row)">{{ row.username }}</span>
        </template>
    </el-table-column>
    <el-table-column label="Name" align="center" width="120px">
        <template slot-scope="{row}">
        <span class="link-type" @click="selectGuideHandle(row)">{{ row.name }}</span>
        </template>
    </el-table-column>
    <el-table-column label="Phone" width="120px" align="center" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
        <span class="link-type" @click="selectGuideHandle(row)">{{ row.phone }}</span>
        </template>
    </el-table-column>
    <el-table-column label="Company" width="200px" align="center">
        <template slot-scope="{row}">
        <span v-if="row.company" class="link-type" @click="selectGuideHandle(row)">{{ row.company.name }}</span>
        </template>
    </el-table-column>
    <el-table-column label="Average Score" width="130px" align="center">
        <template slot-scope="{row}">
        <span class="link-type" @click="selectGuideHandle(row)">{{ row.avg_score }}</span>
        </template>
    </el-table-column>
    <el-table-column label="Total Score" width="130px" align="center">
        <template slot-scope="{row}">
        <span class="link-type" @click="selectGuideHandle(row)">{{ row.total_score }}</span>
        </template>
    </el-table-column>
    <el-table-column label="Introduction" min-width="150px" align="center">
        <template slot-scope="{row}">
        <span class="link-type" @click="selectGuideHandle(row)">{{ row.introduction }}</span>
        </template>
    </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { getUsers } from '@/api/user'

export default {
  data() {
    return {
      query: {
        is_actived: true,
        is_tourguide: true
      },
      list: [],
      loading: false
    }
  },
  created() {
    this.loadGuides()
  },
  methods: {
    loadGuides() {
      this.loading = true
      this.list = []
      getUsers(this.query).then(response => {
        this.list = response.data
        this.loading = false
      }).catch(error => {
        this.loading = false
      })
    }
  },
}
</script>

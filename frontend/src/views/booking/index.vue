<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.search" placeholder="id " style="width: 240px" class="filter-item" @keyup.enter.native="handleFilter" />
      
      <el-date-picker class="filter-item" v-model="listQuery.start_time" type="datetime" format="yyyy-MM-dd HH:mm" placeholder="Start Time:" />
      <el-date-picker class="filter-item" v-model="listQuery.end_time" type="datetime" format="yyyy-MM-dd HH:mm" placeholder="End Time:" />

      <el-select class="filter-item" v-model="listQuery.status" placeholder="Status" clearable>
        <el-option v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
      
      <el-button class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">
        Search
      </el-button>
      <el-button class="filter-item" type="primary" icon="el-icon-edit" @click="handleCreate" >
        Add
      </el-button>
    </div>

    <el-table 
      :key="tableKey"
      :data="list"
      v-loading="listLoading" 
      border 
      stripe
      fit
      highlight-current-row
      style="width: 100%;"
      @sort-change="sortChange"
    >
      <el-table-column label="OrderId" width="120px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.orderId }}</span>
        </template>
      </el-table-column>
      
    </el-table>
    
    
  </div>
</template>

<script>
import { getBookings } from '@/api/booking'

const Status = [
  { value: 0, label: 'Darft'},
  { value: 1, label: 'Confirm'},
  { value: 2, label: 'Cancel'},
]

export default {
  data() {
    return {
      tableKey: 0,
      list: null,
      listLoading: true,
      listQuery: {
        page: 1, 
        limit: 20,
        search: undefined,
        start_time: undefined,
        end_time: undefined,
        status: undefined
      },
      options: Status
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      getBookings(this.listQuery).then( response => {
        console.log(response)
        this.list = response.data.items
        this.total = response.data.total
        this.listLoading = false
      }).catch(() => {
        this.listLoading = false
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      this.getList()
    },
    handleCreate() {},
    sortChange() {}
  }
}
</script>

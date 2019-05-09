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
      <el-table-column label="BookingId" width="180px" align="center">
        <template slot-scope="{row}">
          <router-link :to="'/booking/edit/'+row.id" class="link-type">
            <span>{{ row.bookingId }}</span>
          </router-link>
        </template>
      </el-table-column>
      <el-table-column label="Start Time" width="160px" align="center">
        <template slot-scope="{row}">
          <router-link :to="'/booking/edit/'+row.id" class="link-type">
            <span>{{ row.start_time }}</span>
          </router-link>
        </template>
      </el-table-column>
      <el-table-column label="End Time" width="160px" align="center">
        <template slot-scope="{row}">
          <router-link :to="'/booking/edit/'+row.id" class="link-type">
            <span>{{ row.end_time }}</span>
          </router-link>
        </template>
      </el-table-column>
      <el-table-column label="Create at" width="160px" align="center">
        <template slot-scope="{row}">
          <router-link :to="'/booking/edit/'+row.id" class="link-type">
            <span>{{ row.change_at }}</span>
          </router-link>
        </template>
      </el-table-column>
      <el-table-column label="Change at" width="160px" align="center">
        <template slot-scope="{row}">
          <router-link :to="'/booking/edit/'+row.id" class="link-type">
            <span>{{ row.change_at }}</span>
          </router-link>
        </template>
      </el-table-column>
      <el-table-column label="Vehicle" width="120px" align="center">
        <template slot-scope="{row}">
          <router-link :to="'/booking/edit/'+row.id" class="link-type">
            <span v-if=row.vehicle>{{ row.vehicle.traffic_plate_no }}</span>
          </router-link>          
        </template>
      </el-table-column>
      <el-table-column label="Guide" width="120px" align="center">
        <template slot-scope="{row}">
          <router-link :to="'/booking/edit/'+row.id" class="link-type">
            <span v-if=row.guide>{{ row.guide.name || row.guide.username }}</span>
          </router-link>          
        </template>
      </el-table-column>
      <el-table-column label="Remark" min_width="240px" align="center">
        <template slot-scope="{row}">
          <router-link :to="'/booking/edit/'+row.id" class="link-type">
            <span v-if=row.remark>{{ row.remark }}</span>
          </router-link>          
        </template>
      </el-table-column>
      <el-table-column label="Status" width="100px" class-name="status-col" align="center">
        <template slot-scope="{row}">
          <el-tag :type="row.status | typeStatus">
            {{ row.status | transStatus }}
          </el-tag>          
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
  filters: {
    transStatus(status) {
      const statusMap = {
        0: 'Darft',
        1: 'Confirm',
        2: 'Cancel',
        3: 'Delete'
      }
      return statusMap[status]
    },
    typeStatus(status) {
      const statusMap = {
        0: 'info',
        1: 'success',
        2: 'danger',
        3: 'danger'
      }
      return statusMap[status]
    },
  },
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

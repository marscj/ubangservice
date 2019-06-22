<template>
  <div>
    <div class="filter-container">
      <el-input v-model="listQuery.search" placeholder="" style="width: 240px" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-date-picker v-model="listQuery.start_time" class="filter-item" type="datetime" format="yyyy-MM-dd HH:mm" placeholder="Start Time:" />
      <el-date-picker v-model="listQuery.end_time" class="filter-item" type="datetime" format="yyyy-MM-dd HH:mm" placeholder="End Time:" />
      <el-select v-model="listQuery.status" class="filter-item" placeholder="Status" clearable @change="handleFilter">
        <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value" />
      </el-select>
      <el-button class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">
        Search
      </el-button>
      <el-button class="filter-item" type="primary" icon="el-icon-edit" @click="handleCreate">
        Add
      </el-button>
    </div>
    <el-table
      :key="tableKey"
      v-loading="listLoading"
      :data="list"
      border
      stripe
      fit
      highlight-current-row
      style="width: 100%;"
      row-key="id"
    >
      <el-table-column prop="bookingId" label="BookingId" width="220px" align="center">
        <template slot-scope="{row}">
          <router-link  :to="'/booking/edit/'+ row.id" class="link-type">
            <span>{{ row.bookingId }}</span>
          </router-link>
        </template>
      </el-table-column>
      <el-table-column prop="confirmId" label="ConfirmId" width="220px" align="center">
        <template slot-scope="{row}">
          <router-link  :to="'/booking/edit/'+ row.id" class="link-type">
            <span>{{ row.confirmId }}</span>
          </router-link>
        </template>
      </el-table-column>
      <el-table-column label="Start Time" width="160px" align="center">
        <template slot-scope="{row}">
          <router-link :to="'/booking/edit/'+row.id" class="link-type">
            <span>{{ row.start_time | moment("YYYY-MM-DD HH:mm") }}</span>
          </router-link>
        </template>
      </el-table-column>
      <el-table-column label="End Time" width="160px" align="center">
        <template slot-scope="{row}">
          <router-link :to="'/booking/edit/'+row.id" class="link-type">
            <span>{{ row.end_time | moment("YYYY-MM-DD HH:mm") }}</span>
          </router-link>
        </template>
      </el-table-column>
      <el-table-column label="Creator" min-width="120px" align="center">
        <template slot-scope="{row}">
          <router-link :to="'/booking/edit/'+row.id" class="link-type">
            <span v-if="row.create_by">{{ row.create_by.name || row.create_by.username }}</span>
          </router-link>
        </template>
      </el-table-column>
      <el-table-column label="Vehicle" min-width="120px" align="center">
        <template slot-scope="{row}">
          <router-link :to="'/booking/edit/'+row.id" class="link-type">
            <span v-if="row.vehicle">{{ row.vehicle.traffic_plate_no }}</span>
          </router-link>
        </template>
      </el-table-column>
      <el-table-column label="Driver" min-width="140px" align="center">
        <template slot-scope="{row}">
          <router-link :to="'/booking/edit/'+row.id" class="link-type">
            <span v-if="row.vehicle&&row.vehicle.driver">{{ row.vehicle.driver.username }}</span>
            <br>
            <span v-if="row.vehicle&&row.vehicle.driver">{{row.vehicle.driver.phone}}</span>
          </router-link>
        </template>
      </el-table-column>
      <el-table-column label="Guide" min-width="120px" align="center">
        <template slot-scope="{row}">
          <router-link :to="'/booking/edit/'+row.id" class="link-type">
            <span v-if="row.guide">{{ row.guide.name || row.guide.username }}</span>
          </router-link>
        </template>
      </el-table-column>
      <el-table-column label="Status" width="100px" class-name="status-col" align="center">
        <template slot-scope="{row}">
          <el-tag :type="row.status | typeStatus">
            {{ row.status }}
          </el-tag>
        </template>
      </el-table-column>
    </el-table>
    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />
  </div>
</template>

<script>
import { getBookings } from '@/api/booking'
import Pagination from '@/components/Pagination'

const Status = [
  { value: 'Created', label: 'Created' },
  { value: 'Process', label: 'Process' },
  { value: 'Complete', label: 'Complete' },
  { value: 'Cancel', label: 'Cancel' },
  { value: 'Delete', label: 'Delete' }
]

export default {
  components: { Pagination },
  props: {
    query: {
      type: Object,
      default: {
        page: 1,
        limit: 20,
        search: undefined,
        start_time: undefined,
        end_time: undefined,
        status: undefined,
        create_by: undefined
      }
    }
  },
  filters: {
    typeStatus(status) {
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
      tableKey: 0,
      total: 0,
      list: null,
      listLoading: true,
      options: Status,
      listQuery: Object.assign({}, this.query)
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      getBookings(this.listQuery).then(response => {
        this.list = response.data.items
        this.total = response.data.total
        this.listLoading = false
      }).catch(() => {
        this.listLoading = false
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      this.listQuery.list = null
      this.getList()
    },
    handleCreate() {
      this.$router.push({ path: '/booking/create/' })
    },
    mounted() {
    },
  }
}
</script>

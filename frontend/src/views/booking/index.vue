<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.search" placeholder="id " style="width: 240px" class="filter-item" @keyup.enter.native="handleFilter" />
      
      <el-date-picker class="filter-item" v-model="listQuery.start_time" type="datetime" format="yyyy-MM-dd HH:mm:ss" placeholder="Start Time:" />
      <el-date-picker class="filter-item" v-model="listQuery.end_time" type="datetime" format="yyyy-MM-dd HH:mm:ss" placeholder="End Time:" />

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
  </div>
</template>

<script>

const Status = [
  { value: 0, label: 'Darft'},
  { value: 1, label: 'Confirm'},
  { value: 2, label: 'Cancel'},
]

export default {
  data() {
    return {
      listQuery: {
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
    getList() {},
    handleFilter() {},
    handleCreate() {}
  }
}
</script>

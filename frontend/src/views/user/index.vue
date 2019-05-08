<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.search" placeholder="username name phone email" style="width: 240px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-select v-model="options" multiple placeholder="Type" clearable class="filter-item" style="width: 180px" @change="handleFilter">
        <el-option v-for="item in TypeOptions" :key="item.value" :label="item.label" :value="item.value" />
      </el-select>
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">
        Search
      </el-button>
      <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreate">
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
      @sort-change="sortChange"
    >
      <el-table-column label="ID" prop="id" sortable="custom" align="center" width="60">
        <template slot-scope="{row}">
          <span>{{ row.id }}</span>
        </template>
      </el-table-column>
      <el-table-column label="UserName" align="center" width="180">
        <template slot-scope="{row}">
          <span>{{ row.username }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Name" align="center" width="120">
        <template slot-scope="{row}">
          <span class="link-type" @click="handleUpdate(row)">{{ row.name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Phone" width="120" align="center" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <span class="link-type" @click="handleUpdate(row)">{{ row.phone }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Email" width="180" align="center" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <span class="link-type" @click="handleUpdate(row)">{{ row.email }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Company" width="200px" align="center">
        <template slot-scope="{row}">
          <span v-if=row.company class="link-type" @click="handleUpdate(row)">{{ row.company.name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Introduction" min-width="150px">
        <template slot-scope="{row}">
          <span class="link-type" @click="handleUpdate(row)">{{ row.introduction }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Driver" width="80" align="center">
        <template slot-scope="{row}">
          <el-checkbox v-model="row.is_driver" @change="handleChangeStatus(row, 'is_driver')" />
        </template>
      </el-table-column>
      <el-table-column label="Guide" width="80" align="center" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <el-checkbox v-model="row.is_tourguide" @change="handleChangeStatus(row, 'is_tourguide')" />
        </template>
      </el-table-column>
      <el-table-column label="Active" align="center" width="80" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <el-checkbox v-model="row.is_actived" @change="handleChangeStatus(row, 'is_actived')" />
        </template>
      </el-table-column>
      <el-table-column label="Actions" align="center" width="100" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <el-button type="primary" size="mini" @click="handleUpdate(row)">
            Edit
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />
    
    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :rules="rules" :model="temp" label-position="left" label-width="100px" style="width: 400px; margin-left:50px;">
        <el-form-item label="Name" prop="name">
          <el-input v-model="temp.name" />
        </el-form-item>
        <el-form-item label="Phone" prop="phone">
          <el-input v-model="temp.phone" />
        </el-form-item>
        <el-form-item label="email" prop="email">
          <el-input v-model="temp.email" />
        </el-form-item>
        <el-form-item label="introduction" prop="introduction">
          <el-input v-model="temp.introduction" />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">
          Cancel
        </el-button>
        <el-button type="primary" @click="dialogStatus==='create'?createData():updateData()">
          Confirm
        </el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { getUsers, updateUser } from '@/api/user'
import waves from '@/directive/waves'
import { parseTime } from '@/utils'
import Pagination from '@/components/Pagination'

const TypeOptions = [
  { value: 'driver', label: 'Driver' }, 
  { value: 'guide', label: 'Guide' }
]

export default {
  components: { Pagination },
  directives: { waves },
  data() {
    return {
      tableKey: 0,
      list: null,
      total: 0,
      listLoading: true,
      options: undefined,
      listQuery: {
        page: 1,
        limit: 20,
        search: undefined,
        is_driver: undefined,
        is_tourguide: undefined,
        sort: 'id'
      },
      temp: {
        id: undefined,
        name: '',
        phone: '',
        email: '',
        introduction: ''
      },
      textMap: {
        update: 'Edit',
        create: 'Create'
      },
      dialogFormVisible: false,
      dialogStatus: '',
      rules: {},
      TypeOptions
    }
  },
  created() {
    this.getList()
  },
  methods: {
    getList() {
      this.listLoading = true
      getUsers(this.listQuery).then(response => {
        this.list = response.data.items
        this.total = response.data.total
        this.listLoading = false
      }).catch(() => {
        this.listLoading = false
      })
    },
    handleFilter() {
      this.listQuery.page = 1

      if(this.options.includes('driver')){
        this.listQuery.is_driver = true
      } else {
        this.listQuery.is_driver = undefined
      }

      if(this.options.includes('guide')){
        this.listQuery.is_tourguide = true
      } else {
        this.listQuery.is_tourguide = undefined
      }

      console.log(this.listQuery.is_driver, this.listQuery.is_tourguide)
      console.log(this.options)

      this.getList()
    },
    handleChangeStatus(row, key) {
      this.listLoading = true
      var context = {
        id: row.id,
        username: row.username
      }
      context[key] = row[key]
      updateUser(row.id, context).then(response => {
        this.listLoading = false

        this.$notify({
          title: 'Success',
          message: 'Change Successfully',
          type: 'success',
          duration: 2000
        })
      }).catch(() => {
        row[key] = !row[key]
        this.listLoading = false
      })
    },
    sortChange(data) {
      const { prop, order } = data
      if (prop === 'id') {
        this.sortByID(order)
      }
    },
    sortByID(order) {
      if (order === 'ascending') {
        this.listQuery.sort = 'id'
      } else {
        this.listQuery.sort = '-id'
      }
      this.handleFilter()
    },
    resetTemp() {
      this.temp = {
        id: undefined,
        name: '',
        phone: '',
        email: '',
        introduction: ''
      }
    },
    handleCreate() {
      this.resetTemp()
      this.dialogStatus = 'create'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    handleUpdate(row) {
      console.log(row.id)
      this.temp = Object.assign({}, {
        id: row.id,
        username: row.username,
        name: row.name,
        email: row.email,
        phone: row.phone,
        introduction: row.introduction
      })
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.temp)
          updateUser(tempData.id, tempData).then(() => {
            for (const v of this.list) {
              if (v.id === this.temp.id) {
                const index = this.list.indexOf(v)
                this.list.splice(index, 1, this.temp)
                break
              }
            }
            this.dialogFormVisible = false
            this.$notify({
              title: 'Success',
              message: 'Update Successfully',
              type: 'success',
              duration: 2000
            })
          })
        }
      })
    }
  }
}
</script>

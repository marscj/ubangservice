<template>
  <div>
    <!-- <div class="filter-container">
      <el-input v-model="listQuery.search" placeholder="username name phone email" style="width: 240px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">
        Search
      </el-button>
      <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreate">
        Add
      </el-button>
    </div> -->

    <el-table
      :key="tableKey"
      :data="list"
      v-loading="listLoading"
      border
      stripe
      fit
      highlight-current-row
    >
      <el-table-column label="UserName" align="center" width="180px">
        <template slot-scope="{row}">
          <!-- <span class="link-type" @click="handleUpdate(row)">{{ row.username }}</span> -->
          <span>{{ row.username }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Name" align="center" width="120px">
        <template slot-scope="{row}">
          <span>{{ row.name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Phone" width="120px" align="center" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <span>{{ row.phone }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Email" width="180px" align="center" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <span>{{ row.email }}</span>
        </template>
      </el-table-column>
      <!-- <el-table-column label="Role" min-width="180px" align="center" class-name="small-padding fixed-width">
        <template slot-scope="{row}">
          <span class="link-type" @click="handleUpdate(row)">{{ userRole(row) }}</span>
        </template>
      </el-table-column> -->
    </el-table>

    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />
    
    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :rules="rules" :model="temp" label-position="left" label-width="100px" style="width: 400px; margin-left:20px;">
        <el-form-item label="UserName:" prop="username">
          <el-input v-model="temp.username" disabled/>
        </el-form-item>
        <el-form-item label="Name:" prop="name">
          <el-input v-model="temp.name" />
        </el-form-item>
        <el-form-item label="Phone:" prop="phone">
          <el-input v-model="temp.phone" />
        </el-form-item>
        <el-form-item label="Email:" prop="email">
          <el-input v-model="temp.email" />
        </el-form-item>
        <!-- <el-form-item label="Role:" prop="role">
          <el-select v-model="temp.role_id" multiple :loading="role.loading">
            <el-option
              v-for="item in role.data"
              :key="item.id"
              :label="item.name"
              :value="item.id">
            </el-option>
          </el-select>
        </el-form-item> -->
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
import { getRoles } from '@/api/role'

export default {
  components: { Pagination },
  directives: { waves },
  props: {
    query: {
      type: Object,
      default: {
        page: 1,
        limit: 20,
        search: undefined,
        company: undefined
      }
    }
  },
  data() {
    return {
      tableKey: 0,
      list: null,
      total: 0,
      listLoading: true,
      listQuery: Object.assign({}, this.query),
      temp: {
        id: undefined,
        name: undefined,
        phone: undefined,
        email: undefined,
        role_id: undefined,
        company_id: this.$store.getters.user.company.id
      },
      textMap: {
        update: 'Edit',
        create: 'Create'
      },
      dialogFormVisible: false,
      dialogStatus: '',
      rules: {},
      role: {
        data: [],
        loading: false,
        role_id: [],
      }
    }
  },
  created() {
    this.getList()
  },
  methods: {
    userRole(row){
      return row.role.map((f) => {
        return f.name
      }).join(',')
    },
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
    handleCreate() {
      this.temp = {
        id: undefined,
        name: undefined,
        phone: undefined,
        email: undefined,
        role_id: undefined,
        company_id: this.$store.getters.user.company.id
      }
      if(this.role.data.length == 0) {
        this.role.loading = true
        getRoles({
          company: this.$store.getters.user.company.id
        }).then(response => {
          this.role.data = response.data
          this.role.loading = false
        }).catch(error => {
          this.role.loading = false
        })
      }
      this.dialogStatus = 'create'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    handleUpdate(row) {
      this.temp = Object.assign({}, {
        id: row.id,
        username: row.username,
        name: row.name,
        email: row.email,
        phone: row.phone,
        role_id: row.role.map((f) => {
          return f.id
        }),
        company_id: this.$store.getters.user.company.id
      })
      if(this.role.data.length == 0) {
        this.role.loading = true
        getRoles({
          company: this.$store.getters.user.company.id
        }).then(response => {
          this.role.data = response.data
          this.role.loading = false
        }).catch(error => {
          this.role.loading = false
        })
      }
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          updateUser(this.temp.id, this.temp).then((response) => {
            const { data } = response
            for (const v of this.list) {
              if (v.id === data.id) {
                const index = this.list.indexOf(v)
                this.list.splice(index, 1, data)
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

<template>
  <div>
    <div class="filter-container">
      <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreate">
        Add
      </el-button>
    </div>
    <div>
      <el-table 
      :data="list.data"
      v-loading="list.loading"
      border 
      stripe>
        <el-table-column label="Name" align="center" width="180px">
          <template slot-scope="{row}">
            <span class="link-type" @click="handleUpdate(row)">{{ row.name }}</span>
          </template>
      </el-table-column>
      </el-table>
    </div>
    <div>
      <el-dialog
          :title="dialog.title"
          :visible.sync="dialog.visible"
          v-loading="dialog.loading"
          width="55%">
          <el-form :model="temp" ref="roleForm" label-width="80px" label-position="left" style="width: 600px; margin-left:20px;">
              <el-form-item label="Name:" prop="name">
                <el-input v-model="temp.name"></el-input>
              </el-form-item>
              <el-form-item label="Permission:" prop="permission">
                <el-transfer v-model="temp.permission" :data="permission" @change="handlePermissionChange"></el-transfer>
              </el-form-item>
          </el-form>
          
          <span slot="footer">
              <el-button @click=" dialog.visible = false">Cancel</el-button>
              <el-button type="primary" @click="updateForm">Confirm</el-button>
          </span>
      </el-dialog>
      
    </div>
  </div>
</template>

<script>
import { getRoles, getRole, updateRole, createRole } from '@/api/role'
import { getPermissions } from '@/api/permission'

export default {
  created() {
    this.getList()
  },
  data() {
    return {
      list: {
        loading: false,
        data: []
      },
      permission: [],
      listFilter: {
        company: this.$store.getters.user.company.id
      },
      dialog: {
        title: 'Edit Role',
        visible: false,
        data: undefined,
        loading: false,
      },
      temp: {
        id: undefined,
        name: '',
        permission: [],
        company: this.$store.getters.user.company.id
      }
    }
  },
  methods: {
    getList: function() {
      this.list.loading = true
      getRoles(this.listFilter).then(response => {
        this.list.loading = false
        this.list.data = response.data
      }).catch(error => {
        this.list.loading = false
      })
    },
    handleUpdate(row) {
      this.dialog.visible = true
    },
    updateForm() {
      updateRole().then(response => {
        this.dialog.visible = false
      }).catch(error => {
        this.dialog.visible = false
      })
    },
    handleCreate() {
      this.temp = {
        id: undefined,
        name: '',
        permission: [],
        company: this.$store.getters.user.company.id
      }
      this.dialog.visible = true
      if(this.permission.length == 0){
        this.dialog.loading = true
        getPermissions().then(response => {
          this.dialog.loading = false
          this.permission = response.data
        }).catch(error => {
          this.dialog.loading = false
        })
      }
      this.$nextTick(() => {
        this.$refs['roleForm'].clearValidate()
      })
    },
    createForm() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          createRole(this.temp).then(response => {
            this.dialog.visible = false
          }).catch(error => {
            this.dialog.visible = false
          })
        }
      })
    },
    handlePermissionChange(value, direction, movedKeys) {
      console.log(this.temp.permission)
    }
  },
}
</script>
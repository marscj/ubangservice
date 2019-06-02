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
          width="55%">
          
          <span slot="footer">
              <el-button @click=" dialog.visible = false">Cancel</el-button>
              <el-button type="primary" @click="updateForm()">Confirm</el-button>
          </span>
      </el-dialog>
      
    </div>
  </div>
</template>

<script>
import { getRoles, getRole, updateRole, createRole } from '@/api/role'

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
      dialog: {
        title: 'Edit Role',
        visible: false,
        data: undefined,
      },
      temp: {
        name: '',
        permission: []
      }
    }
  },
  methods: {
    getList: function() {
      this.list.loading = true
      getRoles().then(response => {
        this.list.loading = true
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
      this.dialog.visible = true
    },
    createForm() {
      createRole().then(response => {
        this.dialog.visible = false
      }).catch(error => {
        this.dialog.visible = false
      })
    }
  },
}
</script>
<template>
  <div class="dashboard-editor-container">
    <panel-group/>

    <el-row :gutter="8">
      <el-col :xs="{span: 24}" :sm="{span: 12}" :md="{span: 12}" :lg="{span: 6}" :xl="{span: 6}" style="margin-bottom:30px;">
        <company-panel />
      </el-col> 
      <el-col :xs="{span: 24}" :sm="{span: 24}" :md="{span: 24}" :lg="{span: 12}" :xl="{span: 12}" style="padding-right:8px;margin-bottom:30px;">
        <booking-list />
      </el-col>
      <!-- <el-col :xs="{span: 24}" :sm="{span: 12}" :md="{span: 12}" :lg="{span: 6}" :xl="{span: 6}" style="margin-bottom:30px;">
        <todo-list />
      </el-col>-->
    </el-row>
  </div>
</template>

<script>
import PanelGroup from './components/PanelGroup'
import BookingList from './components/BookingList'
import CompanyPanel from './components/CompanyPanel'

export default {
  name: 'Dashboard',
  components: {
    PanelGroup, BookingList, CompanyPanel
  }
}
</script>

<style lang="scss" scoped>
.dashboard-editor-container {
  padding: 16px;
  background-color: rgb(240, 242, 245);
  position: relative;
}
</style>

<template>
  <div class="createPost-container" >
    <el-form ref="postForm" :model="postForm" :rules="rules" label-position="top" label-width="120px" class="form-container">
      <sticky :z-index="10" :class-name="'sub-navbar '+postForm.status">
        <el-button v-if="isEdit" v-loading="loading" style="margin-left: 10px;" type="danger" >
          Delete
        </el-button>
        <el-button v-if="isEdit" v-loading="loading" style="margin-left: 10px;" type="warning" >
          Cancel
        </el-button>
        <el-button v-if="!isEdit" v-loading="loading" style="margin-left: 10px;" type="success" @click="createForm">
          Create
        </el-button>
        <el-button v-else v-loading="loading" style="margin-left: 10px;" type="success" @click="updateForm">
          Edit
        </el-button>
      </sticky>
      <div class="createPost-main-container" >
        <div class="bookingInfo-container" >
          <el-row :gutter="20">
            <el-col :span="16">
              <el-card>
                <el-form-item label="Start time:" prop="start_time" >
                    <el-date-picker v-model="postForm.start_time" type="datetime" value-format="yyyy-MM-dd HH:mm" format="yyyy-MM-dd HH:mm" placeholder="Select date and time" clearable/>
                </el-form-item>
                <el-form-item label="End time:" prop="end_time" >
                    <el-date-picker v-model="postForm.end_time" type="datetime" value-format="yyyy-MM-dd HH:mm" format="yyyy-MM-dd HH:mm" placeholder="Select date and time" clearable/>
                </el-form-item>
                <el-form-item label="Contact name:" prop="contact_name" style="width: 300px;" >
                    <el-input v-model="postForm.contact_name" placeholder=""></el-input>
                </el-form-item>
                <el-form-item label="Contact phone:" prop="contact_phone" style="width: 300px;" >
                    <el-input v-model="postForm.contact_phone"></el-input>
                </el-form-item>
                <el-form-item v-if="postForm.start_time && postForm.end_time" label="Vehicle:" prop="vehicle_id" style="width: 300px;" >
                    <el-input v-model="vehicle" @focus="handleVehicle" suffix-icon="el-icon-search" readonly></el-input>
                </el-form-item>
                <el-form-item v-if="postForm.start_time && postForm.end_time" label="Guide:" style="width: 30%;">
                  <el-input v-model="guide"></el-input>
                </el-form-item>
                <el-form-item label="Pick up address:">
                    <el-input v-model="postForm.pick_up_addr"></el-input>  
                </el-form-item>
                <el-form-item label="Drop off address:">
                    <el-input v-model="postForm.drop_off_addr"></el-input>  
                </el-form-item>
                <el-form-item label="Remark:">
                    <el-input v-model="postForm.remark" :autosize="{ minRows: 4, maxRows: 4}" type="textarea"></el-input>  
                </el-form-item>
              </el-card>
            </el-col>
            <el-col :span="8">
              <el-row>
                <el-card >
                  <el-form-item label="Status:">
                    <el-input v-model="postForm.status" v-if="postForm.status" disabled></el-input>
                    <el-input v-else disabled></el-input>
                  </el-form-item>
                  <el-form-item label="Order:">
                    <el-input v-model="order" disabled></el-input>
                  </el-form-item>
                  <el-form-item label="Creator:">
                    <el-input v-model="create_by" disabled></el-input>
                  </el-form-item>
                  <el-form-item label="Company:">
                    <el-input v-model="company_by" disabled></el-input>
                  </el-form-item>
                  <el-form-item label="Create at:">
                    <el-input v-model="postForm.create_at" v-if="postForm.create_at" disabled></el-input>
                    <el-input v-else disabled></el-input>
                  </el-form-item>
                  <el-form-item label="Change at:">
                    <el-input v-model="postForm.change_at" v-if="postForm.change_at" disabled></el-input>
                    <el-input v-else disabled></el-input>
                  </el-form-item>
                  <el-form-item label="Expiry date:">
                    <el-input v-model="postForm.expiry_date" v-if="postForm.expiry_date" disabled></el-input>
                    <el-input v-else disabled></el-input>
                  </el-form-item>
                  <el-form-item label="Root:">
                    <el-input v-model="parent" disabled></el-input>
                  </el-form-item>
                </el-card>
              </el-row>
            </el-col>
          </el-row>
        </div>
        <div class="itinerary-container">
          <el-row>
            <el-col >
              <el-card >
                <div slot="header">
                  <span>Itinerary</span>
                </div>
              </el-card>
            </el-col>
          </el-row>
        </div>
      </div>
    </el-form>
    <el-dialog title="Select Vehicle" :visible.sync="vehicleDialog.show" width="60%">
      <div class="filter-container">
        <el-select 
          v-model="vehicleDialog.query.model"
          reserve-keyword
          clearable
          :loading="vehicleDialog.modelLoading"
          placeholder="Vehicle Model"
          @change="handleFilterVehicle"
          class="filter-item">
          <el-option
            v-for="item in vehicleDialog.modelOptions"
            :key="item.id"
            :label="item.name"
            :value="item.id">
          </el-option>
        </el-select>
      </div>
      <el-table :data="vehicleDialog.vehicleList"
        :key="tableKey"
        :loading="vehicleDialog.vehicleLoading"
        border 
        stripe
        fit
        highlight-current-row
        style="width: 100%;"
      >
        <el-table-column label="Brand" align="center" width="120px">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectVechicleHandle(row)">{{ row.model.brand.name }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Model" align="center" width="220px">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectVechicleHandle(row)">{{ row.model.name }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Year" align="center" width="120px">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectVechicleHandle(row)">{{ row.model.year }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Type" align="center" width="120px">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectVechicleHandle(row)">{{ row.model.type }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Category" align="center" width="120px">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectVechicleHandle(row)">{{ row.model.category }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Passengers" align="center" width="120px">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectVechicleHandle(row)">{{ row.model.passengers }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Traffic Number" align="center" min-width="120px">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectVechicleHandle(row)">{{ row.traffic_plate_no }}</span>
          </template>
        </el-table-column>
      </el-table>
    </el-dialog>
  </div>
</template>

<script>
import Sticky from '@/components/Sticky'
import { validURL } from '@/utils/validate'
import { getBooking, updateBooking, createBooking } from '@/api/booking'
import { getModels, getVehicles } from '@/api/vehicle'
import { objectPop } from '@/utils/util'

const defaultForm = {
  id: undefined,
  bookingId: undefined,
  status: undefined,
  start_time: undefined,
  end_time: undefined,
  contact_name: undefined,
  contact_phone: undefined,
  pick_up_addr: undefined,
  drop_off_addr: undefined,
  remark: undefined,
  expiry_date: undefined,
  create_at: undefined,
  change_at: undefined,  
  vehicle_id: undefined,
  guide_id: undefined,
}

export default {
  name: 'BookingDetail',
  components: { Sticky },
  props: {
    isEdit: {
      type: Boolean,
      default: false
    }
  },
  mounted(){
  },
  data() {
    return {
      tableKey: 0,
      postForm: Object.assign({}, defaultForm),
      loading: false,
      rules: {
        start_time: [
          { required: true, message: 'This fields is required', trigger: 'change' }
        ],
        end_time: [
          { required: true, message: 'This fields is required', trigger: 'change' }
        ],
        contact_name: [
          { required: true, message: 'This fields is required', trigger: 'change' }
        ],
        contact_phone: [
          { required: true, message: 'This fields is required', trigger: 'change' }
        ],
        vehicle_id: [
          { required: true, message: 'This fields is required', trigger: 'change' }
        ],
      },
      tempRoute: {},
      relatedKey: {
        vehicle: undefined,
        guide: undefined,
        parent: undefined,
        order: undefined,
        create_by: undefined,
        company_by: undefined,
      },
      vehicleDialog: {
        show: false,
        query: {
          model: undefined,
          is_actived: true
        },
        modelOptions: [],
        vehicleList: undefined,
        modelLoading: false,
        vehicleLoading: false,
      },  
    }
  },
  computed: {
    vehicle: {
      get() {
        if(this.relatedKey.vehicle) {
          return this.relatedKey.vehicle.traffic_plate_no
        }
        return undefined
      },
      set(value) {
        if(value) {
          this.relatedKey.vehicle = value
          this.postForm.vehicle_id = value.id
        }
      }
    },
    guide: {
      get() {
        if(this.relatedKey.guide) {
          return this.relatedKey.guide.name || this.relatedKey.guide.username
        }
        return undefined
      },
      set(value) {
        if(value) {
          this.relatedKey.guide = value
          this.postForm.guide_id = value.id
        }        
      }
    },
    parent: {
      get() {
        if(this.relatedKey.parent) {
          return this.relatedKey.parent.bookingId
        }
        return undefined
      },
      set(value) {
        if(value) {
          this.relatedKey.parent = value
        }
      }
    },
    order: {
      get() {
        if(this.relatedKey.order) {
          return this.relatedKey.order.orderId
        }
        return undefined
      },
      set(value) {}
    }, 
    create_by: {
      get() {
        if(this.relatedKey.create_by) {
          return this.relatedKey.create_by.name || this.relatedKey.create_by.username
        }
        return undefined
      },
      set(value) {}
    },
    company_by: {
      get() {
        if(this.relatedKey.company_by) {
          return this.relatedKey.company_by.name
        }
        return undefined
      },
      set(value) {}
    },
  },
  created() {
    if (this.isEdit) {
      const id = this.$route.params && this.$route.params.id
      this.fetchData(id)
    } else {
      this.postForm = Object.assign({}, defaultForm)
    }
    this.tempRoute = Object.assign({}, this.$route)
  },
  methods: {
    fetchData(id) {
      getBooking(id).then(response => {
        this.postForm = response.data
        this.vehicle = objectPop(this.postForm, 'vehicle')
        this.guide = objectPop(this.postForm, 'guide')
        this.parent = objectPop(this.postForm, 'parent')
        this.order = objectPop(this.postForm, 'order')
        this.create_by = objectPop(this.postForm, 'create_by')
        this.company_by = objectPop(this.postForm, 'company_by')
        this.setTagsViewTitle()
      }).catch(err => {
        
      })
    },
    setTagsViewTitle() {
      const title = 'Edit Booking'
      const route = Object.assign({}, this.tempRoute, { title: `${title}-${this.postForm.bookingId}` })
      this.$store.dispatch('tagsView/updateVisitedView', route)
    },
    createForm() {
      this.$refs.postForm.validate(valid => {
        if (valid) {
          this.loading = true
          this.postForm.status = 'Created'
          createBooking(this.postForm).then(response => {
            var id = response.data['id']
            this.$router.push({ 
              path: `/booking/edit/${id}`
            })
            this.loading = false
          }).catch(err => {
            this.loading = false
          })
        } else {
          return false
        }
      })
    },
    updateForm() {
      this.$refs.postForm.validate(valid => {
        if (valid) {
          this.loading = true
          console.log(this.postForm)
          updateBooking(this.postForm.id, this.postForm).then(response => {
            this.$notify({
              title: 'Success',
              message: 'Change Successfully',
              type: 'success',
              duration: 2000
            })
            this.loading = false
          }).catch(error => {
            this.loading = false
          })
          
        } else {
          return false
        }
      })
    },
    handleVehicle(event) {
      this.vehicleDialog.show = true
      this.vehicleDialog.query.model = undefined
      if(this.vehicleDialog.modelOptions.length === 0){
        this.vehicleDialog.modelLoading = true
        getModels().then(response => {
          this.vehicleDialog.modelLoading = false
          this.vehicleDialog.modelOptions = response.data
        }).catch(err => {
          console.log(err)
          this.vehicleDialog.modelLoading = false
        })
      } 
      this.$nextTick(() => {
        this.$refs['postForm'].clearValidate()
      })
    },
    handleFilterVehicle() {
      this.vehicleDialog.vehicleLoading = true
      getVehicles(this.vehicleDialog.query).then(response => {
        this.vehicleDialog.vehicleList = response.data
        this.vehicleDialog.vehicleLoading = false
      }).catch(error => {
        this.vehicleDialog.vehicleLoading = false
      })
    },
    selectVechicleHandle(row) {
      this.vehicleDialog.show = false
      this.relatedKey.vehicle = Object.assign({}, row)
    }
  }
}
</script>

<style lang="scss" scoped>
@import "~@/styles/mixin.scss";

.createPost-container {
  position: relative;

  .createPost-main-container {
    padding: 20px 20px 20px 20px;

    .bookingInfo-container {
      position: relative;
      @include clearfix;
      padding-bottom: 20px;

      .bookingInfo-container-item {
        float: left;
      }
    }

    .itinerary-container {
      position: relative;
      @include clearfix;
      padding-bottom: 50px;
    }
  }


}

</style>

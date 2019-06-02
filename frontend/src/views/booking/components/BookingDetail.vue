<template>
  <div class="createPost-container" >
    <sticky v-if="postForm.can_delete || postForm.can_cancel || postForm.can_save" :z-index="10" :class-name="'sub-navbar ' + postForm.status" v-loading="loading">
      <el-button v-if="postForm.can_delete" style="margin-left: 10px;" @click="deleteFormConfirm" type="danger" >
        Delete
      </el-button>
      <el-button v-if="postForm.can_cancel" style="margin-left: 10px;" @click="cancelFormConfirm" type="warning" >
        Cancel
      </el-button>
      <el-button v-if="postForm.can_save" style="margin-left: 10px;" type="success" @click="updateForm">
        Save
      </el-button>
    </sticky>
    <sticky v-else-if="!isEdit" :z-index="10" :class-name="'sub-navbar ' + postForm.status">
      <el-button style="margin-left: 10px;" type="success" @click="createForm(true)">
        Create
      </el-button>
    </sticky>
    <el-form ref="postForm" :model="postForm" :rules="rules" label-position="top" label-width="120px" class="form-container">
      <div class="createPost-main-container" >      
        <div class="bookingInfo-container" >
          <el-row :gutter="24">
            <el-col :span="16">
              <el-card>
                <el-form-item label="Start time:" prop="start_time" >
                  <el-date-picker v-model="postForm.start_time" type="datetime" format="yyyy-MM-dd HH:mm" placeholder="Select date and time" clearable @change="handleDuration" :disabled="isEdit"/>
                </el-form-item>
                <el-form-item label="End time:" prop="end_time" >
                  <el-date-picker v-model="postForm.end_time" type="datetime" format="yyyy-MM-dd HH:mm" placeholder="Select date and time" clearable @change="handleDuration" :disabled="isEdit"/>
                </el-form-item>
                <el-form-item label="Contact name:" prop="contact_name" style="width: 300px;" >
                  <el-input v-model="postForm.contact_name" :disabled="!postForm.can_save && isEdit"></el-input>
                </el-form-item>
                <el-form-item label="Contact phone:" prop="contact_phone" style="width: 300px;" >
                  <el-input v-model="postForm.contact_phone" :disabled="!postForm.can_save && isEdit"></el-input>
                </el-form-item>
                <el-form-item v-if="postForm.start_time && postForm.end_time" label="Vehicle:" prop="vehicle_id" style="width: 300px;" >
                  <el-input v-if="vehicle" v-model="vehicle.traffic_plate_no" @focus="handleVehicle" suffix-icon="el-icon-search" readonly :disabled="isEdit"></el-input>
                  <el-input v-else v-model="vehicle" @focus="handleVehicle" suffix-icon="el-icon-search" readonly></el-input>
                </el-form-item>
                <el-form-item v-if="postForm.start_time && postForm.end_time" label="Guide:" prop="guide_id" style="width: 300px;">
                  <el-input v-model="guide" @focus="handleGuide" suffix-icon="el-icon-search" readonly :disabled="isEdit"></el-input>
                </el-form-item>
                <el-form-item label="Pick up address:">
                  <el-input v-model="postForm.pick_up_addr" :disabled="!postForm.can_save && isEdit"></el-input>  
                </el-form-item>
                <el-form-item label="Drop off address:">
                  <el-input v-model="postForm.drop_off_addr" :disabled="!postForm.can_save && isEdit"></el-input>  
                </el-form-item>
                <el-form-item label="Remark:" >
                  <el-input v-model="postForm.remark" :autosize="{ minRows: 4, maxRows: 4}" type="textarea" :maxlength="256" :show-word-limit="true" :disabled="!postForm.can_save && isEdit"></el-input>  
                </el-form-item>
              </el-card>
            </el-col>
            <el-col :span="8">
              <el-card >
                <el-form-item label="Status:">
                  <el-input v-model="postForm.status" v-if="postForm.status" disabled></el-input>
                  <el-input v-else disabled></el-input>
                </el-form-item>
                <el-form-item label="Order:">
                  <el-input v-model="order" disabled></el-input>
                </el-form-item>
                <el-form-item label="Creator:">
                  <el-input v-model="creator" disabled></el-input>
                </el-form-item>
                <el-form-item label="Company:">
                  <el-input v-model="company" disabled></el-input>
                </el-form-item>
                <el-form-item v-if="postForm.create_at" label="Create at:">
                  <span>{{postForm.create_at | moment('YYYY-MM-DD HH:mm')}}</span>
                </el-form-item>
                <el-form-item v-if="postForm.change_at" label="Change at:">
                  <span>{{postForm.change_at | moment('YYYY-MM-DD HH:mm')}}</span>
                </el-form-item>
              </el-card>
            </el-col>
          </el-row>
        </div>      
        <div class="itinerary-container">
          <el-card >
            <div slot="header">
              <el-row type="flex" justify="space-between">
                <el-col :span="6"><div align="left">Itinerary</div></el-col>
              </el-row>              
            </div>
            <div v-if="vehicle">
              <el-table              
                :key="tableKey"
                :data="postForm.itinerary" 
                border
                stripe
                fit
                :summary-method="getSummaries"
                show-summary
                highlight-current-row
                style="width: 100%;"
                row-key="id">
                <el-table-column width="120px" label="Day" fixed="left" align="center">
                  <template slot-scope="{row}">
                    <span>{{ row.day }}</span>
                  </template>
                </el-table-column>
                <el-table-column label="Fullday" width="80px" align="center" class-name="small-padding fixed-width">
                  <template slot-scope="{row}">
                    <el-checkbox v-model="row.full_day" disabled/>
                  </template>
                </el-table-column>
                <el-table-column label="Freedomday" width="100px" align="center" class-name="small-padding fixed-width">
                  <template slot-scope="{row}">
                    <el-checkbox v-model="row.freedom_day" disabled/>
                  </template>
                </el-table-column>
                <el-table-column width="300px" label="Itinerary" align="center">
                  <template slot-scope="{row}">
                    <span>{{ row.itinerary }}</span>
                  </template>                    
                </el-table-column>
                <el-table-column width="140px" label="Vehicle Charge" prop="vehicle_gross_charge" align="center">
                  <template slot-scope="{row}">  
                    <span v-if="row.vehicle_gross_charge">{{ row.vehicle_gross_charge }} AED</span>
                  </template>
                </el-table-column>
                <el-table-column width="140px" label="Guide Charge" prop="guide_charge" align="center">
                  <template slot-scope="{row}">
                    <span v-if="row.guide_charge">{{ row.guide_charge }} AED</span>
                  </template>
                </el-table-column>                
                <el-table-column min-width="300px" label="Remark" align="center">
                  <template slot-scope="{row}">
                    <span>{{ row.remark }}</span>
                  </template>
                </el-table-column> 
                <el-table-column label="Actions" align="center" width="100px" fixed="right" class-name="small-padding fixed-width">
                  <template slot-scope="{row}">
                    <el-button type="primary" size="mini" @click="handleItinerary(row)" :disabled="isEdit">
                      Edit
                    </el-button>
                  </template>
                </el-table-column>
              </el-table>
            </div>
          </el-card>
        </div>
        <div v-if="isEdit && postForm.can_comment" class="comment-container">
          <el-card >
            <div slot="header">
              <span>Comment</span>
            </div>
            <div>
              <el-row>
                <el-col :span="5" v-if="vehicle">
                  <el-form-item label="Vehicle Score:">
                    <el-rate
                      v-model="postForm.vehicle_score"
                      :max="5"
                      :colors="['#99A9BF', '#F7BA2A', '#FF9900']"
                      :low-threshold="1"
                      :high-threshold="5"
                      style="margin-top:8px;"/>
                  </el-form-item>
                </el-col>
                <el-col :span="5" v-if="guide">
                  <el-form-item label="Guide Score:">
                    <el-rate
                      v-model="postForm.guide_score"
                      :max="5"
                      :colors="['#99A9BF', '#F7BA2A', '#FF9900']"
                      :low-threshold="1"
                      :high-threshold="5"
                      style="margin-top:8px;"/>
                  </el-form-item>
                </el-col>
              </el-row>
              <el-row>
                <el-col>
                  <el-form-item label="Comment:" >
                    <el-input v-model="postForm.comment" :autosize="{ minRows: 4, maxRows: 4}" type="textarea" :maxlength="256"></el-input>  
                  </el-form-item>
                </el-col>
              </el-row>
            </div>        
          </el-card>          
        </div>
      </div>
    </el-form>
    <el-dialog title="Select Vehicle" :visible.sync="vehicleDialog.show" width="85%" @close="handleVehicleClose">
      <div class="filter-container">
        <el-select 
          v-model="vehicleDialog.query.model"
          reserve-keyword 
          clearable
          :loading="vehicleDialog.modelLoading"
          placeholder="Vehicle Model"
          @change="loadVehicles"
          class="filter-item">
          <el-option
            v-for="item in vehicleDialog.modelOptions"
            :key="item.id"
            :label="item.name"
            :value="item.id">
          </el-option>
        </el-select>
        <el-button type="primary" @click="loadVehicles" class="filter-item">Refresh</el-button>
      </div>
      <el-table
        :key="tableKey"
        v-loading="vehicleDialog.vehicleLoading"
        :data="vehicleDialog.vehicleList"
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
        <el-table-column label="Model" align="center" width="160px">
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
        <el-table-column label="Average Score" width="130px" align="center">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectVechicleHandle(row)">{{ row.avg_score }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Total Score" width="130px" align="center">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectVechicleHandle(row)">{{ row.total_score }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Traffic Number" align="center" min-width="120px">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectVechicleHandle(row)">{{ row.traffic_plate_no }}</span>
          </template>
        </el-table-column>
      </el-table>
    </el-dialog>
    <el-dialog title="Select Guide" :visible.sync="guideDialog.show" width="85%" @close="handleGuideClose">
      <div class="filter-container">
        <el-button type="primary" @click="loadGuides" class="filter-item">Refresh</el-button>
      </div>
      <el-table :data="guideDialog.list"
      :key="tableKey"
      v-loading="guideDialog.loading"
      border 
      stripe
      fit
      highlight-current-row
      style="width: 100%;"
      >
        <el-table-column label="UserName" align="center" width="180px">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectGuideHandle(row)">{{ row.username }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Name" align="center" width="120px">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectGuideHandle(row)">{{ row.name }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Phone" width="120px" align="center" class-name="small-padding fixed-width">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectGuideHandle(row)">{{ row.phone }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Company" width="200px" align="center">
          <template slot-scope="{row}">
            <span v-if="row.company" class="link-type" @click="selectGuideHandle(row)">{{ row.company.name }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Average Score" width="130px" align="center">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectGuideHandle(row)">{{ row.avg_score }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Total Score" width="130px" align="center">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectGuideHandle(row)">{{ row.total_score }}</span>
          </template>
        </el-table-column>
        <el-table-column label="Introduction" min-width="150px" align="center">
          <template slot-scope="{row}">
            <span class="link-type" @click="selectGuideHandle(row)">{{ row.introduction }}</span>
          </template>
        </el-table-column>
      </el-table>
    </el-dialog>
    <el-dialog title="Edit Itinerary" :visible.sync="itineraryDialog.show" width="800px">
      <el-form ref="itineraryForm" :model="itineraryDialog.data" :rules="itineraryDialog.rules" label-position="left" label-width="120px" style="width: 400px; margin-left:20px;">
        <el-form-item label="Day" prop="day" :rules="{ required: true, message: 'This fields is required', trigger: 'change' }">
          <el-date-picker v-model="itineraryDialog.data.day" type="date" format="yyyy-MM-dd" placeholder="Select date" clearable disabled/>
        </el-form-item> 
        <el-form-item label="Freedom Day" prop="freedom">
          <el-checkbox v-model="itineraryDialog.data.freedom_day"/>
        </el-form-item>
        <el-form-item v-if="vehicle" label="Itinerary" prop="itinerary">
          <el-select v-model="itineraryDialog.data.itinerary" placeholder="Select Itinerary" @change="handleItineraryChange" :disabled="itineraryDialog.data.freedom_day">
            <el-option v-for="item in vehicle.model.price"
              :key="item.id"
              :label="item.itinerary"
              :value="item.itinerary">
            </el-option>
          </el-select>
        </el-form-item>        
        <el-form-item label="remark" prop="remark">
          <el-input v-model="itineraryDialog.data.remark" :autosize="{ minRows: 2, maxRows: 4}" :maxlength="256" type="textarea"/>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="itineraryDialog.show = false">
          Cancel
        </el-button>
        <el-button type="primary" @click="updateItineraryData">
          Confirm
        </el-button>
      </div>
    </el-dialog> 
    <el-dialog :title="createDialog.title" :visible.sync="createDialog.show" width="800px">
      <el-form label-position="left" label-width="120px" style="width: 400px; margin-left:20px;">
        <el-form-item label="Start Time:" prop="start_time">
          <el-date-picker v-model="postForm.start_time" type="datetime" format="yyyy-MM-dd HH:mm" readonly/>
        </el-form-item>
        <el-form-item label="End Time:" prop="end_time">
          <el-date-picker v-model="postForm.end_time" type="datetime" format="yyyy-MM-dd HH:mm" readonly/>
        </el-form-item>
        <el-form-item v-if="vehicle" label="Vehicle:" prop="vehicle_id">
          <el-input v-model="vehicle.traffic_plate_no" readonly></el-input>
        </el-form-item>
        <el-form-item v-if="guide" label="Guide:" prop="guide_id">
          <el-input v-model="guide" readonly></el-input>
        </el-form-item>
        <el-form-item v-if="vehicle" label="Vehicle Charge:" >
          <span>{{ vehicle_charge() }} AED</span>
        </el-form-item>
        <el-form-item v-if="guide" label="Guide Charge:" >
          <span>{{ guide_charge() }} AED</span>
        </el-form-item>
        <el-form-item label="Discount:" >
          <span>{{ discount() }} AED</span>
        </el-form-item>
        <el-form-item label="Total:" >
          <span>{{ total() }} AED</span>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="itineraryDialog.show = false">
          Cancel
        </el-button>
        <el-button type="primary" @click="createForm(false)">
          Create
        </el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import Sticky from '@/components/Sticky'
import { validURL } from '@/utils/validate'
import { getBooking, updateBooking, createBooking } from '@/api/booking'
import { getModels, getVehicles } from '@/api/vehicle'
import { getUsers } from '@/api/user'

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
  create_at: undefined,
  change_at: undefined,
  vehicle_id: undefined,
  guide_id: undefined,
  itinerary: []
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
  mounted(){},
  data() {
    const validateItinerary = (rule, value, callback) => {
      if (value === '' || value === undefined) {
        if(!this.itineraryDialog.data.freedom_day) {
          callback(new Error('This fields is required'))
        } else {
          callback()
        }
      } else {
        callback()
      }
    }
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
        order: undefined,
        create_by: undefined,
        company_by: undefined,
      },
      vehicleDialog: {
        show: false,
        select: false,
        query: {
          model: undefined,
          is_actived: true
        },
        modelOptions: [],
        vehicleList: [],
        modelLoading: false,
        vehicleLoading: false,
      },
      guideDialog: {
        show: false,
        select: false,
        query: {
          is_actived: true,
          is_tourguide: true
        },
        list: [],
        loading: false
      },
      itineraryDialog: {
        show: false,
        data: {
          day: undefined,
          itinerary: undefined,
          full_day: undefined,
          freedom_day: undefined,
          vehicle_cost_charge: undefined,
          vehicle_gross_charge: undefined,
          guide_charge: undefined,
          remark:undefined
        },
        rules: {
          itinerary: [{ validator: validateItinerary, trigger: 'change' }]
        }
      },
      createDialog: {
        show: false,
        title: 'Please check the information again.',
      }
    }
  },
  computed: {    
    vehicle: {
      get() {
        if(this.relatedKey.vehicle) {
          return this.relatedKey.vehicle
        }
        return undefined
      },
      set(value) {
        if(value) {
          this.postForm.vehicle_id = value.id
        } else {
          this.postForm.vehicle_id = undefined
        }
        this.relatedKey.vehicle = value
        delete this.postForm.vehicle
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
          this.postForm.guide_id = value.id          
        } else {
          this.postForm.guide_id = undefined
        }
        this.relatedKey.guide = value
        delete this.postForm.guide
      }
    },    
    order: {
      get() {
        if(this.relatedKey.order) {
          return this.relatedKey.order.orderId
        }
        return undefined
      },
      set(value) {
        if(value) {
          this.relatedKey.order = value
          delete this.postForm.order
        }
      }
    }, 
    creator: {
      get() {
        if(this.relatedKey.create_by) {
          return this.relatedKey.create_by.name || this.relatedKey.create_by.username
        }
        return undefined
      },
      set(value) {
        if(value) {
          this.relatedKey.create_by = value
          delete this.postForm.create_by
        }
      }
    },
    company: {
      get() {
        if(this.relatedKey.company_by) {
          return this.relatedKey.company_by.name
        }
        return undefined
      },
      set(value) {
        if(value) {
          this.relatedKey.company_by = value
          delete this.postForm.company_by
        }
      }
    }  
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
    setData(data) {
      this.postForm = data
      this.vehicle = this.postForm.vehicle
      this.guide = this.postForm.guide
      this.order = this.postForm.order
      this.creator = this.postForm.create_by
      this.company = this.postForm.company_by
      this.history = this.postForm.history
      this.handleDuration()
    },
    fetchData(id) {
      getBooking(id).then(response => {
        this.setData(response.data)
        this.setTagsViewTitle()
      })
    },
    setTagsViewTitle() {
      const title = 'Edit Booking'
      const route = Object.assign({}, this.tempRoute, { title: `${title}-${this.postForm.bookingId}` })
      this.$store.dispatch('tagsView/updateVisitedView', route)
    },
    createForm(show) {
      this.$refs.postForm.validate(valid => {
        if (valid && this.valideItinerary()) {
          if (show){
            this.createDialog.show = true
          } else {
            this.createDialog.show = false
            this.loading = true
            this.postForm.status = 'Created'
            createBooking(this.postForm).then(response => {
              var id = response.data['id']
              this.loading = false
              this.$store.dispatch('tagsView/delView', this.$route).then(() => {
                this.$nextTick(() => {
                  this.$router.replace({
                    path: '/booking/edit/' + id
                  })
                })
              })
            }).catch(err => {
              this.loading = false
            })
          }
        } else {
          return false
        }
      })
    },
    updateForm() {
      this.$refs.postForm.validate(valid => {
        if (valid) {
          this.loading = true
          updateBooking(this.postForm.id, this.postForm).then(response => {
            this.setData(response.data)
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
    updateStatus(status) {
      this.loading = true
      this.postForm.status = status
      updateBooking(this.postForm.id, this.postForm).then(response => {
        this.setData(response.data)
        this.$notify({
          title: 'Success',
          message: status + 'Successfully',
          type: 'success',
          duration: 2000
        })
        this.loading = false
        
        if(this.postForm.status === 'Delete') {
          var view = this.$route
          this.$store.dispatch('tagsView/delView', view).then(({ visitedViews }) => {
            const latestView = visitedViews.slice(-1)[0]
            const firstView = visitedViews[0]
            this.$router.push(latestView)
            // if (latestView && latestView != firstView) {
            //   this.$router.push(latestView)
            // } 

            // this.$store.dispatch('tagsView/delCachedView', firstView).then(() => {
            //   const { fullPath } = firstView
            //   this.$nextTick(() => {
            //     this.$router.replace({
            //       path: '/redirect' + fullPath
            //     })
            //   })
            // })
          })
        }
      }).catch(error => {
        this.loading = false
      })   
    },
    cancelFormConfirm() {
      this.$confirm('Are you sure to cancel the booking?', 'Alert', {
          confirmButtonText: 'Confirm',
          cancelButtonText: 'Cancel',
          type: 'warning'
        }).then(() => {
          this.updateStatus('Cancel')
        })
    },
    deleteFormConfirm() {
      this.$confirm('Are you sure to delete the booking?', 'Alert', {
          confirmButtonText: 'Confirm',
          cancelButtonText: 'Cancel',
          type: 'warning'
        }).then(() => {
          this.updateStatus('Delete')
        })
    },
    handleVehicle(event) {
      this.vehicleDialog.show = true
      this.vehicleDialog.select = false
      
      if(this.vehicleDialog.modelOptions.length === 0){
        this.vehicleDialog.modelLoading = true
        getModels().then(response => {
          this.vehicleDialog.modelLoading = false
          this.vehicleDialog.modelOptions = response.data
        }).catch(err => {
          this.vehicleDialog.modelLoading = false
        })
      } 
      this.$nextTick(() => {
        this.$refs['postForm'].clearValidate()
      })
    },
    loadVehicles() {
      this.vehicleDialog.vehicleLoading = true
      this.vehicleDialog.vehicleList = []
      getVehicles(this.vehicleDialog.query).then(response => {
        this.vehicleDialog.vehicleList = response.data
        this.vehicleDialog.vehicleLoading = false
      }).catch(error => {
        this.vehicleDialog.vehicleLoading = false
      })
    },
    loadGuides() {
      this.guideDialog.loading = true
      this.guideDialog.list = []
      getUsers(this.guideDialog.query).then(response => {
        this.guideDialog.list = response.data
        this.guideDialog.loading = false
      }).catch(error => {
        this.guideDialog.loading = false
      })
    },
    handleGuide() {
      this.guideDialog.show = true
      this.guideDialog.select = false
      if(this.guideDialog.list.length == 0) {
        this.loadGuides()
      }
    },
    handleGuideClose() {
      if(!this.guideDialog.select) {
        this.guide = null
      }
    },
    handleVehicleClose() {
      if(!this.vehicleDialog.select) {
        this.vehicle = null
      }
    },
    handleItinerary(data) {
      this.itineraryDialog.show = true
      this.itineraryDialog.data = Object.assign({}, data)
      this.$nextTick(() => {
        this.$refs['itineraryForm'].clearValidate()
      })
    },
    selectVechicleHandle(row) {
      this.vehicleDialog.show = false
      this.vehicleDialog.select = true
      this.vehicle = Object.assign({}, row)
    },
    selectGuideHandle(row) {
      this.guideDialog.show = false
      this.guideDialog.select = true
      this.guide = Object.assign({}, row)
    },
    valideItinerary() {
      for(const itinerary of this.postForm.itinerary) {
        if(itinerary.itinerary === '' || itinerary.itinerary === undefined) {
          this.$message({
            message: 'Itinerary information is incomplete',
            type: 'error'
          })
          return false
        }
      }
      return true
    },
    guide_charge() {
      var total = 0.0
      for(var itinerary of this.postForm.itinerary) {
        total += Number(itinerary.guide_charge)
      }
      return total
    },
    vehicle_charge() {
      var total = 0.0
      for(var itinerary of this.postForm.itinerary) {
        total += Number(itinerary.vehicle_gross_charge)
      }
      return total
    },
    discount() {
      var total = 0.0
      var user = this.$store.getters.user
      if (user && user.company && user.company.discount) {
        var discount = Number(user.company.discount.value)

        for(var itinerary of this.postForm.itinerary) {
          total += Math.abs(itinerary.vehicle_gross_charge - itinerary.vehicle_cost_charge) * discount
        }
      }

      return total
    },
    total() {
      return Number(this.vehicle_charge() + this.guide_charge() - this.discount())
    },
    updateItineraryData() {
      if(this.itineraryDialog.data.freedom_day) {
        this.itineraryDialog.data.full_day = true
        this.itineraryDialog.data.itinerary = 'Freedom Day'
        this.itineraryDialog.data.vehicle_cost_charge = 0.00
        this.itineraryDialog.data.vehicle_gross_charge = 0.00
        this.itineraryDialog.data.guide_charge = 0.00
      }

      this.$refs['itineraryForm'].validate((valid) => {
        if(valid) {
          for (const v of this.postForm.itinerary) {
            if (v.day === this.itineraryDialog.data.day) {
              const index = this.postForm.itinerary.indexOf(v)
              this.postForm.itinerary.splice(index, 1, this.itineraryDialog.data)
              break
            }
          }
          this.itineraryDialog.show = false
        }
      })
    },
    handleDuration() {
      if(this.postForm.start_time && this.postForm.end_time) {
        var start_time = this.$moment(this.postForm.start_time, 'YYYY-MM-DD')
        var end_time = this.$moment(this.postForm.end_time, 'YYYY-MM-DD')
        var duration = this.$moment.duration(end_time.diff(start_time))

        if(!this.isEdit) {
          this.postForm.itinerary = []

          for(var i = 0; i < Math.floor(duration.asDays()) + 1; i++){
            var nextDay = this.$moment(start_time).add(i, 'days')
            this.postForm.itinerary.push({
              day: this.$moment(nextDay).format('YYYY-MM-DD'),
              itinerary: '',
              full_day: true,
              freedom_day: false,
              vehicle_cost_charge: 0.0,
              vehicle_gross_charge: 0.0,
              guide_charge: 0.0,
              remark:''
            });
          }
        }
      }
    },
    handleItineraryChange(value) {
      for(var itinerary of this.vehicle.model.price) {        
        if(itinerary.itinerary === value) {
          this.itineraryDialog.data.vehicle_cost_charge = Number(itinerary.cost_price)
          this.itineraryDialog.data.vehicle_gross_charge = Number(itinerary.gross_price)
          this.itineraryDialog.data.full_day = itinerary.full_day

          if(this.guide) {
            if(itinerary.full_day) {
              this.itineraryDialog.data.guide_charge = 400.0
            } else {
              this.itineraryDialog.data.guide_charge = 200.0
            }
          }         
          break;
        }
      }    
    },
    getSummaries(param) {
        const { columns, data } = param;
        const sums = [];
        columns.forEach((column, index) => {
          if (index === 0) {
            sums[index] = 'Sum';
            return;
          }
          const values = data.map(item => Number(item[column.property]));
          if (!values.every(value => isNaN(value))) {
            sums[index] = values.reduce((prev, curr) => {
              const value = Number(curr);
              if (!isNaN(value)) {
                return prev + curr;
              } else {
                return prev;
              }
            }, 0);
            sums[index] += ' AED';
          } else {
            sums[index] = 'N/A';
          }
        });
        return sums
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
      padding-bottom: 20px;
    }

    .comment-container {
      position: relative;
      @include clearfix;
      padding-bottom: 20px;
    }

    .log-container {
      position: relative;
      @include clearfix;
      padding-bottom: 20px;
    }
  }
}

.edit-input {
  padding-right: 100px;
}

.cancel-btn {
  position: absolute;
  right: 15px;
  top: 10px;
}
</style>

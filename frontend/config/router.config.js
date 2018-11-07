export default [
  // user
  {
    path: '/user',
    component: '../layouts/UserLayout',
    routes: [
      { path: '/user', redirect: '/user/login' },
      { path: '/user/login', component: './User/Login' },
      { path: '/user/register', component: './User/Register' },
      { path: '/user/register-result', component: './User/RegisterResult' },
    ],
  },
  // app
  {
    path: '/',
    component: '../layouts/BasicLayout',
    Routes: ['src/pages/Authorized'],
    authority: ['admin', 'user'],
    routes: [
      // dashboard
      { path: '/', redirect: '/dashboard' },
      {
        path: '/dashboard',
        name: 'dashboard',
        icon: 'dashboard',
        component: './Dashboard/Dashboard',
      },

      // equipment
      {
        path: '/equipment',
        icon: 'laptop',
        name: 'equipment',
        routes: [
          {
            path: '/equipment/product-list',
            name: 'product-list',
            component: './Product/ProductList',
          },
          {
            path: '/equipment/product-profile/:product_id',
            name: 'product-profile',
            hideInMenu: true,
            component: './Product/ProductProfile',
          },

          {
            path: '/equipment/device-list',
            name: 'device-list',
            component: './Device/DeviceList',
          },

          {
            path: '/equipment/device-profile/:device_id',
            name: 'device-profile',
            hideInMenu: true,
            component: './Device/DeviceProfile',
          },

          {
            path: '/equipment/group',
            name: 'device-group',
            hideInMenu: true,

            component: './Project/ProjectList',
          },
        ],
      },

       // project
      {
        path: '/project',
        icon: 'laptop',
        name: 'project',
        routes: [
          {
            path: '/project/project-list',
            name: 'project-list',
            component: './Project/ProjectList',
          },

        ],
      },

      // status
      {
        path: '/status',
        icon: 'block',
        name: 'status',
        routes: [
          {
            // path: '/status/fabric',
            path: 'http://www.smartlinkcloud.com:8008/conf2d/fabric',
            name: 'configure',
            // component: './Status/Status',

          },
          {
            path: 'http://www.smartlinkcloud.com:8008/conf2d/errorlog',
            name: 'errorlog',
            component: './Status/Errorlog',

          },
          {
            path: 'http://www.smartlinkcloud.com:8008/conf3d/storehouse',
            name: '3D',
          },
          {
            path: '/status/digital/:device_id',
            // redirect: '/dashboard/history/2',
            name: 'digital',
            hideInMenu: true,

            component: './Display/Digital',
          },        
          {
            path: '/status/bar/:device_id',
            // redirect: '/dashboard/history/2',
            name: 'bar',
            hideInMenu: true,

            component: './Display/Bar',
          },
          {
            path: '/status/line/:device_id',
            // redirect: '/dashboard/history/2',
            name: 'line',
            hideInMenu: true,
            component: './Display/Line',
          },

          {
            path: '/status/digital/2',
            name: 'digital',
            component: './Display/Digital',
          },        
          {
            path: '/status/bar/2',
            name: 'bar',
            component: './Display/Bar',
          },
          {
            path: '/status/line/2',
            name: 'line',
            component: './Display/Line',
          },
          {
            path: '/status/gauge/2',
            name: 'gauge',
            component: './Display/Gauge',
          },          

          {
            path: '/status/history/:device_id',
            name: 'history',
            hideInMenu: true,

            component: './Dashboard/Monitor',
          },
          {
            path: '/status/warning/:device_id',
            name: 'warning',
            component: './Dashboard/Monitor',
            hideInMenu: true,

          },
        ],
      },

      //Operations

      {
        path: '/operations',
        icon: 'schedule',
        name: 'operations',
        routes: [
          {
            path: 'http://www.smartlinkcloud.com:6688/tickets',
            name: 'ticket',
          },
          {
            path: '/operations/maintenance-record',
            name: 'maintenance-record',
            component: './Operation/MaintenanceRecord',
          },
          {
            path: '/operations/spare-parts-management',
            name: 'spare-parts-management',
            component: './Project/ProjectList',
            hideInMenu: true,
          },
          {
            path: '/operations/maintenance-tips',
            name: 'maintenance-tips',
            hideInMenu: true,

            component: './Project/ProjectList',
          },
        ],
      },

      //Big Data Analytics

      {
        path: '/analytics',
        icon: 'schedule',
        name: 'analytics',
        routes: [
          {
            path: '/analytics/data-source-config',
            name: 'data-source-config',
            hideInMenu: true,

            component: './Project/ProjectList',
          },
          {
            path: '/analytics/kpi',
            name: 'kpi',
            component: './DataAnalytics/KPI',
          },
          {
            path: '/analytics/energy',
            name: 'energy',

            component: './DataAnalytics/Energy',
          },
          {
            path: '/analytics/spatial-data-analysis',
            name: 'spatial-data-analysis',

            component: './DataAnalytics/Spatial',
          },
          {
            path: '/analytics/stream-data-analysis',
            name: 'stream-data-analysis',

            component: './DataAnalytics/Stream',
          },
        ],
      },

      //customer management

      {
        path: '/customer-management',
        icon: 'schedule',
        name: 'customer-management',
        routes: [
          {
            path: '/customer-management/authorization',
            name: 'authorization',
            component: './Project/ProjectList',
          },
          {
            path: '/customer-management/profile',
            name: 'user-profile',
            component: './Project/ProjectList',
          },
        ],
      },

      //extension module

      {
        path: '/extensions',
        icon: 'schedule',
        name: 'extensions',
        routes: [
          {
            path: '/extensions/security',
            name: 'security',
            component: './Project/ProjectList',
          },
          {
            path: '/extensions/expert-system',
            name: 'expert-system',
            component: './Project/ProjectList',
          },

          //Edge

          {
            path: '/extensions/edge',
            icon: 'schedule',
            name: 'edge',
            routes: [
              {
                path: '/extensions/edge/group',
                name: 'edge-group',
                component: './Project/ProjectList',
              },
              {
                path: '/extensions/edge/driver',
                name: 'edge-driver',
                component: './Project/ProjectList',
                routes: [
                  {
                    path: '/extensions/edge/driver/opc-ua',
                    name: 'opc-ua',
                    component: './Project/ProjectList',
                  },
                  {
                    path: '/extensions/edge/driver/modbus',
                    name: 'modbus',
                    component: './Project/ProjectList',
                  },
                ]
              },
            ],
          },

          //Rule engine

          {
            path: '/extensions/rule-engine',
            icon: 'schedule',
            name: 'rule-engine',
            routes: [
              {
                path: 'http://www.smartlinkcloud.com:1880',

                name: 'node-red',
                component: './Project/ProjectList',
              },
            ],
          },
        ],
      },

      //version

      {
        path: '/version',
        icon: 'save',
        name: 'version',
        routes: [
          {
            path: '/version/changelog',
            name: 'changelog',
            component: './Version/Changelog',
          },
          {
            path: '/version/todolist',
            name: 'todolist',
            component: './Version/Todolist',
          },
          {
            path: '/version/buglist',
            name: 'buglist',
            component: './Bug/BugList',
          },
          {
            path: '/version/bugprofile',
            name: 'bugprofile',
            hideInMenu: true,
            component: './Bug/BugProfile',
          },
        ],
      },

      // forms
      {
        path: '/form',
        icon: 'form',
        name: 'form',
        hideInMenu: true,
        routes: [
          {
            path: '/form/basic-form',
            name: 'basicform',
            component: './Forms/BasicForm',
          },
          {
            path: '/form/step-form',
            name: 'stepform',
            component: './Forms/StepForm',
            hideChildrenInMenu: true,
            routes: [
              {
                path: '/form/step-form',
                redirect: '/form/step-form/info',
              },
              {
                path: '/form/step-form/info',
                name: 'info',
                component: './Forms/StepForm/Step1',
              },
              {
                path: '/form/step-form/confirm',
                name: 'confirm',
                component: './Forms/StepForm/Step2',
              },
              {
                path: '/form/step-form/result',
                name: 'result',
                component: './Forms/StepForm/Step3',
              },
            ],
          },
          {
            path: '/form/advanced-form',
            name: 'advancedform',
            authority: ['admin'],
            component: './Forms/AdvancedForm',
          },
        ],
      },
      // list
      {
        path: '/list',
        icon: 'table',
        name: 'list',
        hideInMenu: true,
        routes: [
          {
            path: '/list/table-list',
            name: 'searchtable',
            component: './List/TableList',
          },
          {
            path: '/list/basic-list',
            name: 'basiclist',
            component: './List/BasicList',
          },
          {
            path: '/list/card-list',
            name: 'cardlist',
            component: './List/CardList',
          },
          {
            path: '/list/search',
            name: 'searchlist',
            component: './List/List',
            routes: [
              {
                path: '/list/search',
                redirect: '/list/search/articles',
              },
              {
                path: '/list/search/articles',
                name: 'articles',
                component: './List/Articles',
              },
              {
                path: '/list/search/projects',
                name: 'projects',
                component: './List/Projects',
              },
              {
                path: '/list/search/applications',
                name: 'applications',
                component: './List/Applications',
              },
            ],
          },
        ],
      },
      {
        path: '/profile',
        name: 'profile',
        icon: 'profile',
        hideInMenu: true,
        routes: [
          // profile
          {
            path: '/profile/basic',
            name: 'basic',
            component: './Profile/BasicProfile',
          },
          {
            path: '/profile/advanced',
            name: 'advanced',
            authority: ['admin'],
            component: './Profile/AdvancedProfile',
          },
        ],
      },
      {
        name: 'result',
        icon: 'check-circle-o',
        path: '/result',
        hideInMenu: true,
        routes: [
          // result
          {
            path: '/result/success',
            name: 'success',
            component: './Result/Success',
          },
          { path: '/result/fail', name: 'fail', component: './Result/Error' },
        ],
      },
      {
        name: 'exception',
        icon: 'warning',
        path: '/exception',
        hideInMenu: true,
        routes: [
          // exception
          {
            path: '/exception/403',
            name: 'not-permission',
            component: './Exception/403',
          },
          {
            path: '/exception/404',
            name: 'not-find',
            component: './Exception/404',
          },
          {
            path: '/exception/500',
            name: 'server-error',
            component: './Exception/500',
          },
          {
            path: '/exception/trigger',
            name: 'trigger',
            hideInMenu: true,
            component: './Exception/TriggerException',
          },
        ],
      },
      
      {
        name: 'account',
        icon: 'user',
        path: '/account',
        routes: [
          {
            path: '/account/center',
            name: 'center',
            component: './Account/Center/Center',
            routes: [
              {
                path: '/account/center',
                redirect: '/account/center/articles',
              },
              {
                path: '/account/center/articles',
                component: './Account/Center/Articles',
              },
              {
                path: '/account/center/applications',
                component: './Account/Center/Applications',
              },
              {
                path: '/account/center/projects',
                component: './Account/Center/Projects',
              },
            ],
          },

          {
            path: '/account/settings',
            name: 'settings',
            component: './Account/Settings/Info',
            routes: [
              {
                path: '/account/settings',
                redirect: '/account/settings/base',
              },
              {
                path: '/account/settings/base',
                component: './Account/Settings/BaseView',
              },
              {
                path: '/account/settings/security',
                component: './Account/Settings/SecurityView',
              },
              {
                path: '/account/settings/binding',
                component: './Account/Settings/BindingView',
              },
              {
                path: '/account/settings/notification',
                component: './Account/Settings/NotificationView',
              },
            ],
          },
        ],
      },
      {
        component: '404',
      },
    ],
  },
];

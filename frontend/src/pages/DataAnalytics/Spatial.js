import React, { Component } from 'react';

// 引入 ECharts 主模块
import echarts from 'echarts/lib/echarts';
// 引入柱状图
import  'echarts/lib/chart/pie';
import  'echarts/lib/chart/map';
import china from 'echarts/map/js/china'
// 引入提示框和标题组件
import 'echarts/lib/component/tooltip';
import 'echarts/lib/component/title';
// import 'echarts/config';

class EchartsTest extends Component {
    componentDidMount() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('main'));
        // 绘制图表
        


        var option = {
            title : {
                text: '全国设备分布图',
                subtext: '2018-11-06数据'
            },
            tooltip : {
                trigger: 'item'
            },
            legend: {
                x:'right',
                selectedMode:false,
                data:['北京','上海','广东']
            },
            dataRange: {
                orient: 'horizontal',
                min: 0,
                max: 550,
                text:['高','低'],           // 文本，默认为数值文本
                splitNumber:0
            },
            toolbox: {
                show : true,
                orient: 'vertical',
                x:'right',
                y:'center',
                feature : {
                    mark : {show: true},
                    dataView : {show: true, readOnly: false}
                }
            },
            series : [
                {
                    name: '全国设备分布图',
                    type: 'map',
                    mapType: 'china',
                    mapLocation: {
                        x: 'left'
                    },
                    selectedMode : 'multiple',
                    itemStyle:{
                        normal:{label:{show:true}},
                        emphasis:{label:{show:true}}
                    },
                    data:[
                        {name:'西藏', value:22},
                        {name:'青海', value:32},
                        {name:'宁夏', value:11},
                        {name:'海南', value:25},
                        {name:'甘肃', value:50},
                        {name:'贵州', value:57},
                        {name:'新疆', value:66},
                        {name:'云南', value:88},
                        {name:'重庆', value:100},
                        {name:'吉林', value:105},
                        {name:'山西', value:112},
                        {name:'天津', value:113},
                        {name:'江西', value:117},
                        {name:'广西', value:117},
                        {name:'陕西', value:125},
                        {name:'黑龙江', value:125},
                        {name:'内蒙古', value:143},
                        {name:'安徽', value:153},
                        {name:'北京', value:224, selected:true},
                        {name:'福建', value:175},
                        {name:'上海', value:260, selected:true},
                        {name:'湖北', value:196},
                        {name:'湖南', value:196},
                        {name:'四川', value:210},
                        {name:'辽宁', value:222},
                        {name:'河北', value:245},
                        {name:'河南', value:169},
                        {name:'浙江', value:323},
                        {name:'山东', value:453},
                        {name:'江苏', value:491},
                        {name:'广东', value:156, selected:true}
                    ]
                },
                {
                    name:'全国设备分布比例',
                    type:'pie',
                    roseType : 'area',
                    tooltip: {
                        trigger: 'item',
                        formatter: "{a} <br/>{b} : {c} ({d}%)"
                    },
                    center: [document.getElementById('main').offsetWidth - 250, 225],
                    radius: [30, 120],
                    data:[
                        {name: '北京', value: 224},
                        {name: '上海', value: 260},
                        {name: '广东', value: 156}
                    ]
                }
            ],
            animation: false
        };

        myChart.setOption(option, true);

        // var ecConfig = require('echarts/config');
        // var ecConfig = echarts.config
        // myChart.on(ecConfig.EVENT.MAP_SELECTED, function (param){
        //     var selected = param.selected;
        //     var mapSeries = option.series[0];
        //     var data = [];
        //     var legendData = [];
        //     var name;
        //     for (var p = 0, len = mapSeries.data.length; p < len; p++) {
        //         name = mapSeries.data[p].name;
        //         //mapSeries.data[p].selected = selected[name];
        //         if (selected[name]) {
        //             data.push({
        //                 name: name,
        //                 value: mapSeries.data[p].value
        //             });
        //             legendData.push(name);
        //         }
        //     }
        //     option.legend.data = legendData;
        //     option.series[1].data = data;
        //     myChart.setOption(option, true);
        // });
                            
                            
                    
    }
    render() {
        return (
            <div id="main" style={{ width: 1000, height: 600 }}></div>
        );
    }
}

export default EchartsTest;
import React, { Component, Fragment } from 'react';
import { connect } from 'dva';
import {
  Row,
  Col,
  Button,
  Icon,
  Card,
  Tabs,
  Table,
  Radio,
  DatePicker,
  Menu,
  Dropdown,
} from 'antd';
import numeral from 'numeral';

import styles from './Analysis.less';


@connect(({ alarm, loading }) => ({
  alarm,
  loading: loading.effects['alarm/fetchDaqAlarm'],
}))

export default class Alarm extends Component {


  componentDidMount() {
    // this.props.dispatch({
    //   type: 'survey/fetchCurrentPowerData',
    //   payload: {
    //     device_id: '20180704',
    //   },
    // });
    console.log('this.props')
    console.log(this.props);
    const device_id = this.props.match.params.device_id;

    console.log(device_id);

    this.props.dispatch({
        type: 'alarm/fetchDaqAlarm',
        payload: {
          device_id: device_id,
        },
      });


    this.timer = setInterval(() => {

      this.props.dispatch({
        type: 'alarm/fetchDaqAlarm',
        payload: {
          device_id: device_id,
        },
      });

    }, 10000);

    console.log('component did mount!')
  }

  componentWillUnmount() {
    const { dispatch } = this.props;
    dispatch({
      type: 'alarm/clear',
    });
  }


  render() {

    const { alarm, loading } = this.props;
    console.log('--alarm,loading--')
    console.log(alarm)
    console.log(loading)
    const { deviceDaqAlarm } = alarm;

    return (
      <Fragment>
        
        <Row gutter={24}>
          {deviceDaqAlarm.map((item, i) => (
            <Col >
              <Button type={item.type} icon={item.icon} size='large'> {item.channel}</Button>
            </Col>
            )
          )}
        </Row>


      </Fragment>
    );
  }
}

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
  loading: loading.effects['alarm/fetchTemperatureAlarm'],
}))

export default class Alarm extends Component {


  componentDidMount() {
    // this.props.dispatch({
    //   type: 'survey/fetchCurrentPowerData',
    //   payload: {
    //     worker_name: '20180704',
    //   },
    // });
    console.log('this.props')
    console.log(this.props);
    const worker_name = this.props.match.params.worker_name;

    console.log(worker_name);


    this.timer = setInterval(() => {

      this.props.dispatch({
        type: 'alarm/fetchTemperatureAlarm',
        payload: {
          worker_name: worker_name,
        },
      });

    }, 3000);

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
    const { temperatureAlarm } = alarm;

    return (
      <Fragment>
        
        <Row gutter={24}>
          {temperatureAlarm.map((item, i) => (
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

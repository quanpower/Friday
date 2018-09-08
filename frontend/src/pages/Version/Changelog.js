import React, { PureComponent } from 'react';
import moment from 'moment';
import { connect } from 'dva';
import { Row, Col, Form, Card, Select, List } from 'antd';
import ReactMarkdown from 'react-markdown';


/* eslint react/no-array-index-key: 0 */
@connect(({ version, loading }) => ({
  version,
  loading: loading.effects['version/fetchChangelog'],
}))

export default class Changelog extends PureComponent {
  componentDidMount() {
    this.props.dispatch({
      type: 'version/fetchChangelog',
    });

    // this.timer = setInterval(() => {

    // this.props.dispatch({
    //   type: 'version/fetchChangelog',
    // });

    // }, 10000);
  }


  render() {
    const { changelog, loading } = this.props.version;

    return (
      <ReactMarkdown source={changelog} />
    );
  }
}

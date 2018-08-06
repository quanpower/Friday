import React, { PureComponent } from 'react';
import moment from 'moment';
import { connect } from 'dva';
import { Row, Col, Form, Card, Select, List } from 'antd';
import ReactMarkdown from 'react-markdown';


/* eslint react/no-array-index-key: 0 */
@connect(({ version, loading }) => ({
  version,
  loading: loading.effects['version/fetchTodolist'],
}))

export default class Changelog extends PureComponent {
  componentDidMount() {
    this.props.dispatch({
      type: 'version/fetchTodolist',
    });

    // this.timer = setInterval(() => {

    // this.props.dispatch({
    //   type: 'version/fetchChangelog',
    // });

    // }, 10000);
  }


  render() {
    const { todolist, loading } = this.props.version;

    return (
      <ReactMarkdown source={todolist} />
    );
  }
}

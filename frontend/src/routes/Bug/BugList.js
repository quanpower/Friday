import React, { Component, Fragment } from 'react';
import moment from 'moment';
import { connect } from 'dva';
import { 
  Row, 
  Col, 
  Card, 
  Select, 
  List, 
  Button, 
  Progress, 
  Icon, 
  Dropdown, 
  Menu, 
  Avatar, 
  Modal, 
  Form, 
  Input, 
  Radio,
  Tag,
} from 'antd';

import Ellipsis from 'components/Ellipsis';
import PageHeaderLayout from '../../layouts/PageHeaderLayout';
import styles from './BugList.less';
import bugImg from '../../assets/bug.jpeg';

const RadioButton = Radio.Button;
const RadioGroup = Radio.Group;
const { Search } = Input;

const ListContent = ({ data: { tester, gmt_report, severity, priority, status } }) => (
  <div className={styles.listContent}>
    <div className={styles.listContentItem}>
      <span>提交人</span>
      <p>{tester}</p>
    </div>
    <div className={styles.listContentItem}>
      <span>提交时间</span>
      <p>{moment(gmt_report).format('YYYY-MM-DD HH:mm')}</p>
    </div>
    <div className={styles.listContentItem}>
      <Tag color="red">red</Tag>
    </div>
  </div>
);


const FormItem = Form.Item;

const CollectionCreateForm = Form.create()(
  class extends Component {
    render() {
      const { visible, onCancel, onCreate, form } = this.props;
      const { getFieldDecorator } = form;
      return (
        <Modal
          visible={visible}
          title="提交新Bug"
          okText="提交"
          onCancel={onCancel}
          onOk={onCreate}
        >
          <Form layout="vertical">
            <FormItem label="Title">
              {getFieldDecorator('title', {
                rules: [{ required: true, message: 'Please input the title of collection!' }],
              })(
                <Input />
              )}
            </FormItem>
            <FormItem label="Description">
              {getFieldDecorator('description')(<Input type="textarea" />)}
            </FormItem>
            <FormItem className="collection-create-form_last-form-item">
              {getFieldDecorator('modifier', {
                initialValue: 'public',
              })(
                <Radio.Group>
                  <Radio value="public">Public</Radio>
                  <Radio value="private">Private</Radio>
                </Radio.Group>
              )}
            </FormItem>
          </Form>
        </Modal>
      );
    }
  }
);

/* eslint react/no-array-index-key: 0 */
@connect(({ bug, loading }) => ({
  bug,
  loading: loading.effects['bug/fetchBugs'],
}))

export default class Bug extends Component {


  state = {
    visible: false,
  };

  componentDidMount() {
    this.props.dispatch({
      type: 'bug/fetchBugs',
    });
  };

  showModal = () => {
    this.setState({ visible: true });
  };

  handleCancel = () => {
    this.setState({ visible: false });
  };

  handleCreate = () => {
    const form = this.formRef.props.form;
    form.validateFields((err, values) => {
      if (err) {
        return;
      }

      console.log('Received values of form: ', values);
      form.resetFields();
      this.setState({ visible: false });
    });
  };

  saveFormRef = (formRef) => {
    this.formRef = formRef;
  };

  render() {
    const { bug: { bugLists = [] }, loading } = this.props;

    console.log(this.props)
    console.log(bugLists)

    const Info = ({ title, value, bordered }) => (
      <div className={styles.headerInfo}>
        <span>{title}</span>
        <p>{value}</p>
        {bordered && <em />}
      </div>
    );

    const extraContent = (
      <div className={styles.extraContent}>
        <RadioGroup defaultValue="all">
          <RadioButton value="all">全部</RadioButton>
          <RadioButton value="progress">进行中</RadioButton>
          <RadioButton value="waiting">等待中</RadioButton>
        </RadioGroup>
        <Search className={styles.extraContentSearch} placeholder="请输入" onSearch={() => ({})} />
      </div>
    );

    const paginationProps = {
      showSizeChanger: true,
      showQuickJumper: true,
      pageSize: 5,
      total: 50,
    };

    const menu = (
      <Menu>
        <Menu.Item>
          <a>编辑</a>
        </Menu.Item>
        <Menu.Item>
          <a>删除</a>
        </Menu.Item>
      </Menu>
    );

    const MoreBtn = () => (
      <Dropdown overlay={menu}>
        <a>
          更多 <Icon type="down" />
        </a>
      </Dropdown>
    );



    return (
      <PageHeaderLayout>



      <div className={styles.standardList}>
        <Card bordered={false}>
          <Row>
            <Col sm={8} xs={24}>
              <Info title="新增Bug" value="8个" bordered />
            </Col>
            <Col sm={8} xs={24}>
              <Info title="本周处理中" value="3个" bordered />
            </Col>
            <Col sm={8} xs={24}>
              <Info title="本周完成数" value="12个" />
            </Col>
          </Row>
        </Card>

        <Card
          className={styles.listCard}
          bordered={false}
          title="Bug列表"
          style={{ marginTop: 24 }}
          bodyStyle={{ padding: '0 32px 40px 32px' }}
          extra={extraContent}
        >
      
          <Button type="dashed" onClick={this.showModal} style={{ width: '100%', marginBottom: 8 }} icon="plus">
            提交新Bug
          </Button>

          <CollectionCreateForm
          wrappedComponentRef={this.saveFormRef}
          visible={this.state.visible}
          onCancel={this.handleCancel}
          onCreate={this.handleCreate}
          />

          <List
            size="large"
            rowKey="id"
            loading={loading}
            pagination={paginationProps}
            dataSource={bugLists}
            renderItem={item => (
              <List.Item actions={[<a>编辑</a>, <MoreBtn />]}>
                <List.Item.Meta
                  avatar={<Avatar src={bugImg} shape="square" size="large" />}
                  // title={<a href={item.href}>{item.title}</a>}
                  title={<a href='#'>{item.title}</a>}
                  description={item.description}
                />
                <ListContent data={item} />
              </List.Item>
            )}
          />
        </Card>
      </div>


      </PageHeaderLayout>

    );
  }
}


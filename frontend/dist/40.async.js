(window['webpackJsonp'] = window['webpackJsonp'] || []).push([
  [40],
  {
    cfSo: function(e, t, a) {
      e.exports = { title: 'antd-pro-pages-profile-basic-profile-title' };
    },
    hJFj: function(e, t, a) {
      'use strict';
      var n = a('TqRt'),
        r = a('284h');
      Object.defineProperty(t, '__esModule', { value: !0 }), (t.default = void 0), a('IzEo');
      var l = n(a('bx4M'));
      a('g9YV');
      var d = n(a('wCAj'));
      a('/zsF');
      var i = n(a('PArb')),
        u = n(a('lwsE')),
        o = n(a('W8MJ')),
        c = n(a('a1gu')),
        f = n(a('Nsbk')),
        s = n(a('7W2i'));
      a('Awhp');
      var m,
        p,
        g = n(a('KrTs')),
        E = r(a('q1tI')),
        h = a('MuoO'),
        y = n(a('+kNj')),
        k = n(a('zHco')),
        v = n(a('cfSo')),
        x = y.default.Description,
        b = [
          { title: '\u65f6\u95f4', dataIndex: 'time', key: 'time' },
          { title: '\u5f53\u524d\u8fdb\u5ea6', dataIndex: 'rate', key: 'rate' },
          {
            title: '\u72b6\u6001',
            dataIndex: 'status',
            key: 'status',
            render: function(e) {
              return 'success' === e
                ? E.default.createElement(g.default, { status: 'success', text: '\u6210\u529f' })
                : E.default.createElement(g.default, {
                    status: 'processing',
                    text: '\u8fdb\u884c\u4e2d',
                  });
            },
          },
          { title: '\u64cd\u4f5c\u5458ID', dataIndex: 'operator', key: 'operator' },
          { title: '\u8017\u65f6', dataIndex: 'cost', key: 'cost' },
        ],
        I = ((m = (0, h.connect)(function(e) {
          var t = e.profile,
            a = e.loading;
          return { profile: t, loading: a.effects['profile/fetchBasic'] };
        })),
        m(
          (p = (function(e) {
            function t() {
              return (
                (0, u.default)(this, t),
                (0, c.default)(this, (0, f.default)(t).apply(this, arguments))
              );
            }
            return (
              (0, s.default)(t, e),
              (0, o.default)(t, [
                {
                  key: 'componentDidMount',
                  value: function() {
                    var e = this.props.dispatch;
                    e({ type: 'profile/fetchBasic' });
                  },
                },
                {
                  key: 'render',
                  value: function() {
                    var e = this.props,
                      t = e.profile,
                      a = e.loading,
                      n = t.basicGoods,
                      r = t.basicProgress,
                      u = [];
                    if (n.length) {
                      var o = 0,
                        c = 0;
                      n.forEach(function(e) {
                        (o += Number(e.num)), (c += Number(e.amount));
                      }),
                        (u = n.concat({ id: '\u603b\u8ba1', num: o, amount: c }));
                    }
                    var f = function(e, t, a) {
                        var r = { children: e, props: {} };
                        return a === n.length && (r.props.colSpan = 0), r;
                      },
                      s = [
                        {
                          title: '\u5546\u54c1\u7f16\u53f7',
                          dataIndex: 'id',
                          key: 'id',
                          render: function(e, t, a) {
                            return a < n.length
                              ? E.default.createElement('a', { href: '' }, e)
                              : {
                                  children: E.default.createElement(
                                    'span',
                                    { style: { fontWeight: 600 } },
                                    '\u603b\u8ba1'
                                  ),
                                  props: { colSpan: 4 },
                                };
                          },
                        },
                        {
                          title: '\u5546\u54c1\u540d\u79f0',
                          dataIndex: 'name',
                          key: 'name',
                          render: f,
                        },
                        {
                          title: '\u5546\u54c1\u6761\u7801',
                          dataIndex: 'barcode',
                          key: 'barcode',
                          render: f,
                        },
                        {
                          title: '\u5355\u4ef7',
                          dataIndex: 'price',
                          key: 'price',
                          align: 'right',
                          render: f,
                        },
                        {
                          title: '\u6570\u91cf\uff08\u4ef6\uff09',
                          dataIndex: 'num',
                          key: 'num',
                          align: 'right',
                          render: function(e, t, a) {
                            return a < n.length
                              ? e
                              : E.default.createElement('span', { style: { fontWeight: 600 } }, e);
                          },
                        },
                        {
                          title: '\u91d1\u989d',
                          dataIndex: 'amount',
                          key: 'amount',
                          align: 'right',
                          render: function(e, t, a) {
                            return a < n.length
                              ? e
                              : E.default.createElement('span', { style: { fontWeight: 600 } }, e);
                          },
                        },
                      ];
                    return E.default.createElement(
                      k.default,
                      { title: '\u57fa\u7840\u8be6\u60c5\u9875' },
                      E.default.createElement(
                        l.default,
                        { bordered: !1 },
                        E.default.createElement(
                          y.default,
                          {
                            size: 'large',
                            title: '\u9000\u6b3e\u7533\u8bf7',
                            style: { marginBottom: 32 },
                          },
                          E.default.createElement(
                            x,
                            { term: '\u53d6\u8d27\u5355\u53f7' },
                            '1000000000'
                          ),
                          E.default.createElement(
                            x,
                            { term: '\u72b6\u6001' },
                            '\u5df2\u53d6\u8d27'
                          ),
                          E.default.createElement(
                            x,
                            { term: '\u9500\u552e\u5355\u53f7' },
                            '1234123421'
                          ),
                          E.default.createElement(x, { term: '\u5b50\u8ba2\u5355' }, '3214321432')
                        ),
                        E.default.createElement(i.default, { style: { marginBottom: 32 } }),
                        E.default.createElement(
                          y.default,
                          {
                            size: 'large',
                            title: '\u7528\u6237\u4fe1\u606f',
                            style: { marginBottom: 32 },
                          },
                          E.default.createElement(
                            x,
                            { term: '\u7528\u6237\u59d3\u540d' },
                            '\u4ed8\u5c0f\u5c0f'
                          ),
                          E.default.createElement(
                            x,
                            { term: '\u8054\u7cfb\u7535\u8bdd' },
                            '18100000000'
                          ),
                          E.default.createElement(
                            x,
                            { term: '\u5e38\u7528\u5feb\u9012' },
                            '\u83dc\u9e1f\u4ed3\u50a8'
                          ),
                          E.default.createElement(
                            x,
                            { term: '\u53d6\u8d27\u5730\u5740' },
                            '\u6d59\u6c5f\u7701\u676d\u5dde\u5e02\u897f\u6e56\u533a\u4e07\u5858\u8def18\u53f7'
                          ),
                          E.default.createElement(x, { term: '\u5907\u6ce8' }, '\u65e0')
                        ),
                        E.default.createElement(i.default, { style: { marginBottom: 32 } }),
                        E.default.createElement(
                          'div',
                          { className: v.default.title },
                          '\u9000\u8d27\u5546\u54c1'
                        ),
                        E.default.createElement(d.default, {
                          style: { marginBottom: 24 },
                          pagination: !1,
                          loading: a,
                          dataSource: u,
                          columns: s,
                          rowKey: 'id',
                        }),
                        E.default.createElement(
                          'div',
                          { className: v.default.title },
                          '\u9000\u8d27\u8fdb\u5ea6'
                        ),
                        E.default.createElement(d.default, {
                          style: { marginBottom: 16 },
                          pagination: !1,
                          loading: a,
                          dataSource: r,
                          columns: b,
                        })
                      )
                    );
                  },
                },
              ]),
              t
            );
          })(E.Component))
        ) || p),
        w = I;
      t.default = w;
    },
  },
]);

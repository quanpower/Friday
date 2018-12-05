var canvas =new fabric.Canvas('c'); //利用fabric找到我们的画布

        var fan1;
        fabric.Image.fromURL("{{ url_for('static', filename='images/fan1.png') }}", function(oImg) {
          oImg.set({
                left: 300,
                top: 200,
                originX:  'center',
                originY: 'center',
            });
          oImg.scale(0.1);
          canvas.add(oImg);
          // canvas.renderAll();

          fan1 = oImg;
        });


        var color = new fabric.Color('#1af').toRgb();
        console.log(color);

        var rect = new fabric.Rect({  //创建我们的正方形
            left:100,
            top:500,
            originY: 'bottom',
            fill:color,

            width:50,
            height:50
        });
        canvas.add(rect);//把我们创建好的正方形加到画布上

        var rect1 = new fabric.Rect({  //创建我们的正方形
            left:100,
            top:500,
            originY: 'bottom',
            opacity:0.2,
            // backgroundColor:'red',

            width:50,
            height:100
        });
        canvas.add(rect1);//把我们创建好的正方形加到画布上

        var text1 = new fabric.Text('65', {
            fontSize: 30,
            left:100,
            top:465,
            fill: 'white',
            originY: 'bottom',

        })

        //进行组合
        var group = new fabric.Group([rect, rect1, text1], {
            left: 150,
            top: 100,
            angle: 0
        })

        canvas.add(group);

        group.item(0).setFill('red');
        group.item(2).set({
            text: '75%',
        });


        var int=self.setInterval("clock()",100);

        function clock()
        {
         var curAngle = fan1.getAngle();
         var curHeight = rect.getHeight();
         fan1.setAngle(curAngle+15); 

         if (curHeight < 100)
          {
            curHeight += 1;
          }
        else
        {
          curHeight = 100;
        }

         rect.setHeight(curHeight);

        group.item(2).set({
            text: String(curHeight),
        });
         canvas.renderAll();
        document.getElementById("clock").value=t;
        }

        console.log(JSON.stringify(canvas.toJSON()));
        // console.log(canvas.toSVG());
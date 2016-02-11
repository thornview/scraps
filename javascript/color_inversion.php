<!doctype html>
<html>
<head>
    <title>
       ScRAtChpAd
    </title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
    <script>
        function pad(num)
        {
            if (num.length < 2)
            {
                num = "0" + num;
            }
            return num;
        }

        /**
         * @todo Sanitize inputs, 
         * @param num
         * @returns {*}
         */
        function hexInvert(num)
        {
            // Assumes six digit hexidecimal number with no hash.

            var r = parseInt(num.substring(0,2), 16);
            var g = parseInt(num.substring(2,4), 16);
            var b = parseInt(num.substring(4), 16);

            var r1 = pad((255 - r).toString(16));
            var g1 = pad((255 - g).toString(16));
            var b1 = pad((255 - b).toString(16));

            return r1 + g1 + b1;
        }

        $(document).ready(function(){
           $('#btn1').on('click', function(){
               var h = $('#in1').val();
               var out = hexInvert(h);
               $('#out1').html(out);
               h1 = "#" + h;
               out1 = "#" + out;
               $('#box1').css("background-color", h1);
               $('#box2').css("background-color", out1);
           });
        });

    </script>

    <style>
        .box {
            height: 100px;
            width: 100px;
            border: 1px solid #ccc;
            display: inline-block;
        }
    </style>

</head>
<body>
    <h1>Color Inversion</h1>
    <div class='container'>
<!-- ==== PUT STUFF HERE ============================================================== -->
        <h2>Hex Inversion</h2>

        <div class="box" id="box1"></div>
        <div class="box" id="box2"></div>
        <br>
        Start Value: <input id="in1"><br>
        End Value: <span class="outbox" id="out1"></span><br>
        <button id="btn1">Invert</button>


        <!-- ===== END OF PRETTY CONTAINER ==================================================== -->
    </div>
</body>
</html>

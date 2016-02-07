<!DOCTYPE HTML>
<html>
<head>
<title>Weave - Live Weather Data, Live Temperature, Live min temperature, live max temperature, live wind speed, live humidity, live pressure, live clouds percentage, live weather description</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="All live weather data, live weather, live pressure, live time, live zip code, live temperature, live humidity, live wind speed, live wind direction, live clouds percentage, live weather forcase, live weather description, live rainfall chances, based on your location, local pressure" />
<script type="applijewelleryion/x-javascript"> addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false); function hideURLbar(){ window.scrollTo(0,1); } </script>
<!-- Custom Theme files -->
<link href="style.css" rel='stylesheet' type='text/css' />	
<!-- Custom Theme files -->
<link href='//fonts.googleapis.com/css?family=Montserrat:700,400' rel='stylesheet' type='text/css'>
<!-- Custom Theme files -->
</head>
<body>
<!--main-->
     <h1>Weave</h1>
    <div class="main effect2"> 
    <div class="time-bg">
				<h3>{{city}}</h3>
			<p id="demo">{{region}}, {{country_code}}</p>
		   </div>
	     <div class="climate"> 
		    <div class="sunny">
				<img src="images/{{icon}}.png" alt="">
				<h3>{{description}}</h3>
				<h2>{{avg_temp}}°</h2>
			 </div>
			 <div class="west-chance">
						<div class="west-grids">
							<div class="west-left">
								<img src="images/pic2.png" alt="">
							</div>
							<div class="west-right">
								<h3>{{wind_speed}}</h3>
								<ul>
									<li>m/s</li>
									<li>{{wind_direction}}</li>
								</ul>
							</div>
							<div class="clearfix"></div>
						</div>
						<div class="west-grids">
							<div class="west-left">
								<img src="images/umbre.png" alt="">
							</div>
							<div class="west-right">
								<h4>{{cloud_cover}}%<span>CLOUDS</span></h4>
							</div>
							<div class="clear"></div>
						</div>
					<div class="clear"></div>
					<div class="west-grids">
							<div class="west-left">
								<img src="images/pressure.png" alt="">
							</div>
							<div class="west-right">
								<h3>{{pressure}}</h3>
								<ul>
									<li>mm</li>
									<li>Hg</li>
								</ul>
							</div>
							<div class="clearfix"></div>
						</div>
						<div class="west-grids">
							<div class="west-left">
								<img src="images/humidity.png" alt="">
							</div>
							<div class="west-right">
								<h4>{{humidity}}%<span>HUMIDITY</span></h4>
							</div>
							<div class="clear"></div>
						</div>
					<div class="clear"></div>
			</div>
			<div class="shades">
				<h3>{{min_temp}}° <span>MIN</span></h3>
				<ul>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
					<li></li>
					<div class="clear"></div>
				</ul>
				<h3>{{max_temp}}°<span>MAX</span></h3>
				<div class="clear"></div>
			</div>
		</div>
			<div class="time-bg">
				<h3>Time(GMT{{time_zone}})</h3>
			<p id="demo"><span id="time">{{local_time}}</span></p>
			
				<script>
				var myVar=setInterval(function(){myTimer()},1000);

				function myTimer() {
					var d = new Date();
					document.getElementById("time").innerHTML = d.toLocaleTimeString();
				}
				</script>
		   </div>
        </div>
	</div>
	<!--start-copyright-->
   		<div class="copy-right">
				<p> &copy; 2016 <a href="http://facebook.com/anivarth" target="_blank">Anivarth Peesapati</a>. All rights  Reserved | <a href="credits">Credits</a> | <a href="faq">F.A.Q</a> </p><br />
				<p>Your Location: {{city}}, {{region}}, {{country}}, {{zipcode}}</p>
		</div>
	<!--//end-copyright-->
</body>
</html>
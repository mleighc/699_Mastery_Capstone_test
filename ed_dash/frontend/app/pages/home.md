<body>
<div id="myarticle">
<h1>Welcome to FastAPI Starter</h1>
<p>
Please read <a href="https://levelup.gitconnected.com/building-a-website-starter-with-fastapi-92d077092864">my Medium article.</a>
</p>
<p>
This project uses <a href="https://fastapi.tiangolo.com/">FastAPI</a>, <a href="https://jinja.palletsprojects.com/en/2.11.x/">Jinja2</a>, and <a href="https://getbootstrap.com/docs/4.1/getting-started/introduction/">Bootstrap4</a>.
</p>
</div>
<div id="myplot"></div>
  <div id="myplot2"></div>
  <script>
  fetch('/plot')
    .then(function(response) { return response.json(); })
    .then(function(item) { return Bokeh.embed.embed_item(item); })
  </script>
  <script>
  fetch('/plot2')
    .then(function(response) { return response.json(); })
    .then(function(item) { return Bokeh.embed.embed_item(item, "myplot2"); })
  </script>
</body>
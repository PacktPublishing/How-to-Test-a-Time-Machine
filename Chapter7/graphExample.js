
d3.json("crawledData.json", function(d) {
    createChart(d);
});

function createChart(data) {
    // set the dimensions and margins of the graph
var margin = {top: 10, right: 30, bottom: 30, left: 40},
  width = 400 - margin.left - margin.right,
  height = 400 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("chart")
.append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
.append("g")
  .attr("transform",
        "translate(" + margin.left + "," + margin.top + ")");

 var link = svg.append("g")
    .selectAll("line")
    .data(data.links)
    .enter()
    .append("line")
    .style("stroke", "#777")

  var node = svg.append("g")
    .selectAll("g")
    .data(data.nodes)
    .enter().append("g")

  var circles = node.append("circle")
    .attr("r", 45)
      .style("fill", "#777777");
     
var lables = node.append("text")
      .text(function(d) {
        return d.id;
      })
      .style("font-size", 5)
      .style("text-anchor", "middle")

      
node.append("title")
      .text(function(d) { return d.id; });

  var simulation = d3.forceSimulation()            
      .force("link", d3.forceLink()                               
            .id(function(d) { return d.id; })                           
      )
      .force("charge", d3.forceManyBody().strength(-2500))        
      .force("center", d3.forceCenter(width / 2, height / 2))    

      simulation
      .nodes(data.nodes)
      .on("end", ticked);

  simulation.force("link")
      .links(data.links);

  function ticked() {
    link
        .attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });
    node
        .attr("transform", function(d) {
          return "translate(" + d.x + "," + d.y + ")";
        })
  }

};
var width = 400  
    height = 400
var outerRadius = Math.min(width, height) / 2 - 30 
var svg = d3.select("chart")  
  .append("svg")  
    .attr("width", width)  
    .attr("height", height)  
  .append("g")  
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");  

d3.json("testcases.json", function(d) {
    createChart(d);
});

function createChart(rows) {
var data = rows;
var color = d3.scaleOrdinal()  
  .domain(data)  
  .range(["#A8DBA8", "#CFF09E", "#79BD9A"])
  // add more colours if we have more cols

var pie = d3.pie()  
  .value(function(d) {return d.value; })  
var pie_data = pie(d3.entries(data))  

// create data
svg  
  .selectAll('div')  
  .data(pie_data)  
  .enter()
  .append('path')  
  .attr('d', d3.arc()  
    .innerRadius(0)  
    .outerRadius(outerRadius)
  )  
  .attr('fill', function(d){ return(color(d.data.key)) })  
  .attr("stroke", "black")  
  .style("stroke-width", "2px")  
  .style("opacity", 0.6)  

//add labels
svg
  .selectAll('div')
  .data(pie_data)
  .enter()
  .append('text')
  .text(function(d){ return d.data.key})
  .attr("transform", function(d) { 
      return "translate(" + d3.arc()
                            .innerRadius(0)
                            .outerRadius(outerRadius).centroid(d) 
                           + ")";  })
  .style("text-anchor", "middle")
  .style("font-size", 20)
}
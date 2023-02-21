window.onload = function () {


var options = {
	title: {
		text: "Desktop OS Market Share in 2017"
	},
	subtitles: [{
		text: "As of November, 2017"
	}],
	animationEnabled: true,
	data: [{
		type: "pie",
		startAngle: 0,
		toolTipContent: "<b>{label}</b>: {y}%",
		showInLegend: "true",
		legendText: "{label}",
		indexLabelFontSize: 16,
		indexLabel: "{label} - {y}%",
		dataPoints: [
			{ y: a1, label: l1 },
			{ y: a2, label: l2 },
			{ y: a3, label: l3 },
			{ y: a4, label: l4 },
			{ y: a5, label: l5 },
		]
	}]
};
$("#chartContainer").CanvasJSChart(options);

}

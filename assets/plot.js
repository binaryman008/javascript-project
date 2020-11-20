fetch("assets/company_data.json")
    .then(res => res.json())
    .then(data => {
        var results = Object.entries(data);
        var capitals = []
        var categoriesList = []
        for (var result of results) {
            capitals.push(result[1]);
            categoriesList.push(result[0]);
        }
        Highcharts.chart('container', {
            chart: {
                type: 'bar'
            },
            title: {
                text: 'Authorized Capital in terms of amount'
            },
            xAxis: {
                title: {
                    text: 'Capital'
                },
                categories: categoriesList
            },
            yAxis: {
                title: {
                    text: 'Number of Companies'
                }
            },
            series: [{
                name: 'Capital',
                data: capitals
            }]
        });
    });

fetch("assets/company_registration_by_year.json")
    .then(res => res.json())
    .then(data => {
        var results = Object.entries(data);
        var capitals = []
        var categoriesList = []
        for (var result of results) {
            capitals.push(result[1]);
            categoriesList.push(result[0]);
        }
        Highcharts.chart('container-2', {
            chart: {
                type: 'bar'
            },
            title: {
                text: 'Number of Company Registrations year-wise from 2001-2011'
            },
            xAxis: {
                title: {
                    text: 'Year of Registration'
                },
                categories: categoriesList
            },
            yAxis: {
                title: {
                    text: 'Number of Companies'
                }
            },
            series: [{
                name: 'companies',
                data: capitals
            }]
        });
    });

fetch("assets/top_10_principal_business_activity.json")
    .then(res => res.json())
    .then(data => {
        var results = Object.entries(data);
        var capitals = []
        var categoriesList = []
        for (var result of results) {
            capitals.push(result[1]);
            categoriesList.push(result[0]);
        }
        Highcharts.chart('container-3', {
            chart: {
                type: 'bar'
            },
            title: {
                text: 'Top 10 Principal Business Activity'
            },
            xAxis: {
                title: {
                    text: 'Principal Business Activity'
                },
                categories: categoriesList
            },
            yAxis: {
                title: {
                    text: 'Number of Companies'
                }
            },
            series: [{
                name: 'Number of Companies',
                data: capitals
            }]
        });
    });

fetch("assets/stacked_plot.json")
    .then(res => res.json())
    .then(data => {
        var results = Object.entries(data);
        var capitals = []
        var categoriesList = []
        for (var result of results) {
            capitals.push(result[1]);
            categoriesList.push(result[0]);
        }
        var activities = [
            "Agriculture and Allied Activities",
            "Trading",
            "Manufacturing (Metals & Chemicals, and products thereof)",
            "Finance",
            "Construction"
        ]
        var result = []
        for (var i = 0; i < activities.length; i++) {
            var obj = {}
            obj["name"] = activities[i]
            obj["data"] = []
            for (var j = 0; j < capitals.length; j++) {
                obj.data.push(capitals[j][i]);
            }
            result.push(obj);
        }
        Highcharts.chart('container-4', {
            chart: {
                type: 'bar'
            },
            title: {
                text: 'Principal Business Activities in Maharashtra from 1990 to 1999'
            },
            xAxis: {
                title: { text: 'Years' },
                categories: categoriesList
            },
            yAxis: {
                title: {
                    text: 'Total Companies'
                }
            },
            series: result
        });
    });
System.register(["@angular/core", "@angular/router", "@angular/http", "leaflet", "angular2-modal", "./risk-graph.service", "./modals/asset-info/asset.info.modal.service", "./modals/asset-info/asset.info.modal", "./modals/threat-info/threat.info.modal", "./modals/action-modal/courses.action.modal"], function (exports_1, context_1) {
    "use strict";
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var __moduleName = context_1 && context_1.id;
    var core_1, router_1, http_1, L, angular2_modal_1, risk_graph_service_1, asset_info_modal_service_1, asset_info_modal_1, threat_info_modal_1, courses_action_modal_1, RiskGraphComponent;
    return {
        setters: [
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (router_1_1) {
                router_1 = router_1_1;
            },
            function (http_1_1) {
                http_1 = http_1_1;
            },
            function (L_1) {
                L = L_1;
            },
            function (angular2_modal_1_1) {
                angular2_modal_1 = angular2_modal_1_1;
            },
            function (risk_graph_service_1_1) {
                risk_graph_service_1 = risk_graph_service_1_1;
            },
            function (asset_info_modal_service_1_1) {
                asset_info_modal_service_1 = asset_info_modal_service_1_1;
            },
            function (asset_info_modal_1_1) {
                asset_info_modal_1 = asset_info_modal_1_1;
            },
            function (threat_info_modal_1_1) {
                threat_info_modal_1 = threat_info_modal_1_1;
            },
            function (courses_action_modal_1_1) {
                courses_action_modal_1 = courses_action_modal_1_1;
            }
        ],
        execute: function () {
            RiskGraphComponent = class RiskGraphComponent {
                constructor(route, vcRef, modal, riskGraphService, assetInfoService) {
                    this.route = route;
                    this.modal = modal;
                    this.riskGraphService = riskGraphService;
                    this.assetInfoService = assetInfoService;
                    this.layers = [
                        L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                            maxZoom: 18,
                            attribution: ''
                        })
                    ];
                    this.zoom = 15;
                    this.systemCoordinates = L.latLng(0, 0);
                    this.assetCoordinates = L.latLng(0, 0);
                    this.missionCoordinates = {
                        'latitude': 0,
                        'longitude': 0
                    };
                    this.noData = 1;
                    this.noDataLoaded = 1;
                    this.detailSection = 0;
                    this.networkSection = 0;
                    this.actionSection = 0;
                    this.hardwareAffected = [];
                    this.softwareAffected = [];
                    this.threatStatus = true;
                    this.coursesOfActionSelected = [];
                    this.allMissions = [];
                    this.missionId = "Please select...";
                    this.systemData = {
                        'geolocation': {
                            'latitude': 0,
                            'longitude': 0
                        }
                    };
                    this.missionData = {
                        'hHour': 0,
                        'missionLength': 0,
                        'name': "",
                        'objective': {}
                    };
                    this.systemName = "";
                    this.systemDescription = "";
                    this.assetRiskData = {};
                    this.riskTable = [];
                    this.riskTableSelected = [];
                    this.actionRows = [];
                    this.actionSelected = [];
                    this.actionColumns = [
                        {
                            name: 'Task ID'
                        },
                        {
                            name: 'Effect'
                        },
                        {
                            name: 'Objective'
                        },
                        {
                            name: 'Unit'
                        },
                        {
                            name: 'Time frame'
                        }
                    ];
                    this.unitList = [];
                    this.effectsList = [];
                    this.objectiveList = [];
                    this.timeFrame = 0;
                    this.selectedDescription = "";
                    this.selectedObjective = {
                        'name': "",
                        'id': ""
                    };
                    this.selectedUnit = {
                        'name': "",
                        'id': "",
                        'affiliation': ""
                    };
                    this.startTime = 0;
                    this.endTime = 0;
                    this.riskAnalysis = [];
                    this.risks = [];
                    this.hostileResponses = [];
                    this.actionsList = [];
                    this.evaluatedActions = 0;
                    this.coursesOfAction = [];
                    this.comparison = [];
                    this.selectedComparativeCOA = {};
                    this.comparativeStatics = 0;
                    this.radarChartLabels = [
                        'Risk change',
                        'Probability',
                        'Total time taken',
                        'Personnel'
                    ];
                    this.radarChartData = [];
                    this.radarChartType = 'radar';
                    this.repeatedCOA = 0;
                    this.dominatedStrategies = [];
                    this.comparativeCOAs = [];
                    this.missionType = [
                        'Offensive',
                        'Defensive'
                    ];
                    this.selectedMissionType = 'offensive';
                    this.dominated = [];
                    this.undominated = [];
                    this.recommendedRows = [];
                    this.doughnutChartLabels = [
                        'Critical',
                        'High',
                        'Medium',
                        'Low',
                        'Very low'
                    ];
                    this.doughnutChartColor = [{
                            backgroundColor: [
                                "#f20046",
                                "#ff0021",
                                "#f89444",
                                "#00d565",
                                "#00aee1"
                            ]
                        }
                    ];
                    this.doughnutChartData = [0, 0, 0, 0, 0];
                    this.doughnutChartType = 'doughnut';
                    this.doughnutOptions = {
                        'cutoutPercentage': 80
                    };
                    this.compareRestrictions = 0;
                    this.compareMissionTime = 0;
                    this.comparePersonnel = 0;
                    this.compareProbability = 0;
                    this.unattainableStrategies = [];
                    this.numberOfAssets = 0;
                    this.numberOfCyberAssets = 0;
                    this.numberOfPhysicalAssets = 0;
                    this.numberOfThreats = 0;
                    this.numberOfVulnerabilities = 0;
                    this.maxAsset = {
                        'riskLabel': "",
                        'riskScore': 0,
                        'name': ""
                    };
                    this.selectedCoaName = '';
                    this.selectedTaskId = '';
                    this.currentTaskIds = [];
                    this.selectedTaskDependencies = [];
                    this.usedTaskId = 0;
                    this.taskSubmitted = 0;
                    this.hasTaskDependents = 0;
                    this.taskDependents = "";
                    this.tasksToDelete = [];
                    this.selectedRiskGraphCOA = "Initial risk profile";
                    this.riskGraphCOAs = [
                        "Initial risk profile"
                    ];
                    this.riskGraphGenerated = 0;
                    this.assetRiskChanges = [];
                    this.viewGanttChart = 0;
                    this.viewDependencyTree = 1;
                    this.estimatedTimeFrame = 0;
                    this.tooFarAway = {};
                    this.tooFarAction = {};
                    this.missionLength = 720;
                    this.taskTime = {};
                    this.missionLengthExceeded = 0;
                    this.loadingMission = false;
                    modal.defaultViewContainer = vcRef;
                }
                ;
                ngOnInit() {
                    this.riskGraphService.getAllMissions()
                        .subscribe(missions => {
                        if (missions.length > 0) {
                            this.noData = 0;
                            this.allMissions = missions;
                        }
                        ;
                    });
                    this.getEffectsList();
                }
                ;
                calculateEstimatedTime() {
                    var taskData = [{
                            'taskId': this.selectedTaskId,
                            'effect': this.selectedEffect,
                            'objective': this.selectedObjective['id'],
                            'actor': this.selectedUnit['id']
                        }];
                    this.riskGraphService.getEstimatedTime(this.systemId, taskData).subscribe(estimatedTimes => {
                        var n = estimatedTimes[this.selectedTaskId]['estimatedTime'];
                        this.estimatedTimeFrame = this.twoDP(n);
                    });
                }
                ;
                twoDP(n) {
                    if (Number(n) === n && n % 1 !== 0) {
                        return n.toFixed(2);
                    }
                    else {
                        return n;
                    }
                    ;
                }
                ;
                selectDependencyTree() {
                    this.viewDependencyTree = 1;
                    this.viewGanttChart = 0;
                    setTimeout(() => {
                        this.generateDependencyGraph(this.actionRows);
                    }, 1);
                }
                ;
                selectGanttChart() {
                    this.viewGanttChart = 1;
                    this.viewDependencyTree = 0;
                    setTimeout(() => {
                        google.charts.setOnLoadCallback(() => this.drawGanttChart(this.actionRows, this.missionData));
                    }, 1);
                }
                ;
                getGoogle() {
                    return google;
                }
                ;
                drawGanttChart(taskData, missionData) {
                    function toMilliseconds(minutes) {
                        return minutes * 60 * 1000;
                    }
                    ;
                    function taskDataToGanttData(taskData, hHour) {
                        var ganttData = [];
                        for (let i = 0; i < taskData.length; i++) {
                            ganttData.push([
                                taskData[i]['name'],
                                taskData[i]['effect'] + ' ' + taskData[i]['objective']['entityName'],
                                taskData[i]['assignee']['entityName'],
                                new Date(hHour + toMilliseconds(taskData[i]['start'])),
                                new Date(hHour + toMilliseconds(taskData[i]['end'])),
                                null,
                                100,
                                taskData[i]['dependencies'].toString()
                            ]);
                        }
                        ;
                        return ganttData;
                    }
                    ;
                    this.ganttData = new google.visualization.DataTable();
                    this.ganttData.addColumn('string', 'Task ID');
                    this.ganttData.addColumn('string', 'Task Name');
                    this.ganttData.addColumn('string', 'Unit');
                    this.ganttData.addColumn('date', 'Start');
                    this.ganttData.addColumn('date', 'End');
                    this.ganttData.addColumn('number', 'Duration');
                    this.ganttData.addColumn('number', 'Percent Complete');
                    this.ganttData.addColumn('string', 'Dependencies');
                    this.ganttData.addRows(taskDataToGanttData(taskData, missionData['hHour']));
                    this.ganttOptions = {
                        gantt: {
                            innerGridHorizLine: {
                                stroke: '#DCDCDC',
                                strokeWidth: 1
                            },
                            innerGridTrack: {
                                fill: '#FFF'
                            },
                            innerGridDarkTrack: {
                                fill: '#FFF'
                            },
                            labelStyle: {
                                fontName: 'Noto Sans',
                                fontSize: 12,
                                color: '#757575'
                            }
                        }
                    };
                    this.ganttChart = this.createGanttChart(document.getElementById('chart_taskGantt'));
                    this.ganttChart.draw(this.ganttData, this.ganttOptions);
                }
                ;
                customCandlestickTooltip(task, estimatedTimes, e) {
                    return '<div style="background-color:#FFF; padding:5px 5px 5px 5px;">' +
                        '<h4 style="padding-bottom:5px; color:#00b0d7;"><strong>Task information</strong></h4>' +
                        '<table class="table" style="border-width:0px;">' +
                        '<tbody>' +
                        '<tr><td><strong>Task ID</strong></td><td>' + task['name'] + '</td></tr>' +
                        '<tr><td><strong>Effect</strong></td><td>' + task['effect'] + '</td></tr>' +
                        '<tr><td><strong>Objective</strong></td><td>' + this.assetIdToName(task['objective']) + '</td></tr>' +
                        '<tr><td><strong>Estimated</strong></td><td>' + this.twoDP(e) + ' hours</td></tr>' +
                        '<tr><td><strong>Max time</strong></td><td>' + this.twoDP(estimatedTimes['quartiles'][3]) + ' hours</td></tr>' +
                        '<tr><td><strong>Min time</strong></td><td>' + this.twoDP(estimatedTimes['quartiles'][0]) + ' hours</td></tr>' +
                        '</tbody>' +
                        '</table>' +
                        '</div>';
                }
                ;
                extractTimeData(estimatedTimes, courseOfAction) {
                    function allTasks(courseOfAction) {
                        var taskIds = [];
                        for (let i = 0; i < courseOfAction.length; i++) {
                            taskIds.push(courseOfAction[i]['taskId']);
                        }
                        ;
                        return taskIds;
                    }
                    ;
                    var timeData = [];
                    var taskIds = allTasks(courseOfAction);
                    for (let i = 0; i < taskIds.length; i++) {
                        timeData.push([
                            taskIds[i],
                            estimatedTimes[taskIds[i]]['quartiles'][0],
                            estimatedTimes[taskIds[i]]['quartiles'][1],
                            estimatedTimes[taskIds[i]]['quartiles'][2],
                            estimatedTimes[taskIds[i]]['quartiles'][3],
                            this.customCandlestickTooltip(courseOfAction[i], estimatedTimes[taskIds[i]], estimatedTimes[taskIds[i]]['estimatedTime'])
                        ]);
                    }
                    ;
                    return timeData;
                }
                ;
                drawCandlestickChart(estimatedTimes, courseOfAction) {
                    this.candlestickData = new google.visualization.DataTable();
                    this.candlestickData.addColumn('string', 'Date');
                    this.candlestickData.addColumn('number');
                    this.candlestickData.addColumn('number');
                    this.candlestickData.addColumn('number');
                    this.candlestickData.addColumn('number');
                    this.candlestickData.addColumn({
                        type: 'string',
                        role: 'tooltip',
                        'p': {
                            'html': true
                        }
                    });
                    this.candlestickData.addRows(this.extractTimeData(estimatedTimes, courseOfAction));
                    this.candlestickOptions = {
                        legend: 'none',
                        tooltip: {
                            isHtml: true
                        },
                        height: 500,
                        width: 1000,
                        vAxis: {
                            title: 'Time (hours)'
                        },
                        hAxis: {
                            title: 'Task ID'
                        },
                        colors: ['#00b0d7']
                    };
                    this.candlestickChart = this.createCandlestickChart(document.getElementById('chart_timeCandlestick'));
                    this.candlestickChart.draw(this.candlestickData, this.candlestickOptions);
                }
                ;
                createGanttChart(element) {
                    return new google.visualization.Gantt(element);
                }
                ;
                createDataTable(array) {
                    return google.visualization.arrayToDataTable(array);
                }
                ;
                createCandlestickChart(element) {
                    return new google.visualization.CandlestickChart(element);
                }
                ;
                exitSystem() {
                    this.noDataLoaded = 1;
                    this.systemData = {
                        'geolocation': {
                            'latitude': 0,
                            'longitude': 0
                        }
                    };
                    this.numberOfPhysicalAssets = 0;
                    this.numberOfCyberAssets = 0;
                    this.systemId = "";
                    this.missionId = "Please select...";
                }
                ;
                toggleCompareRestrictions() {
                    if (this.compareRestrictions == 1) {
                        this.compareRestrictions = 0;
                    }
                    else {
                        this.compareRestrictions = 1;
                    }
                    ;
                }
                ;
                setComparisonResource(event, resource) {
                    var eventValue = event['target']['value'];
                    if (resource == 'personnel') {
                        this.comparePersonnel = eventValue;
                    }
                    else if (resource == 'missionTime') {
                        this.compareMissionTime = eventValue;
                    }
                    else if (resource == 'probability') {
                        this.compareProbability = eventValue;
                    }
                    ;
                }
                ;
                selectMissionType(event) {
                    var value = event['target']['value'];
                    this.selectedMissionType = value.toLowerCase();
                }
                ;
                showComparisonRadar() {
                    this.showRadar = 1;
                    this.showTables = 0;
                    this.showDominated = 0;
                    this.showRecommended = 0;
                }
                ;
                showComparisonTables() {
                    this.showTables = 1;
                    this.showRadar = 0;
                    this.showDominated = 0;
                    this.showRecommended = 0;
                }
                ;
                showDominatedStrategies() {
                    this.showDominated = 1;
                    this.showRadar = 0;
                    this.showTables = 0;
                    this.showRecommended = 0;
                }
                ;
                showRecommendedStrategies() {
                    this.showRecommended = 1;
                    this.showDominated = 0;
                    this.showRadar = 0;
                    this.showTables = 0;
                }
                ;
                chartClicked(e) {
                    console.log(e);
                }
                ;
                chartHovered(e) {
                    console.log(e);
                }
                ;
                getEffectsList() {
                    this.effectsList = [];
                    this.assetInfoService.getEffects()
                        .subscribe(effectList => {
                        this.effectsList = effectList;
                        this.selectedEffect = effectList[0];
                    });
                }
                ;
                comparativedCOA(event, comparison) {
                    this.selectedComparativeCOA[comparison + 1] = event['target']['value'];
                }
                ;
                selectTimeFrame(event) {
                    this.timeFrame = event['target']['value'];
                }
                ;
                selectStartTime(event) {
                    this.startTime = event['target']['value'];
                }
                ;
                selectEndTime(event) {
                    this.endTime = event['target']['value'];
                }
                ;
                deleteAllCOAActions() {
                    this.riskGraphService.getMissionData(this.missionData['id'])
                        .subscribe(missionData => {
                        this.missionData = missionData;
                        for (let i = 0; i < missionData['coAs'].length; i++) {
                            if (missionData['coAs'][i]['name'] == this.selectedCOA) {
                                for (let i = 0; i < this.actionRows.length; i++) {
                                    this.riskGraphService.deleteTask(this.missionData['id'], missionData['coAs'][i]['id'], this.actionRows[i]['id']).subscribe(deletedAction => {
                                        this.populateActionTable(this.selectedCOA);
                                    });
                                }
                                ;
                            }
                            ;
                        }
                        ;
                    });
                }
                ;
                selectEffect(event) {
                    var effect = event['target']['value'];
                    this.selectedEffect = effect;
                    this.calculateEstimatedTime();
                }
                ;
                selectTaskId(event) {
                    this.selectedTaskId = event['target']['value'];
                }
                ;
                selectTaskDescription(event) {
                    this.selectedDescription = event['target']['value'];
                }
                ;
                selectCoaName(event) {
                    this.selectedCoaName = event['target']['value'];
                }
                ;
                selectDependencies() {
                    this.selectedTaskDependencies = [
                        event['target']['value']
                    ];
                }
                ;
                selectObjective(event) {
                    var objectiveName = event['target']['value'];
                    for (var i = 0; i < this.objectiveList.length; i++) {
                        if (objectiveName === this.objectiveList[i]['name']) {
                            this.selectedObjective = {
                                'name': objectiveName,
                                'id': this.objectiveList[i]['id']
                            };
                        }
                        ;
                    }
                    ;
                    this.calculateEstimatedTime();
                }
                ;
                selectUnit(event) {
                    var unitName = event['target']['value'];
                    for (var i = 0; i < this.unitList.length; i++) {
                        if (unitName === this.unitList[i]['name']) {
                            this.selectedUnit = {
                                'name': unitName,
                                'id': this.unitList[i]['id'],
                                'affiliation': this.unitList[i]['affiliation']
                            };
                        }
                        ;
                    }
                    ;
                    this.calculateEstimatedTime();
                }
                ;
                hasTaskIdHasBeenUsed(taskId, tasks) {
                    return false;
                    // for (let i = 0; i < tasks.length; i++) {
                    //   if (tasks[i]['name'] == taskId) {
                    //     return true;
                    //   };
                    // };
                    // return false;
                }
                ;
                submitTaskForm() {
                    this.taskSubmitted = 0;
                    this.selectedUnit = {
                        'name': this.unitList[0]['name'],
                        'id': this.unitList[0]['id'],
                        'affiliation': this.unitList[0]['affiliation']
                    };
                    this.selectedObjective = {
                        'name': this.objectiveList[0]['name'],
                        'id': this.objectiveList[0]['id']
                    };
                    this.selectedEffect = this.effectsList[0];
                    this.selectedTaskDependencies = [];
                    this.calculateEstimatedTime();
                }
                ;
                whereAmI(unitId, taskData) {
                    for (let i = 0; i < taskData.length; i++) {
                        taskData[i];
                    }
                    ;
                }
                ;
                submitNewAction() {
                    for (let i = 0; i < this.missionData['coAs'].length; i++) {
                        if (this.missionData['coAs'][i]['name'] == this.selectedCOA) {
                            var coaId = this.missionData['coAs'][i]['id'];
                        }
                        ;
                    }
                    ;
                    var used = this.hasTaskIdHasBeenUsed(this.selectedTaskId, this.actionRows);
                    if (used) {
                        this.usedTaskId = 1;
                    }
                    else {
                        this.usedTaskId = 0;
                        this.whereAmI(this.selectedUnit['id'], this.actionRows);
                        this.assetInfoService.getUnitDistance(this.systemId, this.selectedObjective['id'], this.selectedUnit['id'])
                            .subscribe(distance => {
                            var d = Number(distance['distance']);
                            var taskDependencies;
                            if (this.selectedTaskDependencies[0] == "None") {
                                taskDependencies = [];
                            }
                            else {
                                taskDependencies = this.selectedTaskDependencies;
                            }
                            ;
                            var actionData = {
                                'type': 'task',
                                'name': this.selectedTaskId,
                                'description': this.selectedDescription,
                                'effect': this.selectedEffect,
                                'objective': {
                                    'entityId': this.selectedObjective['id'],
                                    'entityType': 'asset'
                                },
                                'assignee': {
                                    'entityId': this.selectedUnit['id'],
                                    'entityType': 'unit'
                                },
                                'affiliation': this.selectedUnit['affiliation'],
                                'start': Number(this.startTime),
                                'end': Number(this.endTime)
                            };
                            if (actionData['effect'].toLowerCase() === 'move' || d < 250) {
                                this.riskGraphService.postTask(this.missionData['id'], coaId, actionData)
                                    .subscribe(postedAction => {
                                    this.taskSubmitted = 1;
                                    this.populateActionTable(this.selectedCOA);
                                });
                            }
                            else {
                                this.taskSubmitted = 2;
                                this.assetLocation(this.systemId, actionData['objective']);
                                this.assetLocation(this.systemId, actionData['unit']);
                                this.tooFarAway = {
                                    'distance': d,
                                    'time': Math.round((d / 3) * 100) / 100
                                };
                                this.tooFarAction = actionData;
                            }
                            ;
                        });
                    }
                    ;
                }
                ;
                submitTooFarTask() {
                    var actionRowLength = this.actionRows.length + 1;
                    var moveAction = {
                        'courseOfAction': this.selectedCOA,
                        'name': 'M' + actionRowLength.toString(),
                        'effect': 'MOVE',
                        'objective': this.selectedObjective['id'],
                        'unit': this.selectedUnit['id'],
                        'dependencies': [],
                        'timeFrame': Math.ceil(this.tooFarAway['time'])
                    };
                    this.tooFarAction['dependencies'].push('M1');
                    this.assetInfoService.postEffectsBasedAction(this.systemId, moveAction)
                        .subscribe(postedMoveAction => {
                        this.assetInfoService.postEffectsBasedAction(this.systemId, this.tooFarAction)
                            .subscribe(postedAction => {
                            this.taskSubmitted = 1;
                            this.populateActionTable(this.selectedCOA);
                        });
                    });
                }
                ;
                onMapReady(map) {
                    setTimeout(() => {
                        map.invalidateSize();
                    }, 1);
                }
                ;
                assetLocation(systemId, assetId) {
                    this.assetInfoService.getAssetLocation(systemId, assetId)
                        .subscribe(assetLocationData => {
                        this.assetCoordinates = L.latLng(assetLocationData['latitude'], assetLocationData['longitude']);
                        if (assetLocationData['layerType'] == 'polygon' || assetLocationData['layerType'] == 'polyline') {
                            this.layers.push(L.polygon(assetLocationData['drawing']));
                        }
                        else if (assetLocationData['layerType'] == 'circle' || assetLocationData['layerType'] == 'point') {
                            this.layers.push(L.circle(assetLocationData['drawing'], { radius: assetLocationData['radius'] }));
                        }
                        ;
                    });
                }
                ;
                navToDetailSection() {
                    this.detailSection = 1;
                    this.networkSection = 0;
                    this.actionSection = 0;
                }
                ;
                navToNetworkSection() {
                    this.networkSection = 1;
                    this.detailSection = 0;
                    this.actionSection = 0;
                    if (this.noDataLoaded == 0) {
                        this.getCOAList(this.missionData['id']);
                        this.assetRiskChanges = [];
                        this.selectedRiskGraphCOA = this.riskGraphCOAs[0];
                        this.riskGraphGenerated = 1;
                        // This is a complete hack
                        setTimeout(() => {
                            this.generateRiskGraph(this.systemId, this.systemData, this.assetRiskData, this.networkSection, this.missionData);
                        }, 1);
                    }
                    ;
                }
                ;
                navToActionSection() {
                    this.actionSection = 1;
                    this.detailSection = 0;
                    this.networkSection = 0;
                    if (this.noDataLoaded == 0) {
                        this.selectedCOA = this.coursesOfAction[0];
                        this.selectedComparativeCOA = {};
                        this.selectedComparativeCOA[0] = this.coursesOfAction[0];
                        this.resetTaskEvaluation();
                        this.populateActionTable(this.selectedCOA);
                        if (!this.googleLoaded) {
                            this.googleLoaded = true;
                            google.charts.load('current', {
                                packages: [
                                    'gantt',
                                    'corechart'
                                ]
                            });
                        }
                        ;
                    }
                    ;
                }
                ;
                getObjectiveList(assets) {
                    this.objectiveList = [];
                    for (var i = 0; i < assets.length; i++) {
                        this.objectiveList.push({
                            'name': assets[i]['name'],
                            'id': assets[i]['id']
                        });
                    }
                    ;
                    this.selectedObjective = {
                        'name': assets[0]['name'],
                        'id': assets[0]['id']
                    };
                }
                ;
                resetTaskEvaluation() {
                    this.evaluatedActions = 0;
                    this.actionsList = [];
                    this.hostileResponses = [];
                    this.risks = [];
                }
                ;
                generateTaskName(task) {
                    return task['effect'].substring(0, 3) + '_' +
                        task['assignee']['entityId'].substring(0, 3) + '_' +
                        task['start'];
                }
                ;
                populateActionTable(coa) {
                    this.riskGraphService.getMissionData(this.missionData['id'])
                        .subscribe(missionData => {
                        for (let i = 0; i < missionData['coAs'].length; i++) {
                            if (missionData['coAs'][i]['name'] == coa) {
                                var tasks = missionData['coAs'][i]['tasks'];
                            }
                            ;
                        }
                        ;
                        for (var i = 0; i < tasks.length; i++) {
                            if (tasks[i]['name'] == "") {
                                tasks[i]['name'] = this.generateTaskName(tasks[i]);
                            }
                            ;
                            tasks[i]['dependencies'] = [];
                            tasks[i]['timeFrame'] = tasks[i]['end'] - tasks[i]['start'];
                            for (var j = 0; j < this.unitList.length; j++) {
                                if (tasks[i]['assignee']['entityId'] == this.unitList[j]['id']) {
                                    tasks[i]['assignee']['entityName'] = this.unitList[j]['name'];
                                }
                                ;
                            }
                            ;
                            for (var j = 0; j < this.objectiveList.length; j++) {
                                if (tasks[i]['objective']['entityId'] == this.objectiveList[j]['id']) {
                                    tasks[i]['objective']['entityName'] = this.objectiveList[j]['name'];
                                }
                                ;
                            }
                            ;
                        }
                        ;
                        this.actionRows = tasks;
                        this.currentTaskIds = ["None"];
                        for (var i = 0; i < tasks.length; i++) {
                            this.currentTaskIds.push(tasks[i]['name']);
                        }
                        ;
                        if (this.viewDependencyTree == 1) {
                            this.generateDependencyGraph(this.actionRows);
                        }
                        ;
                        if (this.actionRows.length > 0) {
                            this.getMissionTime(this.missionData, tasks);
                        }
                        ;
                        if (this.viewGanttChart == 1) {
                            google.charts.setOnLoadCallback(() => this.drawGanttChart(this.actionRows, this.missionData));
                        }
                        ;
                    });
                }
                ;
                getMissionTime(missionData, taskData) {
                    function hoursToMillis(hours) {
                        return hours * 60 * 1000;
                    }
                    ;
                    var missionTaskData = {
                        'missionTime': this.missionLength,
                        'courseOfAction': taskData
                    };
                    this.riskGraphService.getMissionTimeAssessment(this.systemId, missionTaskData).subscribe(timeAssessment => {
                        var h = new Date(missionData['hHour']);
                        var z = new Date(missionData['hHour'] + hoursToMillis(timeAssessment['calculatedTotalTime']));
                        var timeOptions = {
                            weekday: 'long',
                            year: 'numeric',
                            month: 'long',
                            day: 'numeric',
                            hour: 'numeric',
                            minute: 'numeric'
                        };
                        this.hHour = h.toLocaleDateString('en-EN', timeOptions);
                        this.zHour = z.toLocaleDateString('en-EN', timeOptions);
                        this.taskTime = timeAssessment;
                        if (this.taskTime['exceedsTime']) {
                            this.missionLengthExceeded = 1;
                        }
                        else {
                            this.missionLengthExceeded = 0;
                        }
                        ;
                    });
                }
                ;
                assetIdToName(assetId) {
                    for (var i = 0; i < this.systemData['assets'].length; i++) {
                        if (this.systemData['assets'][i]['id'] == assetId) {
                            return this.systemData['assets'][i]['name'];
                        }
                        ;
                    }
                    ;
                }
                ;
                evaluateActions() {
                    this.resetTaskEvaluation();
                    this.evaluatedActions = 2;
                    var effectList = [];
                    this.riskAnalysis = [];
                    for (var i = 0; i < this.actionRows.length; i++) {
                        effectList.push({
                            'taskId': this.actionRows[i]['name'],
                            'effect': this.actionRows[i]['effect'],
                            'objective': this.actionRows[i]['objective']['entityId'],
                            'actor': this.actionRows[i]['assignee']['entityId'],
                            'timeFrame': this.actionRows[i]['timeFrame'],
                            'dependencies': this.actionRows[i]['dependencies']
                        });
                    }
                    ;
                    this.riskGraphService.getEstimatedTime(this.systemId, effectList)
                        .subscribe(estimatedTimes => {
                        this.evaluatedActions = 1;
                        setTimeout(() => {
                            google.charts.setOnLoadCallback(() => this.drawCandlestickChart(estimatedTimes, effectList));
                        }, 1);
                    });
                    this.riskGraphService.postEffects(this.systemId, effectList)
                        .subscribe(effectAnalysis => {
                        var riskAnalysis = effectAnalysis['assetRisk'];
                        var riskKeys = Object.keys(riskAnalysis);
                        for (var i = 0; i < riskKeys.length; i++) {
                            if (riskAnalysis[riskKeys[i]]['hostileResponses'] != null) {
                                var effects = [];
                                for (var j = 0; j < riskAnalysis[riskKeys[i]]['actions'].length; j++) {
                                    effects.push(Object.keys(riskAnalysis[riskKeys[i]]['actions'][j])[0]);
                                }
                                ;
                                this.risks.push({
                                    'assetId': riskKeys[i],
                                    'assetName': this.assetIdToName(riskKeys[i]),
                                    'risks': riskAnalysis[riskKeys[i]]['risks']
                                });
                                this.hostileResponses.push({
                                    'assetId': riskKeys[i],
                                    'assetName': this.assetIdToName(riskKeys[i]),
                                    'hostileResponses': riskAnalysis[riskKeys[i]]['hostileResponses']
                                });
                                this.actionsList.push({
                                    'assetId': riskKeys[i],
                                    'assetName': this.assetIdToName(riskKeys[i]),
                                    'actions': []
                                });
                                var actionLength = this.actionsList.length - 1;
                                for (var j = 0; j < effects.length; j++) {
                                    this.actionsList[actionLength]['actions'].push({
                                        'effect': effects[j],
                                        'acts': riskAnalysis[riskKeys[i]]['actions'][j][effects[j]]
                                    });
                                }
                                ;
                                var riskLength = this.risks.length - 1;
                                for (var j = 0; j < riskAnalysis[riskKeys[i]]['risks'].length; j++) {
                                    var riskChange = this.calculateRiskChange(riskKeys[i], riskAnalysis[riskKeys[i]]['risks'][j]['riskScore']);
                                    this.risks[riskLength]['risks'][j]['riskChange'] = riskChange;
                                    this.risks[riskLength]['risks'][j]['effect'] = effects[j];
                                }
                                ;
                            }
                            ;
                        }
                        ;
                        var genNet = this.actionRows;
                        for (let i = 0; i < genNet.length; i++) {
                            var taskObjective = genNet[i]['objective']['entityId'];
                            var assetActions = effectAnalysis['assetRisk'][taskObjective]['actions'];
                            for (let j = 0; j < assetActions.length; j++) {
                                var actionKey = Object.keys(assetActions[j])[0];
                                if (genNet[i]['effect'] == actionKey) {
                                    genNet[i]['riskScore'] = effectAnalysis['assetRisk'][taskObjective]['risks'][j]['likelihoodScore'];
                                }
                                ;
                            }
                            ;
                        }
                        ;
                        this.evaluatedActions = 1;
                        this.generateDependencyGraph(genNet);
                    });
                }
                ;
                calculateRiskChange(assetId, newRiskScore) {
                    for (var i = 0; i < this.riskTable.length; i++) {
                        if (this.riskTable[i]['id'] == assetId) {
                            var riskDifference = this.riskTable[i]['riskScore'] - newRiskScore;
                            return riskDifference;
                        }
                        ;
                    }
                    ;
                }
                ;
                selectCOA(coa) {
                    this.riskAnalysis = [];
                    this.selectedCOA = coa;
                    this.resetTaskEvaluation();
                    this.populateActionTable(coa);
                }
                ;
                deleteCourseOfAction() {
                    this.riskGraphService.getMissionData(this.missionData['id'])
                        .subscribe(missionData => {
                        this.missionData = missionData;
                        for (let i = 0; i < missionData['coAs'].length; i++) {
                            if (missionData['coAs'][i]['name'] == this.selectedCOA) {
                                this.riskGraphService.deleteCOA(this.missionData['id'], missionData['coAs'][i]['id'])
                                    .subscribe(response => {
                                    this.getCOAList(this.missionData['id']);
                                });
                            }
                            ;
                        }
                        ;
                    });
                }
                ;
                getSystemCoordinates(bbox) {
                    let coordinates = bbox.split(",");
                    let missionCoordinates = {
                        'longitude': (Number(coordinates[0]) + Number(coordinates[2])) / 2,
                        'latitude': (Number(coordinates[1]) + Number(coordinates[3])) / 2
                    };
                    return missionCoordinates;
                }
                ;
                selectMission(missionId) {
                    this.missionId = missionId;
                    this.noDataLoaded = 0;
                    this.detailSection = 0;
                    this.networkSection = 0;
                    this.actionSection = 0;
                    this.loadingMission = true;
                    this.riskGraphService
                        .getMissionData(missionId)
                        .subscribe(missionData => {
                        this.missionData = missionData;
                        this.systemId = missionData[0]['systems'][0]['id'];
                        this.riskGraphService
                            .getSystemData(this.systemId)
                            .subscribe(systemData => {
                            console.log(systemData);
                            this.systemCoordinates = L.latLng(systemData[0]['geolocation']['coordinates']['latitude'], systemData[0]['geolocation']['coordinates']['longitude']);
                            this.systemData = systemData[0];
                            this.numberOfAssets = this.systemData['assets'].length;
                            this.numberOfThreats = this.systemData['threats'].length;
                            this.numberOfVulnerabilities = this.systemData['vulnerabilities'].length;
                            for (let i = 0; i < this.numberOfAssets; i++) {
                                if (this.systemData['assets'][i]['assetType'] === 'Physical') {
                                    this.numberOfPhysicalAssets += 1;
                                }
                                else if (this.systemData['assets'][i]['assetType'] === 'Cyber') {
                                    this.numberOfCyberAssets += 1;
                                }
                                ;
                            }
                            ;
                            this.getObjectiveList(this.systemData['assets']);
                            this.riskGraphService.getMissionUnits()
                                .subscribe(unitList => {
                                this.unitList = [];
                                var availableUnits = this.getAvailableUnits(this.missionData['elements'], this.missionData['warningOrder']['taskOrg']['units']);
                                for (let i = 0; i < unitList.length; i++) {
                                    for (let j = 0; j < availableUnits.length; j++) {
                                        if (unitList[i]['id'] == availableUnits[j]) {
                                            this.unitList.push({
                                                'name': unitList[i]['name'],
                                                'id': unitList[i]['id'],
                                                'affiliation': unitList[i]['affiliation']
                                            });
                                        }
                                        ;
                                    }
                                    ;
                                }
                                ;
                                this.selectedUnit = {
                                    'name': this.unitList[0]['name'],
                                    'id': this.unitList[0]['id'],
                                    'affiliation': this.unitList[0]['affiliation']
                                };
                            });
                            this.riskGraphService.postSystemRiskAnalysis(this.systemId)
                                .subscribe(riskData => {
                                this.assetRiskData = riskData['assetRisk'];
                                this.assetRiskDoughnut(riskData['assetRisk']);
                                this.systemRiskTable(riskData['assetRisk'], systemData['assets']);
                                var assets = Object.keys(this.assetRiskData);
                                for (let i = 0; i < assets.length; i++) {
                                    if (this.assetRiskData[assets[i]]['risks'][0]['riskScore'] >= this.maxAsset['riskScore']) {
                                        this.maxAsset['riskScore'] = this.assetRiskData[assets[i]]['risks'][0]['riskScore'];
                                        this.maxAsset['riskLabel'] = this.assetRiskData[assets[i]]['risks'][0]['riskLabel'];
                                        this.maxAsset['name'] = this.assetIdToName(assets[i]);
                                        this.getMaxRiskColour(this.maxAsset['riskScore']);
                                    }
                                    ;
                                }
                                ;
                                this.navToDetailSection();
                                this.loadingMission = false;
                            });
                            this.getCOAList(this.missionData['id']);
                        });
                    });
                }
                ;
                getAvailableUnits(elements, taskOrgUnits) {
                    var units = taskOrgUnits;
                    for (let i = 0; i < elements.length; i++) {
                        if (elements[i]['entityType'] == 'unit') {
                            units.push(elements[i]['entityId']);
                        }
                        ;
                    }
                    ;
                    var uniqueUnits = units.filter((v, i, a) => a.indexOf(v) === i);
                    return uniqueUnits;
                }
                ;
                getMaxRiskColour(riskScore) {
                    if (riskScore >= 80) {
                        this.maxRiskColour = "#F20046";
                    }
                    else if (riskScore >= 60) {
                        this.maxRiskColour = "#FF0021";
                    }
                    else if (riskScore >= 40) {
                        this.maxRiskColour = "#F89444";
                    }
                    else if (riskScore >= 20) {
                        this.maxRiskColour = "#00D565";
                    }
                    else {
                        this.maxRiskColour = "#00AEE1";
                    }
                    ;
                }
                ;
                assetRiskDoughnut(assetRisk) {
                    var assets = Object.keys(assetRisk);
                    this.doughnutChartData = [0, 0, 0, 0, 0];
                    for (let i = 0; i < assets.length; i++) {
                        var riskLabel = assetRisk[assets[i]]['risks'][0]['riskLabel'];
                        if (riskLabel === 'Critical') {
                            this.doughnutChartData[0] += 1;
                        }
                        else if (riskLabel === 'High') {
                            this.doughnutChartData[1] += 1;
                        }
                        else if (riskLabel === 'Medium') {
                            this.doughnutChartData[2] += 1;
                        }
                        else if (riskLabel === 'Low') {
                            this.doughnutChartData[3] += 1;
                        }
                        else {
                            this.doughnutChartData[4] += 1;
                        }
                        ;
                    }
                    ;
                }
                ;
                getCOAList(missionId) {
                    this.coursesOfAction = [];
                    this.riskGraphCOAs = [
                        "Initial risk profile"
                    ];
                    this.selectedRiskGraphCOA = this.riskGraphCOAs[0];
                    this.riskGraphService.getMissionData(missionId)
                        .subscribe(missionData => {
                        if (missionData['coAs'].length > 0) {
                            for (let i = 0; i < missionData['coAs'].length; i++) {
                                this.riskGraphCOAs.push(missionData['coAs'][i]['name']);
                                this.coursesOfAction.push(missionData['coAs'][i]['name']);
                            }
                            ;
                        }
                        else {
                            this.riskGraphService.postCOA(missionData['id'], 'COA1')
                                .subscribe(response => {
                                this.coursesOfAction = [
                                    'COA1'
                                ];
                            });
                        }
                        ;
                        this.selectCOA(this.coursesOfAction[0]);
                    });
                }
                ;
                addCOA() {
                    this.riskGraphService.postCOA(this.missionData['id'], this.selectedCoaName).subscribe(response => {
                        this.coursesOfAction.push(this.selectedCoaName);
                        this.riskGraphService.getMissionData(this.missionData['id']).subscribe(missionData => {
                            this.missionData = missionData;
                        });
                    });
                    return;
                }
                ;
                systemRiskTable(assetRiskData, assetData) {
                    this.riskTable = [];
                    var assetKeys = Object.keys(assetRiskData);
                    for (var i = 0; i < assetKeys.length; i++) {
                        var assetName = "";
                        for (var j = 0; j < assetData.length; j++) {
                            if (assetData[j]['id'] == assetKeys[i]) {
                                assetName = assetData[j]['name'];
                            }
                            ;
                        }
                        ;
                        this.riskTable.push({
                            'assetName': assetName,
                            'id': assetKeys[i],
                            'impact': assetRiskData[assetKeys[i]]['risks'][0]['impactLabel'],
                            'criticality': assetRiskData[assetKeys[i]]['risks'][0]['criticalityLabel'],
                            'risk': assetRiskData[assetKeys[i]]['risks'][0]['riskLabel'],
                            'riskScore': assetRiskData[assetKeys[i]]['risks'][0]['riskScore']
                        });
                    }
                    ;
                }
                ;
                startComparativeStatics() {
                    this.selectedComparativeCOA = {};
                    this.selectedComparativeCOA[0] = this.coursesOfAction[0];
                    this.resetComparativeStatics();
                }
                ;
                resetComparativeStatics() {
                    this.comparison = [];
                    this.comparativeCOAs = [0];
                    this.comparativeStatics = 0;
                    this.compareRestrictions = 0;
                }
                ;
                addComparativeCOA() {
                    var comparativeCOALength = this.comparativeCOAs.length;
                    this.comparativeCOAs.push(comparativeCOALength);
                }
                ;
                compareCOAs() {
                    this.comparativeStatics = 0;
                    var COAs = [];
                    var comparedCOAs = {};
                    var numberOfCOAs = Object.keys(this.selectedComparativeCOA).length;
                    this.radarChartData = [];
                    for (let i = 0; i < numberOfCOAs; i++) {
                        if (COAs.includes(this.selectedComparativeCOA[i])) {
                            this.repeatedCOA = 1;
                            return;
                        }
                        else {
                            COAs.push(this.selectedComparativeCOA[i]);
                        }
                        ;
                    }
                    ;
                    this.dominated = [];
                    this.undominated = [];
                    this.repeatedCOA = 0;
                    this.comparativeStatics = 2;
                    comparedCOAs['coursesOfAction'] = [];
                    var restrictions = {};
                    if (this.compareRestrictions == 1) {
                        restrictions = {
                            'missionTime': Number(this.compareMissionTime),
                            'personnel': Number(this.comparePersonnel),
                            'probability': Number(this.compareProbability)
                        };
                    }
                    ;
                    for (let i = 0; i < numberOfCOAs; i++) {
                        var comparativeEffectList = [];
                        for (let j = 0; j < this.missionData['coAs'].length; j++) {
                            if (this.missionData['coAs'][j]['name'] == this.selectedComparativeCOA[i]) {
                                var courseOfAction = {};
                                courseOfAction['name'] = this.missionData['coAs'][j]['name'];
                                courseOfAction['id'] = this.missionData['coAs'][j]['id'];
                                courseOfAction['tasks'] = [];
                                for (let k = 0; k < this.missionData['coAs'][j]['tasks'].length; k++) {
                                    courseOfAction['tasks'].push({
                                        'taskId': this.generateTaskName(this.missionData['coAs'][j]['tasks'][k]),
                                        'effect': this.missionData['coAs'][j]['tasks'][k]['effect'],
                                        'objective': this.missionData['coAs'][j]['tasks'][k]['objective']['entityId'],
                                        'actor': this.missionData['coAs'][j]['tasks'][k]['assignee']['entityId'],
                                        'timeFrame': this.missionData['coAs'][j]['tasks'][k]['end'] - this.missionData['coAs'][j]['tasks'][k]['start'],
                                        'dependencies': []
                                    });
                                }
                                ;
                            }
                            ;
                        }
                        ;
                        comparedCOAs['coursesOfAction'].push(courseOfAction);
                    }
                    ;
                    if (Object.keys(comparedCOAs['coursesOfAction']).length == numberOfCOAs) {
                        comparedCOAs['missionType'] = this.selectedMissionType;
                        comparedCOAs['restrictions'] = restrictions;
                        this.riskGraphService.compareCOAs(this.systemId, comparedCOAs)
                            .subscribe(comparisonResults => {
                            this.comparison = comparisonResults['coaCost'];
                            if (this.comparison.length) {
                                this.dominatedStrategies = [];
                                this.recommendedStrategy = comparisonResults['recommendedStrategy'];
                                this.unattainableStrategies = comparisonResults['unattainableStrategies'];
                                var COAs = Object.keys(comparisonResults['dominatedStrategies']);
                                for (let i = 0; i < COAs.length; i++) {
                                    this.dominatedStrategies.push({
                                        'courseOfAction': COAs[i],
                                        'dominatedBy': comparisonResults['dominatedStrategies'][COAs[i]]
                                    });
                                }
                                ;
                                for (let i = 0; i < this.comparison.length; i++) {
                                    var dominatedBy = comparisonResults['dominatedStrategies'][this.comparison[i]['courseOfAction']];
                                    if (dominatedBy != null) {
                                        this.dominated.push(this.comparison[i]['courseOfAction']);
                                        this.comparison[i]['dominatedBy'] = dominatedBy.join(", ");
                                    }
                                    else {
                                        this.undominated.push(this.comparison[i]['courseOfAction']);
                                        this.comparison[i]['dominatedBy'] = 'Nothing';
                                    }
                                    ;
                                    this.comparison[i]['probabilityOfCompletion'] = Number(this.comparison[i]['probabilityOfCompletion'].toFixed(2));
                                    this.comparison[i]['probabilityLabel'] = this.getProbabilityLabel(this.comparison[i]['probabilityOfCompletion']);
                                    var data = {
                                        'data': [
                                            this.comparison[i]['totalRisk'],
                                            this.comparison[i]['probabilityOfCompletion'],
                                            this.comparison[i]['totalTime'],
                                            this.comparison[i]['unitsRequired']
                                        ],
                                        'label': this.comparison[i]['courseOfAction']
                                    };
                                    this.radarChartData.push(data);
                                }
                                ;
                                this.showComparisonRadar();
                                this.populateRecommendedTable(this.recommendedStrategy);
                            }
                            ;
                            this.comparativeStatics = 1;
                        });
                    }
                    ;
                }
                ;
                populateRecommendedTable(coa) {
                    this.recommendedRows = [];
                    for (let j = 0; j < this.missionData['coAs'].length; j++) {
                        if (this.missionData['coAs'][j]['name'] == coa) {
                            for (let k = 0; k < this.missionData['coAs'][j]['tasks'].length; k++) {
                                this.recommendedRows.push({
                                    'name': this.generateTaskName(this.missionData['coAs'][j]['tasks'][k]),
                                    'effect': this.missionData['coAs'][j]['tasks'][k]['effect'],
                                    'objective': this.missionData['coAs'][j]['tasks'][k]['objective']['entityId'],
                                    'actor': this.missionData['coAs'][j]['tasks'][k]['assignee']['entityId'],
                                    'timeFrame': this.missionData['coAs'][j]['tasks'][k]['end'] - this.missionData['coAs'][j]['tasks'][k]['start'],
                                    'dependencies': []
                                });
                            }
                            ;
                        }
                        ;
                    }
                    ;
                }
                ;
                getProbabilityLabel(probability) {
                    if (probability >= 80) {
                        return 'Very high';
                    }
                    else if (probability >= 60) {
                        return 'High';
                    }
                    else if (probability >= 40) {
                        return 'Medium';
                    }
                    else if (probability >= 20) {
                        return 'Low';
                    }
                    else {
                        return 'Very low';
                    }
                    ;
                }
                ;
                onClickActionTable(task) {
                    var actorId = task['assignee']['entityId'];
                    var objectiveId = task['objective']['entityId'];
                    var parentTasks = this.findAllParents(task['dependencies'][0], this.actionRows);
                    for (let i = 0; i < this.systemData['assets'].length; i++) {
                        if (this.systemData['assets'][i]['id'] == objectiveId) {
                            var objectiveData = this.systemData['assets'][i];
                        }
                        ;
                    }
                    ;
                    for (let i = 0; i < this.unitList.length; i++) {
                        if (this.unitList[i]['id'] == actorId) {
                            var actorData = this.unitList[i];
                        }
                        ;
                    }
                    ;
                    return this.modal.open(courses_action_modal_1.ActionWindow, new courses_action_modal_1.ActionWindowData(this.systemId, task, objectiveData, actorData, parentTasks, this.assetRiskData[objectiveId]['risks'][0]['riskScore']));
                }
                ;
                findDirectChildren(taskId, taskData) {
                    var taskChildren = [];
                    for (let i = 0; i < taskData.length; i++) {
                        if (taskData[i]['name'] == taskId) {
                            for (let j = 0; j < taskData.length; j++) {
                                if (taskData[j]['dependencies'].includes(taskId)) {
                                    taskChildren.push(taskData[j]['name']);
                                }
                                ;
                            }
                            ;
                        }
                        ;
                    }
                    ;
                    return taskChildren;
                }
                ;
                findAllChildren(taskId, taskData) {
                    var childTasks = [];
                    var allChildren = [taskId];
                    for (let j = 0; j < taskData.length; j++) {
                        var toAdd = [];
                        for (let i = 0; i < taskData.length; i++) {
                            var dependencies = taskData[i]['dependencies'];
                            if (dependencies.length > 0 &&
                                !dependencies.some(val => allChildren.indexOf(val) === -1)) {
                                toAdd.push(taskData[i]['name']);
                            }
                            ;
                        }
                        ;
                        if (toAdd.length > 0) {
                            allChildren = allChildren.concat(toAdd.filter(function (item) {
                                return allChildren.indexOf(item) < 0;
                            }));
                        }
                        ;
                        ;
                    }
                    ;
                    allChildren = allChildren.filter(e => e !== taskId);
                    for (let i = 0; i < allChildren.length; i++) {
                        for (let j = 0; j < taskData.length; j++) {
                            if (taskData[j]['name'] == allChildren[i]) {
                                childTasks.push(taskData[j]);
                            }
                            ;
                        }
                        ;
                    }
                    ;
                    return childTasks;
                }
                ;
                findAllParents(initialParent, taskData) {
                    var parentTasks = [];
                    var allParents = [initialParent];
                    for (let j = 0; j < taskData.length; j++) {
                        for (let i = 0; i < taskData.length; i++) {
                            if (allParents.includes(taskData[i]['name'])) {
                                if (taskData[i]['dependencies'].length > 0) {
                                    allParents.push(taskData[i]['dependencies'][0]);
                                }
                                ;
                                break;
                            }
                            ;
                        }
                        ;
                    }
                    ;
                    var allParents = allParents.filter((v, i, a) => a.indexOf(v) === i);
                    for (let i = 0; i < allParents.length; i++) {
                        for (let j = 0; j < taskData.length; j++) {
                            if (taskData[j]['name'] == allParents[i]) {
                                parentTasks.push(taskData[j]);
                            }
                            ;
                        }
                        ;
                    }
                    ;
                    return parentTasks;
                }
                ;
                findParent(taskId, taskData, rootNodeName) {
                    for (let i = 0; i < taskData.length; i++) {
                        if (taskData[i]['name'] == taskId) {
                            if (taskData[i]['dependencies'].length == 0) {
                                var dependencyName = rootNodeName;
                            }
                            else {
                                var dependencyName = taskData[i]['dependencies'][0];
                            }
                            ;
                            return dependencyName;
                        }
                        ;
                    }
                    ;
                }
                ;
                getChildren(directChildren, taskDetails) {
                    var children = [];
                    for (let i = 0; i < directChildren.length; i++) {
                        children.push(taskDetails[directChildren[i]]);
                    }
                    ;
                    return children;
                }
                ;
                getUnitName(unitId, unitData) {
                    for (let i = 0; i < unitData.length; i++) {
                        if (unitData[i]['id'] == unitId) {
                            return unitData[i]['name'];
                        }
                        ;
                    }
                    ;
                }
                ;
                findTaskDetails(taskId, taskData) {
                    for (let i = 0; i < taskData.length; i++) {
                        if (taskData[i]['name'] == taskId) {
                            if (taskData[i]['riskScore'] == undefined) {
                                var riskScore = undefined;
                            }
                            else {
                                var riskScore = taskData[i]['riskScore'];
                            }
                            return {
                                'objective': taskData[i]['objective'],
                                'objectiveId': taskData[i]['objectiveId'],
                                'unit': taskData[i]['unit'],
                                'unitId': taskData[i]['unitId'],
                                'effect': taskData[i]['effect'],
                                'dependencies': taskData[i]['dependencies'],
                                'timeFrame': taskData[i]['timeFrame'],
                                'riskScore': riskScore
                            };
                        }
                        ;
                    }
                    ;
                }
                ;
                convertTaskData(taskData, rootNodeName) {
                    var layer = [];
                    var taskDetails = {};
                    var rootChildren = [];
                    for (let i = 0; i < taskData.length; i++) {
                        if (taskData[i]['dependencies'].length == 0) {
                            layer.push(taskData[i]['name']);
                        }
                        ;
                    }
                    ;
                    var graphLayers = {
                        0: layer
                    };
                    for (let i = 0; i < Object.keys(graphLayers).length; i++) {
                        layer = [];
                        for (let j = 0; j < taskData.length; j++) {
                            if (graphLayers[i].includes(taskData[j]['dependencies'][0])) {
                                layer.push(taskData[j]['name']);
                            }
                            ;
                        }
                        ;
                        if (layer.length > 0) {
                            var k = i + 1;
                            graphLayers[k] = layer;
                        }
                        ;
                    }
                    ;
                    for (let i = Object.keys(graphLayers).length - 1; i >= 0; i--) {
                        for (let j = 0; j < graphLayers[i].length; j++) {
                            var directChildren = this.findDirectChildren(graphLayers[i][j], taskData);
                            var parent = this.findParent(graphLayers[i][j], taskData, rootNodeName);
                            var details = this.findTaskDetails(graphLayers[i][j], taskData);
                            var nodeName = graphLayers[i][j];
                            taskDetails[nodeName] = {
                                "name": nodeName,
                                "parent": parent,
                                "objective": details['objective'],
                                "objectiveId": details['objectiveId'],
                                "effect": details['effect'],
                                "unit": details['unit'],
                                "unitId": details['unitId'],
                                "dependencies": details['dependencies'],
                                "timeFrame": details['timeFrame'],
                                "taskId": graphLayers[i][j],
                                "riskScore": details['riskScore']
                            };
                            if (directChildren.length > 0) {
                                taskDetails[nodeName]['children'] = this.getChildren(directChildren, taskDetails);
                            }
                            ;
                        }
                        ;
                    }
                    ;
                    var taskIds = Object.keys(taskDetails);
                    for (let i = 0; i < taskIds.length; i++) {
                        if (taskDetails[taskIds[i]]['parent'] == rootNodeName) {
                            rootChildren.push(taskDetails[taskIds[i]]);
                        }
                        ;
                    }
                    ;
                    return [
                        {
                            "name": rootNodeName,
                            "parent": "null",
                            "children": rootChildren
                        }
                    ];
                }
                ;
                generateDependencyGraph(taskData) {
                    d3.select('#dependencyTree').selectAll("*").remove();
                    var margin = { top: 20, right: 120, bottom: 20, left: 120 }, width = 960 - margin.right - margin.left, height = 500 - margin.top - margin.bottom;
                    var i = 0, duration = 750, root;
                    var tree = d3.layout.tree()
                        .size([height, width]);
                    var diagonal = d3.svg.diagonal()
                        .projection(function (d) { return [d.y, d.x]; });
                    var svg = d3.select("#dependencyTree").append("svg")
                        .attr("width", width + margin.right + margin.left)
                        .attr("height", height + margin.top + margin.bottom)
                        .append("g")
                        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
                    var div = d3.select("body").append("div")
                        .attr("class", "tooltip")
                        .style("opacity", 1e-6);
                    var treeData = this.convertTaskData(taskData, "DP");
                    root = treeData[0];
                    root.x0 = height / 2;
                    root.y0 = 0;
                    update(root);
                    d3.select(self.frameElement).style("height", "500px");
                    function update(source) {
                        // Compute the new tree layout.
                        var nodes = tree.nodes(root).reverse(), links = tree.links(nodes);
                        // Normalize for fixed-depth.
                        nodes.forEach(function (d) { d.y = d.depth * 180; });
                        // Update the nodes…
                        var node = svg.selectAll("g.node")
                            .data(nodes, function (d) { return d.id || (d.id = ++i); });
                        // Enter any new nodes at the parent's previous position.
                        var nodeEnter = node.enter().append("g")
                            .attr("class", "node")
                            .attr("transform", function (d) { return "translate(" + source.y0 + "," + source.x0 + ")"; })
                            .on("click", click);
                        nodeEnter.append("circle")
                            .attr("r", 1e-6)
                            .style("fill", function (d) {
                            return "#29363b";
                        })
                            .on("mouseover", showNodeName)
                            .on("mousemove", function (d) {
                            moveNodeName(d);
                        })
                            .on("mouseout", hideNodeName);
                        nodeEnter.append("text")
                            .attr("x", function (d) { return d.children || d._children ? -13 : 13; })
                            .attr("dy", ".35em")
                            .attr("text-anchor", function (d) { return d.children || d._children ? "end" : "start"; })
                            .text(function (d) { return d.name; })
                            .style("fill-opacity", 1e-6);
                        // Transition nodes to their new position.
                        var nodeUpdate = node.transition()
                            .duration(duration)
                            .attr("transform", function (d) { return "translate(" + d.y + "," + d.x + ")"; });
                        nodeUpdate.select("circle")
                            .attr("r", 12)
                            .style("fill", function (d) {
                            if (d['riskScore'] == undefined) {
                                return "#29363b";
                            }
                            else if (d['riskScore'] >= 80) {
                                return "#f20046";
                            }
                            else if (d['riskScore'] >= 60) {
                                return "#ff0021";
                            }
                            else if (d['riskScore'] >= 40) {
                                return "#f89444";
                            }
                            else if (d['riskScore'] >= 20) {
                                return "#00d565";
                            }
                            else {
                                return "#00aee1";
                            }
                        })
                            .style("stroke", function (d) {
                            return '#FFF';
                        });
                        function showNodeName() {
                            div.transition()
                                .duration(300)
                                .style("opacity", 1);
                        }
                        ;
                        function moveNodeName(d) {
                            var nodeName = getNodeName(d);
                            div.text(nodeName)
                                .style("left", (d3.event.pageX) + "px")
                                .style("top", (d3.event.pageY) + "px");
                        }
                        ;
                        function hideNodeName() {
                            div.transition()
                                .duration(300)
                                .style("opacity", 0);
                        }
                        ;
                        function getNodeName(d) {
                            if (d['unit'] == undefined || d['effect'] == undefined || d['objective'] == undefined) {
                                var tooltipString = 'Decision point';
                            }
                            else if (d['riskScore'] == undefined) {
                                var tooltipString = d['unit'] + ' ' + d['effect'] + ' ' + d['objective'];
                            }
                            else {
                                var tooltipString = d['unit'] + ' ' + d['effect'] + ' ' + d['objective'] + ' (Risk: ' + d['riskScore'] + '%)';
                            }
                            return tooltipString;
                        }
                        ;
                        nodeUpdate.select("text")
                            .style("fill-opacity", 1);
                        // Transition exiting nodes to the parent's new position.
                        var nodeExit = node.exit().transition()
                            .duration(duration)
                            .attr("transform", function (d) { return "translate(" + source.y + "," + source.x + ")"; })
                            .remove();
                        nodeExit.select("circle")
                            .attr("r", 1e-6);
                        nodeExit.select("text")
                            .style("fill-opacity", 1e-6);
                        // Update the links…
                        var link = svg.selectAll("path.link")
                            .data(links, function (d) { return d.target.id; });
                        // Enter any new links at the parent's previous position.
                        link.enter().insert("path", "g")
                            .attr("class", "link")
                            .attr("d", function (d) {
                            var o = { x: source.x0, y: source.y0 };
                            return diagonal({ source: o, target: o });
                        });
                        // Transition links to their new position.
                        link.transition()
                            .duration(duration)
                            .attr("d", diagonal);
                        // Transition exiting nodes to the parent's new position.
                        link.exit().transition()
                            .duration(duration)
                            .attr("d", function (d) {
                            var o = { x: source.x, y: source.y };
                            return diagonal({ source: o, target: o });
                        })
                            .remove();
                        // Stash the old positions for transition.
                        nodes.forEach(function (d) {
                            d.x0 = d.x;
                            d.y0 = d.y;
                        });
                    }
                    // Toggle children on click.
                    function click(d) {
                        if (d.children) {
                            d._children = d.children;
                            d.children = null;
                        }
                        else {
                            d.children = d._children;
                            d._children = null;
                        }
                        update(d);
                    }
                }
                ;
                coaRiskGraph(coa) {
                    var taskList = [];
                    this.selectedRiskGraphCOA = coa;
                    this.riskGraphGenerated = 0;
                    this.assetRiskChanges = [];
                    if (this.selectedRiskGraphCOA == this.riskGraphCOAs[0]) {
                        this.riskGraphGenerated = 1;
                        setTimeout(() => {
                            this.generateRiskGraph(this.systemId, this.systemData, this.assetRiskData, this.networkSection, this.missionData);
                        });
                    }
                    else {
                        this.riskGraphService.getMissionData(this.missionData['id'])
                            .subscribe(missionData => {
                            for (let i = 0; i < missionData['coAs'].length; i++) {
                                if (missionData['coAs'][i]['name'] == coa) {
                                    var tasks = missionData['coAs'][i]['tasks'];
                                }
                                ;
                            }
                            ;
                            for (var i = 0; i < tasks.length; i++) {
                                taskList.push({
                                    'taskId': this.generateTaskName(tasks[i]),
                                    'effect': tasks[i]['effect'],
                                    'objective': tasks[i]['objective']['entityId'],
                                    'actor': tasks[i]['assignee']['entityId'],
                                    'timeFrame': tasks[i]['end'] - tasks[i]['start'],
                                    'dependencies': []
                                });
                            }
                            ;
                            this.riskGraphService.postNewSystem(this.systemId, taskList)
                                .subscribe(newSystemData => {
                                this.riskGraphService.postEffects(this.systemId, taskList)
                                    .subscribe(riskData => {
                                    this.riskGraphGenerated = 1;
                                    this.compareAssetRisk(this.assetRiskData, riskData['assetRisk']);
                                    setTimeout(() => {
                                        this.generateRiskGraph(this.systemId, newSystemData, riskData['assetRisk'], this.networkSection, this.missionData);
                                    }, 1);
                                });
                            });
                        });
                    }
                    ;
                }
                ;
                getAssetName(assetId, assetList) {
                    for (let i = 0; i < assetList.length; i++) {
                        if (assetList[i]['id'] == assetId) {
                            return assetList[i]['name'];
                        }
                        ;
                    }
                    ;
                }
                ;
                formatRiskForCircle(riskLabel) {
                    return riskLabel.toLowerCase().trim().split(/\s+/).join('-');
                }
                ;
                compareAssetRisk(currentAssetRisk, newAssetRisk) {
                    this.assetRiskChanges = [];
                    var assets = Object.keys(currentAssetRisk);
                    for (let i = 0; i < assets.length; i++) {
                        var currentRiskScore = currentAssetRisk[assets[i]]['risks'][0]['riskScore'];
                        var currentRiskLabel = currentAssetRisk[assets[i]]['risks'][0]['riskLabel'];
                        var newRiskScore = newAssetRisk[assets[i]]['risks'][0]['riskScore'];
                        var newRiskLabel = newAssetRisk[assets[i]]['risks'][0]['riskLabel'];
                        var likelihoodLabel = newAssetRisk[assets[i]]['risks'][0]['likelihoodLabel'];
                        var likelihoodScore = newAssetRisk[assets[i]]['risks'][0]['likelihoodScore'];
                        if (currentRiskScore - newRiskScore > 0) {
                            var arrow = "fa-long-arrow-down green";
                        }
                        else {
                            var arrow = "fa-long-arrow-up off";
                        }
                        ;
                        if (currentRiskScore != newRiskScore) {
                            this.assetRiskChanges.push({
                                'assetName': this.getAssetName(assets[i], this.objectiveList),
                                'newRiskScore': newRiskScore,
                                'newRiskLabel': newRiskLabel,
                                'newRiskCircle': this.formatRiskForCircle(newRiskLabel),
                                'currentRiskScore': currentRiskScore,
                                'currentRiskLabel': currentRiskLabel,
                                'currentRiskCircle': this.formatRiskForCircle(currentRiskLabel),
                                'likelihoodLabel': likelihoodLabel,
                                'likelihoodScore': likelihoodScore,
                                'arrow': arrow
                            });
                        }
                        ;
                    }
                    ;
                }
                ;
                generateRiskGraph(systemId, systemData, assetRiskData, networkSection, missionData) {
                    d3.select('#riskNetwork').selectAll("*").remove();
                    var modal = this.modal;
                    var systemId = systemId;
                    var coursesOfAction = this.coursesOfAction;
                    var assetRiskData = assetRiskData;
                    var riskGraphService = this.riskGraphService;
                    var width = 1100;
                    var height = 700;
                    var dr = 10;
                    var off = 45;
                    var data, net, force, hullg, hull, linkg, link, nodeg, circleg, node, circle, vis, div, curve, zoom, hullSet, allHulls, drag;
                    var vulnerabilityNumber, vulnerabilityNumberg, vulnerabilityCircle, vulnerabilityCircleg;
                    var threatStatus = true;
                    var margin = {
                        top: -5,
                        right: -5,
                        bottom: -5,
                        left: -5
                    };
                    var groups = [];
                    var expand = {};
                    var linkNodes = [];
                    function noop() {
                        return false;
                    }
                    ;
                    function nodeid(n) {
                        return n.size ? "_g_" + n.group : n.name;
                    }
                    ;
                    function linkid(l) {
                        var u = nodeid(l.source);
                        var v = nodeid(l.target);
                        return u < v ? u + "|" + v : v + "|" + u;
                    }
                    ;
                    function getGroup(n) {
                        return n.group;
                    }
                    ;
                    function toggleThreat(systemData) {
                        if (networkSection == 1) {
                            getNodeInfoData(systemData);
                        }
                        ;
                    }
                    ;
                    // constructs the network to visualize
                    function network(data, prev, index, expand) {
                        expand = expand || {};
                        var gm = {}; // group map
                        var nm = {}; // node map
                        var lm = {}; // link map
                        var gn = {}; // previous group nodes
                        var gc = {}; // previous group centroids
                        var nodes = []; // output nodes
                        var links = []; // output links
                        // process previous nodes for reuse or centroid calculation
                        if (prev) {
                            prev.nodes.forEach(function (n) {
                                var i = index(n), o;
                                if (n.size > 0) {
                                    gn[i] = n;
                                    n.size = 0;
                                }
                                else {
                                    o = gc[i] || (gc[i] = {
                                        x: 0,
                                        y: 0,
                                        count: 0
                                    });
                                    o.x += n.x;
                                    o.y += n.y;
                                    o.count += 1;
                                }
                            });
                        }
                        ;
                        // determine nodes
                        for (var k = 0; k < data.nodes.length; k++) {
                            var n = data.nodes[k], i = index(n), l = gm[i] || (gm[i] = gn[i]) || (gm[i] = {
                                group: i,
                                size: 0,
                                nodes: []
                            });
                            if (expand[i]) {
                                nm[n.name] = nodes.length;
                                nodes.push(n);
                                if (gn[i]) {
                                    n.x = gn[i].x + Math.random();
                                    n.y = gn[i].y + Math.random();
                                }
                            }
                            else {
                                // the node is part of a collapsed cluster
                                if (l.size == 0) {
                                    // if new cluster, add to set and position at centroid of leaf nodes
                                    nm[i] = nodes.length;
                                    nodes.push(l);
                                    if (gc[i]) {
                                        l.x = gc[i].x / gc[i].count;
                                        l.y = gc[i].y / gc[i].count;
                                    }
                                    ;
                                }
                                ;
                                l.nodes.push(n);
                            }
                            ;
                            l.size += 1;
                            n.group_data = l;
                        }
                        ;
                        for (i in gm) {
                            gm[i].link_count = 0;
                        }
                        ;
                        for (k = 0; k < data.links.length; k++) {
                            var e = data.links[k];
                            var u = index(e.source);
                            var v = index(e.target);
                            if (u != v) {
                                gm[u].link_count++;
                                gm[v].link_count++;
                            }
                            ;
                            u = expand[u] ? nm[e.source.name] : nm[u];
                            v = expand[v] ? nm[e.target.name] : nm[v];
                            i = (u < v ? u + "|" + v : v + "|" + u),
                                l = lm[i] || (lm[i] = {
                                    source: u,
                                    target: v,
                                    size: 0
                                });
                            l.size += 1;
                        }
                        ;
                        for (i in lm) {
                            links.push(lm[i]);
                        }
                        ;
                        return {
                            nodes: nodes,
                            links: links
                        };
                    }
                    ;
                    function convexHulls(nodes, index, offset) {
                        var hulls = {};
                        // create point sets
                        for (var k = 0; k < nodes.length; k++) {
                            var n = nodes[k];
                            if (n.group != undefined) {
                                if (n.size)
                                    continue;
                                var i = index(n), l = hulls[i] || (hulls[i] = []);
                                l.push([n.x - offset, n.y - offset]);
                                l.push([n.x - offset, n.y + offset]);
                                l.push([n.x + offset, n.y - offset]);
                                l.push([n.x + offset, n.y + offset]);
                            }
                            ;
                        }
                        ;
                        // create convex hulls
                        var hullset = [];
                        for (i in hulls) {
                            hullset.push({
                                group: i,
                                path: d3.geom.hull(hulls[i])
                            });
                        }
                        ;
                        return hullset;
                    }
                    ;
                    function drawCluster(d) {
                        return curve(d.path); // 0.8
                    }
                    ;
                    function getNodeInfoData(systemData) {
                        curve = d3.svg.line()
                            .interpolate("cardinal-closed")
                            .tension(.85);
                        zoom = d3.behavior.zoom()
                            .scaleExtent([1, 10])
                            .on("zoom", zoomed);
                        drag = d3.behavior.drag()
                            .origin(function (d) { return d; })
                            .on("dragstart", dragstarted)
                            .on("drag", dragged)
                            .on("dragend", dragended);
                        vis = d3.select("#riskNetwork").append("svg")
                            .attr("width", width)
                            .attr("height", height)
                            .append("g")
                            .call(zoom);
                        div = d3.select("body").append("div")
                            .attr("class", "tooltip")
                            .style("opacity", 1e-6);
                        var assetList = systemData['assets'];
                        var threatList = systemData['threats'];
                        var groupList = systemData['groups'];
                        var functionList = systemData['functions'];
                        var vulnerabilityList = systemData['vulnerabilities'];
                        for (var i = 0; i < assetList.length; i++) {
                            for (var j = 0; j < groupList.length; j++) {
                                if (assetList[i]['group'] === groupList[j]['id']) {
                                    assetList[i]['group'] = groupList[j]['name'];
                                    assetList[i]['x'] = (j * ((width / groupList.length)) + Math.floor((Math.random() * 50) + 1));
                                    assetList[i]['y'] = Math.floor((Math.random() * height) + 1);
                                }
                                ;
                            }
                            ;
                            for (var j = 0; j < functionList.length; j++) {
                                if (assetList[i]['function'] === functionList[j]['id']) {
                                    assetList[i]['function'] = functionList[j]['name'];
                                }
                                ;
                            }
                            ;
                            for (var j = 0; j < threatList.length; j++) {
                                for (var k = 0; k < threatList[j]['assetsThreatened'].length; k++) {
                                    if (threatList[j]['assetsThreatened'][k] === assetList[i]['id']) {
                                        threatList[j]['assetsThreatened'][k] = assetList[i]['name'];
                                    }
                                    ;
                                }
                                ;
                            }
                            ;
                            assetList[i]['numberOfVulnerabilities'] = 0;
                            for (var j = 0; j < vulnerabilityList.length; j++) {
                                if (vulnerabilityList[j]['assets'].includes(assetList[i]['id'])) {
                                    assetList[i]['numberOfVulnerabilities'] += 1;
                                }
                                ;
                            }
                            ;
                        }
                        ;
                        allHulls = [];
                        for (var i = 0; i < assetList.length; i++) {
                            if (assetList[i]['group'] != undefined) {
                                allHulls.push(assetList[i]['group']);
                            }
                            ;
                        }
                        ;
                        allHulls = [...new Set(allHulls)];
                        hullSet = [];
                        for (var i = 0; i < allHulls.length; i++) {
                            var group = [];
                            for (var j = 0; j < assetList.length; j++) {
                                if (allHulls[i] == assetList[j]['group']) {
                                    group.push(assetList[j]);
                                }
                                ;
                            }
                            ;
                            hullSet.push(group);
                        }
                        ;
                        var links = [];
                        var assetListLength = assetList.length;
                        for (var i = 0; i < threatList.length; i++) {
                            for (var j = 0; j < threatList[i]['assetsThreatened'].length; j++) {
                                for (var k = 0; k < assetList.length; k++) {
                                    if (threatList[i]['assetsThreatened'][j] === assetList[k]['name']) {
                                        links.push({
                                            'source': k,
                                            'target': i + assetListLength,
                                            'weight': 1
                                        });
                                    }
                                    ;
                                }
                                ;
                            }
                            ;
                        }
                        ;
                        for (var i = 0; i < threatList.length; i++) {
                            threatList[i]['type'] = 'threat';
                            assetList.push(threatList[i]);
                        }
                        ;
                        data = {
                            'nodes': assetList,
                            'links': links
                        };
                        for (var i = 0; i < data.links.length; i++) {
                            var o = data.links[i];
                            o.source = data.nodes[o.source];
                            o.target = data.nodes[o.target];
                        }
                        ;
                        for (var i = 0; i < data.nodes.length; i++) {
                            groups[i] = data['nodes'][i].group;
                        }
                        ;
                        var uniqueGroups = groups.filter(onlyUnique);
                        for (var i = 0; i < uniqueGroups.length; i++) {
                            expand[uniqueGroups[i]] = true;
                        }
                        ;
                        // Note that the order of these objects matter for layering
                        hullg = vis.append("g");
                        linkg = vis.append("g");
                        circleg = vis.append("g");
                        nodeg = vis.append("g");
                        vulnerabilityCircleg = vis.append("g");
                        vulnerabilityNumberg = vis.append("g");
                        init();
                        vis.attr("opacity", 1e-6)
                            .transition()
                            .duration(1000)
                            .attr("opacity", 1);
                    }
                    ;
                    function init() {
                        if (force)
                            force.stop();
                        net = network(data, net, getGroup, expand);
                        force = d3.layout
                            .force()
                            .nodes(net.nodes)
                            .links(net.links)
                            .size([width, height])
                            .linkDistance(function (l, i) {
                            var n1 = l.source, n2 = l.target;
                            return 100 +
                                Math.min(20 * Math.min((n1.size || (n1.group != n2.group ? n1.group_data.size : 0)), (n2.size || (n1.group != n2.group ? n2.group_data.size : 0))), -30 +
                                    50 * Math.min((n1.link_count || (n1.group != n2.group ? n1.group_data.link_count : 0)), (n2.link_count || (n1.group != n2.group ? n2.group_data.link_count : 0))), 100);
                        })
                            .linkStrength(function (l, i) {
                            return 0;
                        })
                            .gravity(.02)
                            .charge(-250)
                            .friction(0.3)
                            .size([width, height])
                            .start();
                        hullg.selectAll("path.hull").remove();
                        hull = hullg.selectAll("path.hull")
                            .data(convexHulls(net.nodes, getGroup, off))
                            .enter().append("path")
                            .attr("class", "hull")
                            .attr("d", function (d) {
                            if (d['group'] != 'undefined') {
                                drawCluster;
                            }
                        })
                            .style("fill", function (d) {
                            var colors = ["#616161", "#757575", "#9E9E9E", "#BDBDBD", "#424242"];
                            var randomNumber = Math.floor((Math.random() * colors.length));
                            return colors[randomNumber];
                        })
                            .on("mouseover", showHullName)
                            .on("mousemove", function (d) {
                            moveHullName(d);
                        })
                            .on("mouseout", hideHullName);
                        link = linkg.selectAll("line.link").data(net.links, linkid);
                        link.exit().remove();
                        link.enter().append("line")
                            .attr("class", "link")
                            .attr("marker-end", "url(#end)")
                            .style("stroke-width", function (d) {
                            return Math.sqrt(d.value);
                        })
                            .attr("x1", function (d) { return d.source.x; })
                            .attr("y1", function (d) { return d.source.y; })
                            .attr("x2", function (d) { return d.target.x; })
                            .attr("y2", function (d) { return d.target.y; })
                            .style("stroke-width", function (d) {
                            return 3;
                        })
                            .style("stroke", function (d) {
                            if (d['source']['type'] === 'threat') {
                                if (d['source']['threatLevel'] === 'SEVERE') {
                                    return "#e55";
                                }
                                else {
                                    return "#FFC107";
                                }
                                ;
                            }
                            else if (d['target']['type'] === 'threat') {
                                if (d['target']['threatLevel'] === 'SEVERE') {
                                    return "#e55";
                                }
                                else {
                                    return "#FFC107";
                                }
                                ;
                            }
                            else {
                                return "#424242";
                            }
                            ;
                        });
                        circle = circleg.selectAll(".node")
                            .data(net.nodes, nodeid);
                        circle.enter().append("circle")
                            .attr("r", 25)
                            .attr("class", "node")
                            .style("fill", function (d) {
                            if (d['riskScore'] == undefined) {
                                return 'transparent';
                            }
                            else {
                                if (d['riskScore'] >= 10) {
                                    return '#FFCDD2';
                                }
                                else if (d['riskScore'] >= 7.5) {
                                    return '#FFECB3';
                                }
                                else if (d['riskScore'] >= 5) {
                                    return '#DCEDC8';
                                }
                                else if (d['riskScore'] >= 0) {
                                    return '#B3E5FC';
                                }
                                else {
                                    return 'transparent';
                                }
                                ;
                            }
                            ;
                        });
                        vulnerabilityCircle = vulnerabilityCircleg.selectAll(".node")
                            .data(net.nodes, nodeid);
                        vulnerabilityCircle.enter().append("circle")
                            .style("fill", '#263238')
                            .attr("r", function (d) {
                            if (d['numberOfVulnerabilities'] == undefined) {
                                return 0;
                            }
                            else {
                                if (d['numberOfVulnerabilities'] > 9) {
                                    return 15;
                                }
                                else {
                                    return 10;
                                }
                                ;
                            }
                            ;
                        });
                        vulnerabilityNumber = vulnerabilityNumberg.selectAll(".node")
                            .data(net.nodes, nodeid);
                        vulnerabilityNumber.enter().append("text")
                            .attr("dx", 12)
                            .style("fill", "#FFF")
                            .attr("dy", ".35em")
                            .text(function (d) {
                            return d['numberOfVulnerabilities'];
                        });
                        node = nodeg.selectAll(".node")
                            .data(net.nodes, nodeid);
                        node.enter().append("image")
                            .attr("xlink:href", function (d) {
                            if (assetRiskData[d['id']] === undefined) {
                                return "./app/assets/img/node-icons/sword.png";
                            }
                            else {
                                var riskScore = assetRiskData[d['id']]['risks'][0]['riskScore'];
                                if (riskScore >= 80) {
                                    return "./app/assets/img/node-icons/critical.png";
                                }
                                else if (riskScore >= 60) {
                                    return "./app/assets/img/node-icons/high.png";
                                }
                                else if (riskScore >= 40) {
                                    return "./app/assets/img/node-icons/medium.png";
                                }
                                else if (riskScore >= 20) {
                                    return "./app/assets/img/node-icons/low.png";
                                }
                                else {
                                    return "./app/assets/img/node-icons/very-low.png";
                                }
                                ;
                            }
                            ;
                        })
                            .attr("height", 50)
                            .attr("width", 50)
                            .on("click", function (d) {
                            if (d['type'] === 'threat') {
                                onClickThreatInfo(d);
                            }
                            else {
                                onClickAssetInfo(d);
                            }
                            ;
                        })
                            .on("mouseover", showNodeName)
                            .on("mousemove", function (d) {
                            moveNodeName(d);
                        })
                            .on("mouseout", hideNodeName);
                        node.call(force.drag);
                        force.on("tick", function () {
                            if (!hull.empty()) {
                                hull.data(convexHulls(net.nodes, getGroup, off))
                                    .attr("d", drawCluster);
                            }
                            ;
                            link.attr("x1", function (d) { return d.source.x; })
                                .attr("y1", function (d) { return d.source.y; })
                                .attr("x2", function (d) { return d.target.x; })
                                .attr("y2", function (d) { return d.target.y; });
                            node.attr("transform", function (d) {
                                return "translate(" + (d.x - 20) + "," + (d.y - 25) + ")";
                            });
                            circle.attr("transform", function (d) {
                                return "translate(" + (d.x + 7) + "," + (d.y + 7) + ")";
                            });
                            vulnerabilityCircle.attr("transform", function (d) {
                                if (d['numberOfVulnerabilities'] > 9) {
                                    var dx = 32;
                                }
                                else {
                                    var dx = 28;
                                }
                                ;
                                return "translate(" + (d.x + dx) + "," + (d.y - 10) + ")";
                            });
                            vulnerabilityNumber.attr("transform", function (d) {
                                return "translate(" + (d.x + 12) + "," + (d.y - 10) + ")";
                            });
                        });
                        // Remain static
                        var n = 100;
                        for (var i = n * n; i > 0; --i)
                            force.tick();
                        force.stop();
                    }
                    ;
                    function zoomed() {
                        vis.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
                    }
                    ;
                    function dragstarted(d) {
                        d3.event.sourceEvent.stopPropagation();
                        d3.select(this).classed("dragging", true);
                    }
                    ;
                    function dragged(d) {
                        d3.select(this).attr("cx", d.x = d3.event.x).attr("cy", d.y = d3.event.y);
                    }
                    ;
                    function dragended(d) {
                        d3.select(this).classed("dragging", false);
                    }
                    ;
                    function onlyUnique(value, index, self) {
                        return self.indexOf(value) === index;
                    }
                    ;
                    function expandGroup(d) {
                        expand[d.group] = !expand[d.group];
                        init();
                    }
                    ;
                    function expandHull(d) {
                        expand[d.group] = false;
                        init();
                    }
                    ;
                    function showNodeName() {
                        div.transition()
                            .duration(300)
                            .style("opacity", 1);
                    }
                    ;
                    function moveNodeName(d) {
                        var nodeName = getNodeName(d);
                        div.text(nodeName)
                            .style("left", (d3.event.pageX) + "px")
                            .style("top", (d3.event.pageY) + "px");
                    }
                    ;
                    function hideNodeName() {
                        div.transition()
                            .duration(300)
                            .style("opacity", 0);
                    }
                    ;
                    function getNodeName(d) {
                        if (d['riskScore'] == undefined) {
                            return d['name'];
                        }
                        else {
                            var riskLabel;
                            if (d['riskScore'] >= 10) {
                                riskLabel = 'Critical';
                            }
                            else if (d['riskScore'] >= 7.5) {
                                riskLabel = 'High';
                            }
                            else if (d['riskScore'] >= 5) {
                                riskLabel = 'Medium';
                            }
                            else if (d['riskScore'] >= 2.5) {
                                riskLabel = 'Low';
                            }
                            else {
                                riskLabel = 'Very low';
                            }
                            ;
                            return d.name + " (" + riskLabel + ")";
                        }
                        ;
                    }
                    ;
                    function showHullName() {
                        div.transition()
                            .duration(300)
                            .style("opacity", 1);
                    }
                    ;
                    function moveHullName(d) {
                        var hullName = d['group'];
                        div.text(hullName)
                            .style("left", (d3.event.pageX) + "px")
                            .style("top", (d3.event.pageY) + "px");
                    }
                    ;
                    function hideHullName() {
                        div.transition()
                            .duration(300)
                            .style("opacity", 0);
                    }
                    ;
                    function onClickAssetInfo(event) {
                        return modal.open(asset_info_modal_1.AssetInfoWindow, new asset_info_modal_1.AssetInfoWindowData(event, assetRiskData[event['id']]['risks'][0], systemId, systemData, missionData));
                    }
                    ;
                    function onClickThreatInfo(event) {
                        return modal.open(threat_info_modal_1.ThreatInfoWindow, new threat_info_modal_1.ThreatInfoWindowData(event));
                    }
                    ;
                    getNodeInfoData(systemData);
                }
                ;
                timeScaler(minutes) {
                    if (minutes >= 60) {
                        return (minutes / 60) + " hours";
                    }
                    else if (minutes < 60) {
                        return minutes + " minutes";
                    }
                    ;
                }
                ;
                prepTaskToDelete(action) {
                    this.hasTaskDependents = 0;
                    this.tasksToDelete = [action['id']];
                    var allChildren = this.findAllChildren(action['name'], this.actionRows);
                    if (allChildren.length > 0) {
                        this.hasTaskDependents = 1;
                        var taskList = [];
                        for (let i = 0; i < allChildren.length; i++) {
                            taskList.push(allChildren[i]['name']);
                            this.tasksToDelete.push(allChildren[i]['_id']);
                        }
                        ;
                        if (taskList.length > 1) {
                            this.taskDependents = "Tasks " + arrayToSentence(taskList) + " depend";
                        }
                        else {
                            this.taskDependents = "Task " + taskList.toString() + " depends";
                        }
                        ;
                    }
                    ;
                    function arrayToSentence(arr) {
                        var last = arr.pop();
                        return arr.join(', ') + ' and ' + last;
                    }
                    ;
                }
                ;
                deleteTask() {
                    for (let i = 0; i < this.missionData['coAs'].length; i++) {
                        if (this.missionData['coAs'][i]['name'] == this.selectedCOA) {
                            var coaId = this.missionData['coAs'][i]['id'];
                        }
                        ;
                    }
                    ;
                    for (let i = 0; i < this.tasksToDelete.length; i++) {
                        this.riskGraphService.deleteTask(this.missionData['id'], coaId, this.tasksToDelete[i])
                            .subscribe(deletedActions => {
                            this.populateActionTable(this.selectedCOA);
                        });
                    }
                    ;
                }
                ;
                openNav() {
                    var w = Math.round(window.innerWidth * 0.7);
                    document.getElementById("mySidenav").style.width = Math.max(w, 1000) + "px";
                    document.getElementById("riskNetwork").style.marginLeft = "0px";
                    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
                    this.getActionInfo();
                }
                ;
                formatRisk(riskScore) {
                    if (riskScore < 0) {
                        return 'Increase of ' + riskScore + '%';
                    }
                    else if (riskScore == 0) {
                        return 'No change in risk';
                    }
                    else {
                        return 'Reduction of ' + riskScore + '%';
                    }
                    ;
                }
                ;
                getActionInfo() {
                    this.riskGraphService.getStagedActions()
                        .subscribe(response => {
                        for (var i = 0; i < response.length; i++) {
                            response[i]['actionStatus'] = 'Remove action';
                        }
                        ;
                        var hardware = [];
                        this.stagedActionRows = response;
                        this.numberOfStagedActions = response.length;
                        this.totalResourcesDeployed = (response.length * 2) + " security analysts";
                        this.totalTimeTaken = Number(0);
                        this.riskReduction = Number(0);
                        this.probabilityOfCompleteSuccess = 1;
                        for (var i = 0; i < response.length; i++) {
                            for (var j = 0; j < response[i].hardwareAffected.length; j++) {
                                hardware.push({
                                    'name': response[i].hardwareAffected[j].hardwareName,
                                    'id': response[i].hardwareAffected[j].hardwareid
                                });
                            }
                            ;
                            if (i == 0) {
                                this.probabilityOfCompleteSuccess = response[i].probabilityOfSuccess;
                            }
                            else {
                                this.probabilityOfCompleteSuccess = this.probabilityOfCompleteSuccess * response[i].probabilityOfSuccess;
                            }
                            ;
                            this.totalTimeTaken += response[i].timeTaken.averageTime;
                            this.riskReduction += Number(response[i].benefit);
                        }
                        ;
                        this.hardwareAffected = hardware.filter((hardware, index, self) => self.findIndex(t => t.id === hardware.id && t.name === hardware.name) === index);
                        this.probabilityOfCompleteSuccess = Math.round(this.probabilityOfCompleteSuccess * 100);
                        this.totalTimeTaken = this.timeScaler(this.totalTimeTaken);
                        this.riskReduction = this.formatRisk(Math.round(this.riskReduction));
                    });
                }
                ;
                onSelect({ selected }) {
                }
                ;
            };
            RiskGraphComponent = __decorate([
                core_1.Component({
                    selector: 'RiskGraph',
                    templateUrl: "app/risk-graph/risk-graph.component.html",
                    providers: [risk_graph_service_1.RiskGraphService, asset_info_modal_service_1.AssetInfoService, angular2_modal_1.Modal, http_1.HTTP_PROVIDERS]
                }),
                __metadata("design:paramtypes", [router_1.ActivatedRoute,
                    core_1.ViewContainerRef,
                    angular2_modal_1.Modal,
                    risk_graph_service_1.RiskGraphService,
                    asset_info_modal_service_1.AssetInfoService])
            ], RiskGraphComponent);
            exports_1("RiskGraphComponent", RiskGraphComponent);
            ;
        }
    };
});
//# sourceMappingURL=risk-graph.component.js.map
import { Component, OnInit, ViewContainerRef, ViewEncapsulation } from '@angular/core';
import { HTTP_PROVIDERS } from "@angular/http";

declare let d3, nv: any;
import { nvD3 } from 'ng2-nvd3';
import { Modal } from 'angular2-modal';

import * as L from 'leaflet';

import { DialogRef, ModalComponent } from 'angular2-modal';
import { BSModalContext } from 'angular2-modal/plugins/bootstrap';

import { ActionWindow, ActionWindowData } from '../action-modal/courses.action.modal';

import { AssetInfoService } from './asset.info.modal.service';
import { RiskGraphService } from '../../risk-graph.service';



export class AssetInfoWindowData extends BSModalContext {
  constructor(
    public assetInfoData:object,
    public riskInfo:object,
    public systemId:string,
    public systemData:object,
    public missionData:object
  ) {
    super();
  }
}


@Component({
  selector: 'modal-content',
  templateUrl: './app/risk-graph/modals/asset-info/asset.info.modal.html',
  directives: [nvD3],
  providers: [AssetInfoService, RiskGraphService, Modal, HTTP_PROVIDERS]
})


export class AssetInfoWindow implements OnInit, ModalComponent<AssetInfoWindowData> {
  layers = [
    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 18, attribution: '' })
  ];
  zoom = 16;

  context : AssetInfoWindowData;
  assetInfoData : any;
  riskInfo: any;
  predictedRisk = {
    'label' : 'Very low',
    'score' : 0,
    'change' : 0.00
  };

  riskImpact = {
    'consequence': 10,
    'likelihood': 8
  };
  noThreats = 1;
  threatInfo : any;
  noVulnerabilities = 1;
  vulnerabilityInfo : any;
  riskTimelineData : any;
  riskTimelineOptions = {
    chart: {
      type: 'lineChart',
      height: 400,
      width: 850,
      interpolate: 'basis',
      margin : {
        top: 20,
        right: 20,
        bottom: 50,
        left: 55
      },
      x: function(d) {
        return d.x;
      },
      y: function(d) {
        return d.y;
      },
      showValues: true,
      duration: 500,
      forceY: [0,100],
      xAxis: {
        axisLabel: 'Date',
        showMaxMin: false,
        tickFormat: function(d) {
          return d3.time.format('%b %d %Y')(new Date(d));
        }
      },
      yAxis: {
        axisLabel: 'Risk level',
        axisLabelDistance: -10
      }
    }
  };
  fullNodeData = {};
  riskTimelineRangeSelected: any;
  directVulnerabilities: any;
  maxDays: any;

  noActions : any;
  actionRows : any;
  actionSelected = [];
  actionColumns = [
    {
      name: 'Course of Action'
    },
    {
      name: 'Effect'
    },
    {
      name: 'Unit'
    },
    {
      name: 'Time frame'
    }
  ];

  vulnerabilityRows : any;
  vulnerabilitySelected = [];
  threatRows : any;
  threatSelected = [];
  assetOverview = 1;
  vulnerabilityOverview = 0;
  actionOverview = 0;
  threatOverview = 0;
  noDevices = 0;
  deviceRows : any;
  deviceSelected = [];

  selectedEffect: string;
  effectList = [];

  selectedObjective = {
    'name': "",
    'id': ""
  };
  objectiveList = [];

  selectedUnit = {
    'name': "",
    'id': "",
    'affiliation': ""
  };
  unitList = [];
  timeFrame = 0;

  systemId: string;

  selectedCOA: string;

  coursesOfAction = [];

  vulnerabilityData = [];
  numberOfVulnerabilities: number;
  numberOfThreats: number;
  numberOfTasks: number;

  assetCoordinates: any;

  assetLatLng = {
    'latitude': 0,
    'longitude': 0
  };

  noLocation: number;
  systemData:object;
  missionData:object;
  selectedTaskId:string = "";

  startTime:number = 0;
  endTime:number = 0;
  selectedDescription:string = "";

  constructor(public dialog: DialogRef<AssetInfoWindowData>,
    vcRef: ViewContainerRef,
    public modal: Modal,
    private assetInfoService: AssetInfoService,
    private riskGraphService: RiskGraphService
  ) {
    modal.defaultViewContainer = vcRef;
    dialog['context']['size'] = 'lg';
    this.assetInfoData = this.checkForUnknowns(dialog['context']['assetInfoData']);
    this.systemData = dialog['context']['systemData'];
    this.missionData = dialog['context']['missionData'];
    this.riskInfo = dialog['context']['riskInfo'];
    this.systemId = dialog['context']['systemId'];
  };

  ngOnInit() {
    this.riskGraphService.getC2REST()
    .subscribe(C2REST => {
      this.riskGraphService.C2REST = "http://" + C2REST["c2_rest_api"];
      this.assetView();
      this.getEffectList();
      this.getObjectiveList();
      this.getUnitList(this.assetInfoData['assetType']);
      this.populateActionTable();
      this.getCoursesOfAction(this.missionData);
      this.assetVulnerabilities(this.systemData, this.assetInfoData['id']);
      this.assetThreats(this.assetInfoData['name']);
      this.assetLocation(this.systemId, this.assetInfoData['id']);
    });
  };

  getCoursesOfAction(missionData) {
    this.coursesOfAction = [];
    for (let i = 0; i < missionData['coAs'].length; i++) {
      this.coursesOfAction.push({
        'name': missionData['coAs'][i]['name'],
        'id': missionData['coAs'][i]['id']
      });
    };
    this.selectedCOA = this.coursesOfAction[0];
  };

  checkForUnknowns(assetInfoData) {
    var fieldsToCheck:string[] = [
      'function',
      'group'
    ];
    for (let i = 0; i < fieldsToCheck.length; i++) {
      if (assetInfoData[fieldsToCheck[i]] == '' ||
      assetInfoData[fieldsToCheck[i]] == undefined) {
        assetInfoData[fieldsToCheck[i]] = "Unknown"
      };
    };
    return assetInfoData;
  };

  onMapReady(map) {
    setTimeout(() => {
      map.invalidateSize();
    }, 1);
  };

  selectTaskId(event) {
    this.selectedTaskId = event['target']['value'];
  };

  assetLocation(systemId, assetId) {
    this.assetInfoService.getAssetLocation(systemId, assetId)
    .subscribe(assetLocationData => {
      if (Object.keys(assetLocationData).length === 0) {
        this.noLocation = 1;
      } else {
        this.assetLatLng['latitude'] = assetLocationData['latitude'];
        this.assetLatLng['longitude'] = assetLocationData['longitude'];
        this.assetCoordinates = L.latLng(assetLocationData['latitude'], assetLocationData['longitude']);
        if (assetLocationData['layerType'] == 'polygon' || assetLocationData['layerType'] == 'polyline') {
          this.layers.push(L.polygon(assetLocationData['drawing']));
        } else if (assetLocationData['layerType'] == 'circle' || assetLocationData['layerType'] == 'point') {
          this.layers.push(L.circle(assetLocationData['drawing'], { radius: assetLocationData['radius'] }));
        };
        this.noLocation = 0;
      };
    });
  };

  assetVulnerabilities(systemData, assetId) {
    this.vulnerabilityRows = [];
    var vulnerabilities = this.systemData['vulnerabilities'];
    for (let i = 0; i < vulnerabilities.length; i++) {
      if (vulnerabilities[i]['assets'].includes(assetId)) {
        this.vulnerabilityRows.push(vulnerabilities[i]);
      };
    };
    this.numberOfVulnerabilities = this.vulnerabilityRows.length;
    if (this.numberOfVulnerabilities > 0) {
      this.noVulnerabilities = 0;
    } else {
      this.noVulnerabilities = 1;
    };
  };

  assetThreats(assetName) {
    this.threatRows = [];
    var threats = this.systemData['threats'];
    for (let i = 0; i < threats.length; i++) {
      if (threats[i]['assetsThreatened'].includes(assetName)) {
        this.threatRows.push(threats[i]);
      };
    };
    this.numberOfThreats = this.threatRows.length;
    if (this.numberOfThreats > 0) {
      this.noThreats = 0;
    } else {
      this.noThreats = 1;
    };
  };

  populateActionTable() {
    this.actionRows = [];
    this.riskGraphService.getMissionData(
      this.missionData['globalId']
    ).subscribe(missionData => {
      this.missionData = missionData;
      for (let i = 0; i < missionData['coAs'].length; i++) {
        for (let j = 0; j < missionData['coAs'][i]['tasks'].length; j++) {
          if (missionData['coAs'][i]['tasks'][j]['objective']['entityId']==this.assetInfoData['id']) {
            var task = missionData['coAs'][i]['tasks'][j];
            task['courseOfAction'] = missionData['coAs'][i]['name'];
            task['courseOfActionId'] = missionData['coAs'][i]['id'];
            task['name'] = this.generateTaskName(task);
            for (let k = 0; k < this.unitList.length; k++) {
              if (this.unitList[k]['id'] == task['assignee']['entityId']) {
                task['assignee']['entityName'] = this.unitList[k]['name'];
              };
            };
            this.actionRows.push(
              task
            );
          };
        };
      };
      this.numberOfTasks = this.actionRows.length;
    });
  };

  getEffectList() {
    this.assetInfoService.getEffects()
    .subscribe(effectList => {
      this.effectList = effectList;
      this.selectedEffect = effectList[0];
    });
  };

  getObjectiveList() {
    this.assetInfoService.getObjectives(this.systemId)
    .subscribe(objectiveList => {
      for (var i = 0; i < objectiveList.length; i++) {
        this.objectiveList.push({
          'name': objectiveList[i]['name'],
          'id': objectiveList[i]['id']
        })
      };
    });
  };


  determineUnitCapability(unitInfo, assetType) {
    if (assetType.toLowerCase() == 'cyber') {
      return unitInfo['cyberCapability'];
    } else if (assetType.toLowerCase() == 'physical') {
      return unitInfo['physicalCapability'];
    } else {
      return 0;
    };
  };

  getUnitList(assetType) {
    this.riskGraphService.getMissionUnits()
    .subscribe(unitList => {
      this.unitList = [];
      var availableUnits = this.getAvailableUnits(
        this.missionData['elements'],
        this.missionData['warningOrder']['taskOrg']['units']
      );
      for (let i = 0; i < unitList.length; i++) {
        for (let j = 0; j < availableUnits.length; j++) {
          if (unitList[i]['id'] == availableUnits[j]) {
            this.unitList.push({
              'name': unitList[i]['name'],
              'id': unitList[i]['id'],
              'affiliation': unitList[i]['affiliation']
            });
          };
        };
      };
      this.selectedUnit = {
        'name': this.unitList[0]['name'],
        'id': this.unitList[0]['id'],
        'affiliation': this.unitList[0]['affiliation']
      };
    });
  };

  getAvailableUnits(elements, taskOrgUnits) {
    var units = taskOrgUnits;
    for (let i = 0; i < elements.length; i++) {
      if (elements[i]['entityType'] == 'unit') {
        units.push(elements[i]['entityId']);
      };
    };
    var uniqueUnits = units.filter((v, i, a) => a.indexOf(v) === i);
    return uniqueUnits;
  };

  setStartTime(event) {
    this.startTime = event['target']['value'];
  };

  setEndTime(event) {
    this.endTime = event['target']['value'];
  };

  setDescription(event) {
    this.selectedDescription = event['target']['value'];
  };

  selectEffect(event) {
    var effect = event['target']['value'];
    this.selectedEffect = effect;
  };

  selectCOA(event) {
    var coa = event['target']['value'];
    for (let i = 0; i < this.coursesOfAction.length; i++) {
      if (this.coursesOfAction[i]['name'] == coa) {
        this.selectedCOA = this.coursesOfAction[i];
      };
    };
  };

  selectObjective(objective) {
    this.selectedObjective = {
      'name': objective['name'],
      'id': objective['id']
    };
  };

  selectUnit(event) {
    var unitName = event['target']['value'];
    for (var i = 0; i < this.unitList.length; i++) {
      if (unitName === this.unitList[i]['name']) {
        this.selectedUnit = {
          'name': unitName,
          'id': this.unitList[i]['id'],
          'affiliation': this.unitList[i]['affiliation']
        }
      };
    };
  };

  submitNewAction() {
    var task = {
      'type': 'task',
      'name': this.selectedTaskId,
      'description': this.selectedDescription,
      'effect': this.selectedEffect,
      'objective': {
        'entityId': this.assetInfoData['id'],
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
    this.riskGraphService.postTask(
      this.missionData['globalId'],
      this.selectedCOA['id'],
      task
    ).subscribe(postedTask => {
      this.populateActionTable();
    });
  };

  deleteAction(event) {
    this.riskGraphService.deleteTask(
      this.missionData['globalId'],
      event['courseOfActionId'],
      event['id']
    ).subscribe(deletedAction => {
      this.populateActionTable();
    });
  }

  assetView() {
    this.assetOverview = 1;
    this.vulnerabilityOverview = 0;
    this.actionOverview = 0;
    this.threatOverview = 0;
  };

  threatView() {
    this.threatOverview = 1;
    this.vulnerabilityOverview = 0;
    this.assetOverview = 0;
    this.actionOverview = 0;
  };

  vulnerabilityView() {
    this.vulnerabilityOverview = 1;
    this.assetOverview = 0;
    this.actionOverview = 0;
    this.threatOverview = 0;
  };

  actionView() {
    this.actionOverview = 1;
    this.assetOverview = 0;
    this.vulnerabilityOverview = 0;
    this.threatOverview = 0;
    this.populateActionTable();
  };

  getThreats(assetId) {
    this.assetInfoService.getThreatData(assetId)
    .subscribe(data => {
      var threatData = data;
      if (threatData.length == 0) {
        this.noThreats = 1;
        this.threatInfo = "No known threats for this asset"
      } else if (threatData.length > 0) {
        this.noThreats = 0;
        this.threatRows = threatData;
      };
    });
  };

  onSelect({ selected }) {
  };

  generateTaskName(task) {
    return task['effect'].substring(0, 3) + '_' +
    task['assignee']['entityId'].substring(0, 3) + '_' +
    task['start'];
  };

  closeModal() {
    this.dialog.close();
  };
}

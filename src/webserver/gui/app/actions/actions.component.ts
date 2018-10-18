import { Component, OnInit, ViewContainerRef, ViewEncapsulation } from '@angular/core';
import { HTTP_PROVIDERS } from "@angular/http";

import { Modal } from 'angular2-modal';

import { ActionsService } from './actions.service';


@Component({
  selector: 'actions',
  templateUrl: 'app/actions/actions.component.html',
  providers: [ActionsService, Modal, HTTP_PROVIDERS]
})

export class ActionsComponent implements OnInit {
  constructor(vcRef: ViewContainerRef,
    public modal: Modal,
    private actionsService: ActionsService) {
    modal.defaultViewContainer = vcRef;
  };

  hostileResponses = {};

  effects = [];
  effectType: string;
  effectTypeList = [];
  selectedEffect: string;
  effectDescription: string;

  allActions = [];
  cyberActionList = [];
  physicalActionList = [];
  actorActionList = [];

  responseSection = 0;
  actionSection = 0;
  propertySection = 0;

  noData = 0;

  effectTypes = [
    'Offensive',
    'Defensive'
  ];
  selectedType = 'Offensive';

  selectedMostLikely: string;
  selectedMostDangerous: string;

  ngOnInit() {
    this.actionsService.getEffects()
    .subscribe(effectsList => {
      this.selectedEffect = effectsList[0]
      this.effects = effectsList;
      this.changeEffect(this.selectedEffect);
      this.navToResponseSection();
    });
    this.actionsService.getEffectTypes()
    .subscribe(effectTypes => {
      this.effectTypeList = effectTypes;
      this.selectedMostLikely = this.effects[0];
      this.selectedMostDangerous = this.effects[0];
    });
  };

  selectType(event) {
    this.selectedType = event['target']['value'].toLowerCase();
  };

  selectMostLikely(event) {
    this.selectedMostLikely = event['target']['value'].toUpperCase();
  };

  selectMostDangerous(event) {
    this.selectedMostDangerous = event['target']['value'].toUpperCase();
  };

  submitNewEffect() {
    var effectTerm = document.getElementById("effectTerm")['value'];
    var effectDesc = document.getElementById("effectDescription")['value'];
    var effectData = {
      'effect': effectTerm.toUpperCase(),
      'effectType': this.selectedType.toLowerCase(),
      'description': effectDesc,
      'hostileResponse': {
        'mostDangerous': this.selectedMostDangerous,
        'mostLikely': this.selectedMostLikely
      }
    };
    this.actionsService.submitNewEffect(effectData)
    .subscribe(status => {
      this.ngOnInit();
    });
  };

  navToResponseSection() {
    this.responseSection = 1;
    this.actionSection = 0;
    this.propertySection = 0;
  };

  navToActionSection() {
    this.responseSection = 0;
    this.actionSection = 1;
    this.propertySection = 0;
  };

  navToPropertySection() {
    this.responseSection = 0;
    this.actionSection = 0;
    this.propertySection = 1;
  };

  changeEffect(effect) {
    this.selectedEffect = effect;
    this.actionsService.getHostileResponses(effect)
    .subscribe(hostileResponses => {
      this.hostileResponses = hostileResponses[0]['hostileResponse'];
      this.effectType = hostileResponses[0]['effectType'];
      this.effectDescription = hostileResponses[0]['description'];
    });
    this.actionsService.getActionData()
    .subscribe(actionList => {
      this.allActions = actionList;
      for (var i = 0; i < this.allActions.length; i++) {
        this.allActions[i]['id'] = 'Table-' + i;
        this.allActions[i]['editMode'] = false;
      };
      this.selectedEffect = effect;
      this.cyberActionList = [];
      this.physicalActionList = [];
      this.actorActionList = [];
      for (var i = 0; i < this.allActions.length; i++) {
        if (this.allActions[i]['effect'] == effect) {
          if (this.allActions[i]['type'] === 'physical') {
            this.physicalActionList.push(this.allActions[i]);
          } else if (this.allActions[i]['type'] === 'cyber') {
            this.cyberActionList.push(this.allActions[i]);
          } else if (this.allActions[i]['type'] === 'actor') {
            this.actorActionList.push(this.allActions[i]);
          };
        };
      };
      if (this.physicalActionList.length +
        this.cyberActionList.length +
        this.actorActionList.length == 0) {
        this.noData = 1;
      } else {
        this.noData = 0;
      };
    });
  };

  addPhysicalRow(tableId) {
    for (var i = 0; i < this.physicalActionList.length; i++) {
      if (this.physicalActionList[i]['id'] == tableId) {
        this.physicalActionList[i]['actions'].push("New action...");
      };
    };
  };

  addActorRow(tableId) {
    for (var i = 0; i < this.actorActionList.length; i++) {
      if (this.actorActionList[i]['id'] == tableId) {
        this.actorActionList[i]['actions'].push("New action...");
      };
    };
  };

  addCyberRow(tableId) {
    for (var i = 0; i < this.cyberActionList.length; i++) {
      if (this.cyberActionList[i]['id'] == tableId) {
        this.cyberActionList[i]['actions'].push("New action...");
      };
    };
  };

  togglePhysicalEditing(tableId) {
    for (var i = 0; i < this.physicalActionList.length; i++) {
      if (this.physicalActionList[i]['id'] == tableId) {
        if (this.physicalActionList[i]['editMode']) {
          this.physicalActionList[i]['editMode'] = false;
        } else {
          this.physicalActionList[i]['editMode'] = true;
        };
      };
    };
  };

  toggleActorEditing(tableId) {
    for (var i = 0; i < this.actorActionList.length; i++) {
      if (this.actorActionList[i]['id'] == tableId) {
        if (this.actorActionList[i]['editMode']) {
          this.actorActionList[i]['editMode'] = false;
        } else {
          this.actorActionList[i]['editMode'] = true;
        };
      };
    };
  };

  toggleCyberEditing(tableId) {
    for (var i = 0; i < this.cyberActionList.length; i++) {
      if (this.cyberActionList[i]['id'] == tableId) {
        if (this.cyberActionList[i]['editMode']) {
          this.cyberActionList[i]['editMode'] = false;
        } else {
          this.cyberActionList[i]['editMode'] = true;
        };
      };
    };
  };

  deletePhysicalAction(tableId, action) {
    for (var i = 0; i < this.physicalActionList.length; i++) {
      if (this.physicalActionList[i]['id'] == tableId) {
        for (var j = 0; j < this.physicalActionList[i]['actions'].length; j++) {
          if (action == this.physicalActionList[i]['actions'][j]) {
            this.physicalActionList[i]['actions'].splice(j, 1);
          };
        };
      };
    };
  };

  deleteActorAction(tableId, action) {
    for (var i = 0; i < this.actorActionList.length; i++) {
      if (this.actorActionList[i]['id'] == tableId) {
        for (var j = 0; j < this.actorActionList[i]['actions'].length; j++) {
          if (action == this.actorActionList[i]['actions'][j]) {
            this.actorActionList[i]['actions'].splice(j, 1);
          };
        };
      };
    };
  };

  deleteCyberAction(tableId, action) {
    for (var i = 0; i < this.cyberActionList.length; i++) {
      if (this.cyberActionList[i]['id'] == tableId) {
        for (var j = 0; j < this.cyberActionList[i]['actions'].length; j++) {
          if (action == this.cyberActionList[i]['actions'][j]) {
            this.cyberActionList[i]['actions'].splice(j, 1);
          };
        };
      };
    };
  };

  changeHostileResponse(newEffect, most) {
    this.hostileResponses[most] = newEffect;
    var hostileResponse = {
      hostileResponse: this.hostileResponses
    };
    this.actionsService.patchHostileResponse(this.selectedEffect, hostileResponse)
    .subscribe(returnedData => {
      this.changeEffect(this.selectedEffect);
    });
  };

  updateEffectType(effectType) {
    var updateData = {
      "effectType": effectType.toLowerCase()
    };
    this.actionsService.patchHostileResponse(this.selectedEffect, updateData)
    .subscribe(returnedData => {
      this.changeEffect(this.selectedEffect);
    });
  };

  updateProperty(event, actionInfo, property) {
    actionInfo['properties'][property] = event['target']['valueAsNumber'];
    var propertyChange = {
      'properties': actionInfo['properties']
    };
    this.actionsService.patchActionData(propertyChange, actionInfo['force'], actionInfo['effect'], actionInfo['type'])
    .subscribe(returnedData => {
      this.changeEffect(actionInfo['effect']);
    });
  };

  saveNewPhysicalActionList(actionInfo) {
    var tableArr = [];
    var table = document.getElementById(actionInfo['id']);
    for (var i = 1; i < table['rows'].length; i++) {
      tableArr.push(table['rows'][i].cells[0].innerText);
    };
    var actionChange = {
      'actions': tableArr
    };
    this.actionsService.patchActionData(actionChange, actionInfo['force'], actionInfo['effect'], actionInfo['type'])
    .subscribe(returnedData => {
      this.togglePhysicalEditing(actionInfo['id']);
      this.changeEffect(actionInfo['effect']);
    });
  };

  saveNewActorActionList(actionInfo) {
    var tableArr = [];
    var table = document.getElementById(actionInfo['id']);
    for (var i = 1; i < table['rows'].length; i++) {
      tableArr.push(table['rows'][i].cells[0].innerText);
    };
    var actionChange = {
      'actions': tableArr
    };
    this.actionsService.patchActionData(actionChange, actionInfo['force'], actionInfo['effect'], actionInfo['type'])
    .subscribe(returnedData => {
      this.toggleActorEditing(actionInfo['id']);
      this.changeEffect(actionInfo['effect']);
    });
  };

  saveNewCyberActionList(actionInfo) {
    var tableArr = [];
    var table = document.getElementById(actionInfo['id']);
    for (var i = 1; i < table['rows'].length; i++) {
      tableArr.push(table['rows'][i].cells[0].innerText);
    };
    var actionChange = {
      'actions': tableArr
    };
    this.actionsService.patchActionData(actionChange, actionInfo['force'], actionInfo['effect'], actionInfo['type'])
    .subscribe(returnedData => {
      this.toggleCyberEditing(actionInfo['id']);
      this.changeEffect(actionInfo['effect']);
    });
  };

  deleteEffect() {
    this.actionsService.deleteEffect(this.selectedEffect)
    .subscribe(status => {
      this.ngOnInit();
    });
  };
}

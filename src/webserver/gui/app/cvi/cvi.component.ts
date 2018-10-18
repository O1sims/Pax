import { Component, OnInit, Injectable, ViewContainerRef, ViewEncapsulation } from '@angular/core';
import { HTTP_PROVIDERS } from "@angular/http";

import * as Survey from 'survey-angular';
import { Modal } from 'angular2-modal';

import { CVIService } from './cvi.service';

import 'rxjs/add/operator/map';



@Component({
  selector: 'CVI',
  templateUrl: 'app/cvi/cvi.component.html',
  providers: [CVIService, Modal, HTTP_PROVIDERS]
})


@Injectable()
export class CVIComponent implements OnInit {
  CVIAnswers : any;
  CVIQuestions : any;
  sendingSampleData  = 0;
  sentSampleDataError = 0;
  sentSampleDataSuccess = 0;

  constructor(vcRef: ViewContainerRef, public modal: Modal, private CVIService: CVIService) {
    modal.defaultViewContainer = vcRef;
  };

  ngOnInit() {
    Survey.Survey.cssType = "bootstrap";
    Survey.defaultBootstrapCss.navigationButton = "btn btn-success";
    Survey.defaultBootstrapCss.matrixdynamic.button = "btn btn-default";
    Survey.defaultBootstrapCss.progressBar = "progress-bar progress-bar-success progress-bar-striped active";
    this.CVIService.getCVIQuestions()
    .subscribe(surveyJSON => {
      this.CVIQuestions = surveyJSON
      this.renderCVI({
      });
    });
  };


  renderCVI(data) {
    var cvi = new Survey['Model'](this.CVIQuestions);
    cvi.showProgressBar = "bottom";
    var CVIService = this.CVIService;
    var onNext = function(sender, options) {
      CVIService.getCurrentSection(options['newCurrentPage']['elementsValue'][0]['name']);
      if (options['oldCurrentPage'] != null) {
        for (var i = 0; i < options['oldCurrentPage']['elementsValue'].length; i++) {
          var questionName = options['oldCurrentPage']['elementsValue'][i]['name'];
          if (questionName === 'groups') {
            setChoices(questionName, 'assets', 3);
          } else if (questionName === 'assets') {
            setChoices(questionName, 'impacts', 1);
            setChoices(questionName, 'threats', 6);
            setChoices(questionName, 'vulnerabilities', 3);
          } else if (questionName === 'functions') {
            setChoices(questionName, 'assets', 4);
          };
        };
      };
    };

    var nameToId = function(data) {
      for (var i = 0; i < data['assets'].length; i++) {
        for (var j = 0; j < data['functions'].length; j++) {
          if (data['assets'][i]['function'] === data['functions'][j]['name']) {
            data['assets'][i]['function'] = data['functions'][j]['id'];
          };
        };
        for (var j = 0; j < data['groups'].length; j++) {
          if (data['assets'][i]['group'] === data['groups'][j]['name']) {
            data['assets'][i]['group'] = data['groups'][j]['id'];
          };
        };
        for (var j = 0; j < data['threats'].length; j++) {
          for (var k = 0; k < data['threats'][j]['assetsThreatened'].length; k++) {
            if (data['threats'][j]['assetsThreatened'][k] === data['assets'][i]['name']) {
              data['threats'][j]['assetsThreatened'][k] = data['assets'][i]['id'];
            };
          };
        };
        for (var j = 0; j < data['vulnerabilities'].length; j++) {
          for (var k = 0; k < data['vulnerabilities'][j]['assets'].length; k++) {
            if (data['vulnerabilities'][j]['assets'][k] === data['assets'][i]['name']) {
              data['vulnerabilities'][j]['assets'][k] = data['assets'][i]['id'];
            };
          };
        };
      };
      return data;
    };

    var impactToAsset = function(cviData) {
      for (var i = 0; i < cviData['assets'].length; i++) {
        cviData['assets'][i]['impact'] = {
          'id': cviData['impacts'][i]['id'],
          'integrity': Number(cviData['impacts'][i]['integrity']),
          'confidentiality':  Number(cviData['impacts'][i]['confidentiality']),
          'availability':  Number(cviData['impacts'][i]['availability']),
        };
      };
      delete cviData['impacts'];
      return cviData;
    };

    var mapSensitivity = function(cviData) {
      for (var i = 0; i < cviData['assets'].length; i++) {
        if (cviData['assets'][i]['sensitivity'] == 'Critical') {
          cviData['assets'][i]['sensitivity'] = 5;
        } else if (cviData['assets'][i]['sensitivity'] == 'High') {
          cviData['assets'][i]['sensitivity'] = 4;
        } else if (cviData['assets'][i]['sensitivity'] == 'Medium') {
          cviData['assets'][i]['sensitivity'] = 3;
        } else if (cviData['assets'][i]['sensitivity'] == 'Low') {
          cviData['assets'][i]['sensitivity'] = 2;
        } else {
          cviData['assets'][i]['sensitivity'] = 1;
        };
      };
      return cviData;
    };

    var postCVIData = function(surveyResults) {
      var cviDataPOST = nameToId(surveyResults['data']);
      cviDataPOST = impactToAsset(cviDataPOST);
      cviDataPOST = mapSensitivity(cviDataPOST);
      CVIService.postCVIData(cviDataPOST)
      .subscribe(postResponse => {
      });
    };

    Survey.SurveyNG.render('cvi', {
      model: cvi,
      data: data,
      onCurrentPageChanged: onNext,
      onComplete: postCVIData
    });

    function setChoices(source, targetQuestion, questionNumber) {
      if (cvi.getValue(source)) {
        var value = [];
        var data = cvi.getValue(source);
        for (var i = 0; i < data.length; i++) {
          if (data[i].name) {
            value.push(data[i].name);
          };
        };
        value = value.filter((v, i, a) => a.indexOf(v) === i);
        cvi.getQuestionByName(targetQuestion).columns[questionNumber].choices = value;
        cvi.render();
      };
    };
  };


  insertCVIData() {
    this.CVIService.getCVIAnswers()
    .subscribe(CVIAnswers => {
      this.CVIAnswers = CVIAnswers
      this.renderCVI(this.CVIAnswers);
    });
  };

  postSampleCVI() {
    this.sentSampleDataSuccess = 0;
    this.sentSampleDataError = 0;
    this.sendingSampleData = 1;
    this.CVIService.getSampleCVIData()
    .subscribe(sampleCVIData => {
      this.CVIService.postCVIData(sampleCVIData)
      .subscribe(postResponse => {
        this.sendingSampleData = 0;
        if (postResponse['status'] == 201) {
          this.sentSampleDataSuccess = 1;
        } else {
          this.sentSampleDataError = 1;
        };
      });
    })
  };

  resetCVI() {
    this.renderCVI({
    });
  };
}

import * as Survey from 'survey-angular';

import { Component, OnInit, Injectable } from '@angular/core';
import { HTTP_PROVIDERS } from "@angular/http";

import { SurveyService } from './survey.service';

import 'rxjs/add/operator/map';


@Component({
  selector:'Survey',
  templateUrl: 'app/survey/survey.component.html',
  providers: [SurveyService, HTTP_PROVIDERS]
})

@Injectable()
export class SurveyComponent implements OnInit  {
  riskAppetite : any;

  constructor(private surveyService: SurveyService) {
    this.riskAppetite = surveyService.riskAppetite;
  };

  ngOnInit() {
    Survey.Survey.cssType = "bootstrap";
    Survey.defaultBootstrapCss.navigationButton = "btn btn-success";
    Survey.defaultBootstrapCss.matrixdynamic.button = "btn btn-default";
    Survey.defaultBootstrapCss.progressBar = "progress-bar progress-bar-success progress-bar-striped active";

    this.surveyService.getSurveyQuestions()
    .subscribe(surveyJSON => {
      var surveyJSON = surveyJSON;
      surveyJSON.showProgressBar = "bottom";

      var surveyServicePass = this.surveyService;
      var survey = new Survey.Model(surveyJSON);

      var surveySendResult = function(surveyResults, surveyService = surveyServicePass) {
        surveyService.postRiskAppetiteData(surveyResults.data)
        .subscribe(postResponse => {
          var riskAppetiteResponse = postResponse.json
          surveyService.getRiskAppetiteData(riskAppetiteResponse)
        });
      };

      Survey.SurveyNG.render("surveyElement",
      {
        model: survey,
        onComplete: surveySendResult
      });
    });
  };
}

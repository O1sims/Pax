System.register(["survey-angular", "@angular/core", "@angular/http", "./survey.service", "rxjs/add/operator/map"], function (exports_1, context_1) {
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
    var Survey, core_1, http_1, survey_service_1, SurveyComponent;
    return {
        setters: [
            function (Survey_1) {
                Survey = Survey_1;
            },
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (http_1_1) {
                http_1 = http_1_1;
            },
            function (survey_service_1_1) {
                survey_service_1 = survey_service_1_1;
            },
            function (_1) {
            }
        ],
        execute: function () {
            SurveyComponent = class SurveyComponent {
                constructor(surveyService) {
                    this.surveyService = surveyService;
                    this.riskAppetite = surveyService.riskAppetite;
                }
                ;
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
                        var surveySendResult = function (surveyResults, surveyService = surveyServicePass) {
                            surveyService.postRiskAppetiteData(surveyResults.data)
                                .subscribe(postResponse => {
                                var riskAppetiteResponse = postResponse.json;
                                surveyService.getRiskAppetiteData(riskAppetiteResponse);
                            });
                        };
                        Survey.SurveyNG.render("surveyElement", {
                            model: survey,
                            onComplete: surveySendResult
                        });
                    });
                }
                ;
            };
            SurveyComponent = __decorate([
                core_1.Component({
                    selector: 'Survey',
                    templateUrl: 'app/survey/survey.component.html',
                    providers: [survey_service_1.SurveyService, http_1.HTTP_PROVIDERS]
                }),
                core_1.Injectable(),
                __metadata("design:paramtypes", [survey_service_1.SurveyService])
            ], SurveyComponent);
            exports_1("SurveyComponent", SurveyComponent);
        }
    };
});
//# sourceMappingURL=survey.component.js.map
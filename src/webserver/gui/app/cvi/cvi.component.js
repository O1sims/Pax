System.register(["@angular/core", "@angular/http", "survey-angular", "angular2-modal", "./cvi.service", "rxjs/add/operator/map"], function (exports_1, context_1) {
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
    var core_1, http_1, Survey, angular2_modal_1, cvi_service_1, CVIComponent;
    return {
        setters: [
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (http_1_1) {
                http_1 = http_1_1;
            },
            function (Survey_1) {
                Survey = Survey_1;
            },
            function (angular2_modal_1_1) {
                angular2_modal_1 = angular2_modal_1_1;
            },
            function (cvi_service_1_1) {
                cvi_service_1 = cvi_service_1_1;
            },
            function (_1) {
            }
        ],
        execute: function () {
            CVIComponent = class CVIComponent {
                constructor(vcRef, modal, CVIService) {
                    this.modal = modal;
                    this.CVIService = CVIService;
                    this.sendingSampleData = 0;
                    this.sentSampleDataError = 0;
                    this.sentSampleDataSuccess = 0;
                    modal.defaultViewContainer = vcRef;
                }
                ;
                ngOnInit() {
                    Survey.Survey.cssType = "bootstrap";
                    Survey.defaultBootstrapCss.navigationButton = "btn btn-success";
                    Survey.defaultBootstrapCss.matrixdynamic.button = "btn btn-default";
                    Survey.defaultBootstrapCss.progressBar = "progress-bar progress-bar-success progress-bar-striped active";
                    this.CVIService.getCVIQuestions()
                        .subscribe(surveyJSON => {
                        this.CVIQuestions = surveyJSON;
                        this.renderCVI({});
                    });
                }
                ;
                renderCVI(data) {
                    var cvi = new Survey['Model'](this.CVIQuestions);
                    cvi.showProgressBar = "bottom";
                    var CVIService = this.CVIService;
                    var onNext = function (sender, options) {
                        CVIService.getCurrentSection(options['newCurrentPage']['elementsValue'][0]['name']);
                        if (options['oldCurrentPage'] != null) {
                            for (var i = 0; i < options['oldCurrentPage']['elementsValue'].length; i++) {
                                var questionName = options['oldCurrentPage']['elementsValue'][i]['name'];
                                if (questionName === 'groups') {
                                    setChoices(questionName, 'assets', 3);
                                }
                                else if (questionName === 'assets') {
                                    setChoices(questionName, 'impacts', 1);
                                    setChoices(questionName, 'threats', 6);
                                    setChoices(questionName, 'vulnerabilities', 3);
                                }
                                else if (questionName === 'functions') {
                                    setChoices(questionName, 'assets', 4);
                                }
                                ;
                            }
                            ;
                        }
                        ;
                    };
                    var nameToId = function (data) {
                        for (var i = 0; i < data['assets'].length; i++) {
                            for (var j = 0; j < data['functions'].length; j++) {
                                if (data['assets'][i]['function'] === data['functions'][j]['name']) {
                                    data['assets'][i]['function'] = data['functions'][j]['id'];
                                }
                                ;
                            }
                            ;
                            for (var j = 0; j < data['groups'].length; j++) {
                                if (data['assets'][i]['group'] === data['groups'][j]['name']) {
                                    data['assets'][i]['group'] = data['groups'][j]['id'];
                                }
                                ;
                            }
                            ;
                            for (var j = 0; j < data['threats'].length; j++) {
                                for (var k = 0; k < data['threats'][j]['assetsThreatened'].length; k++) {
                                    if (data['threats'][j]['assetsThreatened'][k] === data['assets'][i]['name']) {
                                        data['threats'][j]['assetsThreatened'][k] = data['assets'][i]['id'];
                                    }
                                    ;
                                }
                                ;
                            }
                            ;
                            for (var j = 0; j < data['vulnerabilities'].length; j++) {
                                for (var k = 0; k < data['vulnerabilities'][j]['assets'].length; k++) {
                                    if (data['vulnerabilities'][j]['assets'][k] === data['assets'][i]['name']) {
                                        data['vulnerabilities'][j]['assets'][k] = data['assets'][i]['id'];
                                    }
                                    ;
                                }
                                ;
                            }
                            ;
                        }
                        ;
                        return data;
                    };
                    var impactToAsset = function (cviData) {
                        for (var i = 0; i < cviData['assets'].length; i++) {
                            cviData['assets'][i]['impact'] = {
                                'id': cviData['impacts'][i]['id'],
                                'integrity': Number(cviData['impacts'][i]['integrity']),
                                'confidentiality': Number(cviData['impacts'][i]['confidentiality']),
                                'availability': Number(cviData['impacts'][i]['availability']),
                            };
                        }
                        ;
                        delete cviData['impacts'];
                        return cviData;
                    };
                    var mapSensitivity = function (cviData) {
                        for (var i = 0; i < cviData['assets'].length; i++) {
                            if (cviData['assets'][i]['sensitivity'] == 'Critical') {
                                cviData['assets'][i]['sensitivity'] = 5;
                            }
                            else if (cviData['assets'][i]['sensitivity'] == 'High') {
                                cviData['assets'][i]['sensitivity'] = 4;
                            }
                            else if (cviData['assets'][i]['sensitivity'] == 'Medium') {
                                cviData['assets'][i]['sensitivity'] = 3;
                            }
                            else if (cviData['assets'][i]['sensitivity'] == 'Low') {
                                cviData['assets'][i]['sensitivity'] = 2;
                            }
                            else {
                                cviData['assets'][i]['sensitivity'] = 1;
                            }
                            ;
                        }
                        ;
                        return cviData;
                    };
                    var postCVIData = function (surveyResults) {
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
                                }
                                ;
                            }
                            ;
                            value = value.filter((v, i, a) => a.indexOf(v) === i);
                            cvi.getQuestionByName(targetQuestion).columns[questionNumber].choices = value;
                            cvi.render();
                        }
                        ;
                    }
                    ;
                }
                ;
                insertCVIData() {
                    this.CVIService.getCVIAnswers()
                        .subscribe(CVIAnswers => {
                        this.CVIAnswers = CVIAnswers;
                        this.renderCVI(this.CVIAnswers);
                    });
                }
                ;
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
                            }
                            else {
                                this.sentSampleDataError = 1;
                            }
                            ;
                        });
                    });
                }
                ;
                resetCVI() {
                    this.renderCVI({});
                }
                ;
            };
            CVIComponent = __decorate([
                core_1.Component({
                    selector: 'CVI',
                    templateUrl: 'app/cvi/cvi.component.html',
                    providers: [cvi_service_1.CVIService, angular2_modal_1.Modal, http_1.HTTP_PROVIDERS]
                }),
                core_1.Injectable(),
                __metadata("design:paramtypes", [core_1.ViewContainerRef, angular2_modal_1.Modal, cvi_service_1.CVIService])
            ], CVIComponent);
            exports_1("CVIComponent", CVIComponent);
        }
    };
});
//# sourceMappingURL=cvi.component.js.map
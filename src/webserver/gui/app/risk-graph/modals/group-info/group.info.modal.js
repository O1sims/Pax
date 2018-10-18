System.register(["@angular/core", "@angular/http", "angular2-modal", "angular2-modal/plugins/bootstrap", "../../../courses/modals/action-modal/courses.action.modal", "../asset-info/asset.info.modal.service"], function (exports_1, context_1) {
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
    var core_1, http_1, angular2_modal_1, angular2_modal_2, bootstrap_1, courses_action_modal_1, asset_info_modal_service_1, GroupInfoWindowData, GroupInfoWindow;
    return {
        setters: [
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (http_1_1) {
                http_1 = http_1_1;
            },
            function (angular2_modal_1_1) {
                angular2_modal_1 = angular2_modal_1_1;
                angular2_modal_2 = angular2_modal_1_1;
            },
            function (bootstrap_1_1) {
                bootstrap_1 = bootstrap_1_1;
            },
            function (courses_action_modal_1_1) {
                courses_action_modal_1 = courses_action_modal_1_1;
            },
            function (asset_info_modal_service_1_1) {
                asset_info_modal_service_1 = asset_info_modal_service_1_1;
            }
        ],
        execute: function () {
            GroupInfoWindowData = class GroupInfoWindowData extends bootstrap_1.BSModalContext {
                constructor(groupInfoData) {
                    super();
                    this.groupInfoData = groupInfoData;
                }
            };
            exports_1("GroupInfoWindowData", GroupInfoWindowData);
            GroupInfoWindow = class GroupInfoWindow {
                constructor(dialog, vcRef, modal, assetInfoService) {
                    this.dialog = dialog;
                    this.modal = modal;
                    this.assetInfoService = assetInfoService;
                    this.noThreats = 0;
                    this.threatData = [];
                    this.threatSelected = [];
                    this.impactInfo = {
                        'confidentiality': 0,
                        'integrity': 0,
                        'availability': 0
                    };
                    this.assetSelected = [];
                    this.noActions = 0;
                    this.actionRows = [];
                    this.actionSelected = [];
                    this.groupOverview = 0;
                    this.actionOverview = 0;
                    this.riskImpact = {
                        'consequence': 10,
                        'likelihood': 8
                    };
                    modal.defaultViewContainer = vcRef;
                    dialog.context.size = 'lg';
                    this.groupInfoData = dialog['context']['groupInfoData'];
                    this.groupName = this.groupInfoData[0]['group'];
                    this.groupFunction = this.groupInfoData[0]['function'];
                    this.impactInfo['confidentiality'] = this.groupInfoData[0]['confidentiality'];
                    this.impactInfo['integrity'] = this.groupInfoData[0]['integrity'];
                    this.impactInfo['availability'] = this.groupInfoData[0]['availability'];
                }
                ;
                ngOnInit() {
                    this.groupView();
                }
                ;
                groupView() {
                    this.groupOverview = 1;
                    this.actionOverview = 0;
                    this.maxRisk = 0;
                    for (var i = 0; i < this.groupInfoData.length; i++) {
                        this.groupInfoData[i]['riskLabel'] = this.getRiskLabel(this.groupInfoData[i]['currentRiskScore']);
                        this.assetInfoService.getThreatData(this.groupInfoData[i]['assetId'])
                            .subscribe(threats => {
                            var threatLength = threats.length;
                            if (threatLength > 0) {
                                for (var j = 0; j < threatLength; j++) {
                                    var threatId = threats[j]['id'];
                                    var inThisAlready = 0;
                                    if (this.threatData.length == 0) {
                                        this.threatData.push(threats[j]);
                                    }
                                    else {
                                        for (var k = 0; k < this.threatData.length; k++) {
                                            if (threatId === this.threatData[k]['id']) {
                                                inThisAlready = 1;
                                            }
                                            ;
                                        }
                                        ;
                                        if (inThisAlready == 0) {
                                            this.threatData.push(threats[j]);
                                        }
                                        ;
                                    }
                                    ;
                                }
                                ;
                            }
                            ;
                            if (this.threatData.length == 0) {
                                this.noThreats = 1;
                            }
                            else {
                                this.noThreats = 0;
                                this.threatRows = this.threatData;
                            }
                            ;
                        });
                        if (this.groupInfoData[i]['currentRiskScore'] > this.maxRisk) {
                            this.maxRisk = this.groupInfoData[i]['currentRiskScore'];
                        }
                        ;
                    }
                    ;
                    this.maxRiskLabel = this.getRiskLabel(this.maxRisk);
                    this.assetRows = this.groupInfoData;
                }
                ;
                actionView() {
                    this.groupOverview = 0;
                    this.actionOverview = 1;
                    for (var i = 0; i < this.groupInfoData.length; i++) {
                        this.getActions(this.groupInfoData[i]['assetId']);
                    }
                    ;
                }
                ;
                getActions(assetId) {
                    this.assetInfoService.getActions(assetId)
                        .subscribe(actionData => {
                        for (var j = 0; j < actionData.length; j++) {
                            var actionId = actionData[j]['id'];
                            var inThisAlready = 0;
                            if (this.actionRows.length == 0) {
                                if (actionData[j]['staged'] == 1) {
                                    actionData[j]['actionStatus'] = 'Remove action';
                                }
                                else {
                                    actionData[j]['actionStatus'] = 'Stage action';
                                }
                                ;
                                this.actionRows.push(actionData[j]);
                            }
                            else {
                                for (var k = 0; k < this.actionRows.length; k++) {
                                    if (actionId === this.actionRows[k]['id']) {
                                        inThisAlready = 1;
                                    }
                                    ;
                                }
                                ;
                                if (inThisAlready == 0) {
                                    if (actionData[j]['staged'] == 1) {
                                        actionData[j]['actionStatus'] = 'Remove action';
                                    }
                                    else {
                                        actionData[j]['actionStatus'] = 'Stage action';
                                    }
                                    ;
                                    this.actionRows.push(actionData[j]);
                                }
                                ;
                            }
                            ;
                        }
                        ;
                        if (this.actionRows.length > 0) {
                            this.noActions = 0;
                        }
                        else {
                            this.noActions = 1;
                        }
                        ;
                    });
                }
                ;
                toggleActiveAction(event, action) {
                    if (action['staged']) {
                        action['staged'] = 0;
                        action.actionStatus = 'Stage action';
                    }
                    else {
                        action['staged'] = 1;
                        action.actionStatus = 'Remove action';
                    }
                    ;
                    this.assetInfoService.toggleAction(action['actionId'], action['staged'])
                        .subscribe(activeData => {
                        for (var i = 0; i < this.groupInfoData.length; i++) {
                            this.getActions(this.groupInfoData[i]['id']);
                        }
                        ;
                    });
                }
                ;
                getRiskLabel(riskScore) {
                    if (riskScore >= 10) {
                        return 'Critical';
                    }
                    else if (riskScore >= 7.5) {
                        return 'High';
                    }
                    else if (riskScore >= 5) {
                        return 'Medium';
                    }
                    else if (riskScore >= 2.5) {
                        return 'Low';
                    }
                    else {
                        return 'Very low';
                    }
                    ;
                }
                ;
                onSelect({ selected }) {
                }
                ;
                onClickActionTable(event) {
                    return this.modal.open(courses_action_modal_1.ActionWindow, new courses_action_modal_1.ActionWindowData(event.row, this.riskImpact));
                }
                ;
                closeModal() {
                    this.dialog.close();
                }
                ;
            };
            GroupInfoWindow = __decorate([
                core_1.Component({
                    selector: 'modal-content',
                    templateUrl: './app/risk-graph/modals/group-info/group.info.modal.html',
                    providers: [asset_info_modal_service_1.AssetInfoService, angular2_modal_1.Modal, http_1.HTTP_PROVIDERS]
                }),
                __metadata("design:paramtypes", [angular2_modal_2.DialogRef, core_1.ViewContainerRef, angular2_modal_1.Modal, asset_info_modal_service_1.AssetInfoService])
            ], GroupInfoWindow);
            exports_1("GroupInfoWindow", GroupInfoWindow);
        }
    };
});
//# sourceMappingURL=group.info.modal.js.map
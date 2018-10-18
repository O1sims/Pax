System.register(["@angular/core", "@angular/http", "./home.service"], function (exports_1, context_1) {
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
    var core_1, http_1, home_service_1, HomeComponent;
    return {
        setters: [
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (http_1_1) {
                http_1 = http_1_1;
            },
            function (home_service_1_1) {
                home_service_1 = home_service_1_1;
            }
        ],
        execute: function () {
            HomeComponent = class HomeComponent {
                constructor(homeService) {
                    this.homeService = homeService;
                    this.dataStatus = {
                        'status': 'Checking now...',
                        'reason': ''
                    };
                    this.counter = 0;
                    this.threatDataLoading = 0;
                    this.networkDataLoading = 0;
                }
                ;
                ngOnInit() {
                    this.checkForData();
                }
                ;
                checkForData() {
                    this.counter = 0;
                    var dbURLs = [
                        'application/network/',
                        'application/risk_appetite/',
                        'application/missions/'
                    ];
                    var flags = new Array(dbURLs.length).fill(0);
                    for (var i = 0; i < dbURLs.length; i++) {
                        this.homeService.checkData(dbURLs[i])
                            .subscribe(dataCheck => {
                            this.dataStatus.status = 'Checking now...';
                            if (dataCheck.count > 0) {
                                flags[this.counter] = 1;
                            }
                            else {
                                flags[this.counter] = 0;
                            }
                            ;
                            if (this.counter == dbURLs.length - 1) {
                                if (flags.reduce((pv, cv) => pv + cv, 0) == dbURLs.length) {
                                    this.dataStatus.status = 'All relevant data is loaded into the database';
                                    this.dataStatus.reason = '';
                                }
                                else {
                                    this.dataStatus.status = 'Please insert relevant data into the database';
                                    if (flags[3] == 0 && flags[0] == 1) {
                                        this.dataStatus.reason = '(Threat data required)';
                                    }
                                    else if (flags[3] == 1 && flags[0] == 0) {
                                        this.dataStatus.reason = '(Network data required)';
                                    }
                                    else {
                                        this.dataStatus.reason = '(Threat and network data required)';
                                    }
                                    ;
                                }
                                ;
                            }
                            ;
                            this.counter++;
                        });
                    }
                    ;
                }
                ;
                postNetworkData() {
                    this.homeService.getNetworkData()
                        .subscribe(networkData => {
                        this.homeService.postNetworkData(networkData)
                            .subscribe(response => {
                            this.networkDataStatus = response.status;
                            this.networkDataLoading = 0;
                            this.checkForData();
                        });
                    });
                }
                ;
                postRiskAppetiteData() {
                    this.homeService.getRiskAppetiteData()
                        .subscribe(riskAppetiteData => {
                        this.homeService.postRiskAppetiteData(riskAppetiteData)
                            .subscribe(response => {
                            this.riskAppetiteDataStatus = response.status;
                        });
                    });
                }
                ;
                postThreatActorData(threatActor, threatCategory) {
                    this.threatDataLoading = 1;
                    this.homeService.getThreatActorData(threatActor)
                        .subscribe(threatActorData => {
                        var threatActorData = threatActorData;
                        this.homeService.getThreatActions()
                            .subscribe(threatActions => {
                            var threatActions = threatActions;
                            var threatData = {};
                            for (var key in threatActorData)
                                threatData[key] = threatActorData[key];
                            for (var key in threatActions)
                                threatData[key] = threatActions[key];
                            threatData['threat_category'] = threatCategory;
                            this.homeService.postThreatData(threatData)
                                .subscribe(response => {
                                this.threatActorStatus = response.status;
                                this.threatDataLoading = 0;
                                this.checkForData();
                            });
                        });
                    });
                }
                ;
                postAllData() {
                    this.networkDataLoading = 1;
                    this.postNetworkData();
                    this.postRiskAppetiteData();
                }
                ;
                dropAllData() {
                    var urlList = [
                        'network',
                        'threats',
                        'risk_appetite',
                        'missions',
                        'actions',
                        'groups',
                        'functions',
                        'impacts',
                        'cvi',
                        'vulnerabilities',
                        'assets',
                        'devices'
                    ];
                    for (var i = 0; i < urlList.length; i++) {
                        this.homeService.dropData('/application/' + urlList[i] + '/')
                            .subscribe(response => {
                            this.dropDataStatus = response.status;
                        });
                    }
                    ;
                    this.checkForData();
                }
                ;
            };
            HomeComponent = __decorate([
                core_1.Component({
                    selector: 'Home',
                    templateUrl: "app/home/home.component.html",
                    providers: [home_service_1.HomeService, http_1.HTTP_PROVIDERS]
                }),
                __metadata("design:paramtypes", [home_service_1.HomeService])
            ], HomeComponent);
            exports_1("HomeComponent", HomeComponent);
        }
    };
});
//# sourceMappingURL=home.component.js.map
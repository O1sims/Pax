System.register(["@angular/http", "@angular/core", "rxjs/add/operator/map"], function (exports_1, context_1) {
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
    var http_1, core_1, HomeService;
    return {
        setters: [
            function (http_1_1) {
                http_1 = http_1_1;
            },
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (_1) {
            }
        ],
        execute: function () {
            HomeService = class HomeService {
                constructor(http) {
                    this.http = http;
                }
                ;
                // CHECK DATA
                checkData(url) {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: url
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                // GET
                getNetworkData() {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: 'app/home/data/network.data.json'
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                getRiskAppetiteData() {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: 'app/home/data/risk.appetite.data.json'
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                getThreatActions() {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: 'app/home/data/threat-data/threat.actions.data.json'
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                getThreatActorData(threatActor) {
                    var threatDataURL = 'app/home/data/threat-data/threat-actor/' + threatActor + '.threat.data.json';
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: threatDataURL
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                // POST
                postNetworkData(networkData) {
                    var headers = new http_1.Headers();
                    headers.append("Content-Type", 'application/json');
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Post,
                        url: 'application/network/',
                        headers: headers,
                        body: JSON.stringify(networkData)
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map((res) => {
                        if (res) {
                            return {
                                status: res.status
                            };
                        }
                    });
                }
                ;
                postRiskAppetiteData(riskAppetiteData) {
                    var headers = new http_1.Headers();
                    headers.append("Content-Type", 'application/json');
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Post,
                        url: 'application/risk_appetite/',
                        headers: headers,
                        body: JSON.stringify(riskAppetiteData)
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map((res) => {
                        if (res) {
                            return {
                                status: res.status
                            };
                        }
                    });
                }
                ;
                postThreatData(threatData) {
                    var headers = new http_1.Headers();
                    headers.append("Content-Type", 'application/json');
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Post,
                        url: 'application/threats/',
                        headers: headers,
                        body: JSON.stringify(threatData)
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map((res) => {
                        if (res) {
                            return {
                                status: res.status
                            };
                        }
                    });
                }
                ;
                // DELETE
                dropData(url) {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Delete,
                        url: url
                    });
                    return this.http.request(new http_1.Request(requestoptions));
                }
                ;
            };
            HomeService = __decorate([
                core_1.Injectable(),
                __metadata("design:paramtypes", [http_1.Http])
            ], HomeService);
            exports_1("HomeService", HomeService);
        }
    };
});
//# sourceMappingURL=home.service.js.map
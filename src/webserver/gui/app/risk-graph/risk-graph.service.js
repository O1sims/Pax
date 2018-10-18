System.register(["@angular/http", "../environment/environment", "@angular/core", "rxjs/add/operator/map"], function (exports_1, context_1) {
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
    var http_1, environment_1, core_1, RiskGraphService;
    return {
        setters: [
            function (http_1_1) {
                http_1 = http_1_1;
            },
            function (environment_1_1) {
                environment_1 = environment_1_1;
            },
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (_1) {
            }
        ],
        execute: function () {
            RiskGraphService = class RiskGraphService {
                constructor(http) {
                    this.http = http;
                    this.api = "/api/v" + environment_1.environment.API_VERSION;
                }
                ;
                getMissionTimeAssessment(systemId, missionTaskData) {
                    var headers = new http_1.Headers();
                    headers.append("Content-Type", 'application/json');
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Post,
                        url: this.api + '/system/mission_time/' + systemId + '/',
                        headers: headers,
                        body: JSON.stringify(missionTaskData)
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                getEstimatedTime(systemId, task) {
                    var headers = new http_1.Headers();
                    headers.append("Content-Type", 'application/json');
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Post,
                        url: this.api + '/actions/estimated_time/' + systemId + '/',
                        headers: headers,
                        body: JSON.stringify(task)
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                // GET Unit list
                getMissionUnits() {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: this.C2REST + 'entity/Unit'
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                // GET Mission data
                getAllMissions() {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: this.api + '/missions/'
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                getMissionData(missionId) {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: this.api + '/missions/' + missionId
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                // POST Task
                postTask(missionId, coaId, task) {
                    var headers = new http_1.Headers();
                    headers.append("Content-Type", 'application/json');
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Post,
                        url: this.C2REST + 'coa/mission/' + missionId + '/coa/' + coaId + '/task',
                        headers: headers,
                        body: JSON.stringify(task)
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map((res) => {
                        if (res) {
                            return {
                                status: res.status
                            };
                        }
                        ;
                    });
                }
                ;
                // DELETE Task
                deleteTask(missionId, coaId, taskId) {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Delete,
                        url: this.C2REST + 'coa/mission/' + missionId + '/coa/' + coaId + '/task/' + taskId
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map((res) => {
                        if (res) {
                            return {
                                status: res.status
                            };
                        }
                        ;
                    });
                }
                ;
                // Create new COA
                postCOA(missionId, name) {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Post,
                        url: this.C2REST + 'coa/mission/' + missionId + '/coa/' + name
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map((res) => {
                        if (res) {
                            return { status: res.status };
                        }
                        ;
                    });
                }
                ;
                // DELETE COA
                deleteCOA(missionId, coaId) {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Delete,
                        url: this.C2REST + 'coa/mission/' + missionId + '/coa/' + coaId
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map((res) => {
                        if (res) {
                            return { status: res.status };
                        }
                        ;
                    });
                }
                ;
                postSystemRiskAnalysis(systemId) {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Post,
                        url: 'application/risk_analysis/system/' + systemId + '/'
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                postNewSystem(systemId, taskList) {
                    var headers = new http_1.Headers();
                    headers.append("Content-Type", 'application/json');
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Post,
                        url: 'application/system/task_update/' + systemId + '/',
                        headers: headers,
                        body: JSON.stringify(taskList)
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                postEffects(systemId, effectList) {
                    var headers = new http_1.Headers();
                    headers.append("Content-Type", 'application/json');
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Post,
                        url: 'application/risk_analysis/task_dependency/' + systemId + '/',
                        headers: headers,
                        body: JSON.stringify(effectList)
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                compareCOAs(systemId, coAs) {
                    var headers = new http_1.Headers();
                    headers.append("Content-Type", 'application/json');
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Post,
                        url: 'application/risk_analysis/compare_system/' + systemId + '/',
                        headers: headers,
                        body: JSON.stringify(coAs)
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                // GET System data
                getSystemData(systemId) {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: this.api + '/cvi/' + systemId
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
            };
            RiskGraphService = __decorate([
                core_1.Injectable(),
                __metadata("design:paramtypes", [http_1.Http])
            ], RiskGraphService);
            exports_1("RiskGraphService", RiskGraphService);
            ;
        }
    };
});
//# sourceMappingURL=risk-graph.service.js.map
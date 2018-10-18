System.register(["@angular/http", "../../../environment/environment", "@angular/core", "rxjs/add/operator/map"], function (exports_1, context_1) {
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
    var http_1, environment_1, core_1, AssetInfoService;
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
            AssetInfoService = class AssetInfoService {
                constructor(_http) {
                    this._http = _http;
                    this.api = "/api/v" + environment_1.environment.API_VERSION;
                }
                getMissionData() {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: 'application/missions'
                    });
                    return this._http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                getAssetVulnerabilities(systemId, assetId) {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: 'application/system/vulnerabilities/' + systemId + '/' + assetId + '/'
                    });
                    return this._http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                getUnitDistance(systemId, assetId, actorId) {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: 'application/geolocation/distance/' + systemId + '/' + assetId + '/' + actorId + '/'
                    });
                    return this._http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                getAssetLocation(systemId, assetId) {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: 'application/system/location/' + systemId + '/' + assetId + '/'
                    });
                    return this._http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                getAssetThreats(systemId, assetId) {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: 'application/system/threats/' + systemId + '/' + assetId + '/'
                    });
                    return this._http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                getAllEffectsBasedActions(systemId) {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: 'application/actions/effects/' + systemId
                    });
                    return this._http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                getEffectsBasedActionsObjective(systemId, objectiveId) {
                    let params = new http_1.URLSearchParams();
                    params.set('objective', objectiveId);
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: 'application/actions/effects/' + systemId,
                        search: params
                    });
                    return this._http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                postEffectsBasedAction(systemId, effectActionData) {
                    var headers = new http_1.Headers();
                    headers.append("Content-Type", 'application/json');
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Post,
                        url: 'application/actions/effects/' + systemId + '/',
                        headers: headers,
                        body: JSON.stringify(effectActionData)
                    });
                    return this._http.request(new http_1.Request(requestoptions))
                        .map((res) => {
                        if (res) {
                            return {
                                status: res.status
                            };
                        }
                    });
                }
                ;
                deleteEffectsBasedActions(systemId, taskIds) {
                    var headers = new http_1.Headers();
                    headers.append("Content-Type", 'application/json');
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Delete,
                        url: 'application/actions/effects/' + systemId + '/',
                        headers: headers,
                        body: JSON.stringify({ 'effectIds': taskIds })
                    });
                    return this._http.request(new http_1.Request(requestoptions))
                        .map((res) => {
                        if (res) {
                            return {
                                status: res.status
                            };
                        }
                    });
                }
                ;
                getEffects() {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: this.api + '/effects/'
                    });
                    return this._http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                getObjectives(systemId) {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: 'application/system/assets/' + systemId
                    });
                    return this._http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                getUnits(systemId) {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: 'application/system/units/' + systemId
                    });
                    return this._http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                getUnitsAsset(systemId, assetId) {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: 'application/system/unit_distance/' + systemId + '/' + assetId
                    });
                    return this._http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                getNodeData(globalId) {
                    let params = new http_1.URLSearchParams();
                    params.set('globalId', globalId);
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: 'application/node-data',
                        search: params
                    });
                    return this._http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                getThreatData(assetId) {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: 'application/threats/asset/' + assetId
                    });
                    return this._http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                getVulnerabilityData(assetId) {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: 'application/vulnerabilities/asset/' + assetId
                    });
                    return this._http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                getDevices(assetId) {
                    let params = new http_1.URLSearchParams();
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: 'application/devices/asset/' + assetId,
                        search: params
                    });
                    return this._http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                getActions(assetId) {
                    let params = new http_1.URLSearchParams();
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: 'application/actions/asset/id/' + assetId,
                        search: params
                    });
                    return this._http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                toggleAction(actionId, newStagedStatus) {
                    var data = {
                        'staged': newStagedStatus
                    };
                    var headers = new http_1.Headers();
                    headers.append("Content-Type", 'application/json');
                    headers.append("Accept", 'application/json');
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Patch,
                        url: 'application/actions/staged/' + actionId,
                        headers: headers,
                        body: JSON.stringify(data)
                    });
                    return this._http.request(new http_1.Request(requestoptions))
                        .map((res) => {
                        if (res) {
                            return {
                                data: res.status
                            };
                        }
                    });
                }
                ;
            };
            AssetInfoService = __decorate([
                core_1.Injectable(),
                __metadata("design:paramtypes", [http_1.Http])
            ], AssetInfoService);
            exports_1("AssetInfoService", AssetInfoService);
        }
    };
});
//# sourceMappingURL=asset.info.modal.service.js.map
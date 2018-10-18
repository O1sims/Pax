System.register(["@angular/http", "@angular/core"], function (exports_1, context_1) {
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
    var http_1, core_1, ActionsService;
    return {
        setters: [
            function (http_1_1) {
                http_1 = http_1_1;
            },
            function (core_1_1) {
                core_1 = core_1_1;
            }
        ],
        execute: function () {
            ActionsService = class ActionsService {
                constructor(http) {
                    this.http = http;
                }
                ;
                deleteEffect(effect) {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Delete,
                        url: 'application/hostile_response/' + effect + '/'
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
                getHostileResponses(effect) {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: 'application/hostile_response/' + effect
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                patchHostileResponse(effect, hostileResponse) {
                    var headers = new http_1.Headers();
                    headers.append("Content-Type", 'application/json');
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Patch,
                        url: 'application/hostile_response/' + effect + '/',
                        headers: headers,
                        body: JSON.stringify(hostileResponse)
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
                submitNewEffect(data) {
                    var headers = new http_1.Headers();
                    headers.append("Content-Type", 'application/json');
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Post,
                        url: 'application/hostile_response/',
                        headers: headers,
                        body: JSON.stringify(data)
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map((res) => {
                        if (res) {
                            return { status: res.status };
                        }
                    });
                }
                ;
                getEffects() {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: 'application/effects/'
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                getEffectTypes() {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: 'app/actions/data/effect.types.json'
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                getActionData(force = "hostile") {
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Get,
                        url: 'application/action_list/all/' + force
                    });
                    return this.http.request(new http_1.Request(requestoptions))
                        .map(res => res.json());
                }
                ;
                patchActionData(actions, force, effect, type) {
                    var headers = new http_1.Headers();
                    headers.append("Content-Type", 'application/json');
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Patch,
                        url: 'application/action_list/type/' + force + '/' + effect + '/' + type + '/',
                        headers: headers,
                        body: JSON.stringify(actions)
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
            };
            ActionsService = __decorate([
                core_1.Injectable(),
                __metadata("design:paramtypes", [http_1.Http])
            ], ActionsService);
            exports_1("ActionsService", ActionsService);
        }
    };
});
//# sourceMappingURL=actions.service.js.map
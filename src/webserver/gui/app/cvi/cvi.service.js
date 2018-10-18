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
    var http_1, core_1, CVIService;
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
            CVIService = class CVIService {
                constructor(http) {
                    this.http = http;
                    this.section = {
                        'current': ''
                    };
                }
                ;
                getCVIQuestions() {
                    return this.http.get('app/cvi/data/cvi.questions.json')
                        .map(res => res.json());
                }
                ;
                getCVIAnswers() {
                    return this.http.get('app/cvi/data/cvi.answers.json')
                        .map(res => res.json());
                }
                ;
                getSampleCVIData() {
                    return this.http.get('app/cvi/data/c2-api-get-system-response.json')
                        .map(res => res.json());
                }
                ;
                getCurrentSection(currentSection) {
                    this.section['current'] = currentSection;
                }
                ;
                postCVIData(data) {
                    var headers = new http_1.Headers();
                    headers.append("Content-Type", 'application/json');
                    headers.append("Accept", 'application/json');
                    var requestoptions = new http_1.RequestOptions({
                        method: http_1.RequestMethod.Post,
                        url: 'application/system/',
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
            };
            CVIService = __decorate([
                core_1.Injectable(),
                __metadata("design:paramtypes", [http_1.Http])
            ], CVIService);
            exports_1("CVIService", CVIService);
        }
    };
});
//# sourceMappingURL=cvi.service.js.map
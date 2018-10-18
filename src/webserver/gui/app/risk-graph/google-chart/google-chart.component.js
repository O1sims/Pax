System.register(["@angular/core"], function (exports_1, context_1) {
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
    var core_1, GoogleChartComponent, GoogleChartComponent_1;
    return {
        setters: [
            function (core_1_1) {
                core_1 = core_1_1;
            }
        ],
        execute: function () {
            GoogleChartComponent = GoogleChartComponent_1 = class GoogleChartComponent {
                constructor() {
                    console.log("Here is GoogleChartComponent");
                }
                getGoogle() {
                    return google;
                }
                ngOnInit() {
                    if (!GoogleChartComponent_1.googleLoaded) {
                        GoogleChartComponent_1.googleLoaded = true;
                        google.charts.load('current', { packages: ['corechart', 'bar'] });
                    }
                    google.charts.setOnLoadCallback(() => this.drawGraph());
                }
                drawGraph() {
                    console.log("DrawGraph base class!!!! ");
                }
                createBarChart(element) {
                    return new google.visualization.BarChart(element);
                }
                createDataTable(array) {
                    return google.visualization.arrayToDataTable(array);
                }
            };
            GoogleChartComponent = GoogleChartComponent_1 = __decorate([
                core_1.Component({
                    selector: 'chart'
                }),
                __metadata("design:paramtypes", [])
            ], GoogleChartComponent);
            exports_1("GoogleChartComponent", GoogleChartComponent);
            ;
        }
    };
});
//# sourceMappingURL=google-chart.component.js.map
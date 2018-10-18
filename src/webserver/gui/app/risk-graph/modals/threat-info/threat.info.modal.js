System.register(["@angular/core", "@angular/http", "angular2-modal", "angular2-modal/plugins/bootstrap"], function (exports_1, context_1) {
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
    var core_1, http_1, angular2_modal_1, bootstrap_1, ThreatInfoWindowData, ThreatInfoWindow;
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
            },
            function (bootstrap_1_1) {
                bootstrap_1 = bootstrap_1_1;
            }
        ],
        execute: function () {
            ThreatInfoWindowData = class ThreatInfoWindowData extends bootstrap_1.BSModalContext {
                constructor(threatInfoData) {
                    super();
                    this.threatInfoData = threatInfoData;
                }
            };
            exports_1("ThreatInfoWindowData", ThreatInfoWindowData);
            ThreatInfoWindow = class ThreatInfoWindow {
                constructor(dialog) {
                    this.dialog = dialog;
                    dialog.context.size = 'lg';
                    this.threatInfoData = dialog.context['threatInfoData'];
                }
                ;
                closeModal() {
                    this.dialog.close();
                }
                ;
            };
            ThreatInfoWindow = __decorate([
                core_1.Component({
                    selector: 'modal-content',
                    templateUrl: './app/risk-graph/modals/threat-info/threat.info.modal.html',
                    providers: [http_1.HTTP_PROVIDERS]
                }),
                __metadata("design:paramtypes", [angular2_modal_1.DialogRef])
            ], ThreatInfoWindow);
            exports_1("ThreatInfoWindow", ThreatInfoWindow);
        }
    };
});
//# sourceMappingURL=threat.info.modal.js.map
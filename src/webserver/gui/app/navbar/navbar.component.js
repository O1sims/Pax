System.register(["@angular/core"], function (exports_1, context_1) {
    "use strict";
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __moduleName = context_1 && context_1.id;
    var core_1, NavBarComponent;
    return {
        setters: [
            function (core_1_1) {
                core_1 = core_1_1;
            }
        ],
        execute: function () {
            NavBarComponent = class NavBarComponent {
                ngOnInit() {
                    this.getPathname();
                }
                ;
                getPathname() {
                    this.pathName = window.location.pathname;
                    if (this.pathName == '/' || this.pathName == '/risk-graph') {
                        this.selectedTab = 'riskNetwork';
                    }
                    else if (this.pathName == '/cvi' || this.pathName == '/cvi/') {
                        this.selectedTab = 'cvi';
                    }
                    else if (this.pathName == '/risk-appetite' || this.pathName == '/risk-appetite/') {
                        this.selectedTab = 'riskAppetite';
                    }
                    else if (this.pathName == '/actions' || this.pathName == '/actions/') {
                        this.selectedTab = 'actions';
                    }
                    ;
                }
                ;
                assignSelectedTab(tabString) {
                    this.selectedTab = tabString;
                }
                ;
            };
            NavBarComponent = __decorate([
                core_1.Component({
                    selector: 'navbar',
                    templateUrl: 'app/navbar/navbar.component.html'
                })
            ], NavBarComponent);
            exports_1("NavBarComponent", NavBarComponent);
        }
    };
});
//# sourceMappingURL=navbar.component.js.map
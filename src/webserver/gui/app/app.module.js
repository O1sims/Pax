System.register(["@angular/core", "@angular/platform-browser", "ngx-popover", "angular2-modal", "angular2-modal/plugins/bootstrap", "ng2-charts", "@asymmetrik/ngx-leaflet", "@swimlane/ngx-datatable", "./app.component", "./survey/survey.component", "./risk-graph/risk-graph.component", "./risk-graph/modals/action-modal/courses.action.modal", "./risk-graph/modals/asset-info/asset.info.modal", "./risk-graph/modals/threat-info/threat.info.modal", "./navbar/navbar.component", "./not-found/not-found.component", "./app.routing"], function (exports_1, context_1) {
    "use strict";
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __moduleName = context_1 && context_1.id;
    var core_1, platform_browser_1, ngx_popover_1, angular2_modal_1, bootstrap_1, ng2_charts_1, ngx_leaflet_1, ngx_datatable_1, app_component_1, survey_component_1, risk_graph_component_1, courses_action_modal_1, asset_info_modal_1, threat_info_modal_1, navbar_component_1, not_found_component_1, app_routing_1, AppModule;
    return {
        setters: [
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (platform_browser_1_1) {
                platform_browser_1 = platform_browser_1_1;
            },
            function (ngx_popover_1_1) {
                ngx_popover_1 = ngx_popover_1_1;
            },
            function (angular2_modal_1_1) {
                angular2_modal_1 = angular2_modal_1_1;
            },
            function (bootstrap_1_1) {
                bootstrap_1 = bootstrap_1_1;
            },
            function (ng2_charts_1_1) {
                ng2_charts_1 = ng2_charts_1_1;
            },
            function (ngx_leaflet_1_1) {
                ngx_leaflet_1 = ngx_leaflet_1_1;
            },
            function (ngx_datatable_1_1) {
                ngx_datatable_1 = ngx_datatable_1_1;
            },
            function (app_component_1_1) {
                app_component_1 = app_component_1_1;
            },
            function (survey_component_1_1) {
                survey_component_1 = survey_component_1_1;
            },
            function (risk_graph_component_1_1) {
                risk_graph_component_1 = risk_graph_component_1_1;
            },
            function (courses_action_modal_1_1) {
                courses_action_modal_1 = courses_action_modal_1_1;
            },
            function (asset_info_modal_1_1) {
                asset_info_modal_1 = asset_info_modal_1_1;
            },
            function (threat_info_modal_1_1) {
                threat_info_modal_1 = threat_info_modal_1_1;
            },
            function (navbar_component_1_1) {
                navbar_component_1 = navbar_component_1_1;
            },
            function (not_found_component_1_1) {
                not_found_component_1 = not_found_component_1_1;
            },
            function (app_routing_1_1) {
                app_routing_1 = app_routing_1_1;
            }
        ],
        execute: function () {
            AppModule = class AppModule {
            };
            AppModule = __decorate([
                core_1.NgModule({
                    imports: [
                        angular2_modal_1.ModalModule.forRoot(),
                        ngx_leaflet_1.LeafletModule.forRoot(),
                        //       LeafletDrawModule.forRoot(),
                        bootstrap_1.BootstrapModalModule,
                        ngx_datatable_1.NgxDatatableModule,
                        platform_browser_1.BrowserModule,
                        ngx_popover_1.PopoverModule,
                        ng2_charts_1.ChartsModule,
                        app_routing_1.routing
                    ],
                    declarations: [
                        app_component_1.AppComponent,
                        survey_component_1.SurveyComponent,
                        risk_graph_component_1.RiskGraphComponent,
                        navbar_component_1.NavBarComponent,
                        not_found_component_1.NotFoundComponent
                    ],
                    bootstrap: [
                        app_component_1.AppComponent
                    ],
                    entryComponents: [
                        courses_action_modal_1.ActionWindow,
                        asset_info_modal_1.AssetInfoWindow,
                        threat_info_modal_1.ThreatInfoWindow
                    ]
                })
            ], AppModule);
            exports_1("AppModule", AppModule);
        }
    };
});
//# sourceMappingURL=app.module.js.map
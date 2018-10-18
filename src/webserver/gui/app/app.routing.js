System.register(["@angular/router", "./risk-graph/risk-graph.component", "./actions/actions.component", "./survey/survey.component", "./cvi/cvi.component", "./not-found/not-found.component"], function (exports_1, context_1) {
    "use strict";
    var __moduleName = context_1 && context_1.id;
    var router_1, risk_graph_component_1, actions_component_1, survey_component_1, cvi_component_1, not_found_component_1, routing;
    return {
        setters: [
            function (router_1_1) {
                router_1 = router_1_1;
            },
            function (risk_graph_component_1_1) {
                risk_graph_component_1 = risk_graph_component_1_1;
            },
            function (actions_component_1_1) {
                actions_component_1 = actions_component_1_1;
            },
            function (survey_component_1_1) {
                survey_component_1 = survey_component_1_1;
            },
            function (cvi_component_1_1) {
                cvi_component_1 = cvi_component_1_1;
            },
            function (not_found_component_1_1) {
                not_found_component_1 = not_found_component_1_1;
            }
        ],
        execute: function () {
            exports_1("routing", routing = router_1.RouterModule.forRoot([
                { path: 'risk-appetite', component: survey_component_1.SurveyComponent },
                { path: '', component: risk_graph_component_1.RiskGraphComponent },
                { path: 'risk-graph/:systemId', component: risk_graph_component_1.RiskGraphComponent },
                { path: 'cvi', component: cvi_component_1.CVIComponent },
                { path: 'actions', component: actions_component_1.ActionsComponent },
                { path: 'not-found', component: not_found_component_1.NotFoundComponent },
                { path: '**', redirectTo: 'not-found' }
            ]));
        }
    };
});
//# sourceMappingURL=app.routing.js.map
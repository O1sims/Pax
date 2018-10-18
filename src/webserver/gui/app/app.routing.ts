
import { RouterModule }                  from '@angular/router';

import { RiskGraphComponent }            from './risk-graph/risk-graph.component';
import { ActionsComponent }         	   from './actions/actions.component';
import { SurveyComponent }               from './survey/survey.component';
import { CVIComponent }         		     from './cvi/cvi.component';

import { NotFoundComponent }             from './not-found/not-found.component';


export const routing = RouterModule.forRoot([
	{ path: 'risk-appetite', component: SurveyComponent },
	{ path: '', component: RiskGraphComponent },
	{ path: 'risk-graph/:systemId', component: RiskGraphComponent },
	{ path: 'cvi', component: CVIComponent },
	{ path: 'actions', component: ActionsComponent },
	{ path: 'not-found', component: NotFoundComponent },
	{ path: '**', redirectTo: 'not-found' }
]);

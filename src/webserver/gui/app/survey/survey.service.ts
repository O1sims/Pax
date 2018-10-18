import { Http, Response, Request, Headers, RequestOptions, RequestMethod } from "@angular/http";
import { Injectable } from '@angular/core';

import 'rxjs/add/operator/map';


@Injectable()
export class SurveyService {
	riskAppetite = {
		class : "",
		completed : false,
		riskAppetiteLabel : "",
		riskAppetiteScore : 0
	};

	constructor(private _http: Http) {
	}

	getSurveyQuestions() {
		return this._http.get('app/survey/data/survey.questions.json')
		.map(res => res.json());
  }

	getRiskAppetiteData(riskAppetiteData) {
		this.riskAppetite.riskAppetiteLabel = riskAppetiteData.riskAppetiteLabel;
		this.riskAppetite.riskAppetiteScore = riskAppetiteData.riskAppetiteScore;
		this.riskAppetite.completed = true;

		if (riskAppetiteData.riskAppetiteLabel == "Very High") {
			this.riskAppetite.class = "label label-danger";
		} else if (riskAppetiteData.riskAppetiteLabel == "High") {
			this.riskAppetite.class = "label label-warning";
		} else if (riskAppetiteData.riskAppetiteLabel == "Neutral") {
			this.riskAppetite.class = "label label-success";
		} else {
			this.riskAppetite.class = "label label-info";
		};
	};

	postRiskAppetiteData(data) {
		var headers = new Headers();
		headers.append("Content-Type", 'application/json');
		headers.append("Accept", 'application/json');

		var requestoptions = new RequestOptions({
			method: RequestMethod.Post,
			url: 'application/risk-appetite-data',
			headers: headers,
			body: JSON.stringify(data)
		});

		return this._http.request(new Request(requestoptions))
		.map((res: Response) => {
			if (res) {
				return {
					       status: res.status,
					       json: res.json()
							 }
			}
		});
	}
}

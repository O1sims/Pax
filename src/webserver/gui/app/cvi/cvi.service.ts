import { Http, Response, Request, Headers, RequestOptions, RequestMethod } from "@angular/http";
import { Injectable } from '@angular/core';

import 'rxjs/add/operator/map';



@Injectable()
export class CVIService {
	section = {
    'current' : ''
  };

	constructor(private http: Http) {
	};

	getCVIQuestions() {
		return this.http.get('app/cvi/data/cvi.questions.json')
		.map(res => res.json());
  };

	getCVIAnswers() {
		return this.http.get('app/cvi/data/cvi.answers.json')
		.map(res => res.json());
  };

	getSampleCVIData() {
		return this.http.get('app/cvi/data/c2-api-get-system-response.json')
		.map(res => res.json());
  };

	getCurrentSection(currentSection) {
		this.section['current'] = currentSection;
	};

	postCVIData(data) {
		var headers = new Headers();
		headers.append("Content-Type", 'application/json');
		headers.append("Accept", 'application/json');

		var requestoptions = new RequestOptions({
			method: RequestMethod.Post,
			url: 'application/system/',
			headers: headers,
			body: JSON.stringify(data)
		});

		return this.http.request(new Request(requestoptions))
		.map((res: Response) => {
			if (res) {
				return { status: res.status }
			}
		});
	}
}

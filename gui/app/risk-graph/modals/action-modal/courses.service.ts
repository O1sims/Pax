import { Http, Response, Request, Headers, RequestOptions, RequestMethod, URLSearchParams } from "@angular/http";
import { Injectable } from '@angular/core';

import 'rxjs/add/operator/map';


@Injectable()
export class ActionModalService  {

  constructor(private http: Http) {
	};

  postEffects(systemId, task) {
    var headers = new Headers();
		headers.append("Content-Type", 'application/json');

    var requestoptions = new RequestOptions({
			method: RequestMethod.Post,
			url: 'application/risk_analysis/task_dependency/' + systemId + '/',
      headers: headers,
      body: JSON.stringify(task)
		});

		return this.http.request(new Request(requestoptions))
		.map(res => res.json());
  };


  getTaskActions(force, effect, actionType) {
    var requestoptions = new RequestOptions({
			method: RequestMethod.Get,
			url: 'application/action_list/type/' +
      force + '/' + 
      effect.toUpperCase() + '/' +
      actionType.toLowerCase() + '/'
		});
		return this.http.request(new Request(requestoptions))
		.map(res => res.json());
  };

};

import { Http, Response, Request, Headers, RequestOptions, RequestMethod } from "@angular/http";
import { Injectable } from '@angular/core';

import 'rxjs/add/operator/map';


@Injectable()
export class HomeService  {

  constructor(private http: Http) {
	};

  // CHECK DATA
  checkData(url) {
		var requestoptions = new RequestOptions({
			method: RequestMethod.Get,
			url: url
		});

		return this.http.request(new Request(requestoptions))
		.map(res => res.json());
  };

  // GET
  getNetworkData() {
    var requestoptions = new RequestOptions({
			method: RequestMethod.Get,
			url: 'app/home/data/network.data.json'
		});

		return this.http.request(new Request(requestoptions))
		.map(res => res.json());
  };

  getRiskAppetiteData() {
    var requestoptions = new RequestOptions({
			method: RequestMethod.Get,
			url: 'app/home/data/risk.appetite.data.json'
		});

		return this.http.request(new Request(requestoptions))
		.map(res => res.json());
  };

  getThreatActions() {
    var requestoptions = new RequestOptions({
			method: RequestMethod.Get,
			url: 'app/home/data/threat-data/threat.actions.data.json'
		});

		return this.http.request(new Request(requestoptions))
		.map(res => res.json());
  };

  getThreatActorData(threatActor) {
    var threatDataURL = 'app/home/data/threat-data/threat-actor/' + threatActor + '.threat.data.json';

    var requestoptions = new RequestOptions({
			method: RequestMethod.Get,
			url: threatDataURL
		});

		return this.http.request(new Request(requestoptions))
		.map(res => res.json());
  };


  // POST
  postNetworkData(networkData) {
    var headers = new Headers();
		headers.append("Content-Type", 'application/json');

		var requestoptions = new RequestOptions({
			method: RequestMethod.Post,
			url: 'application/network/',
			headers: headers,
			body: JSON.stringify(networkData)
		});

		return this.http.request(new Request(requestoptions))
		.map((res: Response) => {
			if (res) {
				return {
          status: res.status
				}
			}
		});
  };

  postRiskAppetiteData(riskAppetiteData) {
    var headers = new Headers();
		headers.append("Content-Type", 'application/json');

		var requestoptions = new RequestOptions({
			method: RequestMethod.Post,
			url: 'application/risk_appetite/',
			headers: headers,
			body: JSON.stringify(riskAppetiteData)
		});

		return this.http.request(new Request(requestoptions))
		.map((res: Response) => {
			if (res) {
				return {
          status: res.status
				}
			}
		});
  };

  postThreatData(threatData) {
    var headers = new Headers();
		headers.append("Content-Type", 'application/json');

		var requestoptions = new RequestOptions({
			method: RequestMethod.Post,
			url: 'application/threats/',
			headers: headers,
			body: JSON.stringify(threatData)
		});

		return this.http.request(new Request(requestoptions))
		.map((res: Response) => {
			if (res) {
				return {
          status: res.status
				}
			}
		});
  };

  // DELETE
  dropData(url) {
    var requestoptions = new RequestOptions({
			method: RequestMethod.Delete,
			url: url
		});

		return this.http.request(new Request(requestoptions))
  };
}

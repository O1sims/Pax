import { Http, Response, Request, Headers, RequestOptions, RequestMethod } from "@angular/http";
import { Injectable } from '@angular/core';

@Injectable()
export class ActionsService  {
  constructor(private http: Http) {
  };

  deleteEffect(effect) {
    var requestoptions = new RequestOptions({
      method: RequestMethod.Delete,
      url: 'application/hostile_response/' + effect + '/'
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

  getHostileResponses(effect) {
    var requestoptions = new RequestOptions({
      method: RequestMethod.Get,
      url: 'application/hostile_response/' + effect
    });

    return this.http.request(new Request(requestoptions))
    .map(res => res.json());
  };

  patchHostileResponse(effect, hostileResponse) {
    var headers = new Headers();
    headers.append("Content-Type", 'application/json');

    var requestoptions = new RequestOptions({
      method: RequestMethod.Patch,
      url: 'application/hostile_response/' + effect + '/',
      headers: headers,
      body: JSON.stringify(hostileResponse)
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

  submitNewEffect(data) {
    var headers = new Headers();
    headers.append("Content-Type", 'application/json');

    var requestoptions = new RequestOptions({
      method: RequestMethod.Post,
      url: 'application/hostile_response/',
      headers: headers,
      body: JSON.stringify(data)
    });
    return this.http.request(new Request(requestoptions))
    .map((res: Response) => {
      if (res) {
        return { status: res.status }
      }
    });
  };

  getEffects() {
    var requestoptions = new RequestOptions({
      method: RequestMethod.Get,
      url: 'application/effects/'
    });

    return this.http.request(new Request(requestoptions))
    .map(res => res.json());
  };

  getEffectTypes() {
    var requestoptions = new RequestOptions({
      method: RequestMethod.Get,
      url: 'app/actions/data/effect.types.json'
    });

    return this.http.request(new Request(requestoptions))
    .map(res => res.json());
  };

  getActionData(force="hostile") {
    var requestoptions = new RequestOptions({
      method: RequestMethod.Get,
      url: 'application/action_list/all/' + force
    });

    return this.http.request(new Request(requestoptions))
    .map(res => res.json());
  };

  patchActionData(actions, force, effect, type) {
    var headers = new Headers();
    headers.append("Content-Type", 'application/json');

    var requestoptions = new RequestOptions({
      method: RequestMethod.Patch,
      url: 'application/action_list/type/' + force + '/' + effect + '/' + type + '/',
      headers: headers,
      body: JSON.stringify(actions)
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
}

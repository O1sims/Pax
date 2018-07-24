import { Http, Response, Request, Headers, RequestOptions, RequestMethod, URLSearchParams } from "@angular/http";
import { Injectable } from '@angular/core';

import 'rxjs/add/operator/map';


@Injectable()
export class AssetInfoService {
  constructor(private _http: Http) {
	}

  getMissionData() {
    var requestoptions = new RequestOptions({
			method: RequestMethod.Get,
			url: 'application/missions'
		});

		return this._http.request(new Request(requestoptions))
		.map(res => res.json());
  };

  getAssetVulnerabilities(systemId, assetId) {
    var requestoptions = new RequestOptions({
      method: RequestMethod.Get,
      url: 'application/system/vulnerabilities/' + systemId + '/' + assetId + '/'
    });

    return this._http.request(new Request(requestoptions))
    .map(res => res.json());
  };

  getUnitDistance(systemId, assetId, actorId) {
    var requestoptions = new RequestOptions({
      method: RequestMethod.Get,
      url: 'application/geolocation/distance/' + systemId + '/' + assetId + '/' + actorId + '/'
    });

    return this._http.request(new Request(requestoptions))
    .map(res => res.json());
  };

  getAssetLocation(systemId, assetId) {
    var requestoptions = new RequestOptions({
      method: RequestMethod.Get,
      url: 'application/system/location/' + systemId + '/' + assetId + '/'
    });

    return this._http.request(new Request(requestoptions))
    .map(res => res.json());
  };


  getAssetThreats(systemId, assetId) {
    var requestoptions = new RequestOptions({
      method: RequestMethod.Get,
      url: 'application/system/threats/' + systemId + '/' + assetId + '/'
    });

    return this._http.request(new Request(requestoptions))
    .map(res => res.json());
  };

  getAllEffectsBasedActions(systemId) {
    var requestoptions = new RequestOptions({
      method: RequestMethod.Get,
      url: 'application/actions/effects/' + systemId
    });

    return this._http.request(new Request(requestoptions))
    .map(res => res.json());
  };

  getEffectsBasedActionsObjective(systemId, objectiveId) {
    let params = new URLSearchParams();
    params.set('objective', objectiveId);

    var requestoptions = new RequestOptions({
      method: RequestMethod.Get,
      url: 'application/actions/effects/' + systemId,
      search: params
    });

    return this._http.request(new Request(requestoptions))
    .map(res => res.json());
  };

  postEffectsBasedAction(systemId, effectActionData) {
    var headers = new Headers();
		headers.append("Content-Type", 'application/json');

    var requestoptions = new RequestOptions({
			method: RequestMethod.Post,
			url: 'application/actions/effects/' + systemId + '/',
      headers: headers,
      body: JSON.stringify(effectActionData)
		});

    return this._http.request(new Request(requestoptions))
		.map((res: Response) => {
			if (res) {
				return {
          status: res.status
				}
			}
		});
  };

  deleteEffectsBasedActions(systemId, taskIds) {
    var headers = new Headers();
		headers.append("Content-Type", 'application/json');

    var requestoptions = new RequestOptions({
      method: RequestMethod.Delete,
      url: 'application/actions/effects/' + systemId + '/',
      headers: headers,
      body: JSON.stringify({'effectIds': taskIds})
    });

    return this._http.request(new Request(requestoptions))
    .map((res: Response) => {
			if (res) {
				return {
          status: res.status
				}
			}
		});
  };

  getEffects() {
    var requestoptions = new RequestOptions({
			method: RequestMethod.Get,
			url: 'application/effects/'
		});

    return this._http.request(new Request(requestoptions))
		.map(res => res.json());
  };

  getObjectives(systemId) {
    var requestoptions = new RequestOptions({
			method: RequestMethod.Get,
			url: 'application/system/assets/' + systemId
		});

		return this._http.request(new Request(requestoptions))
		.map(res => res.json());
  };

  getUnits(systemId) {
    var requestoptions = new RequestOptions({
			method: RequestMethod.Get,
			url: 'application/system/units/' + systemId
		});

		return this._http.request(new Request(requestoptions))
		.map(res => res.json());
  };
  
  getUnitsAsset(systemId, assetId) {
    var requestoptions = new RequestOptions({
			method: RequestMethod.Get,
			url: 'application/system/unit_distance/' + systemId + '/' + assetId
		});

		return this._http.request(new Request(requestoptions))
		.map(res => res.json());
  };

  getNodeData(globalId) {
    let params = new URLSearchParams();
    params.set('globalId', globalId);

    var requestoptions = new RequestOptions({
			method: RequestMethod.Get,
			url: 'application/node-data',
      search: params
		});

		return this._http.request(new Request(requestoptions))
		.map(res => res.json());
  };

  getThreatData(assetId) {
    var requestoptions = new RequestOptions({
			method: RequestMethod.Get,
			url: 'application/threats/asset/' + assetId
		});

		return this._http.request(new Request(requestoptions))
		.map(res => res.json());
  };

  getVulnerabilityData(assetId) {
    var requestoptions = new RequestOptions({
			method: RequestMethod.Get,
			url: 'application/vulnerabilities/asset/' + assetId
		});

		return this._http.request(new Request(requestoptions))
		.map(res => res.json());
  };

  getDevices(assetId) {
    let params = new URLSearchParams();

    var requestoptions = new RequestOptions({
			method: RequestMethod.Get,
			url: 'application/devices/asset/' + assetId,
      search: params
		});

		return this._http.request(new Request(requestoptions))
		.map(res => res.json());
  };

  getActions(assetId) {
    let params = new URLSearchParams();
    var requestoptions = new RequestOptions({
			method: RequestMethod.Get,
			url: 'application/actions/asset/id/' + assetId,
      search: params
		});

		return this._http.request(new Request(requestoptions))
		.map(res => res.json());
  };

  toggleAction(actionId, newStagedStatus) {
    var data = {
      'staged': newStagedStatus
    };
    var headers = new Headers();
		headers.append("Content-Type", 'application/json');
		headers.append("Accept", 'application/json');
    var requestoptions = new RequestOptions({
			method: RequestMethod.Patch,
			url: 'application/actions/staged/' + actionId,
      headers: headers,
      body: JSON.stringify(data)
		});
    return this._http.request(new Request(requestoptions))
    .map((res: Response) => {
			if (res) {
        return {
          data : res.status
        }
      }
		});
  };
}

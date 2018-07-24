import { Component } from '@angular/core';
import { HTTP_PROVIDERS } from "@angular/http";

import { DialogRef, ModalComponent } from 'angular2-modal';
import { BSModalContext } from 'angular2-modal/plugins/bootstrap';



export class ThreatInfoWindowData extends BSModalContext {
  constructor(public threatInfoData: {}) {
    super();
  }
}


@Component({
  selector: 'modal-content',
  templateUrl: './app/risk-graph/modals/threat-info/threat.info.modal.html',
  providers: [HTTP_PROVIDERS]
})


export class ThreatInfoWindow implements ModalComponent<ThreatInfoWindowData> {
  context : ThreatInfoWindowData;

  threatInfoData : any;

  constructor(public dialog: DialogRef<ThreatInfoWindowData>) {
    dialog.context.size = 'lg';
    this.threatInfoData = dialog.context['threatInfoData'];
  };

  closeModal() {
    this.dialog.close();
  };
}

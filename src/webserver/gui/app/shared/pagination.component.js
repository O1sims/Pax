System.register(["@angular/core"], function (exports_1, context_1) {
    "use strict";
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var __moduleName = context_1 && context_1.id;
    var core_1, PaginationComponent;
    return {
        setters: [
            function (core_1_1) {
                core_1 = core_1_1;
            }
        ],
        execute: function () {
            PaginationComponent = class PaginationComponent {
                constructor() {
                    this.items = [];
                    this.pageSize = 10;
                    this.pageChanged = new core_1.EventEmitter();
                }
                ngOnChanges() {
                    this.currentPage = 1;
                    var pagesCount = this.items.length / this.pageSize;
                    this.pages = [];
                    for (var i = 1; i <= pagesCount; i++)
                        this.pages.push(i);
                }
                changePage(page) {
                    this.currentPage = page;
                    this.pageChanged.emit(page);
                }
                previous() {
                    if (this.currentPage == 1)
                        return;
                    this.currentPage--;
                    this.pageChanged.emit(this.currentPage);
                }
                next() {
                    if (this.currentPage == this.pages.length)
                        return;
                    this.currentPage++;
                    this.pageChanged.emit(this.currentPage);
                }
            };
            __decorate([
                core_1.Input(),
                __metadata("design:type", Object)
            ], PaginationComponent.prototype, "items", void 0);
            __decorate([
                core_1.Input('page-size'),
                __metadata("design:type", Object)
            ], PaginationComponent.prototype, "pageSize", void 0);
            __decorate([
                core_1.Output('page-changed'),
                __metadata("design:type", Object)
            ], PaginationComponent.prototype, "pageChanged", void 0);
            PaginationComponent = __decorate([
                core_1.Component({
                    selector: 'pagination',
                    template: `
    <nav *ngIf="items.length > pageSize">
        <ul class="pagination">
            <li [class.disabled]="currentPage == 1">
                <a (click)="previous()" aria-label="Previous">
                <span aria-hidden="true">&laquo;</span>
                </a>
            </li>
            <li [class.active]="currentPage == page" *ngFor="let page of pages" (click)="changePage(page)">
                <a>{{ page }}</a>
            </li>
            <li [class.disabled]="currentPage == pages.length">
                <a (click)="next()" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
                </a>
            </li>
        </ul>
    </nav>  
`
                })
            ], PaginationComponent);
            exports_1("PaginationComponent", PaginationComponent);
        }
    };
});
//# sourceMappingURL=pagination.component.js.map
import { Component } from '@angular/core';
//import { ReportsService } from 'src/app/services/reports.service';
import { DataService } from 'src/app/services/data.service';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'app-reports',
  templateUrl: './reports.component.html',
  styleUrls: ['./reports.component.css']
})
export class ReportsComponent {

  files: any[] = [{file: "", name:"reporte1.txt", type:"txt"}, {file:"", name:"reporte2.txt", type:"txt"}];
  url = "https://quickchart.io/graphviz?graph=digraph G { A -> B; }";

  constructor(private service: DataService, private sanitizer: DomSanitizer) { }

  item_selected(i:number) {
    console.log(i);
  }

  getSafeUrl() {
    return this.sanitizer.bypassSecurityTrustResourceUrl(this.url);
  }

}
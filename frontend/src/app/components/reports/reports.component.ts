import { Component } from '@angular/core';
import { DataService } from 'src/app/services/data.service';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'app-reports',
  templateUrl: './reports.component.html',
  styleUrls: ['./reports.component.css']
})
export class ReportsComponent {

  url = 'https://contenedorpy2.s3.us-east-2.amazonaws.com/reports/'
  //files: any[] = [{name:"reporte", type:"png"}, {name:"disk.png", type:"png"}];
  files: any[] = [];
  index: number = 0;
  title: string = "Titulo Reportes";

  constructor(private service: DataService, private sanitizer: DomSanitizer) { 
    this.service.getReports({}).subscribe((data:any) => {
      this.files = data.reports;
      console.log(data.reports);
    });
  }

  item_selected(i:number) {
    this.index = i;
    this.title = this.files[i].name;
  }

  getSafeUrl() {
    if (this.files.length == 0) {
      return "";
    } else {
      return this.sanitizer.bypassSecurityTrustResourceUrl(this.url + this.files[this.index].name);
    }
  }

}
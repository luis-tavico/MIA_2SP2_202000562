import { Component } from '@angular/core';
import { DataService } from 'src/app/services/data.service';
import { DomSanitizer } from '@angular/platform-browser';
import { ToastrService } from 'ngx-toastr';
import { Router } from '@angular/router';

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

  constructor(private router: Router, private service: DataService, private sanitizer: DomSanitizer, private toastr: ToastrService) { 
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

  logout() {
    const command = 'logout'
    const postData = { "request" : [command, "None"]}
    this.service.logout(postData).subscribe(
      (response) => {
        var r = response as any;
        if (r.status == "Ok") {
          this.toastr.success('Exito', r.message, 
          {
            positionClass: 'toast-top-left'
          });
          this.router.navigate(['/reports']);
        } 
        this.router.navigate(['/login']);
      },
      (error) => {
        console.error('Error:', error);
      }
    );
  }

}
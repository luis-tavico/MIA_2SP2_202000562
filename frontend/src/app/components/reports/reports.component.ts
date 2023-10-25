import { Component } from '@angular/core';
import { ReportsService } from 'src/app/services/reports.service';


@Component({
  selector: 'app-reports',
  templateUrl: './reports.component.html',
  styleUrls: ['./reports.component.css']
})
export class ReportsComponent {

  constructor(private service: ReportsService) { }

}

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class ReportsService {

  url = 'http://127.0.0.1:5000/reports';

  constructor(private http: HttpClient) { }

  postLogin(data: any) {
    return this.http.post(this.url, data);
  }

}
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  //url = 'http://3.147.238.57'
  url = 'http://127.0.0.1:5000';

  constructor(private http: HttpClient) { }

  postCode(data: any) {
    return this.http.post(this.url+"/", data);
  }

  postLogin(data: any) {
    return this.http.post(this.url+"/login", data);
  }

  getReports(data: any) {
    return this.http.post(this.url+"/reports", data);
  }

}
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  url = '18.227.81.247'
  //url = 'http://127.0.0.1:5000';

  constructor(private http: HttpClient) { }

  setCode(data: any) {
    return this.http.post(this.url+"/", data);
  }

  login(data: any) {
    return this.http.post(this.url+"/login", data);
  }

  getReports(data: any) {
    return this.http.get(this.url+"/reports", data);
  }

  logout(data: any) {
    return this.http.post(this.url+"/logout", data);
  }

}
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ConsoleService {

  url = 'http://127.0.0.1:5000/';

  constructor(private http: HttpClient) { }

  postCode(data: any) {
    return this.http.post(this.url, data);
  }
  
}

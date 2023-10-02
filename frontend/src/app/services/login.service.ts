import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  url = 'http://127.0.0.1:5000/login';

  constructor(private http: HttpClient) { }

  postLogin(data: any) {
    return this.http.post(this.url, data);
  }

}

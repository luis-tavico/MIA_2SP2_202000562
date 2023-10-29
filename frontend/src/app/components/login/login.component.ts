import { Component } from '@angular/core';
import { DataService } from 'src/app/services/data.service';
import { ToastrService } from 'ngx-toastr';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  inputPartition: string = "";
  inputUsername: string = "";
  inputPassword: string = "";

  constructor(private router: Router, private service: DataService, private toastr: ToastrService) { }

  login() {
    if (this.inputUsername != "" && this.inputPassword != "" && this.inputPartition !="") {
      const command = 'login -user="'+this.inputUsername+'" -pass="'+this.inputPassword+'" -id='+this.inputPartition
      const postData = { "request" : [command, "None"]}
      this.service.login(postData).subscribe(
        (response) => {
          var r = response as any;
          if (r.status == "Ok") {
            this.toastr.success('Exito', r.message, 
            {
              positionClass: 'toast-top-left'
            });
            this.router.navigate(['/reports']);
          } else if (r.status == "Error") {
            this.toastr.error('Error', r.message, 
            {
              positionClass: 'toast-top-left'
            });        
          } else if (r.status == "Warning") {
            this.toastr.warning('Advertencia', r.message, 
            {
              positionClass: 'toast-top-left'
            });   
          } else {
            alert(r.sattus)
          }
        },
        (error) => {
          console.error('Error:', error);
        }
      );
    } else {
      this.toastr.warning('Advertencia', 'Complete los campos vacios', 
      {
        positionClass: 'toast-top-left'
      });  
    }
  }

}
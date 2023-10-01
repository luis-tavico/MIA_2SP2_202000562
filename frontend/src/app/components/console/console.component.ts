import { Component, ElementRef, ViewChild } from '@angular/core';
import { ConsoleService } from 'src/app/services/console.service';

@Component({
  selector: 'app-console',
  templateUrl: './console.component.html',
  styleUrls: ['./console.component.css']
})
export class ConsoleComponent {

  @ViewChild('outputCodeConsole') outputCodeConsole!: ElementRef;
  @ViewChild('inputCodeConsole') inputCodeConsole!: ElementRef;
  rspt : string = "";

  constructor(private service: ConsoleService) { }

    cargarArchivo(event: any) {
      const archivoSeleccionado = event.target.files[0];
      if (archivoSeleccionado) {
        const lector = new FileReader();
        lector.onload = (e: any) => {
          this.outputCodeConsole.nativeElement.innerHTML = "";
          this.inputCodeConsole.nativeElement.value = e.target.result;
        };
        lector.readAsText(archivoSeleccionado); }
      }

    enviarComandos() {
      var commands = this.inputCodeConsole.nativeElement.value
      const postData = {"request": [commands, "None"]};
      
      this.service.postCode(postData).subscribe(
        (response) => {
          var r = response as any;
          var contenido_anterior = this.outputCodeConsole.nativeElement.innerHTML;
          this.outputCodeConsole.nativeElement.innerHTML = contenido_anterior + r.response;
          this.outputCodeConsole.nativeElement.scrollTop = this.outputCodeConsole.nativeElement.scrollHeight;
        },
        (error) => {
          console.error('Error:', error);
        }
      );
      
    }

    enviarRespuesta(event: KeyboardEvent) {
      if (event.key === 'Enter') {
        const postData = {"request": ["", this.rspt]}
        this.service.postCode(postData).subscribe(
          (response) => {
            var r = response as any;
            var contenido_anterior = this.outputCodeConsole.nativeElement.innerHTML;
            this.outputCodeConsole.nativeElement.innerHTML = contenido_anterior + r.response;
            this.outputCodeConsole.nativeElement.scrollTop = this.outputCodeConsole.nativeElement.scrollHeight;      
          },
          (error) => {
            console.error('Error:', error);
          }
        );
        this.rspt = ""  
      } else if (event.key === 'Backspace') {
        this.rspt = this.rspt.slice(0, -1);
      } else {
        this.rspt = this.rspt + event.key;
      }
    }

}
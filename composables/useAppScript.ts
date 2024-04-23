
// interface BodyContent {
//   fecha: string;
//   horasExtrasAntes: boolean;
//   horasExtrasDespues: boolean;
//   labor: string;
//   lote: number;
//   trabajador: string;
//   horaFinalAntes: string | null;
//   horaFinalDespues: string | null;
//   horaInicioAntes: string | null;
//   horaInicioDespues: string | null;
// }

// export const useAppScriptPostNewActivity = async ( data : BodyContent ) => {
//   let headersList = {
//     "Accept": "*/*",
//     "Content-Type": "application/json"
//   }
  
//   let bodyContent = JSON.stringify( data );
  
//   return await fetch("https://script.google.com/macros/s/AKfycbyxflabla-_wfYAu1IsiLgBMnKG3aOR7sK0UERdT8m1yqF6EauNCoOKMP8CXs_N_3Q/exec?nuevaActividad=true", {
//     method: "POST",
//     body: bodyContent,
//     headers: headersList
//   });
// }

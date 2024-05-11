import './App.css';
import Inicio from './components/Inicio';
import Menu from './components/Menu';
import {BrowserRouter, Navigate, Route, Routes} from "react-router-dom";
import Peliculas from './components/peliculas/Peliculas'
import Series from './components/series/Series';
import Actores from './components/actores/Actores';
import Directores from './components/directores/Directores';
import Estudios from './components/estudios/Estudios';
import { Footer } from './components/Footer';

function App() {
  return (
    <>
    <BrowserRouter>
    <Menu />
    <div className="App intro-opacity-1-5">
      <Routes>
        <Route path='/Inicio' element={<Inicio />}/>
        <Route path='/series' element={<Series />}/>
        <Route path='/peliculas' element={<Peliculas />}/>
        <Route path='/actores' element={<Actores />}/>
        <Route path='/directores' element={<Directores />}/>
        <Route path='/estudios' element={<Estudios />}/>

        <Route path='*' element={<Navigate to="/Inicio" replace />}/>
      </Routes>
    </div>
    <Footer />
    </BrowserRouter>
    </>
  );
}

export default App;

import React from "react";

function Footer(){
    return(
        <footer className="text-center">
            <small>
                <span> © Productora 2023 </span>
                <span className="m-4">-</span>
                <a href="tel:113" className="phone-number me-4">
                    <span className="fa fa-phone me-2"></span>
                    0351-442-7773
                </a>
                <a className="redes" href="https://www.facebook.com" style={{"backgroundColor":"#333"}} target="_blank" rel="noreferrer">
                    <i title="Facebook" className="fab fa-facebook-f"></i>
                </a>
                <a className="redes" href="https://twitter.com" style={{"backgroundColor":"#333"}} target="_blank" rel="noreferrer">
                    <i title="Twitter" className="fab fa-twitter"></i>
                </a>
                <a className="redes" href="https://www.instragram.com" style={{"backgroundColor":"#333"}} target="_blank" rel="noreferrer">
                    <i title="Instagram" className="fab fa-instagram"></i>
                </a>
                <a className="redes" href="https://www.whatsapp.com" style={{"backgroundColor":"#333"}} target="_blank" rel="noreferrer">
                    <i title="Whatsapp" className="fab fa-whatsapp"></i>
                </a>
            </small>
        </footer>
    );
}

export { Footer };
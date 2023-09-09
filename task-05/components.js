class Header extends HTMLElement {
    connectedCallback() {
      this.innerHTML = `
      <div class="banner">   
          <div class="navbar">
              <nav>
                 <li><a href="index.html"> <img class="logo" src="assets/navbar/logo.png"></a></li>
              <ul>      
                 <li><a href="https://open.spotify.com/artist/53XhwfbYqKCa1cC15pYq2q" ><img class="spotify" src="assets/navbar/spotify.png"></a></li>   
                 <li><a href="https://www.youtube.com/channel/UCT9zcQNlyht7fRlcjmflRSA" ><img src="assets/navbar/youtube.svg"></a></li> 
                 <li><a href="https://twitter.com/Imaginedragons" ><img src="assets/navbar/twitter.svg"></a></li>
                 <li><a href="https://www.instagram.com/imaginedragons/?hl=en" ><img src="assets/navbar/instagram.svg"></a></li>
              </ul>
              </nav>
          </div>
      </div>    
        `;
       
    }
  }
  class Footer extends HTMLElement {
    connectedCallback() {
      this.innerHTML = `    
      <footer class="copy_right">
         <p>&copy; 2023 KK Surendran.</p>
      </footer>    
      `;
    }
  }

  customElements.define('my-header', Header);
  customElements.define('my-footer', Footer);
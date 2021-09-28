<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]




<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">Whatsapp Tracker</h3>

  <p align="center">
    have you ever wanted to know when your favourite contact was online on Whatsapp?
    now it is possible by using Whatsapp Tracker!
    Whatsapp Tracker is a Selenium based automation, it extracts details of your contact
    activity and stores it on your local machine for you to review it later! 
    <br />
    <a href="https://github.com/itay-bardugo/whatsapp_tracker/issues">Report Bug</a>
    ·
    <a href="https://github.com/itay-bardugo/whatsapp_tracker/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## <a name="about-the-project"></a>About The Project

[![Product Name Screen Shot][product-screenshot]]()

WhatsappTracker is a selenium based automation.
it makes it possible to tracking your contact's without your touch, it stores time series of metrics
to your local machine as a csv file, so you can have a look once finished.

below is a list of supported metrics.
please open a feature request for any extra metrics suggestions

### current metrics

**status** - what was the status of your contact

**name** - contact's name



### Built With

* [Python3.9](https://www.python.org/)
* [Selenium](https://www.selenium.dev/)
* [Numpy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites
* [Google Chrome](https://www.google.com/chrome)
* [Chromedriver](https://chromedriver.chromium.org/downloads) - as far as I know, it should be 
as the same version of your GoogleChrome browser.
  extract the zip and keep the path of the file, you will need to send it as an input to the software
  
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/itay-bardugo/whatsapp_tracker.git
   ```
2. Install python packages
   ```sh
   pip install -r requirements.txt
   ```


<!-- USAGE EXAMPLES -->
## Usage
```sh
python whatsapp_tracker/wt_main.py --browser-path chromedriver --contact "contact name" --save-path /Users/itay/Downloads --minutes 2 --resolution 5
```
### Arguments map
|  arg   |  description |  value for example |
|  ---   |  ----------- |  ----------------- |
|   h    |  displays arguments map | |     
|  browser-path | an absolute path for executable chromedriver | /Downloads/chromedrivers/chromedriver |
|  contact  |  contact name for tracking  |  Anonymous |
| save-path | where to store the results | /Users/itay/Desktop |
| minutes   | for how long you want to tracking your contact, in minutes | 30 |
| resolution | represents the sampling resolution in seconds | 5 |


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/itay-bardugo/whatsapp_tracker/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Itay Bardugo - [@twitter_handle](https://twitter.com/itaybardugo) - itaybardugo91@gmail.com

Project Link: [https://github.com/itay-bardugo/whatsapp_tracker](https://github.com/itay-bardugo/whatsapp_tracker)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/itay-bardugo/whatsapp_tracker.svg?style=for-the-badge
[contributors-url]: https://github.com/itay-bardugo/whatsapp_tracker/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/itay-bardugo/whatsapp_tracker.svg?style=for-the-badge
[forks-url]: https://github.com/itay-bardugo/whatsapp_tracker/network/members
[stars-shield]: https://img.shields.io/github/stars/itay-bardugo/whatsapp_tracker.svg?style=for-the-badge
[stars-url]: https://github.com/itay-bardugo/whatsapp_tracker/stargazers
[issues-shield]: https://img.shields.io/github/issues/itay-bardugo/whatsapp_tracker.svg?style=for-the-badge
[issues-url]: https://github.com/itay-bardugo/whatsapp_tracker/issues
[license-shield]: https://img.shields.io/github/license/itay-bardugo/whatsapp_tracker.svg?style=for-the-badge
[license-url]: https://github.com/itay-bardugo/whatsapp_tracker/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/itay-bardugo-411571a5
[product-screenshot]: docs/images/screenshot.png

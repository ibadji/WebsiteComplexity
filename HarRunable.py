from HARGenerator import generator
from HARGenerator import parser


#arrays of websites fed to the generator and parser 
Keeward =['frenchculturalcenter.org','johnnyfarah.com','www.tabbah.com','blinkmycar.com','masculinmagazine.com','raseef22.com','www.antoineonline.com','bookwitty.com','exotica.com','thewantonbishops.com','tamyras.com','lebelik.com','ashkalalwan.org','www.metropoliscinema.net','gate-37.com','www.bargylus.com','baderlebanon.com','www.krikorjabotian.com','hadjithomasjoreige.com','www.homeresa.com','www.hachette-antoine.com']
BornInteractive=['www.katakeet-boutique.com','www.sasco.com','www.llfp.com','cmimarseille.org','www.iptgroup.com','www.blombankegypt.com','www.codeone.online','www.speakingrosesuae.com','www.placepasteur.com','www.banotrading.com','www.azmuniversity.edu.lb','www.ak-construction.com','www.warde.com','www.imagic.tv','www.virginmegastore.com','www.un.org.lb','store.alrifai.com','www.essmak.com','www.luckytobeyoung.com','www.terrabludesign.com','www.mindclinics.org']
Activeweb=['www.virginradio.com','www.sleepcomfort.com','siblinelb.com','www.lda.org.lb','www.wise.net.lb','globemedacademy.com','dictalive.com','daze-me.com','www.safetyvision.me','dataa2z.com','www.upb-beyrouth.com','cookpad.com','www.latheneedebeyrouth.edu.lb','www.at-lawfirm.com','www.amanainsurance.com','www.menacitylawyers.com','www.saccal.com','www.hallab.com','www.fiorihotel.com']
ClearTag=['semsom.com','rymcopowersports.com','www.mitarabcompetition.com','www.rymco.com','www.sfbsal.com','www.loubnanicard.com','ellingtongroup.com','qudrahholding.com','www.transmed.com','www.vinlite.com','www.picsati.com','www.samsungctc.com','beirutdigitaldistrict.com','nicolasaudi.com','saifisuites.com','www.parktowersuites.com','chateauksara.com','www.mtn.com.ye','www.diwanalmuhanna.com','www.lotuscarslebanon.com','lucid-investment.com']
LeLabo=['baakleenlibrary.org']

#both methods take an array of websites and a number that specifies
#how many times the code will be run for each website (number of har files created)
generator = generator(LeLabo,1)
parser = parser(LeLabo,1)

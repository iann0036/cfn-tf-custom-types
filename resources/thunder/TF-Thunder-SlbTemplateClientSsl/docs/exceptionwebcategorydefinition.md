# TF::Thunder::SlbTemplateClientSsl ExceptionWebCategoryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#exceptionabortion" title="ExceptionAbortion">ExceptionAbortion</a>" : <i>Double</i>,
    "<a href="#exceptionadultandpornography" title="ExceptionAdultAndPornography">ExceptionAdultAndPornography</a>" : <i>Double</i>,
    "<a href="#exceptionalcoholandtobacco" title="ExceptionAlcoholAndTobacco">ExceptionAlcoholAndTobacco</a>" : <i>Double</i>,
    "<a href="#exceptionauctions" title="ExceptionAuctions">ExceptionAuctions</a>" : <i>Double</i>,
    "<a href="#exceptionbotnets" title="ExceptionBotNets">ExceptionBotNets</a>" : <i>Double</i>,
    "<a href="#exceptionbusinessandeconomy" title="ExceptionBusinessAndEconomy">ExceptionBusinessAndEconomy</a>" : <i>Double</i>,
    "<a href="#exceptioncdns" title="ExceptionCdns">ExceptionCdns</a>" : <i>Double</i>,
    "<a href="#exceptioncheating" title="ExceptionCheating">ExceptionCheating</a>" : <i>Double</i>,
    "<a href="#exceptioncomputerandinternetinfo" title="ExceptionComputerAndInternetInfo">ExceptionComputerAndInternetInfo</a>" : <i>Double</i>,
    "<a href="#exceptioncomputerandinternetsecurity" title="ExceptionComputerAndInternetSecurity">ExceptionComputerAndInternetSecurity</a>" : <i>Double</i>,
    "<a href="#exceptionconfirmedspamsources" title="ExceptionConfirmedSpamSources">ExceptionConfirmedSpamSources</a>" : <i>Double</i>,
    "<a href="#exceptioncultandoccult" title="ExceptionCultAndOccult">ExceptionCultAndOccult</a>" : <i>Double</i>,
    "<a href="#exceptiondating" title="ExceptionDating">ExceptionDating</a>" : <i>Double</i>,
    "<a href="#exceptiondeadsites" title="ExceptionDeadSites">ExceptionDeadSites</a>" : <i>Double</i>,
    "<a href="#exceptiondrugs" title="ExceptionDrugs">ExceptionDrugs</a>" : <i>Double</i>,
    "<a href="#exceptiondynamiccomment" title="ExceptionDynamicComment">ExceptionDynamicComment</a>" : <i>Double</i>,
    "<a href="#exceptioneducationalinstitutions" title="ExceptionEducationalInstitutions">ExceptionEducationalInstitutions</a>" : <i>Double</i>,
    "<a href="#exceptionentertainmentandarts" title="ExceptionEntertainmentAndArts">ExceptionEntertainmentAndArts</a>" : <i>Double</i>,
    "<a href="#exceptionfashionandbeauty" title="ExceptionFashionAndBeauty">ExceptionFashionAndBeauty</a>" : <i>Double</i>,
    "<a href="#exceptionfinancialservices" title="ExceptionFinancialServices">ExceptionFinancialServices</a>" : <i>Double</i>,
    "<a href="#exceptionfoodanddining" title="ExceptionFoodAndDining">ExceptionFoodAndDining</a>" : <i>Double</i>,
    "<a href="#exceptiongambling" title="ExceptionGambling">ExceptionGambling</a>" : <i>Double</i>,
    "<a href="#exceptiongames" title="ExceptionGames">ExceptionGames</a>" : <i>Double</i>,
    "<a href="#exceptiongovernment" title="ExceptionGovernment">ExceptionGovernment</a>" : <i>Double</i>,
    "<a href="#exceptiongross" title="ExceptionGross">ExceptionGross</a>" : <i>Double</i>,
    "<a href="#exceptionhacking" title="ExceptionHacking">ExceptionHacking</a>" : <i>Double</i>,
    "<a href="#exceptionhateandracism" title="ExceptionHateAndRacism">ExceptionHateAndRacism</a>" : <i>Double</i>,
    "<a href="#exceptionhealthandmedicine" title="ExceptionHealthAndMedicine">ExceptionHealthAndMedicine</a>" : <i>Double</i>,
    "<a href="#exceptionhomeandgarden" title="ExceptionHomeAndGarden">ExceptionHomeAndGarden</a>" : <i>Double</i>,
    "<a href="#exceptionhuntingandfishing" title="ExceptionHuntingAndFishing">ExceptionHuntingAndFishing</a>" : <i>Double</i>,
    "<a href="#exceptionillegal" title="ExceptionIllegal">ExceptionIllegal</a>" : <i>Double</i>,
    "<a href="#exceptionimageandvideosearch" title="ExceptionImageAndVideoSearch">ExceptionImageAndVideoSearch</a>" : <i>Double</i>,
    "<a href="#exceptioninternetcommunications" title="ExceptionInternetCommunications">ExceptionInternetCommunications</a>" : <i>Double</i>,
    "<a href="#exceptioninternetportals" title="ExceptionInternetPortals">ExceptionInternetPortals</a>" : <i>Double</i>,
    "<a href="#exceptionjobsearch" title="ExceptionJobSearch">ExceptionJobSearch</a>" : <i>Double</i>,
    "<a href="#exceptionkeyloggersandmonitoring" title="ExceptionKeyloggersAndMonitoring">ExceptionKeyloggersAndMonitoring</a>" : <i>Double</i>,
    "<a href="#exceptionkids" title="ExceptionKids">ExceptionKids</a>" : <i>Double</i>,
    "<a href="#exceptionlegal" title="ExceptionLegal">ExceptionLegal</a>" : <i>Double</i>,
    "<a href="#exceptionlocalinformation" title="ExceptionLocalInformation">ExceptionLocalInformation</a>" : <i>Double</i>,
    "<a href="#exceptionmalwaresites" title="ExceptionMalwareSites">ExceptionMalwareSites</a>" : <i>Double</i>,
    "<a href="#exceptionmarijuana" title="ExceptionMarijuana">ExceptionMarijuana</a>" : <i>Double</i>,
    "<a href="#exceptionmilitary" title="ExceptionMilitary">ExceptionMilitary</a>" : <i>Double</i>,
    "<a href="#exceptionmotorvehicles" title="ExceptionMotorVehicles">ExceptionMotorVehicles</a>" : <i>Double</i>,
    "<a href="#exceptionmusic" title="ExceptionMusic">ExceptionMusic</a>" : <i>Double</i>,
    "<a href="#exceptionnewsandmedia" title="ExceptionNewsAndMedia">ExceptionNewsAndMedia</a>" : <i>Double</i>,
    "<a href="#exceptionnudity" title="ExceptionNudity">ExceptionNudity</a>" : <i>Double</i>,
    "<a href="#exceptiononlinegreetingcards" title="ExceptionOnlineGreetingCards">ExceptionOnlineGreetingCards</a>" : <i>Double</i>,
    "<a href="#exceptionopenhttpproxies" title="ExceptionOpenHttpProxies">ExceptionOpenHttpProxies</a>" : <i>Double</i>,
    "<a href="#exceptionparkeddomains" title="ExceptionParkedDomains">ExceptionParkedDomains</a>" : <i>Double</i>,
    "<a href="#exceptionpaytosurf" title="ExceptionPayToSurf">ExceptionPayToSurf</a>" : <i>Double</i>,
    "<a href="#exceptionpeertopeer" title="ExceptionPeerToPeer">ExceptionPeerToPeer</a>" : <i>Double</i>,
    "<a href="#exceptionpersonalsitesandblogs" title="ExceptionPersonalSitesAndBlogs">ExceptionPersonalSitesAndBlogs</a>" : <i>Double</i>,
    "<a href="#exceptionpersonalstorage" title="ExceptionPersonalStorage">ExceptionPersonalStorage</a>" : <i>Double</i>,
    "<a href="#exceptionphilosophyandpolitics" title="ExceptionPhilosophyAndPolitics">ExceptionPhilosophyAndPolitics</a>" : <i>Double</i>,
    "<a href="#exceptionphishingandotherfraud" title="ExceptionPhishingAndOtherFraud">ExceptionPhishingAndOtherFraud</a>" : <i>Double</i>,
    "<a href="#exceptionprivateipaddresses" title="ExceptionPrivateIpAddresses">ExceptionPrivateIpAddresses</a>" : <i>Double</i>,
    "<a href="#exceptionproxyavoidandanonymizers" title="ExceptionProxyAvoidAndAnonymizers">ExceptionProxyAvoidAndAnonymizers</a>" : <i>Double</i>,
    "<a href="#exceptionquestionable" title="ExceptionQuestionable">ExceptionQuestionable</a>" : <i>Double</i>,
    "<a href="#exceptionrealestate" title="ExceptionRealEstate">ExceptionRealEstate</a>" : <i>Double</i>,
    "<a href="#exceptionrecreationandhobbies" title="ExceptionRecreationAndHobbies">ExceptionRecreationAndHobbies</a>" : <i>Double</i>,
    "<a href="#exceptionreferenceandresearch" title="ExceptionReferenceAndResearch">ExceptionReferenceAndResearch</a>" : <i>Double</i>,
    "<a href="#exceptionreligion" title="ExceptionReligion">ExceptionReligion</a>" : <i>Double</i>,
    "<a href="#exceptionsearchengines" title="ExceptionSearchEngines">ExceptionSearchEngines</a>" : <i>Double</i>,
    "<a href="#exceptionsexeducation" title="ExceptionSexEducation">ExceptionSexEducation</a>" : <i>Double</i>,
    "<a href="#exceptionsharewareandfreeware" title="ExceptionSharewareAndFreeware">ExceptionSharewareAndFreeware</a>" : <i>Double</i>,
    "<a href="#exceptionshopping" title="ExceptionShopping">ExceptionShopping</a>" : <i>Double</i>,
    "<a href="#exceptionsocialnetwork" title="ExceptionSocialNetwork">ExceptionSocialNetwork</a>" : <i>Double</i>,
    "<a href="#exceptionsociety" title="ExceptionSociety">ExceptionSociety</a>" : <i>Double</i>,
    "<a href="#exceptionspamurls" title="ExceptionSpamUrls">ExceptionSpamUrls</a>" : <i>Double</i>,
    "<a href="#exceptionsports" title="ExceptionSports">ExceptionSports</a>" : <i>Double</i>,
    "<a href="#exceptionspywareandadware" title="ExceptionSpywareAndAdware">ExceptionSpywareAndAdware</a>" : <i>Double</i>,
    "<a href="#exceptionstockadviceandtools" title="ExceptionStockAdviceAndTools">ExceptionStockAdviceAndTools</a>" : <i>Double</i>,
    "<a href="#exceptionstreamingmedia" title="ExceptionStreamingMedia">ExceptionStreamingMedia</a>" : <i>Double</i>,
    "<a href="#exceptionswimsuitsandintimateapparel" title="ExceptionSwimsuitsAndIntimateApparel">ExceptionSwimsuitsAndIntimateApparel</a>" : <i>Double</i>,
    "<a href="#exceptiontrainingandtools" title="ExceptionTrainingAndTools">ExceptionTrainingAndTools</a>" : <i>Double</i>,
    "<a href="#exceptiontranslation" title="ExceptionTranslation">ExceptionTranslation</a>" : <i>Double</i>,
    "<a href="#exceptiontravel" title="ExceptionTravel">ExceptionTravel</a>" : <i>Double</i>,
    "<a href="#exceptionuncategorized" title="ExceptionUncategorized">ExceptionUncategorized</a>" : <i>Double</i>,
    "<a href="#exceptionunconfirmedspamsources" title="ExceptionUnconfirmedSpamSources">ExceptionUnconfirmedSpamSources</a>" : <i>Double</i>,
    "<a href="#exceptionviolence" title="ExceptionViolence">ExceptionViolence</a>" : <i>Double</i>,
    "<a href="#exceptionweapons" title="ExceptionWeapons">ExceptionWeapons</a>" : <i>Double</i>,
    "<a href="#exceptionwebadvertisements" title="ExceptionWebAdvertisements">ExceptionWebAdvertisements</a>" : <i>Double</i>,
    "<a href="#exceptionwebbasedemail" title="ExceptionWebBasedEmail">ExceptionWebBasedEmail</a>" : <i>Double</i>,
    "<a href="#exceptionwebhostingsites" title="ExceptionWebHostingSites">ExceptionWebHostingSites</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#exceptionabortion" title="ExceptionAbortion">ExceptionAbortion</a>: <i>Double</i>
<a href="#exceptionadultandpornography" title="ExceptionAdultAndPornography">ExceptionAdultAndPornography</a>: <i>Double</i>
<a href="#exceptionalcoholandtobacco" title="ExceptionAlcoholAndTobacco">ExceptionAlcoholAndTobacco</a>: <i>Double</i>
<a href="#exceptionauctions" title="ExceptionAuctions">ExceptionAuctions</a>: <i>Double</i>
<a href="#exceptionbotnets" title="ExceptionBotNets">ExceptionBotNets</a>: <i>Double</i>
<a href="#exceptionbusinessandeconomy" title="ExceptionBusinessAndEconomy">ExceptionBusinessAndEconomy</a>: <i>Double</i>
<a href="#exceptioncdns" title="ExceptionCdns">ExceptionCdns</a>: <i>Double</i>
<a href="#exceptioncheating" title="ExceptionCheating">ExceptionCheating</a>: <i>Double</i>
<a href="#exceptioncomputerandinternetinfo" title="ExceptionComputerAndInternetInfo">ExceptionComputerAndInternetInfo</a>: <i>Double</i>
<a href="#exceptioncomputerandinternetsecurity" title="ExceptionComputerAndInternetSecurity">ExceptionComputerAndInternetSecurity</a>: <i>Double</i>
<a href="#exceptionconfirmedspamsources" title="ExceptionConfirmedSpamSources">ExceptionConfirmedSpamSources</a>: <i>Double</i>
<a href="#exceptioncultandoccult" title="ExceptionCultAndOccult">ExceptionCultAndOccult</a>: <i>Double</i>
<a href="#exceptiondating" title="ExceptionDating">ExceptionDating</a>: <i>Double</i>
<a href="#exceptiondeadsites" title="ExceptionDeadSites">ExceptionDeadSites</a>: <i>Double</i>
<a href="#exceptiondrugs" title="ExceptionDrugs">ExceptionDrugs</a>: <i>Double</i>
<a href="#exceptiondynamiccomment" title="ExceptionDynamicComment">ExceptionDynamicComment</a>: <i>Double</i>
<a href="#exceptioneducationalinstitutions" title="ExceptionEducationalInstitutions">ExceptionEducationalInstitutions</a>: <i>Double</i>
<a href="#exceptionentertainmentandarts" title="ExceptionEntertainmentAndArts">ExceptionEntertainmentAndArts</a>: <i>Double</i>
<a href="#exceptionfashionandbeauty" title="ExceptionFashionAndBeauty">ExceptionFashionAndBeauty</a>: <i>Double</i>
<a href="#exceptionfinancialservices" title="ExceptionFinancialServices">ExceptionFinancialServices</a>: <i>Double</i>
<a href="#exceptionfoodanddining" title="ExceptionFoodAndDining">ExceptionFoodAndDining</a>: <i>Double</i>
<a href="#exceptiongambling" title="ExceptionGambling">ExceptionGambling</a>: <i>Double</i>
<a href="#exceptiongames" title="ExceptionGames">ExceptionGames</a>: <i>Double</i>
<a href="#exceptiongovernment" title="ExceptionGovernment">ExceptionGovernment</a>: <i>Double</i>
<a href="#exceptiongross" title="ExceptionGross">ExceptionGross</a>: <i>Double</i>
<a href="#exceptionhacking" title="ExceptionHacking">ExceptionHacking</a>: <i>Double</i>
<a href="#exceptionhateandracism" title="ExceptionHateAndRacism">ExceptionHateAndRacism</a>: <i>Double</i>
<a href="#exceptionhealthandmedicine" title="ExceptionHealthAndMedicine">ExceptionHealthAndMedicine</a>: <i>Double</i>
<a href="#exceptionhomeandgarden" title="ExceptionHomeAndGarden">ExceptionHomeAndGarden</a>: <i>Double</i>
<a href="#exceptionhuntingandfishing" title="ExceptionHuntingAndFishing">ExceptionHuntingAndFishing</a>: <i>Double</i>
<a href="#exceptionillegal" title="ExceptionIllegal">ExceptionIllegal</a>: <i>Double</i>
<a href="#exceptionimageandvideosearch" title="ExceptionImageAndVideoSearch">ExceptionImageAndVideoSearch</a>: <i>Double</i>
<a href="#exceptioninternetcommunications" title="ExceptionInternetCommunications">ExceptionInternetCommunications</a>: <i>Double</i>
<a href="#exceptioninternetportals" title="ExceptionInternetPortals">ExceptionInternetPortals</a>: <i>Double</i>
<a href="#exceptionjobsearch" title="ExceptionJobSearch">ExceptionJobSearch</a>: <i>Double</i>
<a href="#exceptionkeyloggersandmonitoring" title="ExceptionKeyloggersAndMonitoring">ExceptionKeyloggersAndMonitoring</a>: <i>Double</i>
<a href="#exceptionkids" title="ExceptionKids">ExceptionKids</a>: <i>Double</i>
<a href="#exceptionlegal" title="ExceptionLegal">ExceptionLegal</a>: <i>Double</i>
<a href="#exceptionlocalinformation" title="ExceptionLocalInformation">ExceptionLocalInformation</a>: <i>Double</i>
<a href="#exceptionmalwaresites" title="ExceptionMalwareSites">ExceptionMalwareSites</a>: <i>Double</i>
<a href="#exceptionmarijuana" title="ExceptionMarijuana">ExceptionMarijuana</a>: <i>Double</i>
<a href="#exceptionmilitary" title="ExceptionMilitary">ExceptionMilitary</a>: <i>Double</i>
<a href="#exceptionmotorvehicles" title="ExceptionMotorVehicles">ExceptionMotorVehicles</a>: <i>Double</i>
<a href="#exceptionmusic" title="ExceptionMusic">ExceptionMusic</a>: <i>Double</i>
<a href="#exceptionnewsandmedia" title="ExceptionNewsAndMedia">ExceptionNewsAndMedia</a>: <i>Double</i>
<a href="#exceptionnudity" title="ExceptionNudity">ExceptionNudity</a>: <i>Double</i>
<a href="#exceptiononlinegreetingcards" title="ExceptionOnlineGreetingCards">ExceptionOnlineGreetingCards</a>: <i>Double</i>
<a href="#exceptionopenhttpproxies" title="ExceptionOpenHttpProxies">ExceptionOpenHttpProxies</a>: <i>Double</i>
<a href="#exceptionparkeddomains" title="ExceptionParkedDomains">ExceptionParkedDomains</a>: <i>Double</i>
<a href="#exceptionpaytosurf" title="ExceptionPayToSurf">ExceptionPayToSurf</a>: <i>Double</i>
<a href="#exceptionpeertopeer" title="ExceptionPeerToPeer">ExceptionPeerToPeer</a>: <i>Double</i>
<a href="#exceptionpersonalsitesandblogs" title="ExceptionPersonalSitesAndBlogs">ExceptionPersonalSitesAndBlogs</a>: <i>Double</i>
<a href="#exceptionpersonalstorage" title="ExceptionPersonalStorage">ExceptionPersonalStorage</a>: <i>Double</i>
<a href="#exceptionphilosophyandpolitics" title="ExceptionPhilosophyAndPolitics">ExceptionPhilosophyAndPolitics</a>: <i>Double</i>
<a href="#exceptionphishingandotherfraud" title="ExceptionPhishingAndOtherFraud">ExceptionPhishingAndOtherFraud</a>: <i>Double</i>
<a href="#exceptionprivateipaddresses" title="ExceptionPrivateIpAddresses">ExceptionPrivateIpAddresses</a>: <i>Double</i>
<a href="#exceptionproxyavoidandanonymizers" title="ExceptionProxyAvoidAndAnonymizers">ExceptionProxyAvoidAndAnonymizers</a>: <i>Double</i>
<a href="#exceptionquestionable" title="ExceptionQuestionable">ExceptionQuestionable</a>: <i>Double</i>
<a href="#exceptionrealestate" title="ExceptionRealEstate">ExceptionRealEstate</a>: <i>Double</i>
<a href="#exceptionrecreationandhobbies" title="ExceptionRecreationAndHobbies">ExceptionRecreationAndHobbies</a>: <i>Double</i>
<a href="#exceptionreferenceandresearch" title="ExceptionReferenceAndResearch">ExceptionReferenceAndResearch</a>: <i>Double</i>
<a href="#exceptionreligion" title="ExceptionReligion">ExceptionReligion</a>: <i>Double</i>
<a href="#exceptionsearchengines" title="ExceptionSearchEngines">ExceptionSearchEngines</a>: <i>Double</i>
<a href="#exceptionsexeducation" title="ExceptionSexEducation">ExceptionSexEducation</a>: <i>Double</i>
<a href="#exceptionsharewareandfreeware" title="ExceptionSharewareAndFreeware">ExceptionSharewareAndFreeware</a>: <i>Double</i>
<a href="#exceptionshopping" title="ExceptionShopping">ExceptionShopping</a>: <i>Double</i>
<a href="#exceptionsocialnetwork" title="ExceptionSocialNetwork">ExceptionSocialNetwork</a>: <i>Double</i>
<a href="#exceptionsociety" title="ExceptionSociety">ExceptionSociety</a>: <i>Double</i>
<a href="#exceptionspamurls" title="ExceptionSpamUrls">ExceptionSpamUrls</a>: <i>Double</i>
<a href="#exceptionsports" title="ExceptionSports">ExceptionSports</a>: <i>Double</i>
<a href="#exceptionspywareandadware" title="ExceptionSpywareAndAdware">ExceptionSpywareAndAdware</a>: <i>Double</i>
<a href="#exceptionstockadviceandtools" title="ExceptionStockAdviceAndTools">ExceptionStockAdviceAndTools</a>: <i>Double</i>
<a href="#exceptionstreamingmedia" title="ExceptionStreamingMedia">ExceptionStreamingMedia</a>: <i>Double</i>
<a href="#exceptionswimsuitsandintimateapparel" title="ExceptionSwimsuitsAndIntimateApparel">ExceptionSwimsuitsAndIntimateApparel</a>: <i>Double</i>
<a href="#exceptiontrainingandtools" title="ExceptionTrainingAndTools">ExceptionTrainingAndTools</a>: <i>Double</i>
<a href="#exceptiontranslation" title="ExceptionTranslation">ExceptionTranslation</a>: <i>Double</i>
<a href="#exceptiontravel" title="ExceptionTravel">ExceptionTravel</a>: <i>Double</i>
<a href="#exceptionuncategorized" title="ExceptionUncategorized">ExceptionUncategorized</a>: <i>Double</i>
<a href="#exceptionunconfirmedspamsources" title="ExceptionUnconfirmedSpamSources">ExceptionUnconfirmedSpamSources</a>: <i>Double</i>
<a href="#exceptionviolence" title="ExceptionViolence">ExceptionViolence</a>: <i>Double</i>
<a href="#exceptionweapons" title="ExceptionWeapons">ExceptionWeapons</a>: <i>Double</i>
<a href="#exceptionwebadvertisements" title="ExceptionWebAdvertisements">ExceptionWebAdvertisements</a>: <i>Double</i>
<a href="#exceptionwebbasedemail" title="ExceptionWebBasedEmail">ExceptionWebBasedEmail</a>: <i>Double</i>
<a href="#exceptionwebhostingsites" title="ExceptionWebHostingSites">ExceptionWebHostingSites</a>: <i>Double</i>
</pre>

## Properties

#### ExceptionAbortion

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionAdultAndPornography

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionAlcoholAndTobacco

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionAuctions

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionBotNets

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionBusinessAndEconomy

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionCdns

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionCheating

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionComputerAndInternetInfo

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionComputerAndInternetSecurity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionConfirmedSpamSources

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionCultAndOccult

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionDating

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionDeadSites

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionDrugs

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionDynamicComment

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionEducationalInstitutions

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionEntertainmentAndArts

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionFashionAndBeauty

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionFinancialServices

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionFoodAndDining

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionGambling

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionGames

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionGovernment

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionGross

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionHacking

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionHateAndRacism

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionHealthAndMedicine

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionHomeAndGarden

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionHuntingAndFishing

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionIllegal

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionImageAndVideoSearch

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionInternetCommunications

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionInternetPortals

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionJobSearch

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionKeyloggersAndMonitoring

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionKids

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionLegal

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionLocalInformation

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionMalwareSites

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionMarijuana

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionMilitary

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionMotorVehicles

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionMusic

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionNewsAndMedia

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionNudity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionOnlineGreetingCards

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionOpenHttpProxies

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionParkedDomains

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionPayToSurf

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionPeerToPeer

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionPersonalSitesAndBlogs

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionPersonalStorage

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionPhilosophyAndPolitics

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionPhishingAndOtherFraud

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionPrivateIpAddresses

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionProxyAvoidAndAnonymizers

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionQuestionable

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionRealEstate

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionRecreationAndHobbies

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionReferenceAndResearch

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionReligion

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionSearchEngines

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionSexEducation

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionSharewareAndFreeware

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionShopping

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionSocialNetwork

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionSociety

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionSpamUrls

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionSports

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionSpywareAndAdware

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionStockAdviceAndTools

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionStreamingMedia

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionSwimsuitsAndIntimateApparel

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionTrainingAndTools

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionTranslation

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionTravel

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionUncategorized

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionUnconfirmedSpamSources

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionViolence

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionWeapons

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionWebAdvertisements

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionWebBasedEmail

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionWebHostingSites

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


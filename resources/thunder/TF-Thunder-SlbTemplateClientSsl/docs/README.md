# TF::Thunder::SlbTemplateClientSsl

`thunder_slb_template_client_ssl` Provides details about thunder slb template client ssl

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplateClientSsl",
    "Properties" : {
        "<a href="#adgrouplist" title="AdGroupList">AdGroupList</a>" : <i>String</i>,
        "<a href="#alerttype" title="AlertType">AlertType</a>" : <i>String</i>,
        "<a href="#authsg" title="AuthSg">AuthSg</a>" : <i>String</i>,
        "<a href="#authsgdn" title="AuthSgDn">AuthSgDn</a>" : <i>Double</i>,
        "<a href="#authsgfilter" title="AuthSgFilter">AuthSgFilter</a>" : <i>String</i>,
        "<a href="#authusername" title="AuthUsername">AuthUsername</a>" : <i>String</i>,
        "<a href="#authusernameattribute" title="AuthUsernameAttribute">AuthUsernameAttribute</a>" : <i>String</i>,
        "<a href="#authenname" title="AuthenName">AuthenName</a>" : <i>String</i>,
        "<a href="#authorization" title="Authorization">Authorization</a>" : <i>Double</i>,
        "<a href="#bypasscertissuerclasslistname" title="BypassCertIssuerClassListName">BypassCertIssuerClassListName</a>" : <i>String</i>,
        "<a href="#bypasscertsanclasslistname" title="BypassCertSanClassListName">BypassCertSanClassListName</a>" : <i>String</i>,
        "<a href="#bypasscertsubjectclasslistname" title="BypassCertSubjectClassListName">BypassCertSubjectClassListName</a>" : <i>String</i>,
        "<a href="#cachepersistencelistname" title="CachePersistenceListName">CachePersistenceListName</a>" : <i>String</i>,
        "<a href="#caseinsensitive" title="CaseInsensitive">CaseInsensitive</a>" : <i>Double</i>,
        "<a href="#cert" title="Cert">Cert</a>" : <i>String</i>,
        "<a href="#certaltpartitionshared" title="CertAltPartitionShared">CertAltPartitionShared</a>" : <i>Double</i>,
        "<a href="#certalternate" title="CertAlternate">CertAlternate</a>" : <i>String</i>,
        "<a href="#certrevokeaction" title="CertRevokeAction">CertRevokeAction</a>" : <i>String</i>,
        "<a href="#certsharedstr" title="CertSharedStr">CertSharedStr</a>" : <i>String</i>,
        "<a href="#certunknownaction" title="CertUnknownAction">CertUnknownAction</a>" : <i>String</i>,
        "<a href="#chaincert" title="ChainCert">ChainCert</a>" : <i>String</i>,
        "<a href="#chaincertsharedstr" title="ChainCertSharedStr">ChainCertSharedStr</a>" : <i>String</i>,
        "<a href="#classlistname" title="ClassListName">ClassListName</a>" : <i>String</i>,
        "<a href="#clientauthcaseinsensitive" title="ClientAuthCaseInsensitive">ClientAuthCaseInsensitive</a>" : <i>Double</i>,
        "<a href="#clientauthclasslist" title="ClientAuthClassList">ClientAuthClassList</a>" : <i>String</i>,
        "<a href="#clientcertificate" title="ClientCertificate">ClientCertificate</a>" : <i>String</i>,
        "<a href="#closenotify" title="CloseNotify">CloseNotify</a>" : <i>Double</i>,
        "<a href="#dgversion" title="Dgversion">Dgversion</a>" : <i>Double</i>,
        "<a href="#dhtype" title="DhType">DhType</a>" : <i>String</i>,
        "<a href="#directclientserverauth" title="DirectClientServerAuth">DirectClientServerAuth</a>" : <i>Double</i>,
        "<a href="#disablesslv3" title="DisableSslv3">DisableSslv3</a>" : <i>Double</i>,
        "<a href="#earlydata" title="EarlyData">EarlyData</a>" : <i>Double</i>,
        "<a href="#enabletlsalertlogging" title="EnableTlsAlertLogging">EnableTlsAlertLogging</a>" : <i>Double</i>,
        "<a href="#exceptionadgrouplist" title="ExceptionAdGroupList">ExceptionAdGroupList</a>" : <i>String</i>,
        "<a href="#exceptioncertificateissuerclname" title="ExceptionCertificateIssuerClName">ExceptionCertificateIssuerClName</a>" : <i>String</i>,
        "<a href="#exceptioncertificatesanclname" title="ExceptionCertificateSanClName">ExceptionCertificateSanClName</a>" : <i>String</i>,
        "<a href="#exceptioncertificatesubjectclname" title="ExceptionCertificateSubjectClName">ExceptionCertificateSubjectClName</a>" : <i>String</i>,
        "<a href="#exceptionsniclname" title="ExceptionSniClName">ExceptionSniClName</a>" : <i>String</i>,
        "<a href="#exceptionusernamelist" title="ExceptionUserNameList">ExceptionUserNameList</a>" : <i>String</i>,
        "<a href="#expirehours" title="ExpireHours">ExpireHours</a>" : <i>Double</i>,
        "<a href="#forwardencrypted" title="ForwardEncrypted">ForwardEncrypted</a>" : <i>String</i>,
        "<a href="#forwardpassphrase" title="ForwardPassphrase">ForwardPassphrase</a>" : <i>String</i>,
        "<a href="#forwardproxyaltsign" title="ForwardProxyAltSign">ForwardProxyAltSign</a>" : <i>Double</i>,
        "<a href="#forwardproxyblockmessage" title="ForwardProxyBlockMessage">ForwardProxyBlockMessage</a>" : <i>String</i>,
        "<a href="#forwardproxycacert" title="ForwardProxyCaCert">ForwardProxyCaCert</a>" : <i>String</i>,
        "<a href="#forwardproxycakey" title="ForwardProxyCaKey">ForwardProxyCaKey</a>" : <i>String</i>,
        "<a href="#forwardproxycertcachelimit" title="ForwardProxyCertCacheLimit">ForwardProxyCertCacheLimit</a>" : <i>Double</i>,
        "<a href="#forwardproxycertcachetimeout" title="ForwardProxyCertCacheTimeout">ForwardProxyCertCacheTimeout</a>" : <i>Double</i>,
        "<a href="#forwardproxycertexpiry" title="ForwardProxyCertExpiry">ForwardProxyCertExpiry</a>" : <i>Double</i>,
        "<a href="#forwardproxycertnotreadyaction" title="ForwardProxyCertNotReadyAction">ForwardProxyCertNotReadyAction</a>" : <i>String</i>,
        "<a href="#forwardproxycertrevokeaction" title="ForwardProxyCertRevokeAction">ForwardProxyCertRevokeAction</a>" : <i>Double</i>,
        "<a href="#forwardproxycertunknownaction" title="ForwardProxyCertUnknownAction">ForwardProxyCertUnknownAction</a>" : <i>Double</i>,
        "<a href="#forwardproxycrldisable" title="ForwardProxyCrlDisable">ForwardProxyCrlDisable</a>" : <i>Double</i>,
        "<a href="#forwardproxydecrypteddscp" title="ForwardProxyDecryptedDscp">ForwardProxyDecryptedDscp</a>" : <i>Double</i>,
        "<a href="#forwardproxydecrypteddscpbypass" title="ForwardProxyDecryptedDscpBypass">ForwardProxyDecryptedDscpBypass</a>" : <i>Double</i>,
        "<a href="#forwardproxyenable" title="ForwardProxyEnable">ForwardProxyEnable</a>" : <i>Double</i>,
        "<a href="#forwardproxyfailsafedisable" title="ForwardProxyFailsafeDisable">ForwardProxyFailsafeDisable</a>" : <i>Double</i>,
        "<a href="#forwardproxylogdisable" title="ForwardProxyLogDisable">ForwardProxyLogDisable</a>" : <i>Double</i>,
        "<a href="#forwardproxynosharedcipheraction" title="ForwardProxyNoSharedCipherAction">ForwardProxyNoSharedCipherAction</a>" : <i>Double</i>,
        "<a href="#forwardproxynosniaction" title="ForwardProxyNoSniAction">ForwardProxyNoSniAction</a>" : <i>String</i>,
        "<a href="#forwardproxyocspdisable" title="ForwardProxyOcspDisable">ForwardProxyOcspDisable</a>" : <i>Double</i>,
        "<a href="#forwardproxyrequiresnicertmatched" title="ForwardProxyRequireSniCertMatched">ForwardProxyRequireSniCertMatched</a>" : <i>String</i>,
        "<a href="#forwardproxyselfsignredir" title="ForwardProxySelfsignRedir">ForwardProxySelfsignRedir</a>" : <i>Double</i>,
        "<a href="#forwardproxysslversion" title="ForwardProxySslVersion">ForwardProxySslVersion</a>" : <i>Double</i>,
        "<a href="#forwardproxyverifycertfailaction" title="ForwardProxyVerifyCertFailAction">ForwardProxyVerifyCertFailAction</a>" : <i>Double</i>,
        "<a href="#fpaltcert" title="FpAltCert">FpAltCert</a>" : <i>String</i>,
        "<a href="#fpaltencrypted" title="FpAltEncrypted">FpAltEncrypted</a>" : <i>String</i>,
        "<a href="#fpaltkey" title="FpAltKey">FpAltKey</a>" : <i>String</i>,
        "<a href="#fpaltpassphrase" title="FpAltPassphrase">FpAltPassphrase</a>" : <i>String</i>,
        "<a href="#fpaltshared" title="FpAltShared">FpAltShared</a>" : <i>Double</i>,
        "<a href="#fpcakeyshared" title="FpCaKeyShared">FpCaKeyShared</a>" : <i>Double</i>,
        "<a href="#fpcashared" title="FpCaShared">FpCaShared</a>" : <i>Double</i>,
        "<a href="#fpcertextaiacaissuers" title="FpCertExtAiaCaIssuers">FpCertExtAiaCaIssuers</a>" : <i>String</i>,
        "<a href="#fpcertextaiaocsp" title="FpCertExtAiaOcsp">FpCertExtAiaOcsp</a>" : <i>String</i>,
        "<a href="#fpcertextcrldp" title="FpCertExtCrldp">FpCertExtCrldp</a>" : <i>String</i>,
        "<a href="#fpcertfetchautonat" title="FpCertFetchAutonat">FpCertFetchAutonat</a>" : <i>String</i>,
        "<a href="#fpcertfetchautonatprecedence" title="FpCertFetchAutonatPrecedence">FpCertFetchAutonatPrecedence</a>" : <i>Double</i>,
        "<a href="#fpcertfetchnatpoolname" title="FpCertFetchNatpoolName">FpCertFetchNatpoolName</a>" : <i>String</i>,
        "<a href="#fpcertfetchnatpoolnameshared" title="FpCertFetchNatpoolNameShared">FpCertFetchNatpoolNameShared</a>" : <i>String</i>,
        "<a href="#fpcertfetchnatpoolprecedence" title="FpCertFetchNatpoolPrecedence">FpCertFetchNatpoolPrecedence</a>" : <i>Double</i>,
        "<a href="#handshakeloggingenable" title="HandshakeLoggingEnable">HandshakeLoggingEnable</a>" : <i>Double</i>,
        "<a href="#hsmtype" title="HsmType">HsmType</a>" : <i>String</i>,
        "<a href="#inspectcertificateissuerclname" title="InspectCertificateIssuerClName">InspectCertificateIssuerClName</a>" : <i>String</i>,
        "<a href="#inspectcertificatesanclname" title="InspectCertificateSanClName">InspectCertificateSanClName</a>" : <i>String</i>,
        "<a href="#inspectcertificatesubjectclname" title="InspectCertificateSubjectClName">InspectCertificateSubjectClName</a>" : <i>String</i>,
        "<a href="#inspectlistname" title="InspectListName">InspectListName</a>" : <i>String</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#keyaltencrypted" title="KeyAltEncrypted">KeyAltEncrypted</a>" : <i>String</i>,
        "<a href="#keyaltpartitionshared" title="KeyAltPartitionShared">KeyAltPartitionShared</a>" : <i>Double</i>,
        "<a href="#keyaltpassphrase" title="KeyAltPassphrase">KeyAltPassphrase</a>" : <i>String</i>,
        "<a href="#keyalternate" title="KeyAlternate">KeyAlternate</a>" : <i>String</i>,
        "<a href="#keyencrypted" title="KeyEncrypted">KeyEncrypted</a>" : <i>String</i>,
        "<a href="#keypassphrase" title="KeyPassphrase">KeyPassphrase</a>" : <i>String</i>,
        "<a href="#keysharedencrypted" title="KeySharedEncrypted">KeySharedEncrypted</a>" : <i>String</i>,
        "<a href="#keysharedpassphrase" title="KeySharedPassphrase">KeySharedPassphrase</a>" : <i>String</i>,
        "<a href="#keysharedstr" title="KeySharedStr">KeySharedStr</a>" : <i>String</i>,
        "<a href="#ldapbasednfromcert" title="LdapBaseDnFromCert">LdapBaseDnFromCert</a>" : <i>Double</i>,
        "<a href="#ldapsearchfilter" title="LdapSearchFilter">LdapSearchFilter</a>" : <i>String</i>,
        "<a href="#locallogging" title="LocalLogging">LocalLogging</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#noantireplay" title="NoAntiReplay">NoAntiReplay</a>" : <i>Double</i>,
        "<a href="#nosharedcipheraction" title="NoSharedCipherAction">NoSharedCipherAction</a>" : <i>String</i>,
        "<a href="#nonsslbypassl4session" title="NonSslBypassL4session">NonSslBypassL4session</a>" : <i>Double</i>,
        "<a href="#nonsslbypassservicegroup" title="NonSslBypassServiceGroup">NonSslBypassServiceGroup</a>" : <i>String</i>,
        "<a href="#notafter" title="Notafter">Notafter</a>" : <i>Double</i>,
        "<a href="#notafterday" title="Notafterday">Notafterday</a>" : <i>Double</i>,
        "<a href="#notaftermonth" title="Notaftermonth">Notaftermonth</a>" : <i>Double</i>,
        "<a href="#notafteryear" title="Notafteryear">Notafteryear</a>" : <i>Double</i>,
        "<a href="#notbefore" title="Notbefore">Notbefore</a>" : <i>Double</i>,
        "<a href="#notbeforeday" title="Notbeforeday">Notbeforeday</a>" : <i>Double</i>,
        "<a href="#notbeforemonth" title="Notbeforemonth">Notbeforemonth</a>" : <i>Double</i>,
        "<a href="#notbeforeyear" title="Notbeforeyear">Notbeforeyear</a>" : <i>Double</i>,
        "<a href="#ocspstapling" title="OcspStapling">OcspStapling</a>" : <i>Double</i>,
        "<a href="#ocspstcacert" title="OcspstCaCert">OcspstCaCert</a>" : <i>String</i>,
        "<a href="#ocspstocsp" title="OcspstOcsp">OcspstOcsp</a>" : <i>Double</i>,
        "<a href="#ocspstsg" title="OcspstSg">OcspstSg</a>" : <i>String</i>,
        "<a href="#ocspstsgdays" title="OcspstSgDays">OcspstSgDays</a>" : <i>Double</i>,
        "<a href="#ocspstsghours" title="OcspstSgHours">OcspstSgHours</a>" : <i>Double</i>,
        "<a href="#ocspstsgminutes" title="OcspstSgMinutes">OcspstSgMinutes</a>" : <i>Double</i>,
        "<a href="#ocspstsgtimeout" title="OcspstSgTimeout">OcspstSgTimeout</a>" : <i>Double</i>,
        "<a href="#ocspstsrvr" title="OcspstSrvr">OcspstSrvr</a>" : <i>String</i>,
        "<a href="#ocspstsrvrdays" title="OcspstSrvrDays">OcspstSrvrDays</a>" : <i>Double</i>,
        "<a href="#ocspstsrvrhours" title="OcspstSrvrHours">OcspstSrvrHours</a>" : <i>Double</i>,
        "<a href="#ocspstsrvrminutes" title="OcspstSrvrMinutes">OcspstSrvrMinutes</a>" : <i>Double</i>,
        "<a href="#ocspstsrvrtimeout" title="OcspstSrvrTimeout">OcspstSrvrTimeout</a>" : <i>Double</i>,
        "<a href="#renegotiationdisable" title="RenegotiationDisable">RenegotiationDisable</a>" : <i>Double</i>,
        "<a href="#requirewebcategory" title="RequireWebCategory">RequireWebCategory</a>" : <i>Double</i>,
        "<a href="#servernameautomap" title="ServerNameAutoMap">ServerNameAutoMap</a>" : <i>Double</i>,
        "<a href="#sessioncachesize" title="SessionCacheSize">SessionCacheSize</a>" : <i>Double</i>,
        "<a href="#sessioncachetimeout" title="SessionCacheTimeout">SessionCacheTimeout</a>" : <i>Double</i>,
        "<a href="#sessionticketdisable" title="SessionTicketDisable">SessionTicketDisable</a>" : <i>Double</i>,
        "<a href="#sessionticketlifetime" title="SessionTicketLifetime">SessionTicketLifetime</a>" : <i>Double</i>,
        "<a href="#sharedpartitionciphertemplate" title="SharedPartitionCipherTemplate">SharedPartitionCipherTemplate</a>" : <i>Double</i>,
        "<a href="#sharedpartitionpool" title="SharedPartitionPool">SharedPartitionPool</a>" : <i>Double</i>,
        "<a href="#snienablelog" title="SniEnableLog">SniEnableLog</a>" : <i>Double</i>,
        "<a href="#sslfalsestartdisable" title="SslFalseStartDisable">SslFalseStartDisable</a>" : <i>Double</i>,
        "<a href="#sslilogging" title="SsliLogging">SsliLogging</a>" : <i>Double</i>,
        "<a href="#sslilogging" title="Sslilogging">Sslilogging</a>" : <i>String</i>,
        "<a href="#sslv2bypassservicegroup" title="Sslv2BypassServiceGroup">Sslv2BypassServiceGroup</a>" : <i>String</i>,
        "<a href="#templatecipher" title="TemplateCipher">TemplateCipher</a>" : <i>String</i>,
        "<a href="#templateciphershared" title="TemplateCipherShared">TemplateCipherShared</a>" : <i>String</i>,
        "<a href="#templatehsm" title="TemplateHsm">TemplateHsm</a>" : <i>String</i>,
        "<a href="#usernamelist" title="UserNameList">UserNameList</a>" : <i>String</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#verifycertfailaction" title="VerifyCertFailAction">VerifyCertFailAction</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>,
        "<a href="#bypasscertissuermulticlasslist" title="BypassCertIssuerMultiClassList">BypassCertIssuerMultiClassList</a>" : <i>[ <a href="bypasscertissuermulticlasslistdefinition.md">BypassCertIssuerMultiClassListDefinition</a>, ... ]</i>,
        "<a href="#bypasscertsanmulticlasslist" title="BypassCertSanMultiClassList">BypassCertSanMultiClassList</a>" : <i>[ <a href="bypasscertsanmulticlasslistdefinition.md">BypassCertSanMultiClassListDefinition</a>, ... ]</i>,
        "<a href="#bypasscertsubjectmulticlasslist" title="BypassCertSubjectMultiClassList">BypassCertSubjectMultiClassList</a>" : <i>[ <a href="bypasscertsubjectmulticlasslistdefinition.md">BypassCertSubjectMultiClassListDefinition</a>, ... ]</i>,
        "<a href="#cacerts" title="CaCerts">CaCerts</a>" : <i>[ <a href="cacertsdefinition.md">CaCertsDefinition</a>, ... ]</i>,
        "<a href="#certificateissuercontainslist" title="CertificateIssuerContainsList">CertificateIssuerContainsList</a>" : <i>[ <a href="certificateissuercontainslistdefinition.md">CertificateIssuerContainsListDefinition</a>, ... ]</i>,
        "<a href="#certificateissuerendswithlist" title="CertificateIssuerEndsWithList">CertificateIssuerEndsWithList</a>" : <i>[ <a href="certificateissuerendswithlistdefinition.md">CertificateIssuerEndsWithListDefinition</a>, ... ]</i>,
        "<a href="#certificateissuerequalslist" title="CertificateIssuerEqualsList">CertificateIssuerEqualsList</a>" : <i>[ <a href="certificateissuerequalslistdefinition.md">CertificateIssuerEqualsListDefinition</a>, ... ]</i>,
        "<a href="#certificateissuerstartswithlist" title="CertificateIssuerStartsWithList">CertificateIssuerStartsWithList</a>" : <i>[ <a href="certificateissuerstartswithlistdefinition.md">CertificateIssuerStartsWithListDefinition</a>, ... ]</i>,
        "<a href="#certificatelist" title="CertificateList">CertificateList</a>" : <i>[ <a href="certificatelistdefinition.md">CertificateListDefinition</a>, ... ]</i>,
        "<a href="#certificatesancontainslist" title="CertificateSanContainsList">CertificateSanContainsList</a>" : <i>[ <a href="certificatesancontainslistdefinition.md">CertificateSanContainsListDefinition</a>, ... ]</i>,
        "<a href="#certificatesanendswithlist" title="CertificateSanEndsWithList">CertificateSanEndsWithList</a>" : <i>[ <a href="certificatesanendswithlistdefinition.md">CertificateSanEndsWithListDefinition</a>, ... ]</i>,
        "<a href="#certificatesanequalslist" title="CertificateSanEqualsList">CertificateSanEqualsList</a>" : <i>[ <a href="certificatesanequalslistdefinition.md">CertificateSanEqualsListDefinition</a>, ... ]</i>,
        "<a href="#certificatesanstartswithlist" title="CertificateSanStartsWithList">CertificateSanStartsWithList</a>" : <i>[ <a href="certificatesanstartswithlistdefinition.md">CertificateSanStartsWithListDefinition</a>, ... ]</i>,
        "<a href="#certificatesubjectcontainslist" title="CertificateSubjectContainsList">CertificateSubjectContainsList</a>" : <i>[ <a href="certificatesubjectcontainslistdefinition.md">CertificateSubjectContainsListDefinition</a>, ... ]</i>,
        "<a href="#certificatesubjectendswithlist" title="CertificateSubjectEndsWithList">CertificateSubjectEndsWithList</a>" : <i>[ <a href="certificatesubjectendswithlistdefinition.md">CertificateSubjectEndsWithListDefinition</a>, ... ]</i>,
        "<a href="#certificatesubjectequalslist" title="CertificateSubjectEqualsList">CertificateSubjectEqualsList</a>" : <i>[ <a href="certificatesubjectequalslistdefinition.md">CertificateSubjectEqualsListDefinition</a>, ... ]</i>,
        "<a href="#certificatesubjectstartswithlist" title="CertificateSubjectStartsWithList">CertificateSubjectStartsWithList</a>" : <i>[ <a href="certificatesubjectstartswithlistdefinition.md">CertificateSubjectStartsWithListDefinition</a>, ... ]</i>,
        "<a href="#cipherwithoutpriolist" title="CipherWithoutPrioList">CipherWithoutPrioList</a>" : <i>[ <a href="cipherwithoutpriolistdefinition.md">CipherWithoutPrioListDefinition</a>, ... ]</i>,
        "<a href="#clientauthcontainslist" title="ClientAuthContainsList">ClientAuthContainsList</a>" : <i>[ <a href="clientauthcontainslistdefinition.md">ClientAuthContainsListDefinition</a>, ... ]</i>,
        "<a href="#clientauthendswithlist" title="ClientAuthEndsWithList">ClientAuthEndsWithList</a>" : <i>[ <a href="clientauthendswithlistdefinition.md">ClientAuthEndsWithListDefinition</a>, ... ]</i>,
        "<a href="#clientauthequalslist" title="ClientAuthEqualsList">ClientAuthEqualsList</a>" : <i>[ <a href="clientauthequalslistdefinition.md">ClientAuthEqualsListDefinition</a>, ... ]</i>,
        "<a href="#clientauthstartswithlist" title="ClientAuthStartsWithList">ClientAuthStartsWithList</a>" : <i>[ <a href="clientauthstartswithlistdefinition.md">ClientAuthStartsWithListDefinition</a>, ... ]</i>,
        "<a href="#containslist" title="ContainsList">ContainsList</a>" : <i>[ <a href="containslistdefinition.md">ContainsListDefinition</a>, ... ]</i>,
        "<a href="#crlcerts" title="CrlCerts">CrlCerts</a>" : <i>[ <a href="crlcertsdefinition.md">CrlCertsDefinition</a>, ... ]</i>,
        "<a href="#eclist" title="EcList">EcList</a>" : <i>[ <a href="eclistdefinition.md">EcListDefinition</a>, ... ]</i>,
        "<a href="#endswithlist" title="EndsWithList">EndsWithList</a>" : <i>[ <a href="endswithlistdefinition.md">EndsWithListDefinition</a>, ... ]</i>,
        "<a href="#equalslist" title="EqualsList">EqualsList</a>" : <i>[ <a href="equalslistdefinition.md">EqualsListDefinition</a>, ... ]</i>,
        "<a href="#exceptionwebcategory" title="ExceptionWebCategory">ExceptionWebCategory</a>" : <i>[ <a href="exceptionwebcategorydefinition.md">ExceptionWebCategoryDefinition</a>, ... ]</i>,
        "<a href="#exceptionwebreputation" title="ExceptionWebReputation">ExceptionWebReputation</a>" : <i>[ <a href="exceptionwebreputationdefinition.md">ExceptionWebReputationDefinition</a>, ... ]</i>,
        "<a href="#forwardproxytrustedcalists" title="ForwardProxyTrustedCaLists">ForwardProxyTrustedCaLists</a>" : <i>[ <a href="forwardproxytrustedcalistsdefinition.md">ForwardProxyTrustedCaListsDefinition</a>, ... ]</i>,
        "<a href="#multiclasslist" title="MultiClassList">MultiClassList</a>" : <i>[ <a href="multiclasslistdefinition.md">MultiClassListDefinition</a>, ... ]</i>,
        "<a href="#reqcalists" title="ReqCaLists">ReqCaLists</a>" : <i>[ <a href="reqcalistsdefinition.md">ReqCaListsDefinition</a>, ... ]</i>,
        "<a href="#servernamelist" title="ServerNameList">ServerNameList</a>" : <i>[ <a href="servernamelistdefinition.md">ServerNameListDefinition</a>, ... ]</i>,
        "<a href="#startswithlist" title="StartsWithList">StartsWithList</a>" : <i>[ <a href="startswithlistdefinition.md">StartsWithListDefinition</a>, ... ]</i>,
        "<a href="#webcategory" title="WebCategory">WebCategory</a>" : <i>[ <a href="webcategorydefinition.md">WebCategoryDefinition</a>, ... ]</i>,
        "<a href="#webreputation" title="WebReputation">WebReputation</a>" : <i>[ <a href="webreputationdefinition.md">WebReputationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbTemplateClientSsl
Properties:
    <a href="#adgrouplist" title="AdGroupList">AdGroupList</a>: <i>String</i>
    <a href="#alerttype" title="AlertType">AlertType</a>: <i>String</i>
    <a href="#authsg" title="AuthSg">AuthSg</a>: <i>String</i>
    <a href="#authsgdn" title="AuthSgDn">AuthSgDn</a>: <i>Double</i>
    <a href="#authsgfilter" title="AuthSgFilter">AuthSgFilter</a>: <i>String</i>
    <a href="#authusername" title="AuthUsername">AuthUsername</a>: <i>String</i>
    <a href="#authusernameattribute" title="AuthUsernameAttribute">AuthUsernameAttribute</a>: <i>String</i>
    <a href="#authenname" title="AuthenName">AuthenName</a>: <i>String</i>
    <a href="#authorization" title="Authorization">Authorization</a>: <i>Double</i>
    <a href="#bypasscertissuerclasslistname" title="BypassCertIssuerClassListName">BypassCertIssuerClassListName</a>: <i>String</i>
    <a href="#bypasscertsanclasslistname" title="BypassCertSanClassListName">BypassCertSanClassListName</a>: <i>String</i>
    <a href="#bypasscertsubjectclasslistname" title="BypassCertSubjectClassListName">BypassCertSubjectClassListName</a>: <i>String</i>
    <a href="#cachepersistencelistname" title="CachePersistenceListName">CachePersistenceListName</a>: <i>String</i>
    <a href="#caseinsensitive" title="CaseInsensitive">CaseInsensitive</a>: <i>Double</i>
    <a href="#cert" title="Cert">Cert</a>: <i>String</i>
    <a href="#certaltpartitionshared" title="CertAltPartitionShared">CertAltPartitionShared</a>: <i>Double</i>
    <a href="#certalternate" title="CertAlternate">CertAlternate</a>: <i>String</i>
    <a href="#certrevokeaction" title="CertRevokeAction">CertRevokeAction</a>: <i>String</i>
    <a href="#certsharedstr" title="CertSharedStr">CertSharedStr</a>: <i>String</i>
    <a href="#certunknownaction" title="CertUnknownAction">CertUnknownAction</a>: <i>String</i>
    <a href="#chaincert" title="ChainCert">ChainCert</a>: <i>String</i>
    <a href="#chaincertsharedstr" title="ChainCertSharedStr">ChainCertSharedStr</a>: <i>String</i>
    <a href="#classlistname" title="ClassListName">ClassListName</a>: <i>String</i>
    <a href="#clientauthcaseinsensitive" title="ClientAuthCaseInsensitive">ClientAuthCaseInsensitive</a>: <i>Double</i>
    <a href="#clientauthclasslist" title="ClientAuthClassList">ClientAuthClassList</a>: <i>String</i>
    <a href="#clientcertificate" title="ClientCertificate">ClientCertificate</a>: <i>String</i>
    <a href="#closenotify" title="CloseNotify">CloseNotify</a>: <i>Double</i>
    <a href="#dgversion" title="Dgversion">Dgversion</a>: <i>Double</i>
    <a href="#dhtype" title="DhType">DhType</a>: <i>String</i>
    <a href="#directclientserverauth" title="DirectClientServerAuth">DirectClientServerAuth</a>: <i>Double</i>
    <a href="#disablesslv3" title="DisableSslv3">DisableSslv3</a>: <i>Double</i>
    <a href="#earlydata" title="EarlyData">EarlyData</a>: <i>Double</i>
    <a href="#enabletlsalertlogging" title="EnableTlsAlertLogging">EnableTlsAlertLogging</a>: <i>Double</i>
    <a href="#exceptionadgrouplist" title="ExceptionAdGroupList">ExceptionAdGroupList</a>: <i>String</i>
    <a href="#exceptioncertificateissuerclname" title="ExceptionCertificateIssuerClName">ExceptionCertificateIssuerClName</a>: <i>String</i>
    <a href="#exceptioncertificatesanclname" title="ExceptionCertificateSanClName">ExceptionCertificateSanClName</a>: <i>String</i>
    <a href="#exceptioncertificatesubjectclname" title="ExceptionCertificateSubjectClName">ExceptionCertificateSubjectClName</a>: <i>String</i>
    <a href="#exceptionsniclname" title="ExceptionSniClName">ExceptionSniClName</a>: <i>String</i>
    <a href="#exceptionusernamelist" title="ExceptionUserNameList">ExceptionUserNameList</a>: <i>String</i>
    <a href="#expirehours" title="ExpireHours">ExpireHours</a>: <i>Double</i>
    <a href="#forwardencrypted" title="ForwardEncrypted">ForwardEncrypted</a>: <i>String</i>
    <a href="#forwardpassphrase" title="ForwardPassphrase">ForwardPassphrase</a>: <i>String</i>
    <a href="#forwardproxyaltsign" title="ForwardProxyAltSign">ForwardProxyAltSign</a>: <i>Double</i>
    <a href="#forwardproxyblockmessage" title="ForwardProxyBlockMessage">ForwardProxyBlockMessage</a>: <i>String</i>
    <a href="#forwardproxycacert" title="ForwardProxyCaCert">ForwardProxyCaCert</a>: <i>String</i>
    <a href="#forwardproxycakey" title="ForwardProxyCaKey">ForwardProxyCaKey</a>: <i>String</i>
    <a href="#forwardproxycertcachelimit" title="ForwardProxyCertCacheLimit">ForwardProxyCertCacheLimit</a>: <i>Double</i>
    <a href="#forwardproxycertcachetimeout" title="ForwardProxyCertCacheTimeout">ForwardProxyCertCacheTimeout</a>: <i>Double</i>
    <a href="#forwardproxycertexpiry" title="ForwardProxyCertExpiry">ForwardProxyCertExpiry</a>: <i>Double</i>
    <a href="#forwardproxycertnotreadyaction" title="ForwardProxyCertNotReadyAction">ForwardProxyCertNotReadyAction</a>: <i>String</i>
    <a href="#forwardproxycertrevokeaction" title="ForwardProxyCertRevokeAction">ForwardProxyCertRevokeAction</a>: <i>Double</i>
    <a href="#forwardproxycertunknownaction" title="ForwardProxyCertUnknownAction">ForwardProxyCertUnknownAction</a>: <i>Double</i>
    <a href="#forwardproxycrldisable" title="ForwardProxyCrlDisable">ForwardProxyCrlDisable</a>: <i>Double</i>
    <a href="#forwardproxydecrypteddscp" title="ForwardProxyDecryptedDscp">ForwardProxyDecryptedDscp</a>: <i>Double</i>
    <a href="#forwardproxydecrypteddscpbypass" title="ForwardProxyDecryptedDscpBypass">ForwardProxyDecryptedDscpBypass</a>: <i>Double</i>
    <a href="#forwardproxyenable" title="ForwardProxyEnable">ForwardProxyEnable</a>: <i>Double</i>
    <a href="#forwardproxyfailsafedisable" title="ForwardProxyFailsafeDisable">ForwardProxyFailsafeDisable</a>: <i>Double</i>
    <a href="#forwardproxylogdisable" title="ForwardProxyLogDisable">ForwardProxyLogDisable</a>: <i>Double</i>
    <a href="#forwardproxynosharedcipheraction" title="ForwardProxyNoSharedCipherAction">ForwardProxyNoSharedCipherAction</a>: <i>Double</i>
    <a href="#forwardproxynosniaction" title="ForwardProxyNoSniAction">ForwardProxyNoSniAction</a>: <i>String</i>
    <a href="#forwardproxyocspdisable" title="ForwardProxyOcspDisable">ForwardProxyOcspDisable</a>: <i>Double</i>
    <a href="#forwardproxyrequiresnicertmatched" title="ForwardProxyRequireSniCertMatched">ForwardProxyRequireSniCertMatched</a>: <i>String</i>
    <a href="#forwardproxyselfsignredir" title="ForwardProxySelfsignRedir">ForwardProxySelfsignRedir</a>: <i>Double</i>
    <a href="#forwardproxysslversion" title="ForwardProxySslVersion">ForwardProxySslVersion</a>: <i>Double</i>
    <a href="#forwardproxyverifycertfailaction" title="ForwardProxyVerifyCertFailAction">ForwardProxyVerifyCertFailAction</a>: <i>Double</i>
    <a href="#fpaltcert" title="FpAltCert">FpAltCert</a>: <i>String</i>
    <a href="#fpaltencrypted" title="FpAltEncrypted">FpAltEncrypted</a>: <i>String</i>
    <a href="#fpaltkey" title="FpAltKey">FpAltKey</a>: <i>String</i>
    <a href="#fpaltpassphrase" title="FpAltPassphrase">FpAltPassphrase</a>: <i>String</i>
    <a href="#fpaltshared" title="FpAltShared">FpAltShared</a>: <i>Double</i>
    <a href="#fpcakeyshared" title="FpCaKeyShared">FpCaKeyShared</a>: <i>Double</i>
    <a href="#fpcashared" title="FpCaShared">FpCaShared</a>: <i>Double</i>
    <a href="#fpcertextaiacaissuers" title="FpCertExtAiaCaIssuers">FpCertExtAiaCaIssuers</a>: <i>String</i>
    <a href="#fpcertextaiaocsp" title="FpCertExtAiaOcsp">FpCertExtAiaOcsp</a>: <i>String</i>
    <a href="#fpcertextcrldp" title="FpCertExtCrldp">FpCertExtCrldp</a>: <i>String</i>
    <a href="#fpcertfetchautonat" title="FpCertFetchAutonat">FpCertFetchAutonat</a>: <i>String</i>
    <a href="#fpcertfetchautonatprecedence" title="FpCertFetchAutonatPrecedence">FpCertFetchAutonatPrecedence</a>: <i>Double</i>
    <a href="#fpcertfetchnatpoolname" title="FpCertFetchNatpoolName">FpCertFetchNatpoolName</a>: <i>String</i>
    <a href="#fpcertfetchnatpoolnameshared" title="FpCertFetchNatpoolNameShared">FpCertFetchNatpoolNameShared</a>: <i>String</i>
    <a href="#fpcertfetchnatpoolprecedence" title="FpCertFetchNatpoolPrecedence">FpCertFetchNatpoolPrecedence</a>: <i>Double</i>
    <a href="#handshakeloggingenable" title="HandshakeLoggingEnable">HandshakeLoggingEnable</a>: <i>Double</i>
    <a href="#hsmtype" title="HsmType">HsmType</a>: <i>String</i>
    <a href="#inspectcertificateissuerclname" title="InspectCertificateIssuerClName">InspectCertificateIssuerClName</a>: <i>String</i>
    <a href="#inspectcertificatesanclname" title="InspectCertificateSanClName">InspectCertificateSanClName</a>: <i>String</i>
    <a href="#inspectcertificatesubjectclname" title="InspectCertificateSubjectClName">InspectCertificateSubjectClName</a>: <i>String</i>
    <a href="#inspectlistname" title="InspectListName">InspectListName</a>: <i>String</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#keyaltencrypted" title="KeyAltEncrypted">KeyAltEncrypted</a>: <i>String</i>
    <a href="#keyaltpartitionshared" title="KeyAltPartitionShared">KeyAltPartitionShared</a>: <i>Double</i>
    <a href="#keyaltpassphrase" title="KeyAltPassphrase">KeyAltPassphrase</a>: <i>String</i>
    <a href="#keyalternate" title="KeyAlternate">KeyAlternate</a>: <i>String</i>
    <a href="#keyencrypted" title="KeyEncrypted">KeyEncrypted</a>: <i>String</i>
    <a href="#keypassphrase" title="KeyPassphrase">KeyPassphrase</a>: <i>String</i>
    <a href="#keysharedencrypted" title="KeySharedEncrypted">KeySharedEncrypted</a>: <i>String</i>
    <a href="#keysharedpassphrase" title="KeySharedPassphrase">KeySharedPassphrase</a>: <i>String</i>
    <a href="#keysharedstr" title="KeySharedStr">KeySharedStr</a>: <i>String</i>
    <a href="#ldapbasednfromcert" title="LdapBaseDnFromCert">LdapBaseDnFromCert</a>: <i>Double</i>
    <a href="#ldapsearchfilter" title="LdapSearchFilter">LdapSearchFilter</a>: <i>String</i>
    <a href="#locallogging" title="LocalLogging">LocalLogging</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#noantireplay" title="NoAntiReplay">NoAntiReplay</a>: <i>Double</i>
    <a href="#nosharedcipheraction" title="NoSharedCipherAction">NoSharedCipherAction</a>: <i>String</i>
    <a href="#nonsslbypassl4session" title="NonSslBypassL4session">NonSslBypassL4session</a>: <i>Double</i>
    <a href="#nonsslbypassservicegroup" title="NonSslBypassServiceGroup">NonSslBypassServiceGroup</a>: <i>String</i>
    <a href="#notafter" title="Notafter">Notafter</a>: <i>Double</i>
    <a href="#notafterday" title="Notafterday">Notafterday</a>: <i>Double</i>
    <a href="#notaftermonth" title="Notaftermonth">Notaftermonth</a>: <i>Double</i>
    <a href="#notafteryear" title="Notafteryear">Notafteryear</a>: <i>Double</i>
    <a href="#notbefore" title="Notbefore">Notbefore</a>: <i>Double</i>
    <a href="#notbeforeday" title="Notbeforeday">Notbeforeday</a>: <i>Double</i>
    <a href="#notbeforemonth" title="Notbeforemonth">Notbeforemonth</a>: <i>Double</i>
    <a href="#notbeforeyear" title="Notbeforeyear">Notbeforeyear</a>: <i>Double</i>
    <a href="#ocspstapling" title="OcspStapling">OcspStapling</a>: <i>Double</i>
    <a href="#ocspstcacert" title="OcspstCaCert">OcspstCaCert</a>: <i>String</i>
    <a href="#ocspstocsp" title="OcspstOcsp">OcspstOcsp</a>: <i>Double</i>
    <a href="#ocspstsg" title="OcspstSg">OcspstSg</a>: <i>String</i>
    <a href="#ocspstsgdays" title="OcspstSgDays">OcspstSgDays</a>: <i>Double</i>
    <a href="#ocspstsghours" title="OcspstSgHours">OcspstSgHours</a>: <i>Double</i>
    <a href="#ocspstsgminutes" title="OcspstSgMinutes">OcspstSgMinutes</a>: <i>Double</i>
    <a href="#ocspstsgtimeout" title="OcspstSgTimeout">OcspstSgTimeout</a>: <i>Double</i>
    <a href="#ocspstsrvr" title="OcspstSrvr">OcspstSrvr</a>: <i>String</i>
    <a href="#ocspstsrvrdays" title="OcspstSrvrDays">OcspstSrvrDays</a>: <i>Double</i>
    <a href="#ocspstsrvrhours" title="OcspstSrvrHours">OcspstSrvrHours</a>: <i>Double</i>
    <a href="#ocspstsrvrminutes" title="OcspstSrvrMinutes">OcspstSrvrMinutes</a>: <i>Double</i>
    <a href="#ocspstsrvrtimeout" title="OcspstSrvrTimeout">OcspstSrvrTimeout</a>: <i>Double</i>
    <a href="#renegotiationdisable" title="RenegotiationDisable">RenegotiationDisable</a>: <i>Double</i>
    <a href="#requirewebcategory" title="RequireWebCategory">RequireWebCategory</a>: <i>Double</i>
    <a href="#servernameautomap" title="ServerNameAutoMap">ServerNameAutoMap</a>: <i>Double</i>
    <a href="#sessioncachesize" title="SessionCacheSize">SessionCacheSize</a>: <i>Double</i>
    <a href="#sessioncachetimeout" title="SessionCacheTimeout">SessionCacheTimeout</a>: <i>Double</i>
    <a href="#sessionticketdisable" title="SessionTicketDisable">SessionTicketDisable</a>: <i>Double</i>
    <a href="#sessionticketlifetime" title="SessionTicketLifetime">SessionTicketLifetime</a>: <i>Double</i>
    <a href="#sharedpartitionciphertemplate" title="SharedPartitionCipherTemplate">SharedPartitionCipherTemplate</a>: <i>Double</i>
    <a href="#sharedpartitionpool" title="SharedPartitionPool">SharedPartitionPool</a>: <i>Double</i>
    <a href="#snienablelog" title="SniEnableLog">SniEnableLog</a>: <i>Double</i>
    <a href="#sslfalsestartdisable" title="SslFalseStartDisable">SslFalseStartDisable</a>: <i>Double</i>
    <a href="#sslilogging" title="SsliLogging">SsliLogging</a>: <i>Double</i>
    <a href="#sslilogging" title="Sslilogging">Sslilogging</a>: <i>String</i>
    <a href="#sslv2bypassservicegroup" title="Sslv2BypassServiceGroup">Sslv2BypassServiceGroup</a>: <i>String</i>
    <a href="#templatecipher" title="TemplateCipher">TemplateCipher</a>: <i>String</i>
    <a href="#templateciphershared" title="TemplateCipherShared">TemplateCipherShared</a>: <i>String</i>
    <a href="#templatehsm" title="TemplateHsm">TemplateHsm</a>: <i>String</i>
    <a href="#usernamelist" title="UserNameList">UserNameList</a>: <i>String</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#verifycertfailaction" title="VerifyCertFailAction">VerifyCertFailAction</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
    <a href="#bypasscertissuermulticlasslist" title="BypassCertIssuerMultiClassList">BypassCertIssuerMultiClassList</a>: <i>
      - <a href="bypasscertissuermulticlasslistdefinition.md">BypassCertIssuerMultiClassListDefinition</a></i>
    <a href="#bypasscertsanmulticlasslist" title="BypassCertSanMultiClassList">BypassCertSanMultiClassList</a>: <i>
      - <a href="bypasscertsanmulticlasslistdefinition.md">BypassCertSanMultiClassListDefinition</a></i>
    <a href="#bypasscertsubjectmulticlasslist" title="BypassCertSubjectMultiClassList">BypassCertSubjectMultiClassList</a>: <i>
      - <a href="bypasscertsubjectmulticlasslistdefinition.md">BypassCertSubjectMultiClassListDefinition</a></i>
    <a href="#cacerts" title="CaCerts">CaCerts</a>: <i>
      - <a href="cacertsdefinition.md">CaCertsDefinition</a></i>
    <a href="#certificateissuercontainslist" title="CertificateIssuerContainsList">CertificateIssuerContainsList</a>: <i>
      - <a href="certificateissuercontainslistdefinition.md">CertificateIssuerContainsListDefinition</a></i>
    <a href="#certificateissuerendswithlist" title="CertificateIssuerEndsWithList">CertificateIssuerEndsWithList</a>: <i>
      - <a href="certificateissuerendswithlistdefinition.md">CertificateIssuerEndsWithListDefinition</a></i>
    <a href="#certificateissuerequalslist" title="CertificateIssuerEqualsList">CertificateIssuerEqualsList</a>: <i>
      - <a href="certificateissuerequalslistdefinition.md">CertificateIssuerEqualsListDefinition</a></i>
    <a href="#certificateissuerstartswithlist" title="CertificateIssuerStartsWithList">CertificateIssuerStartsWithList</a>: <i>
      - <a href="certificateissuerstartswithlistdefinition.md">CertificateIssuerStartsWithListDefinition</a></i>
    <a href="#certificatelist" title="CertificateList">CertificateList</a>: <i>
      - <a href="certificatelistdefinition.md">CertificateListDefinition</a></i>
    <a href="#certificatesancontainslist" title="CertificateSanContainsList">CertificateSanContainsList</a>: <i>
      - <a href="certificatesancontainslistdefinition.md">CertificateSanContainsListDefinition</a></i>
    <a href="#certificatesanendswithlist" title="CertificateSanEndsWithList">CertificateSanEndsWithList</a>: <i>
      - <a href="certificatesanendswithlistdefinition.md">CertificateSanEndsWithListDefinition</a></i>
    <a href="#certificatesanequalslist" title="CertificateSanEqualsList">CertificateSanEqualsList</a>: <i>
      - <a href="certificatesanequalslistdefinition.md">CertificateSanEqualsListDefinition</a></i>
    <a href="#certificatesanstartswithlist" title="CertificateSanStartsWithList">CertificateSanStartsWithList</a>: <i>
      - <a href="certificatesanstartswithlistdefinition.md">CertificateSanStartsWithListDefinition</a></i>
    <a href="#certificatesubjectcontainslist" title="CertificateSubjectContainsList">CertificateSubjectContainsList</a>: <i>
      - <a href="certificatesubjectcontainslistdefinition.md">CertificateSubjectContainsListDefinition</a></i>
    <a href="#certificatesubjectendswithlist" title="CertificateSubjectEndsWithList">CertificateSubjectEndsWithList</a>: <i>
      - <a href="certificatesubjectendswithlistdefinition.md">CertificateSubjectEndsWithListDefinition</a></i>
    <a href="#certificatesubjectequalslist" title="CertificateSubjectEqualsList">CertificateSubjectEqualsList</a>: <i>
      - <a href="certificatesubjectequalslistdefinition.md">CertificateSubjectEqualsListDefinition</a></i>
    <a href="#certificatesubjectstartswithlist" title="CertificateSubjectStartsWithList">CertificateSubjectStartsWithList</a>: <i>
      - <a href="certificatesubjectstartswithlistdefinition.md">CertificateSubjectStartsWithListDefinition</a></i>
    <a href="#cipherwithoutpriolist" title="CipherWithoutPrioList">CipherWithoutPrioList</a>: <i>
      - <a href="cipherwithoutpriolistdefinition.md">CipherWithoutPrioListDefinition</a></i>
    <a href="#clientauthcontainslist" title="ClientAuthContainsList">ClientAuthContainsList</a>: <i>
      - <a href="clientauthcontainslistdefinition.md">ClientAuthContainsListDefinition</a></i>
    <a href="#clientauthendswithlist" title="ClientAuthEndsWithList">ClientAuthEndsWithList</a>: <i>
      - <a href="clientauthendswithlistdefinition.md">ClientAuthEndsWithListDefinition</a></i>
    <a href="#clientauthequalslist" title="ClientAuthEqualsList">ClientAuthEqualsList</a>: <i>
      - <a href="clientauthequalslistdefinition.md">ClientAuthEqualsListDefinition</a></i>
    <a href="#clientauthstartswithlist" title="ClientAuthStartsWithList">ClientAuthStartsWithList</a>: <i>
      - <a href="clientauthstartswithlistdefinition.md">ClientAuthStartsWithListDefinition</a></i>
    <a href="#containslist" title="ContainsList">ContainsList</a>: <i>
      - <a href="containslistdefinition.md">ContainsListDefinition</a></i>
    <a href="#crlcerts" title="CrlCerts">CrlCerts</a>: <i>
      - <a href="crlcertsdefinition.md">CrlCertsDefinition</a></i>
    <a href="#eclist" title="EcList">EcList</a>: <i>
      - <a href="eclistdefinition.md">EcListDefinition</a></i>
    <a href="#endswithlist" title="EndsWithList">EndsWithList</a>: <i>
      - <a href="endswithlistdefinition.md">EndsWithListDefinition</a></i>
    <a href="#equalslist" title="EqualsList">EqualsList</a>: <i>
      - <a href="equalslistdefinition.md">EqualsListDefinition</a></i>
    <a href="#exceptionwebcategory" title="ExceptionWebCategory">ExceptionWebCategory</a>: <i>
      - <a href="exceptionwebcategorydefinition.md">ExceptionWebCategoryDefinition</a></i>
    <a href="#exceptionwebreputation" title="ExceptionWebReputation">ExceptionWebReputation</a>: <i>
      - <a href="exceptionwebreputationdefinition.md">ExceptionWebReputationDefinition</a></i>
    <a href="#forwardproxytrustedcalists" title="ForwardProxyTrustedCaLists">ForwardProxyTrustedCaLists</a>: <i>
      - <a href="forwardproxytrustedcalistsdefinition.md">ForwardProxyTrustedCaListsDefinition</a></i>
    <a href="#multiclasslist" title="MultiClassList">MultiClassList</a>: <i>
      - <a href="multiclasslistdefinition.md">MultiClassListDefinition</a></i>
    <a href="#reqcalists" title="ReqCaLists">ReqCaLists</a>: <i>
      - <a href="reqcalistsdefinition.md">ReqCaListsDefinition</a></i>
    <a href="#servernamelist" title="ServerNameList">ServerNameList</a>: <i>
      - <a href="servernamelistdefinition.md">ServerNameListDefinition</a></i>
    <a href="#startswithlist" title="StartsWithList">StartsWithList</a>: <i>
      - <a href="startswithlistdefinition.md">StartsWithListDefinition</a></i>
    <a href="#webcategory" title="WebCategory">WebCategory</a>: <i>
      - <a href="webcategorydefinition.md">WebCategoryDefinition</a></i>
    <a href="#webreputation" title="WebReputation">WebReputation</a>: <i>
      - <a href="webreputationdefinition.md">WebReputationDefinition</a></i>
</pre>

## Properties

#### AdGroupList

Forward proxy bypass if ad-group matches class-list.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertType

‘fatal’: Log fatal alerts;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthSg

Specify authorization LDAP service group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthSgDn

Use Subject DN as LDAP search base DN.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthSgFilter

Specify LDAP search filter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthUsername

Specify the Username Field in the Client Certificate(If multi-fields are specificed, prior one has higher priority).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthUsernameAttribute

Specify attribute name of username for client SSL authorization.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthenName

Specify authorization LDAP server name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authorization

Specify LDAP server for client SSL authorizaiton.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BypassCertIssuerClassListName

Class List Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BypassCertSanClassListName

Class List Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BypassCertSubjectClassListName

Class List Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CachePersistenceListName

Class List Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaseInsensitive

Case insensitive forward proxy bypass.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cert

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertAltPartitionShared

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertAlternate

Specify the second certificate (Certificate Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertRevokeAction

‘bypass’: bypass SSLi processing; ‘continue’: continue the connection; ‘drop’: close the connection;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertSharedStr

Certificate Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertUnknownAction

‘bypass’: bypass SSLi processing; ‘continue’: continue the connection; ‘drop’: close the connection;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChainCert

Chain Certificate (Chain Certificate Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChainCertSharedStr

Chain Certificate Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassListName

Class List Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientAuthCaseInsensitive

Case insensitive forward proxy client auth bypass.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientAuthClassList

Forward proxy client auth bypass if SNI string matches class-list (Class List Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientCertificate

‘Ignore’: Don’t request client certificate; ‘Require’: Require client certificate; ‘Request’: Request client certificate;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloseNotify

Send close notification when terminate connection.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dgversion

Lower TLS/SSL version can be downgraded.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhType

‘1024’: 1024; ‘1024-dsa’: 1024-dsa; ‘2048’: 2048;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectClientServerAuth

Let backend server does SSL client authentication directly.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableSslv3

Reject Client requests for SSL version 3.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EarlyData

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableTlsAlertLogging

Enable TLS alert logging.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionAdGroupList

Exceptions to forward proxy bypass if ad-group matches class-list.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionCertificateIssuerClName

Exceptions to forward-proxy-bypass.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionCertificateSanClName

Exceptions to forward-proxy-bypass.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionCertificateSubjectClName

Exceptions to forward-proxy-bypass.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionSniClName

Exceptions to forward-proxy-bypass.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionUserNameList

Exceptions to forward proxy bypass if user-name matches class-list.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpireHours

Certificate lifetime in hours.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardEncrypted

Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardPassphrase

Password Phrase.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyAltSign

Forward proxy alternate signing cert and key.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyBlockMessage

Message to be included on the block page (Message, enclose in quotes if spaces are present).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyCaCert

CA Certificate for forward proxy (SSL forward proxy CA Certificate Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyCaKey

CA Private Key for forward proxy (SSL forward proxy CA Key Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyCertCacheLimit

Certificate cache size limit, default is 524288 (set to 0 for unlimited size).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyCertCacheTimeout

Certificate cache timeout, default is 1 hour (seconds, set to 0 for never timeout).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyCertExpiry

Adjust certificate expiry relative to the time when it is created on the device.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyCertNotReadyAction

‘bypass’: bypass the connection; ‘reset’: reset the connection;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyCertRevokeAction

Action taken if a certificate is irreversibly revoked, bypass SSLi processing by default.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyCertUnknownAction

Action taken if a certificate revocation status is unknown, bypass SSLi processing by default.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyCrlDisable

Disable Certificate Revocation List checking for forward proxy.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyDecryptedDscp

Apply a DSCP to decrypted and bypassed traffic (DSCP to apply to decrypted traffic).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyDecryptedDscpBypass

DSCP to apply to bypassed traffic.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyEnable

Enable SSL forward proxy.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyFailsafeDisable

Disable Failsafe for SSL forward proxy.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyLogDisable

Disable SSL forward proxy logging.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyNoSharedCipherAction

Action taken if handshake fails due to no shared ciper, close the connection by default.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyNoSniAction

‘intercept’: intercept in no SNI case; ‘bypass’: bypass in no SNI case; ‘reset’: reset in no SNI case;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyOcspDisable

Disable ocsp-stapling for forward proxy.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyRequireSniCertMatched

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxySelfsignRedir

Redirect connections to pages with self signed certs to a warning page.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxySslVersion

TLS/SSL version, default is TLS1.2 (TLS/SSL version: 31-TLSv1.0, 32-TLSv1.1 and 33-TLSv1.2).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyVerifyCertFailAction

Action taken if certificate verification fails, close the connection by default.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FpAltCert

CA Certificate for forward proxy alternate signing (Certificate name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FpAltEncrypted

Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FpAltKey

CA Private Key for forward proxy alternate signing (Key name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FpAltPassphrase

Password Phrase.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FpAltShared

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FpCaKeyShared

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FpCaShared

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FpCertExtAiaCaIssuers

CA Issuers (Authority Information Access URI).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FpCertExtAiaOcsp

OCSP (Authority Information Access URI).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FpCertExtCrldp

CRL Distribution Point (CRL Distribution Point URI).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FpCertFetchAutonat

‘auto’: Configure auto NAT for server certificate fetching;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FpCertFetchAutonatPrecedence

Set this NAT pool as higher precedence than other source NAT like configued under template policy.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FpCertFetchNatpoolName

Specify NAT pool or pool group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FpCertFetchNatpoolNameShared

Specify NAT pool or pool group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FpCertFetchNatpoolPrecedence

Set this NAT pool as higher precedence than other source NAT like configued under template policy.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HandshakeLoggingEnable

Enable SSL handshake logging.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HsmType

‘thales-embed’: Thales embed key; ‘thales-hwcrhk’: Thales hwcrhk Key;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InspectCertificateIssuerClName

Forward proxy Inspect if Certificate issuer matches class-list.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InspectCertificateSanClName

Forward proxy Inspect if Certificate Subject Alternative Name matches class-list.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InspectCertificateSubjectClName

Forward proxy Inspect if Certificate Subject matches class-list.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InspectListName

Class List Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyAltEncrypted

Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyAltPartitionShared

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyAltPassphrase

Password Phrase.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyAlternate

Specify the second private key (Key Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyEncrypted

Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyPassphrase

Password Phrase.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeySharedEncrypted

Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeySharedPassphrase

Password Phrase.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeySharedStr

Key Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LdapBaseDnFromCert

Use Subject DN as LDAP search base DN.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LdapSearchFilter

Specify LDAP search filter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalLogging

Enable local logging.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Client SSL Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoAntiReplay

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoSharedCipherAction

‘bypass’: bypass SSLi processing; ‘drop’: close the connection;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NonSslBypassL4session

Handle the non-ssl session as L4 for performance optimization.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NonSslBypassServiceGroup

Service Group for Bypass non-ssl traffic (Service Group Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notafter

notAfter date.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notafterday

Day.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notaftermonth

Month.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notafteryear

Year.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notbefore

notBefore date.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notbeforeday

Day.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notbeforemonth

Month.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notbeforeyear

Year.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OcspStapling

Config OCSP stapling support.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OcspstCaCert

CA certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OcspstOcsp

Specify OCSP Authentication.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OcspstSg

Specify authentication service group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OcspstSgDays

Specify update period, in days.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OcspstSgHours

Specify update period, in hours.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OcspstSgMinutes

Specify update period, in minutes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OcspstSgTimeout

Specify retry timeout (Default is 30 mins).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OcspstSrvr

Specify OCSP authentication server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OcspstSrvrDays

Specify update period, in days.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OcspstSrvrHours

Specify update period, in hours.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OcspstSrvrMinutes

Specify update period, in minutes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OcspstSrvrTimeout

Specify retry timeout (Default is 30 mins).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RenegotiationDisable

Disable SSL renegotiation.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireWebCategory

Wait for web category to be resolved before taking bypass decision.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerNameAutoMap

Enable automatic mapping of server name indication in Client hello extension.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionCacheSize

Session Cache Size (Specify 0 to disable Session ID reuse.).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionCacheTimeout

Session Cache Timeout (Timeout value, in seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionTicketDisable

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionTicketLifetime

Session ticket lieftime in seconds from stateless session resumption (Lifetime value in seconds).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionCipherTemplate

Reference a cipher template from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedPartitionPool

Reference a NAT pool or pool group from shared partition.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SniEnableLog

Enable logging of sni-auto-map failures. Disable by default.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslFalseStartDisable

disable SSL False Start.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SsliLogging

SSLi logging level, default is error logging only.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sslilogging

‘disable’: Disable all logging; ‘all’: enable all logging(error, info);.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sslv2BypassServiceGroup

Service Group for Bypass SSLV2 (Service Group Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateCipher

Cipher Template (Cipher Config Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateCipherShared

Cipher Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateHsm

HSM Template (HSM Template Name).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserNameList

Forward proxy bypass if user-name matches class-list.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerifyCertFailAction

‘bypass’: bypass SSLi processing; ‘continue’: continue the connection; ‘drop’: close the connection;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

TLS/SSL version, default is the highest number supported (TLS/SSL version: 30-SSLv3.0, 31-TLSv1.0, 32-TLSv1.1 and 33-TLSv1.2).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BypassCertIssuerMultiClassList

_Required_: No

_Type_: List of <a href="bypasscertissuermulticlasslistdefinition.md">BypassCertIssuerMultiClassListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BypassCertSanMultiClassList

_Required_: No

_Type_: List of <a href="bypasscertsanmulticlasslistdefinition.md">BypassCertSanMultiClassListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BypassCertSubjectMultiClassList

_Required_: No

_Type_: List of <a href="bypasscertsubjectmulticlasslistdefinition.md">BypassCertSubjectMultiClassListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaCerts

_Required_: No

_Type_: List of <a href="cacertsdefinition.md">CaCertsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateIssuerContainsList

_Required_: No

_Type_: List of <a href="certificateissuercontainslistdefinition.md">CertificateIssuerContainsListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateIssuerEndsWithList

_Required_: No

_Type_: List of <a href="certificateissuerendswithlistdefinition.md">CertificateIssuerEndsWithListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateIssuerEqualsList

_Required_: No

_Type_: List of <a href="certificateissuerequalslistdefinition.md">CertificateIssuerEqualsListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateIssuerStartsWithList

_Required_: No

_Type_: List of <a href="certificateissuerstartswithlistdefinition.md">CertificateIssuerStartsWithListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateList

_Required_: No

_Type_: List of <a href="certificatelistdefinition.md">CertificateListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateSanContainsList

_Required_: No

_Type_: List of <a href="certificatesancontainslistdefinition.md">CertificateSanContainsListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateSanEndsWithList

_Required_: No

_Type_: List of <a href="certificatesanendswithlistdefinition.md">CertificateSanEndsWithListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateSanEqualsList

_Required_: No

_Type_: List of <a href="certificatesanequalslistdefinition.md">CertificateSanEqualsListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateSanStartsWithList

_Required_: No

_Type_: List of <a href="certificatesanstartswithlistdefinition.md">CertificateSanStartsWithListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateSubjectContainsList

_Required_: No

_Type_: List of <a href="certificatesubjectcontainslistdefinition.md">CertificateSubjectContainsListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateSubjectEndsWithList

_Required_: No

_Type_: List of <a href="certificatesubjectendswithlistdefinition.md">CertificateSubjectEndsWithListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateSubjectEqualsList

_Required_: No

_Type_: List of <a href="certificatesubjectequalslistdefinition.md">CertificateSubjectEqualsListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateSubjectStartsWithList

_Required_: No

_Type_: List of <a href="certificatesubjectstartswithlistdefinition.md">CertificateSubjectStartsWithListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CipherWithoutPrioList

_Required_: No

_Type_: List of <a href="cipherwithoutpriolistdefinition.md">CipherWithoutPrioListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientAuthContainsList

_Required_: No

_Type_: List of <a href="clientauthcontainslistdefinition.md">ClientAuthContainsListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientAuthEndsWithList

_Required_: No

_Type_: List of <a href="clientauthendswithlistdefinition.md">ClientAuthEndsWithListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientAuthEqualsList

_Required_: No

_Type_: List of <a href="clientauthequalslistdefinition.md">ClientAuthEqualsListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientAuthStartsWithList

_Required_: No

_Type_: List of <a href="clientauthstartswithlistdefinition.md">ClientAuthStartsWithListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainsList

_Required_: No

_Type_: List of <a href="containslistdefinition.md">ContainsListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrlCerts

_Required_: No

_Type_: List of <a href="crlcertsdefinition.md">CrlCertsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EcList

_Required_: No

_Type_: List of <a href="eclistdefinition.md">EcListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndsWithList

_Required_: No

_Type_: List of <a href="endswithlistdefinition.md">EndsWithListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EqualsList

_Required_: No

_Type_: List of <a href="equalslistdefinition.md">EqualsListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionWebCategory

_Required_: No

_Type_: List of <a href="exceptionwebcategorydefinition.md">ExceptionWebCategoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExceptionWebReputation

_Required_: No

_Type_: List of <a href="exceptionwebreputationdefinition.md">ExceptionWebReputationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardProxyTrustedCaLists

_Required_: No

_Type_: List of <a href="forwardproxytrustedcalistsdefinition.md">ForwardProxyTrustedCaListsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MultiClassList

_Required_: No

_Type_: List of <a href="multiclasslistdefinition.md">MultiClassListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReqCaLists

_Required_: No

_Type_: List of <a href="reqcalistsdefinition.md">ReqCaListsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerNameList

_Required_: No

_Type_: List of <a href="servernamelistdefinition.md">ServerNameListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartsWithList

_Required_: No

_Type_: List of <a href="startswithlistdefinition.md">StartsWithListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebCategory

_Required_: No

_Type_: List of <a href="webcategorydefinition.md">WebCategoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebReputation

_Required_: No

_Type_: List of <a href="webreputationdefinition.md">WebReputationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.


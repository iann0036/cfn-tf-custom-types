# TF::Thunder::Import

`thunder_import` Provides details about thunder import

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::Import",
    "Properties" : {
        "<a href="#aflex" title="Aflex">Aflex</a>" : <i>String</i>,
        "<a href="#authjwks" title="AuthJwks">AuthJwks</a>" : <i>String</i>,
        "<a href="#authportal" title="AuthPortal">AuthPortal</a>" : <i>String</i>,
        "<a href="#authportalimage" title="AuthPortalImage">AuthPortalImage</a>" : <i>String</i>,
        "<a href="#bwlist" title="BwList">BwList</a>" : <i>String</i>,
        "<a href="#cacert" title="CaCert">CaCert</a>" : <i>String</i>,
        "<a href="#certificatetype" title="CertificateType">CertificateType</a>" : <i>String</i>,
        "<a href="#classlist" title="ClassList">ClassList</a>" : <i>String</i>,
        "<a href="#classlistconvert" title="ClassListConvert">ClassListConvert</a>" : <i>String</i>,
        "<a href="#classlisttype" title="ClassListType">ClassListType</a>" : <i>String</i>,
        "<a href="#cloudconfig" title="CloudConfig">CloudConfig</a>" : <i>String</i>,
        "<a href="#cloudcreds" title="CloudCreds">CloudCreds</a>" : <i>String</i>,
        "<a href="#dnssecdnskey" title="DnssecDnskey">DnssecDnskey</a>" : <i>String</i>,
        "<a href="#dnssecds" title="DnssecDs">DnssecDs</a>" : <i>String</i>,
        "<a href="#fileinspectionbwlist" title="FileInspectionBwList">FileInspectionBwList</a>" : <i>String</i>,
        "<a href="#geolocation" title="GeoLocation">GeoLocation</a>" : <i>String</i>,
        "<a href="#glmcert" title="GlmCert">GlmCert</a>" : <i>String</i>,
        "<a href="#glmlicense" title="GlmLicense">GlmLicense</a>" : <i>String</i>,
        "<a href="#ipmaplist" title="IpMapList">IpMapList</a>" : <i>String</i>,
        "<a href="#localurifile" title="LocalUriFile">LocalUriFile</a>" : <i>String</i>,
        "<a href="#lw4o6" title="Lw4o6">Lw4o6</a>" : <i>String</i>,
        "<a href="#overwrite" title="Overwrite">Overwrite</a>" : <i>Double</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#pfxpassword" title="PfxPassword">PfxPassword</a>" : <i>String</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#remotefile" title="RemoteFile">RemoteFile</a>" : <i>String</i>,
        "<a href="#secured" title="Secured">Secured</a>" : <i>Double</i>,
        "<a href="#sslcert" title="SslCert">SslCert</a>" : <i>String</i>,
        "<a href="#sslcertkey" title="SslCertKey">SslCertKey</a>" : <i>String</i>,
        "<a href="#sslcrl" title="SslCrl">SslCrl</a>" : <i>String</i>,
        "<a href="#sslkey" title="SslKey">SslKey</a>" : <i>String</i>,
        "<a href="#storename" title="StoreName">StoreName</a>" : <i>String</i>,
        "<a href="#terminal" title="Terminal">Terminal</a>" : <i>Double</i>,
        "<a href="#thaleskmdata" title="ThalesKmdata">ThalesKmdata</a>" : <i>String</i>,
        "<a href="#thalessecworld" title="ThalesSecworld">ThalesSecworld</a>" : <i>String</i>,
        "<a href="#usblicense" title="UsbLicense">UsbLicense</a>" : <i>String</i>,
        "<a href="#usemgmtport" title="UseMgmtPort">UseMgmtPort</a>" : <i>Double</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#webcategorylicense" title="WebCategoryLicense">WebCategoryLicense</a>" : <i>String</i>,
        "<a href="#wsdl" title="Wsdl">Wsdl</a>" : <i>String</i>,
        "<a href="#xmlschema" title="XmlSchema">XmlSchema</a>" : <i>String</i>,
        "<a href="#authsamlidp" title="AuthSamlIdp">AuthSamlIdp</a>" : <i>[ <a href="authsamlidpdefinition.md">AuthSamlIdpDefinition</a>, ... ]</i>,
        "<a href="#healthexternal" title="HealthExternal">HealthExternal</a>" : <i>[ <a href="healthexternaldefinition.md">HealthExternalDefinition</a>, ... ]</i>,
        "<a href="#healthpostfile" title="HealthPostfile">HealthPostfile</a>" : <i>[ <a href="healthpostfiledefinition.md">HealthPostfileDefinition</a>, ... ]</i>,
        "<a href="#store" title="Store">Store</a>" : <i>[ <a href="storedefinition.md">StoreDefinition</a>, ... ]</i>,
        "<a href="#todevice" title="ToDevice">ToDevice</a>" : <i>[ <a href="todevicedefinition.md">ToDeviceDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::Import
Properties:
    <a href="#aflex" title="Aflex">Aflex</a>: <i>String</i>
    <a href="#authjwks" title="AuthJwks">AuthJwks</a>: <i>String</i>
    <a href="#authportal" title="AuthPortal">AuthPortal</a>: <i>String</i>
    <a href="#authportalimage" title="AuthPortalImage">AuthPortalImage</a>: <i>String</i>
    <a href="#bwlist" title="BwList">BwList</a>: <i>String</i>
    <a href="#cacert" title="CaCert">CaCert</a>: <i>String</i>
    <a href="#certificatetype" title="CertificateType">CertificateType</a>: <i>String</i>
    <a href="#classlist" title="ClassList">ClassList</a>: <i>String</i>
    <a href="#classlistconvert" title="ClassListConvert">ClassListConvert</a>: <i>String</i>
    <a href="#classlisttype" title="ClassListType">ClassListType</a>: <i>String</i>
    <a href="#cloudconfig" title="CloudConfig">CloudConfig</a>: <i>String</i>
    <a href="#cloudcreds" title="CloudCreds">CloudCreds</a>: <i>String</i>
    <a href="#dnssecdnskey" title="DnssecDnskey">DnssecDnskey</a>: <i>String</i>
    <a href="#dnssecds" title="DnssecDs">DnssecDs</a>: <i>String</i>
    <a href="#fileinspectionbwlist" title="FileInspectionBwList">FileInspectionBwList</a>: <i>String</i>
    <a href="#geolocation" title="GeoLocation">GeoLocation</a>: <i>String</i>
    <a href="#glmcert" title="GlmCert">GlmCert</a>: <i>String</i>
    <a href="#glmlicense" title="GlmLicense">GlmLicense</a>: <i>String</i>
    <a href="#ipmaplist" title="IpMapList">IpMapList</a>: <i>String</i>
    <a href="#localurifile" title="LocalUriFile">LocalUriFile</a>: <i>String</i>
    <a href="#lw4o6" title="Lw4o6">Lw4o6</a>: <i>String</i>
    <a href="#overwrite" title="Overwrite">Overwrite</a>: <i>Double</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#pfxpassword" title="PfxPassword">PfxPassword</a>: <i>String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#remotefile" title="RemoteFile">RemoteFile</a>: <i>String</i>
    <a href="#secured" title="Secured">Secured</a>: <i>Double</i>
    <a href="#sslcert" title="SslCert">SslCert</a>: <i>String</i>
    <a href="#sslcertkey" title="SslCertKey">SslCertKey</a>: <i>String</i>
    <a href="#sslcrl" title="SslCrl">SslCrl</a>: <i>String</i>
    <a href="#sslkey" title="SslKey">SslKey</a>: <i>String</i>
    <a href="#storename" title="StoreName">StoreName</a>: <i>String</i>
    <a href="#terminal" title="Terminal">Terminal</a>: <i>Double</i>
    <a href="#thaleskmdata" title="ThalesKmdata">ThalesKmdata</a>: <i>String</i>
    <a href="#thalessecworld" title="ThalesSecworld">ThalesSecworld</a>: <i>String</i>
    <a href="#usblicense" title="UsbLicense">UsbLicense</a>: <i>String</i>
    <a href="#usemgmtport" title="UseMgmtPort">UseMgmtPort</a>: <i>Double</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#webcategorylicense" title="WebCategoryLicense">WebCategoryLicense</a>: <i>String</i>
    <a href="#wsdl" title="Wsdl">Wsdl</a>: <i>String</i>
    <a href="#xmlschema" title="XmlSchema">XmlSchema</a>: <i>String</i>
    <a href="#authsamlidp" title="AuthSamlIdp">AuthSamlIdp</a>: <i>
      - <a href="authsamlidpdefinition.md">AuthSamlIdpDefinition</a></i>
    <a href="#healthexternal" title="HealthExternal">HealthExternal</a>: <i>
      - <a href="healthexternaldefinition.md">HealthExternalDefinition</a></i>
    <a href="#healthpostfile" title="HealthPostfile">HealthPostfile</a>: <i>
      - <a href="healthpostfiledefinition.md">HealthPostfileDefinition</a></i>
    <a href="#store" title="Store">Store</a>: <i>
      - <a href="storedefinition.md">StoreDefinition</a></i>
    <a href="#todevice" title="ToDevice">ToDevice</a>: <i>
      - <a href="todevicedefinition.md">ToDeviceDefinition</a></i>
</pre>

## Properties

#### Aflex

aFleX Script Source File.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthJwks

JSON web key.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthPortal

Portal file for http authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthPortalImage

Image file for default portal.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BwList

Black white List File.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaCert

CA Cert File(enter bulk when import an archive file).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateType

‘pem’: pem; ‘der’: der; ‘pfx’: pfx; ‘p7b’: p7b;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassList

Class List File.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassListConvert

Convert Class List File to A10 format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassListType

‘ac’: ac; ‘ipv4’: ipv4; ‘ipv6’: ipv6; ‘string’: string; ‘string-case-insensitive’: string-case-insensitive;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudConfig

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudCreds

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnssecDnskey

DNSSEC DNSKEY(KSK) file for child zone.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnssecDs

DNSSEC DS file for child zone.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileInspectionBwList

Black white List File.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GeoLocation

Geo-location CSV File.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlmCert

GLM certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlmLicense

License File.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpMapList

IP Map List File.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalUriFile

Local URI files for http response.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lw4o6

LW-4over6 Binding Table File.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Overwrite

Overwrite existing file.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

password for the remote site.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PfxPassword

The password for certificate file (pfx type only).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

WAF policy File.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteFile

Profile name for remote url.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Secured

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCert

SSL Cert File(enter bulk when import an archive file).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCertKey

‘bulk’: import an archive file;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCrl

SSL Crl File.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslKey

SSL Key File(enter bulk when import an archive file).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StoreName

Import store name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Terminal

terminal vi.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThalesKmdata

Thales Kmdata files.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThalesSecworld

Thales security world files.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsbLicense

USB License File.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseMgmtPort

Use management port as source port.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebCategoryLicense

License file to enable web-category feature.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Wsdl

Web Service Definition Language File.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### XmlSchema

XML-Schema File.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthSamlIdp

_Required_: No

_Type_: List of <a href="authsamlidpdefinition.md">AuthSamlIdpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthExternal

_Required_: No

_Type_: List of <a href="healthexternaldefinition.md">HealthExternalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthPostfile

_Required_: No

_Type_: List of <a href="healthpostfiledefinition.md">HealthPostfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Store

_Required_: No

_Type_: List of <a href="storedefinition.md">StoreDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ToDevice

_Required_: No

_Type_: List of <a href="todevicedefinition.md">ToDeviceDefinition</a>

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


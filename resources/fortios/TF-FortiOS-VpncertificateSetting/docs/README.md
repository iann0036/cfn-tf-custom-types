# TF::FortiOS::VpncertificateSetting

VPN certificate setting.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::VpncertificateSetting",
    "Properties" : {
        "<a href="#certnamedsa1024" title="CertnameDsa1024">CertnameDsa1024</a>" : <i>String</i>,
        "<a href="#certnamedsa2048" title="CertnameDsa2048">CertnameDsa2048</a>" : <i>String</i>,
        "<a href="#certnameecdsa256" title="CertnameEcdsa256">CertnameEcdsa256</a>" : <i>String</i>,
        "<a href="#certnameecdsa384" title="CertnameEcdsa384">CertnameEcdsa384</a>" : <i>String</i>,
        "<a href="#certnameecdsa521" title="CertnameEcdsa521">CertnameEcdsa521</a>" : <i>String</i>,
        "<a href="#certnameed25519" title="CertnameEd25519">CertnameEd25519</a>" : <i>String</i>,
        "<a href="#certnameed448" title="CertnameEd448">CertnameEd448</a>" : <i>String</i>,
        "<a href="#certnamersa1024" title="CertnameRsa1024">CertnameRsa1024</a>" : <i>String</i>,
        "<a href="#certnamersa2048" title="CertnameRsa2048">CertnameRsa2048</a>" : <i>String</i>,
        "<a href="#certnamersa4096" title="CertnameRsa4096">CertnameRsa4096</a>" : <i>String</i>,
        "<a href="#checkcacert" title="CheckCaCert">CheckCaCert</a>" : <i>String</i>,
        "<a href="#checkcachain" title="CheckCaChain">CheckCaChain</a>" : <i>String</i>,
        "<a href="#cmpkeyusagechecking" title="CmpKeyUsageChecking">CmpKeyUsageChecking</a>" : <i>String</i>,
        "<a href="#cmpsaveextracerts" title="CmpSaveExtraCerts">CmpSaveExtraCerts</a>" : <i>String</i>,
        "<a href="#cnmatch" title="CnMatch">CnMatch</a>" : <i>String</i>,
        "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
        "<a href="#interfaceselectmethod" title="InterfaceSelectMethod">InterfaceSelectMethod</a>" : <i>String</i>,
        "<a href="#ocspdefaultserver" title="OcspDefaultServer">OcspDefaultServer</a>" : <i>String</i>,
        "<a href="#ocspoption" title="OcspOption">OcspOption</a>" : <i>String</i>,
        "<a href="#ocspstatus" title="OcspStatus">OcspStatus</a>" : <i>String</i>,
        "<a href="#sslminprotoversion" title="SslMinProtoVersion">SslMinProtoVersion</a>" : <i>String</i>,
        "<a href="#sslocspsourceip" title="SslOcspSourceIp">SslOcspSourceIp</a>" : <i>String</i>,
        "<a href="#strictcrlcheck" title="StrictCrlCheck">StrictCrlCheck</a>" : <i>String</i>,
        "<a href="#strictocspcheck" title="StrictOcspCheck">StrictOcspCheck</a>" : <i>String</i>,
        "<a href="#subjectmatch" title="SubjectMatch">SubjectMatch</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::VpncertificateSetting
Properties:
    <a href="#certnamedsa1024" title="CertnameDsa1024">CertnameDsa1024</a>: <i>String</i>
    <a href="#certnamedsa2048" title="CertnameDsa2048">CertnameDsa2048</a>: <i>String</i>
    <a href="#certnameecdsa256" title="CertnameEcdsa256">CertnameEcdsa256</a>: <i>String</i>
    <a href="#certnameecdsa384" title="CertnameEcdsa384">CertnameEcdsa384</a>: <i>String</i>
    <a href="#certnameecdsa521" title="CertnameEcdsa521">CertnameEcdsa521</a>: <i>String</i>
    <a href="#certnameed25519" title="CertnameEd25519">CertnameEd25519</a>: <i>String</i>
    <a href="#certnameed448" title="CertnameEd448">CertnameEd448</a>: <i>String</i>
    <a href="#certnamersa1024" title="CertnameRsa1024">CertnameRsa1024</a>: <i>String</i>
    <a href="#certnamersa2048" title="CertnameRsa2048">CertnameRsa2048</a>: <i>String</i>
    <a href="#certnamersa4096" title="CertnameRsa4096">CertnameRsa4096</a>: <i>String</i>
    <a href="#checkcacert" title="CheckCaCert">CheckCaCert</a>: <i>String</i>
    <a href="#checkcachain" title="CheckCaChain">CheckCaChain</a>: <i>String</i>
    <a href="#cmpkeyusagechecking" title="CmpKeyUsageChecking">CmpKeyUsageChecking</a>: <i>String</i>
    <a href="#cmpsaveextracerts" title="CmpSaveExtraCerts">CmpSaveExtraCerts</a>: <i>String</i>
    <a href="#cnmatch" title="CnMatch">CnMatch</a>: <i>String</i>
    <a href="#interface" title="Interface">Interface</a>: <i>String</i>
    <a href="#interfaceselectmethod" title="InterfaceSelectMethod">InterfaceSelectMethod</a>: <i>String</i>
    <a href="#ocspdefaultserver" title="OcspDefaultServer">OcspDefaultServer</a>: <i>String</i>
    <a href="#ocspoption" title="OcspOption">OcspOption</a>: <i>String</i>
    <a href="#ocspstatus" title="OcspStatus">OcspStatus</a>: <i>String</i>
    <a href="#sslminprotoversion" title="SslMinProtoVersion">SslMinProtoVersion</a>: <i>String</i>
    <a href="#sslocspsourceip" title="SslOcspSourceIp">SslOcspSourceIp</a>: <i>String</i>
    <a href="#strictcrlcheck" title="StrictCrlCheck">StrictCrlCheck</a>: <i>String</i>
    <a href="#strictocspcheck" title="StrictOcspCheck">StrictOcspCheck</a>: <i>String</i>
    <a href="#subjectmatch" title="SubjectMatch">SubjectMatch</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### CertnameDsa1024

1024 bit DSA key certificate for re-signing server certificates for SSL inspection.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertnameDsa2048

2048 bit DSA key certificate for re-signing server certificates for SSL inspection.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertnameEcdsa256

256 bit ECDSA key certificate for re-signing server certificates for SSL inspection.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertnameEcdsa384

384 bit ECDSA key certificate for re-signing server certificates for SSL inspection.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertnameEcdsa521

521 bit ECDSA key certificate for re-signing server certificates for SSL inspection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertnameEd25519

253 bit EdDSA key certificate for re-signing server certificates for SSL inspection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertnameEd448

456 bit EdDSA key certificate for re-signing server certificates for SSL inspection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertnameRsa1024

1024 bit RSA key certificate for re-signing server certificates for SSL inspection.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertnameRsa2048

2048 bit RSA key certificate for re-signing server certificates for SSL inspection.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertnameRsa4096

4096 bit RSA key certificate for re-signing server certificates for SSL inspection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckCaCert

Enable/disable verification of the user certificate and pass authentication if any CA in the chain is trusted (default = enable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckCaChain

Enable/disable verification of the entire certificate chain and pass authentication only if the chain is complete and all of the CAs in the chain are trusted (default = disable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CmpKeyUsageChecking

Enable/disable server certificate key usage checking in CMP mode (default = enable). Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CmpSaveExtraCerts

Enable/disable saving extra certificates in CMP mode. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CnMatch

When searching for a matching certificate, control how to find matches in the cn attribute of the certificate subject name. Valid values: `substring`, `value`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

Specify outgoing interface to reach server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceSelectMethod

Specify how to select outgoing interface to reach server. Valid values: `auto`, `sdwan`, `specify`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OcspDefaultServer

Default OCSP server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OcspOption

Specify whether the OCSP URL is from certificate or configured OCSP server. Valid values: `certificate`, `server`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OcspStatus

Enable/disable receiving certificates using the OCSP. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslMinProtoVersion

Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting). Valid values: `default`, `SSLv3`, `TLSv1`, `TLSv1-1`, `TLSv1-2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslOcspSourceIp

Source IP address to use to communicate with the OCSP server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StrictCrlCheck

Enable/disable strict mode CRL checking. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StrictOcspCheck

Enable/disable strict mode OCSP checking. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubjectMatch

When searching for a matching certificate, control how to find matches in the certificate subject name. Valid values: `substring`, `value`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

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


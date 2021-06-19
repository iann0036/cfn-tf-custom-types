# TF::FortiOS::VpncertificateLocal

Local keys and certificates.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::VpncertificateLocal",
    "Properties" : {
        "<a href="#autoregeneratedays" title="AutoRegenerateDays">AutoRegenerateDays</a>" : <i>Double</i>,
        "<a href="#autoregeneratedayswarning" title="AutoRegenerateDaysWarning">AutoRegenerateDaysWarning</a>" : <i>Double</i>,
        "<a href="#caidentifier" title="CaIdentifier">CaIdentifier</a>" : <i>String</i>,
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>String</i>,
        "<a href="#cmppath" title="CmpPath">CmpPath</a>" : <i>String</i>,
        "<a href="#cmpregenerationmethod" title="CmpRegenerationMethod">CmpRegenerationMethod</a>" : <i>String</i>,
        "<a href="#cmpserver" title="CmpServer">CmpServer</a>" : <i>String</i>,
        "<a href="#cmpservercert" title="CmpServerCert">CmpServerCert</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#csr" title="Csr">Csr</a>" : <i>String</i>,
        "<a href="#enrollprotocol" title="EnrollProtocol">EnrollProtocol</a>" : <i>String</i>,
        "<a href="#ikelocalid" title="IkeLocalid">IkeLocalid</a>" : <i>String</i>,
        "<a href="#ikelocalidtype" title="IkeLocalidType">IkeLocalidType</a>" : <i>String</i>,
        "<a href="#lastupdated" title="LastUpdated">LastUpdated</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameencoding" title="NameEncoding">NameEncoding</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#privatekey" title="PrivateKey">PrivateKey</a>" : <i>String</i>,
        "<a href="#range" title="Range">Range</a>" : <i>String</i>,
        "<a href="#sceppassword" title="ScepPassword">ScepPassword</a>" : <i>String</i>,
        "<a href="#scepurl" title="ScepUrl">ScepUrl</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
        "<a href="#sourceip" title="SourceIp">SourceIp</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::VpncertificateLocal
Properties:
    <a href="#autoregeneratedays" title="AutoRegenerateDays">AutoRegenerateDays</a>: <i>Double</i>
    <a href="#autoregeneratedayswarning" title="AutoRegenerateDaysWarning">AutoRegenerateDaysWarning</a>: <i>Double</i>
    <a href="#caidentifier" title="CaIdentifier">CaIdentifier</a>: <i>String</i>
    <a href="#certificate" title="Certificate">Certificate</a>: <i>String</i>
    <a href="#cmppath" title="CmpPath">CmpPath</a>: <i>String</i>
    <a href="#cmpregenerationmethod" title="CmpRegenerationMethod">CmpRegenerationMethod</a>: <i>String</i>
    <a href="#cmpserver" title="CmpServer">CmpServer</a>: <i>String</i>
    <a href="#cmpservercert" title="CmpServerCert">CmpServerCert</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#csr" title="Csr">Csr</a>: <i>String</i>
    <a href="#enrollprotocol" title="EnrollProtocol">EnrollProtocol</a>: <i>String</i>
    <a href="#ikelocalid" title="IkeLocalid">IkeLocalid</a>: <i>String</i>
    <a href="#ikelocalidtype" title="IkeLocalidType">IkeLocalidType</a>: <i>String</i>
    <a href="#lastupdated" title="LastUpdated">LastUpdated</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameencoding" title="NameEncoding">NameEncoding</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#privatekey" title="PrivateKey">PrivateKey</a>: <i>String</i>
    <a href="#range" title="Range">Range</a>: <i>String</i>
    <a href="#sceppassword" title="ScepPassword">ScepPassword</a>: <i>String</i>
    <a href="#scepurl" title="ScepUrl">ScepUrl</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
    <a href="#sourceip" title="SourceIp">SourceIp</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### AutoRegenerateDays

Number of days to wait before expiry of an updated local certificate is requested (0 = disabled).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoRegenerateDaysWarning

Number of days to wait before an expiry warning message is generated (0 = disabled).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaIdentifier

CA identifier of the CA server for signing via SCEP.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

PEM format certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CmpPath

Path location inside CMP server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CmpRegenerationMethod

CMP auto-regeneration method. Valid values: `keyupate`, `renewal`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CmpServer

'ADDRESS:PORT' for CMP server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CmpServerCert

CMP server certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Csr

Certificate Signing Request.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnrollProtocol

Certificate enrollment protocol. Valid values: `none`, `scep`, `cmpv2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeLocalid

Local ID the FortiGate uses for authentication as a VPN client.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeLocalidType

IKE local ID type. Valid values: `asn1dn`, `fqdn`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastUpdated

Time at which certificate was last updated.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameEncoding

Name encoding method for auto-regeneration. Valid values: `printable`, `utf8`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Password as a PEM file.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKey

PEM format key, encrypted with a password.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Range

Either a global or VDOM IP address range for the certificate. Valid values: `global`, `vdom`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScepPassword

SCEP server challenge password for auto-regeneration.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScepUrl

SCEP server URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

Certificate source type.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

Source IP address for communications to the SCEP server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

Certificate Signing Request State.

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


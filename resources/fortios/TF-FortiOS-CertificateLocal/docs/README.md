# TF::FortiOS::CertificateLocal

Local keys and certificates.

Due to the limitations of the current system, the feature is temporarily unavailable. Please use the following resource configuration as an alternative.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::CertificateLocal",
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
Type: TF::FortiOS::CertificateLocal
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

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoRegenerateDaysWarning

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaIdentifier

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CmpPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CmpRegenerationMethod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CmpServer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CmpServerCert

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Csr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnrollProtocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeLocalid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeLocalidType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastUpdated

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameEncoding

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Range

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScepPassword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScepUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

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


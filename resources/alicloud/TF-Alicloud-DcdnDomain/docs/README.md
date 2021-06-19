# TF::Alicloud::DcdnDomain

You can use DCDN to improve the overall performance of your website and accelerate content delivery to improve user experience. For information about Alicloud DCDN Domain and how to use it, see [What is Resource Alicloud DCDN Domain](https://www.alibabacloud.com/help/en/doc-detail/130628.htm).

-> **NOTE:** Available in v1.94.0+.

-> **NOTE:** You must activate the Dynamic Route for CDN (DCDN) service before you create an accelerated domain.

-> **NOTE:** Make sure that you have obtained an Internet content provider (ICP) filling for the accelerated domain.

-> **NOTE:** If the origin content is not saved on Alibaba Cloud, the content must be reviewed by Alibaba Cloud. The review will be completed by the next working day after you submit the application.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::DcdnDomain",
    "Properties" : {
        "<a href="#certname" title="CertName">CertName</a>" : <i>String</i>,
        "<a href="#certtype" title="CertType">CertType</a>" : <i>String</i>,
        "<a href="#checkurl" title="CheckUrl">CheckUrl</a>" : <i>String</i>,
        "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
        "<a href="#forceset" title="ForceSet">ForceSet</a>" : <i>String</i>,
        "<a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>" : <i>String</i>,
        "<a href="#scope" title="Scope">Scope</a>" : <i>String</i>,
        "<a href="#securitytoken" title="SecurityToken">SecurityToken</a>" : <i>String</i>,
        "<a href="#sslpri" title="SslPri">SslPri</a>" : <i>String</i>,
        "<a href="#sslprotocol" title="SslProtocol">SslProtocol</a>" : <i>String</i>,
        "<a href="#sslpub" title="SslPub">SslPub</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#topleveldomain" title="TopLevelDomain">TopLevelDomain</a>" : <i>String</i>,
        "<a href="#sources" title="Sources">Sources</a>" : <i>[ <a href="sourcesdefinition.md">SourcesDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::DcdnDomain
Properties:
    <a href="#certname" title="CertName">CertName</a>: <i>String</i>
    <a href="#certtype" title="CertType">CertType</a>: <i>String</i>
    <a href="#checkurl" title="CheckUrl">CheckUrl</a>: <i>String</i>
    <a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
    <a href="#forceset" title="ForceSet">ForceSet</a>: <i>String</i>
    <a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>: <i>String</i>
    <a href="#scope" title="Scope">Scope</a>: <i>String</i>
    <a href="#securitytoken" title="SecurityToken">SecurityToken</a>: <i>String</i>
    <a href="#sslpri" title="SslPri">SslPri</a>: <i>String</i>
    <a href="#sslprotocol" title="SslProtocol">SslProtocol</a>: <i>String</i>
    <a href="#sslpub" title="SslPub">SslPub</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#topleveldomain" title="TopLevelDomain">TopLevelDomain</a>: <i>String</i>
    <a href="#sources" title="Sources">Sources</a>: <i>
      - <a href="sourcesdefinition.md">SourcesDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CertName

Indicates the name of the certificate if the HTTPS protocol is enabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertType

The type of the certificate. Valid values:
`free`: a free certificate.
`cas`: a certificate purchased from Alibaba Cloud SSL Certificates Service.
`upload`: a user uploaded certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckUrl

The URL that is used to test the accessibility of the origin.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainName

The name of the accelerated domain.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceSet

Specifies whether to check the certificate name for duplicates. If you set the value to 1, the system does not perform the check and overwrites the information of the existing certificate with the same name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupId

The ID of the resource group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

The acceleration region.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityToken

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslPri

The private key. Specify this parameter only if you enable the SSL certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslProtocol

Indicates whether the SSL certificate is enabled. Valid values: `on` enabled, `off` disabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslPub

Indicates the public key of the certificate if the HTTPS protocol is enabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

The status of DCDN Domain. Valid values: `online`, `offline`. Default to `online`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TopLevelDomain

The top-level domain name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sources

_Required_: No

_Type_: List of <a href="sourcesdefinition.md">SourcesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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


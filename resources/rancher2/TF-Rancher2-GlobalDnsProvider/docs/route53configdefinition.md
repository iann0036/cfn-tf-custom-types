# TF::Rancher2::GlobalDnsProvider Route53ConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accesskey" title="AccessKey">AccessKey</a>" : <i>String</i>,
    "<a href="#credentialspath" title="CredentialsPath">CredentialsPath</a>" : <i>String</i>,
    "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
    "<a href="#secretkey" title="SecretKey">SecretKey</a>" : <i>String</i>,
    "<a href="#zonetype" title="ZoneType">ZoneType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#accesskey" title="AccessKey">AccessKey</a>: <i>String</i>
<a href="#credentialspath" title="CredentialsPath">CredentialsPath</a>: <i>String</i>
<a href="#region" title="Region">Region</a>: <i>String</i>
<a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
<a href="#secretkey" title="SecretKey">SecretKey</a>: <i>String</i>
<a href="#zonetype" title="ZoneType">ZoneType</a>: <i>String</i>
</pre>

## Properties

#### AccessKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CredentialsPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


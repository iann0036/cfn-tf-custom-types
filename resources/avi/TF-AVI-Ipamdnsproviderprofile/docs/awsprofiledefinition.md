# TF::AVI::Ipamdnsproviderprofile AwsProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accesskeyid" title="AccessKeyId">AccessKeyId</a>" : <i>String</i>,
    "<a href="#egressservicesubnets" title="EgressServiceSubnets">EgressServiceSubnets</a>" : <i>[ String, ... ]</i>,
    "<a href="#iamassumerole" title="IamAssumeRole">IamAssumeRole</a>" : <i>String</i>,
    "<a href="#publishviptopubliczone" title="PublishVipToPublicZone">PublishVipToPublicZone</a>" : <i>Boolean</i>,
    "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    "<a href="#secretaccesskey" title="SecretAccessKey">SecretAccessKey</a>" : <i>String</i>,
    "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>,
    "<a href="#usabledomains" title="UsableDomains">UsableDomains</a>" : <i>[ String, ... ]</i>,
    "<a href="#usablenetworkuuids" title="UsableNetworkUuids">UsableNetworkUuids</a>" : <i>[ String, ... ]</i>,
    "<a href="#useiamroles" title="UseIamRoles">UseIamRoles</a>" : <i>Boolean</i>,
    "<a href="#vpc" title="Vpc">Vpc</a>" : <i>String</i>,
    "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
    "<a href="#zones" title="Zones">Zones</a>" : <i>[ <a href="zonesdefinition.md">ZonesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#accesskeyid" title="AccessKeyId">AccessKeyId</a>: <i>String</i>
<a href="#egressservicesubnets" title="EgressServiceSubnets">EgressServiceSubnets</a>: <i>
      - String</i>
<a href="#iamassumerole" title="IamAssumeRole">IamAssumeRole</a>: <i>String</i>
<a href="#publishviptopubliczone" title="PublishVipToPublicZone">PublishVipToPublicZone</a>: <i>Boolean</i>
<a href="#region" title="Region">Region</a>: <i>String</i>
<a href="#secretaccesskey" title="SecretAccessKey">SecretAccessKey</a>: <i>String</i>
<a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
<a href="#usabledomains" title="UsableDomains">UsableDomains</a>: <i>
      - String</i>
<a href="#usablenetworkuuids" title="UsableNetworkUuids">UsableNetworkUuids</a>: <i>
      - String</i>
<a href="#useiamroles" title="UseIamRoles">UseIamRoles</a>: <i>Boolean</i>
<a href="#vpc" title="Vpc">Vpc</a>: <i>String</i>
<a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
<a href="#zones" title="Zones">Zones</a>: <i>
      - <a href="zonesdefinition.md">ZonesDefinition</a></i>
</pre>

## Properties

#### AccessKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EgressServiceSubnets

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamAssumeRole

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublishVipToPublicZone

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretAccessKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsableDomains

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsableNetworkUuids

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseIamRoles

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vpc

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zones

_Required_: No

_Type_: List of <a href="zonesdefinition.md">ZonesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


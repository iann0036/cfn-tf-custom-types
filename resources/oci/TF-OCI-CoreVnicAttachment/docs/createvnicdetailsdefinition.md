# TF::OCI::CoreVnicAttachment CreateVnicDetailsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#assignprivatednsrecord" title="AssignPrivateDnsRecord">AssignPrivateDnsRecord</a>" : <i>Boolean</i>,
    "<a href="#assignpublicip" title="AssignPublicIp">AssignPublicIp</a>" : <i>String</i>,
    "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
    "<a href="#hostnamelabel" title="HostnameLabel">HostnameLabel</a>" : <i>String</i>,
    "<a href="#nsgids" title="NsgIds">NsgIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#privateip" title="PrivateIp">PrivateIp</a>" : <i>String</i>,
    "<a href="#skipsourcedestcheck" title="SkipSourceDestCheck">SkipSourceDestCheck</a>" : <i>Boolean</i>,
    "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
    "<a href="#vlanid" title="VlanId">VlanId</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#assignprivatednsrecord" title="AssignPrivateDnsRecord">AssignPrivateDnsRecord</a>: <i>Boolean</i>
<a href="#assignpublicip" title="AssignPublicIp">AssignPublicIp</a>: <i>String</i>
<a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
<a href="#hostnamelabel" title="HostnameLabel">HostnameLabel</a>: <i>String</i>
<a href="#nsgids" title="NsgIds">NsgIds</a>: <i>
      - String</i>
<a href="#privateip" title="PrivateIp">PrivateIp</a>: <i>String</i>
<a href="#skipsourcedestcheck" title="SkipSourceDestCheck">SkipSourceDestCheck</a>: <i>Boolean</i>
<a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
<a href="#vlanid" title="VlanId">VlanId</a>: <i>String</i>
</pre>

## Properties

#### AssignPrivateDnsRecord

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssignPublicIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostnameLabel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsgIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipSourceDestCheck

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VlanId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


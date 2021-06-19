# TF::AVI::Gslbservice MembersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#clouduuid" title="CloudUuid">CloudUuid</a>" : <i>String</i>,
    "<a href="#clusteruuid" title="ClusterUuid">ClusterUuid</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#fqdn" title="Fqdn">Fqdn</a>" : <i>String</i>,
    "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
    "<a href="#ratio" title="Ratio">Ratio</a>" : <i>Double</i>,
    "<a href="#resolvefqdntov6" title="ResolveFqdnToV6">ResolveFqdnToV6</a>" : <i>Boolean</i>,
    "<a href="#vsuuid" title="VsUuid">VsUuid</a>" : <i>String</i>,
    "<a href="#ip" title="Ip">Ip</a>" : <i>[ <a href="ipdefinition.md">IpDefinition</a>, ... ]</i>,
    "<a href="#location" title="Location">Location</a>" : <i>[ <a href="locationdefinition.md">LocationDefinition</a>, ... ]</i>,
    "<a href="#publicip" title="PublicIp">PublicIp</a>" : <i>[ <a href="publicipdefinition.md">PublicIpDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#clouduuid" title="CloudUuid">CloudUuid</a>: <i>String</i>
<a href="#clusteruuid" title="ClusterUuid">ClusterUuid</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#fqdn" title="Fqdn">Fqdn</a>: <i>String</i>
<a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
<a href="#ratio" title="Ratio">Ratio</a>: <i>Double</i>
<a href="#resolvefqdntov6" title="ResolveFqdnToV6">ResolveFqdnToV6</a>: <i>Boolean</i>
<a href="#vsuuid" title="VsUuid">VsUuid</a>: <i>String</i>
<a href="#ip" title="Ip">Ip</a>: <i>
      - <a href="ipdefinition.md">IpDefinition</a></i>
<a href="#location" title="Location">Location</a>: <i>
      - <a href="locationdefinition.md">LocationDefinition</a></i>
<a href="#publicip" title="PublicIp">PublicIp</a>: <i>
      - <a href="publicipdefinition.md">PublicIpDefinition</a></i>
</pre>

## Properties

#### CloudUuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterUuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fqdn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ratio

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolveFqdnToV6

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsUuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

_Required_: No

_Type_: List of <a href="ipdefinition.md">IpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: No

_Type_: List of <a href="locationdefinition.md">LocationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIp

_Required_: No

_Type_: List of <a href="publicipdefinition.md">PublicIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


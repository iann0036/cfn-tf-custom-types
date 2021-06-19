# TF::AVI::Ipamdnsproviderprofile TencentProfileDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudcredentialsref" title="CloudCredentialsRef">CloudCredentialsRef</a>" : <i>String</i>,
    "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    "<a href="#usablesubnetids" title="UsableSubnetIds">UsableSubnetIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
    "<a href="#zones" title="Zones">Zones</a>" : <i>[ <a href="zonesdefinition.md">ZonesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cloudcredentialsref" title="CloudCredentialsRef">CloudCredentialsRef</a>: <i>String</i>
<a href="#region" title="Region">Region</a>: <i>String</i>
<a href="#usablesubnetids" title="UsableSubnetIds">UsableSubnetIds</a>: <i>
      - String</i>
<a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
<a href="#zones" title="Zones">Zones</a>: <i>
      - <a href="zonesdefinition.md">ZonesDefinition</a></i>
</pre>

## Properties

#### CloudCredentialsRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsableSubnetIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zones

_Required_: No

_Type_: List of <a href="zonesdefinition.md">ZonesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


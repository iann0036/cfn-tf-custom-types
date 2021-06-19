# TF::GoogleBeta::GoogleAccessContextManagerAccessLevel ConditionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipsubnetworks" title="IpSubnetworks">IpSubnetworks</a>" : <i>[ String, ... ]</i>,
    "<a href="#members" title="Members">Members</a>" : <i>[ String, ... ]</i>,
    "<a href="#negate" title="Negate">Negate</a>" : <i>Boolean</i>,
    "<a href="#regions" title="Regions">Regions</a>" : <i>[ String, ... ]</i>,
    "<a href="#requiredaccesslevels" title="RequiredAccessLevels">RequiredAccessLevels</a>" : <i>[ String, ... ]</i>,
    "<a href="#devicepolicy" title="DevicePolicy">DevicePolicy</a>" : <i>[ <a href="devicepolicydefinition.md">DevicePolicyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ipsubnetworks" title="IpSubnetworks">IpSubnetworks</a>: <i>
      - String</i>
<a href="#members" title="Members">Members</a>: <i>
      - String</i>
<a href="#negate" title="Negate">Negate</a>: <i>Boolean</i>
<a href="#regions" title="Regions">Regions</a>: <i>
      - String</i>
<a href="#requiredaccesslevels" title="RequiredAccessLevels">RequiredAccessLevels</a>: <i>
      - String</i>
<a href="#devicepolicy" title="DevicePolicy">DevicePolicy</a>: <i>
      - <a href="devicepolicydefinition.md">DevicePolicyDefinition</a></i>
</pre>

## Properties

#### IpSubnetworks

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Members

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Negate

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Regions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequiredAccessLevels

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DevicePolicy

_Required_: No

_Type_: List of <a href="devicepolicydefinition.md">DevicePolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


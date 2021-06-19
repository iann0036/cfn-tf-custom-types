# TF::AVI::Cloud HostsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#nodeavailabilityzone" title="NodeAvailabilityZone">NodeAvailabilityZone</a>" : <i>String</i>,
    "<a href="#segroupref" title="SeGroupRef">SeGroupRef</a>" : <i>String</i>,
    "<a href="#hostattr" title="HostAttr">HostAttr</a>" : <i>[ <a href="hostattrdefinition.md">HostAttrDefinition</a>, ... ]</i>,
    "<a href="#hostip" title="HostIp">HostIp</a>" : <i>[ <a href="hostipdefinition.md">HostIpDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#nodeavailabilityzone" title="NodeAvailabilityZone">NodeAvailabilityZone</a>: <i>String</i>
<a href="#segroupref" title="SeGroupRef">SeGroupRef</a>: <i>String</i>
<a href="#hostattr" title="HostAttr">HostAttr</a>: <i>
      - <a href="hostattrdefinition.md">HostAttrDefinition</a></i>
<a href="#hostip" title="HostIp">HostIp</a>: <i>
      - <a href="hostipdefinition.md">HostIpDefinition</a></i>
</pre>

## Properties

#### NodeAvailabilityZone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeGroupRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostAttr

_Required_: No

_Type_: List of <a href="hostattrdefinition.md">HostAttrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostIp

_Required_: No

_Type_: List of <a href="hostipdefinition.md">HostIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


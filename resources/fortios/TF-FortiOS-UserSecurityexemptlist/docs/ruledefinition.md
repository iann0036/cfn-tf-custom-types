# TF::FortiOS::UserSecurityexemptlist RuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>Double</i>,
    "<a href="#devices" title="Devices">Devices</a>" : <i>[ <a href="devicesdefinition.md">DevicesDefinition</a>, ... ]</i>,
    "<a href="#dstaddr" title="Dstaddr">Dstaddr</a>" : <i>[ <a href="dstaddrdefinition.md">DstaddrDefinition</a>, ... ]</i>,
    "<a href="#service" title="Service">Service</a>" : <i>[ <a href="servicedefinition.md">ServiceDefinition</a>, ... ]</i>,
    "<a href="#srcaddr" title="Srcaddr">Srcaddr</a>" : <i>[ <a href="srcaddrdefinition.md">SrcaddrDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>Double</i>
<a href="#devices" title="Devices">Devices</a>: <i>
      - <a href="devicesdefinition.md">DevicesDefinition</a></i>
<a href="#dstaddr" title="Dstaddr">Dstaddr</a>: <i>
      - <a href="dstaddrdefinition.md">DstaddrDefinition</a></i>
<a href="#service" title="Service">Service</a>: <i>
      - <a href="servicedefinition.md">ServiceDefinition</a></i>
<a href="#srcaddr" title="Srcaddr">Srcaddr</a>: <i>
      - <a href="srcaddrdefinition.md">SrcaddrDefinition</a></i>
</pre>

## Properties

#### Id

ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Devices

_Required_: No

_Type_: List of <a href="devicesdefinition.md">DevicesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dstaddr

_Required_: No

_Type_: List of <a href="dstaddrdefinition.md">DstaddrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No

_Type_: List of <a href="servicedefinition.md">ServiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Srcaddr

_Required_: No

_Type_: List of <a href="srcaddrdefinition.md">SrcaddrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


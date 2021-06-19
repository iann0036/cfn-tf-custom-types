# TF::OpenNebula::VirtualMachineGroup RoleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hostaffined" title="HostAffined">HostAffined</a>" : <i>[ Double, ... ]</i>,
    "<a href="#hostantiaffined" title="HostAntiAffined">HostAntiAffined</a>" : <i>[ Double, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#hostaffined" title="HostAffined">HostAffined</a>: <i>
      - Double</i>
<a href="#hostantiaffined" title="HostAntiAffined">HostAntiAffined</a>: <i>
      - Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#policy" title="Policy">Policy</a>: <i>String</i>
</pre>

## Properties

#### HostAffined

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostAntiAffined

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


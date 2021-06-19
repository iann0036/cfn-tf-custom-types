# TF::FortiOS::RouterRipng InterfaceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#flags" title="Flags">Flags</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#splithorizon" title="SplitHorizon">SplitHorizon</a>" : <i>String</i>,
    "<a href="#splithorizonstatus" title="SplitHorizonStatus">SplitHorizonStatus</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#flags" title="Flags">Flags</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#splithorizon" title="SplitHorizon">SplitHorizon</a>: <i>String</i>
<a href="#splithorizonstatus" title="SplitHorizonStatus">SplitHorizonStatus</a>: <i>String</i>
</pre>

## Properties

#### Flags

Flags.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Interface name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SplitHorizon

Enable/disable split horizon. Valid values: `poisoned`, `regular`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SplitHorizonStatus

Enable/disable split horizon. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


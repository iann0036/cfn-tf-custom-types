# TF::NSXT::PolicyTier0Gateway RouteTargetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#addressfamily" title="AddressFamily">AddressFamily</a>" : <i>String</i>,
    "<a href="#automode" title="AutoMode">AutoMode</a>" : <i>Boolean</i>,
    "<a href="#exporttargets" title="ExportTargets">ExportTargets</a>" : <i>[ String, ... ]</i>,
    "<a href="#importtargets" title="ImportTargets">ImportTargets</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#addressfamily" title="AddressFamily">AddressFamily</a>: <i>String</i>
<a href="#automode" title="AutoMode">AutoMode</a>: <i>Boolean</i>
<a href="#exporttargets" title="ExportTargets">ExportTargets</a>: <i>
      - String</i>
<a href="#importtargets" title="ImportTargets">ImportTargets</a>: <i>
      - String</i>
</pre>

## Properties

#### AddressFamily

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoMode

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExportTargets

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImportTargets

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


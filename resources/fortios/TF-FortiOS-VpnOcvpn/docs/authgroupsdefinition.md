# TF::FortiOS::VpnOcvpn AuthGroupsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authgroup" title="AuthGroup">AuthGroup</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#overlays" title="Overlays">Overlays</a>" : <i>[ <a href="overlaysdefinition.md">OverlaysDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#authgroup" title="AuthGroup">AuthGroup</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#overlays" title="Overlays">Overlays</a>: <i>
      - <a href="overlaysdefinition.md">OverlaysDefinition</a></i>
</pre>

## Properties

#### AuthGroup

Authentication user group for FortiClient access.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Group name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Overlays

_Required_: No

_Type_: List of <a href="overlaysdefinition.md">OverlaysDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


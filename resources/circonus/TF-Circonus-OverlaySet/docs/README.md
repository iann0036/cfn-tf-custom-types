# TF::Circonus::OverlaySet

CloudFormation equivalent of circonus_overlay_set

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Circonus::OverlaySet",
    "Properties" : {
        "<a href="#graphcid" title="GraphCid">GraphCid</a>" : <i>String</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>,
        "<a href="#overlays" title="Overlays">Overlays</a>" : <i>[ <a href="overlaysdefinition.md">OverlaysDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Circonus::OverlaySet
Properties:
    <a href="#graphcid" title="GraphCid">GraphCid</a>: <i>String</i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
    <a href="#overlays" title="Overlays">Overlays</a>: <i>
      - <a href="overlaysdefinition.md">OverlaysDefinition</a></i>
</pre>

## Properties

#### GraphCid

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Overlays

_Required_: No

_Type_: List of <a href="overlaysdefinition.md">OverlaysDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.


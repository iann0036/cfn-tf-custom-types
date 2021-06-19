# TF::CheckPoint::ManagementSetThreatProtection

This command resource allows you to execute Check Point Set Threat Protection.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementSetThreatProtection",
    "Properties" : {
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#followup" title="FollowUp">FollowUp</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#overrides" title="Overrides">Overrides</a>" : <i>[ <a href="overridesdefinition.md">OverridesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementSetThreatProtection
Properties:
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#followup" title="FollowUp">FollowUp</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#overrides" title="Overrides">Overrides</a>: <i>
      - <a href="overridesdefinition.md">OverridesDefinition</a></i>
</pre>

## Properties

#### Comments

Protection comments.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FollowUp

Tag the protection with pre-defined follow-up flag.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Object name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Overrides

_Required_: No

_Type_: List of <a href="overridesdefinition.md">OverridesDefinition</a>

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


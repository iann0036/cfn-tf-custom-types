# TF::OpsGenie::Maintenance

Manages a Maintenance within Opsgenie.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OpsGenie::Maintenance",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#rules" title="Rules">Rules</a>" : <i>[ <a href="rulesdefinition.md">RulesDefinition</a>, ... ]</i>,
        "<a href="#time" title="Time">Time</a>" : <i>[ <a href="timedefinition.md">TimeDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OpsGenie::Maintenance
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#rules" title="Rules">Rules</a>: <i>
      - <a href="rulesdefinition.md">RulesDefinition</a></i>
    <a href="#time" title="Time">Time</a>: <i>
      - <a href="timedefinition.md">TimeDefinition</a></i>
</pre>

## Properties

#### Description

Description for the maintenance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rules

_Required_: No

_Type_: List of <a href="rulesdefinition.md">RulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Time

_Required_: No

_Type_: List of <a href="timedefinition.md">TimeDefinition</a>

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

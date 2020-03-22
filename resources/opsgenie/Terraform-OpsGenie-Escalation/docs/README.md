# Terraform::OpsGenie::Escalation

Manages an Escalation within Opsgenie.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpsGenie::Escalation",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ownerteamid" title="OwnerTeamId">OwnerTeamId</a>" : <i>String</i>,
        "<a href="#repeat" title="Repeat">Repeat</a>" : <i>[ <a href="repeat.md">Repeat</a>, ... ]</i>,
        "<a href="#rules" title="Rules">Rules</a>" : <i>[ <a href="rules.md">Rules</a>, ... ]</i>,
        "<a href="#recipient" title="Recipient">Recipient</a>" : <i>[ <a href="recipient.md">Recipient</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpsGenie::Escalation
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ownerteamid" title="OwnerTeamId">OwnerTeamId</a>: <i>String</i>
    <a href="#repeat" title="Repeat">Repeat</a>: <i>
      - <a href="repeat.md">Repeat</a></i>
    <a href="#rules" title="Rules">Rules</a>: <i>
      - <a href="rules.md">Rules</a></i>
    <a href="#recipient" title="Recipient">Recipient</a>: <i>
      - <a href="recipient.md">Recipient</a></i>
</pre>

## Properties

#### Description

Description of the escalation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the escalation.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OwnerTeamId

Owner team id of the escalation.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repeat

_Required_: No

_Type_: List of <a href="repeat.md">Repeat</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rules

_Required_: No

_Type_: List of <a href="rules.md">Rules</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recipient

_Required_: No

_Type_: List of <a href="recipient.md">Recipient</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.


# TF::OneLogin::AppRules

Manage App Rule resources.

This resource allows you to create and configure App Rules.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OneLogin::AppRules",
    "Properties" : {
        "<a href="#appid" title="AppId">AppId</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#match" title="Match">Match</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#position" title="Position">Position</a>" : <i>Double</i>,
        "<a href="#actions" title="Actions">Actions</a>" : <i>[ <a href="actionsdefinition.md">ActionsDefinition</a>, ... ]</i>,
        "<a href="#conditions" title="Conditions">Conditions</a>" : <i>[ <a href="conditionsdefinition.md">ConditionsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OneLogin::AppRules
Properties:
    <a href="#appid" title="AppId">AppId</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#match" title="Match">Match</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#position" title="Position">Position</a>: <i>Double</i>
    <a href="#actions" title="Actions">Actions</a>: <i>
      - <a href="actionsdefinition.md">ActionsDefinition</a></i>
    <a href="#conditions" title="Conditions">Conditions</a>: <i>
      - <a href="conditionsdefinition.md">ConditionsDefinition</a></i>
</pre>

## Properties

#### AppId

The id of the App resource to which the rule should belong.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Indicate if the rule should go into effect.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Match

Indicates how conditions should be matched. Must be one of `all` or `any`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Rule's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Position

Indicates the order of the rule. When `null` this will default to last position.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Actions

_Required_: No

_Type_: List of <a href="actionsdefinition.md">ActionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Conditions

_Required_: No

_Type_: List of <a href="conditionsdefinition.md">ConditionsDefinition</a>

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

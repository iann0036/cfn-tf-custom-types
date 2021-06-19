# TF::OpsGenie::TeamRoutingRule

Manages a Team Routing Rule within Opsgenie.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OpsGenie::TeamRoutingRule",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#order" title="Order">Order</a>" : <i>Double</i>,
        "<a href="#teamid" title="TeamId">TeamId</a>" : <i>String</i>,
        "<a href="#timezone" title="Timezone">Timezone</a>" : <i>String</i>,
        "<a href="#criteria" title="Criteria">Criteria</a>" : <i>[ <a href="criteriadefinition.md">CriteriaDefinition</a>, ... ]</i>,
        "<a href="#notify" title="Notify">Notify</a>" : <i>[ <a href="notifydefinition.md">NotifyDefinition</a>, ... ]</i>,
        "<a href="#timerestriction" title="TimeRestriction">TimeRestriction</a>" : <i>[ <a href="timerestrictiondefinition.md">TimeRestrictionDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OpsGenie::TeamRoutingRule
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#order" title="Order">Order</a>: <i>Double</i>
    <a href="#teamid" title="TeamId">TeamId</a>: <i>String</i>
    <a href="#timezone" title="Timezone">Timezone</a>: <i>String</i>
    <a href="#criteria" title="Criteria">Criteria</a>: <i>
      - <a href="criteriadefinition.md">CriteriaDefinition</a></i>
    <a href="#notify" title="Notify">Notify</a>: <i>
      - <a href="notifydefinition.md">NotifyDefinition</a></i>
    <a href="#timerestriction" title="TimeRestriction">TimeRestriction</a>: <i>
      - <a href="timerestrictiondefinition.md">TimeRestrictionDefinition</a></i>
</pre>

## Properties

#### Name

Name of the team routing rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Order

The order of the team routing rule within the rules. order value is actually the index of the team routing rule whose minimum value is 0 and whose maximum value is n-1 (number of team routing rules is n).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TeamId

Id of the team owning the routing rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timezone

Timezone of team routing rule. If timezone field is not given, account timezone is used as default.You can refer to Supported Locale IDs for available timezones.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Criteria

_Required_: No

_Type_: List of <a href="criteriadefinition.md">CriteriaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notify

_Required_: No

_Type_: List of <a href="notifydefinition.md">NotifyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeRestriction

_Required_: No

_Type_: List of <a href="timerestrictiondefinition.md">TimeRestrictionDefinition</a>

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


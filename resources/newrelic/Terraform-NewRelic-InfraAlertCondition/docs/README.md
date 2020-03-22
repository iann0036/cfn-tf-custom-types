# Terraform::NewRelic::InfraAlertCondition

CloudFormation equivalent of newrelic_infra_alert_condition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NewRelic::InfraAlertCondition",
    "Properties" : {
        "<a href="#comparison" title="Comparison">Comparison</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#event" title="Event">Event</a>" : <i>String</i>,
        "<a href="#integrationprovider" title="IntegrationProvider">IntegrationProvider</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#policyid" title="PolicyId">PolicyId</a>" : <i>Double</i>,
        "<a href="#processwhere" title="ProcessWhere">ProcessWhere</a>" : <i>String</i>,
        "<a href="#runbookurl" title="RunbookUrl">RunbookUrl</a>" : <i>String</i>,
        "<a href="#select" title="Select">Select</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#violationclosetimer" title="ViolationCloseTimer">ViolationCloseTimer</a>" : <i>Double</i>,
        "<a href="#where" title="Where">Where</a>" : <i>String</i>,
        "<a href="#critical" title="Critical">Critical</a>" : <i>[ <a href="critical.md">Critical</a>, ... ]</i>,
        "<a href="#warning" title="Warning">Warning</a>" : <i>[ <a href="warning.md">Warning</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NewRelic::InfraAlertCondition
Properties:
    <a href="#comparison" title="Comparison">Comparison</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#event" title="Event">Event</a>: <i>String</i>
    <a href="#integrationprovider" title="IntegrationProvider">IntegrationProvider</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#policyid" title="PolicyId">PolicyId</a>: <i>Double</i>
    <a href="#processwhere" title="ProcessWhere">ProcessWhere</a>: <i>String</i>
    <a href="#runbookurl" title="RunbookUrl">RunbookUrl</a>: <i>String</i>
    <a href="#select" title="Select">Select</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#violationclosetimer" title="ViolationCloseTimer">ViolationCloseTimer</a>: <i>Double</i>
    <a href="#where" title="Where">Where</a>: <i>String</i>
    <a href="#critical" title="Critical">Critical</a>: <i>
      - <a href="critical.md">Critical</a></i>
    <a href="#warning" title="Warning">Warning</a>: <i>
      - <a href="warning.md">Warning</a></i>
</pre>

## Properties

#### Comparison

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Event

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntegrationProvider

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyId

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessWhere

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunbookUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Select

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViolationCloseTimer

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Where

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Critical

_Required_: No

_Type_: List of <a href="critical.md">Critical</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Warning

_Required_: No

_Type_: List of <a href="warning.md">Warning</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Id

Returns the <code>Id</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.


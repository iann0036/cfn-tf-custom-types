# TF::GoogleBeta::GoogleHealthcareHl7V2Store

CloudFormation equivalent of google_healthcare_hl7_v2_store

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::GoogleBeta::GoogleHealthcareHl7V2Store",
    "Properties" : {
        "<a href="#dataset" title="Dataset">Dataset</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notificationconfig" title="NotificationConfig">NotificationConfig</a>" : <i>[ <a href="notificationconfigdefinition.md">NotificationConfigDefinition</a>, ... ]</i>,
        "<a href="#notificationconfigs" title="NotificationConfigs">NotificationConfigs</a>" : <i>[ <a href="notificationconfigsdefinition.md">NotificationConfigsDefinition</a>, ... ]</i>,
        "<a href="#parserconfig" title="ParserConfig">ParserConfig</a>" : <i>[ <a href="parserconfigdefinition.md">ParserConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::GoogleBeta::GoogleHealthcareHl7V2Store
Properties:
    <a href="#dataset" title="Dataset">Dataset</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notificationconfig" title="NotificationConfig">NotificationConfig</a>: <i>
      - <a href="notificationconfigdefinition.md">NotificationConfigDefinition</a></i>
    <a href="#notificationconfigs" title="NotificationConfigs">NotificationConfigs</a>: <i>
      - <a href="notificationconfigsdefinition.md">NotificationConfigsDefinition</a></i>
    <a href="#parserconfig" title="ParserConfig">ParserConfig</a>: <i>
      - <a href="parserconfigdefinition.md">ParserConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Dataset

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationConfig

_Required_: No

_Type_: List of <a href="notificationconfigdefinition.md">NotificationConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotificationConfigs

_Required_: No

_Type_: List of <a href="notificationconfigsdefinition.md">NotificationConfigsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParserConfig

_Required_: No

_Type_: List of <a href="parserconfigdefinition.md">ParserConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### SelfLink

Returns the <code>SelfLink</code> value.


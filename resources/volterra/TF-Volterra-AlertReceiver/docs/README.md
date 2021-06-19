# TF::Volterra::AlertReceiver

CloudFormation equivalent of volterra_alert_receiver

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Volterra::AlertReceiver",
    "Properties" : {
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disable" title="Disable">Disable</a>" : <i>Boolean</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#email" title="Email">Email</a>" : <i>[ <a href="emaildefinition.md">EmailDefinition</a>, ... ]</i>,
        "<a href="#opsgenie" title="Opsgenie">Opsgenie</a>" : <i>[ <a href="opsgeniedefinition.md">OpsgenieDefinition</a>, ... ]</i>,
        "<a href="#pagerduty" title="Pagerduty">Pagerduty</a>" : <i>[ <a href="pagerdutydefinition.md">PagerdutyDefinition</a>, ... ]</i>,
        "<a href="#slack" title="Slack">Slack</a>" : <i>[ <a href="slackdefinition.md">SlackDefinition</a>, ... ]</i>,
        "<a href="#sms" title="Sms">Sms</a>" : <i>[ <a href="smsdefinition.md">SmsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Volterra::AlertReceiver
Properties:
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disable" title="Disable">Disable</a>: <i>Boolean</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#email" title="Email">Email</a>: <i>
      - <a href="emaildefinition.md">EmailDefinition</a></i>
    <a href="#opsgenie" title="Opsgenie">Opsgenie</a>: <i>
      - <a href="opsgeniedefinition.md">OpsgenieDefinition</a></i>
    <a href="#pagerduty" title="Pagerduty">Pagerduty</a>: <i>
      - <a href="pagerdutydefinition.md">PagerdutyDefinition</a></i>
    <a href="#slack" title="Slack">Slack</a>: <i>
      - <a href="slackdefinition.md">SlackDefinition</a></i>
    <a href="#sms" title="Sms">Sms</a>: <i>
      - <a href="smsdefinition.md">SmsDefinition</a></i>
</pre>

## Properties

#### Annotations

_Required_: No

_Type_: List of <a href="annotationsdefinition.md">AnnotationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

_Required_: No

_Type_: List of <a href="emaildefinition.md">EmailDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Opsgenie

_Required_: No

_Type_: List of <a href="opsgeniedefinition.md">OpsgenieDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pagerduty

_Required_: No

_Type_: List of <a href="pagerdutydefinition.md">PagerdutyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slack

_Required_: No

_Type_: List of <a href="slackdefinition.md">SlackDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sms

_Required_: No

_Type_: List of <a href="smsdefinition.md">SmsDefinition</a>

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


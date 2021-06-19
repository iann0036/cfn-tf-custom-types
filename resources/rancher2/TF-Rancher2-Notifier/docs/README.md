# TF::Rancher2::Notifier

CloudFormation equivalent of rancher2_notifier

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Rancher2::Notifier",
    "Properties" : {
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#clusterid" title="ClusterId">ClusterId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#sendresolved" title="SendResolved">SendResolved</a>" : <i>Boolean</i>,
        "<a href="#dingtalkconfig" title="DingtalkConfig">DingtalkConfig</a>" : <i>[ <a href="dingtalkconfigdefinition.md">DingtalkConfigDefinition</a>, ... ]</i>,
        "<a href="#msteamsconfig" title="MsteamsConfig">MsteamsConfig</a>" : <i>[ <a href="msteamsconfigdefinition.md">MsteamsConfigDefinition</a>, ... ]</i>,
        "<a href="#pagerdutyconfig" title="PagerdutyConfig">PagerdutyConfig</a>" : <i>[ <a href="pagerdutyconfigdefinition.md">PagerdutyConfigDefinition</a>, ... ]</i>,
        "<a href="#slackconfig" title="SlackConfig">SlackConfig</a>" : <i>[ <a href="slackconfigdefinition.md">SlackConfigDefinition</a>, ... ]</i>,
        "<a href="#smtpconfig" title="SmtpConfig">SmtpConfig</a>" : <i>[ <a href="smtpconfigdefinition.md">SmtpConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#webhookconfig" title="WebhookConfig">WebhookConfig</a>" : <i>[ <a href="webhookconfigdefinition.md">WebhookConfigDefinition</a>, ... ]</i>,
        "<a href="#wechatconfig" title="WechatConfig">WechatConfig</a>" : <i>[ <a href="wechatconfigdefinition.md">WechatConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Rancher2::Notifier
Properties:
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#clusterid" title="ClusterId">ClusterId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#sendresolved" title="SendResolved">SendResolved</a>: <i>Boolean</i>
    <a href="#dingtalkconfig" title="DingtalkConfig">DingtalkConfig</a>: <i>
      - <a href="dingtalkconfigdefinition.md">DingtalkConfigDefinition</a></i>
    <a href="#msteamsconfig" title="MsteamsConfig">MsteamsConfig</a>: <i>
      - <a href="msteamsconfigdefinition.md">MsteamsConfigDefinition</a></i>
    <a href="#pagerdutyconfig" title="PagerdutyConfig">PagerdutyConfig</a>: <i>
      - <a href="pagerdutyconfigdefinition.md">PagerdutyConfigDefinition</a></i>
    <a href="#slackconfig" title="SlackConfig">SlackConfig</a>: <i>
      - <a href="slackconfigdefinition.md">SlackConfigDefinition</a></i>
    <a href="#smtpconfig" title="SmtpConfig">SmtpConfig</a>: <i>
      - <a href="smtpconfigdefinition.md">SmtpConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#webhookconfig" title="WebhookConfig">WebhookConfig</a>: <i>
      - <a href="webhookconfigdefinition.md">WebhookConfigDefinition</a></i>
    <a href="#wechatconfig" title="WechatConfig">WechatConfig</a>: <i>
      - <a href="wechatconfigdefinition.md">WechatConfigDefinition</a></i>
</pre>

## Properties

#### Annotations

_Required_: No

_Type_: List of <a href="annotationsdefinition.md">AnnotationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

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

#### SendResolved

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DingtalkConfig

_Required_: No

_Type_: List of <a href="dingtalkconfigdefinition.md">DingtalkConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MsteamsConfig

_Required_: No

_Type_: List of <a href="msteamsconfigdefinition.md">MsteamsConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PagerdutyConfig

_Required_: No

_Type_: List of <a href="pagerdutyconfigdefinition.md">PagerdutyConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlackConfig

_Required_: No

_Type_: List of <a href="slackconfigdefinition.md">SlackConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmtpConfig

_Required_: No

_Type_: List of <a href="smtpconfigdefinition.md">SmtpConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebhookConfig

_Required_: No

_Type_: List of <a href="webhookconfigdefinition.md">WebhookConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WechatConfig

_Required_: No

_Type_: List of <a href="wechatconfigdefinition.md">WechatConfigDefinition</a>

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


# Terraform::AWS::Route53HealthCheck

CloudFormation equivalent of aws_route53_health_check

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::Route53HealthCheck",
    "Properties" : {
        "<a href="#childhealththreshold" title="ChildHealthThreshold">ChildHealthThreshold</a>" : <i>Double</i>,
        "<a href="#childhealthchecks" title="ChildHealthchecks">ChildHealthchecks</a>" : <i>[ String, ... ]</i>,
        "<a href="#cloudwatchalarmname" title="CloudwatchAlarmName">CloudwatchAlarmName</a>" : <i>String</i>,
        "<a href="#cloudwatchalarmregion" title="CloudwatchAlarmRegion">CloudwatchAlarmRegion</a>" : <i>String</i>,
        "<a href="#enablesni" title="EnableSni">EnableSni</a>" : <i>Boolean</i>,
        "<a href="#failurethreshold" title="FailureThreshold">FailureThreshold</a>" : <i>Double</i>,
        "<a href="#fqdn" title="Fqdn">Fqdn</a>" : <i>String</i>,
        "<a href="#insufficientdatahealthstatus" title="InsufficientDataHealthStatus">InsufficientDataHealthStatus</a>" : <i>String</i>,
        "<a href="#inverthealthcheck" title="InvertHealthcheck">InvertHealthcheck</a>" : <i>Boolean</i>,
        "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
        "<a href="#measurelatency" title="MeasureLatency">MeasureLatency</a>" : <i>Boolean</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#referencename" title="ReferenceName">ReferenceName</a>" : <i>String</i>,
        "<a href="#regions" title="Regions">Regions</a>" : <i>[ String, ... ]</i>,
        "<a href="#requestinterval" title="RequestInterval">RequestInterval</a>" : <i>Double</i>,
        "<a href="#resourcepath" title="ResourcePath">ResourcePath</a>" : <i>String</i>,
        "<a href="#searchstring" title="SearchString">SearchString</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::Route53HealthCheck
Properties:
    <a href="#childhealththreshold" title="ChildHealthThreshold">ChildHealthThreshold</a>: <i>Double</i>
    <a href="#childhealthchecks" title="ChildHealthchecks">ChildHealthchecks</a>: <i>
      - String</i>
    <a href="#cloudwatchalarmname" title="CloudwatchAlarmName">CloudwatchAlarmName</a>: <i>String</i>
    <a href="#cloudwatchalarmregion" title="CloudwatchAlarmRegion">CloudwatchAlarmRegion</a>: <i>String</i>
    <a href="#enablesni" title="EnableSni">EnableSni</a>: <i>Boolean</i>
    <a href="#failurethreshold" title="FailureThreshold">FailureThreshold</a>: <i>Double</i>
    <a href="#fqdn" title="Fqdn">Fqdn</a>: <i>String</i>
    <a href="#insufficientdatahealthstatus" title="InsufficientDataHealthStatus">InsufficientDataHealthStatus</a>: <i>String</i>
    <a href="#inverthealthcheck" title="InvertHealthcheck">InvertHealthcheck</a>: <i>Boolean</i>
    <a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
    <a href="#measurelatency" title="MeasureLatency">MeasureLatency</a>: <i>Boolean</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#referencename" title="ReferenceName">ReferenceName</a>: <i>String</i>
    <a href="#regions" title="Regions">Regions</a>: <i>
      - String</i>
    <a href="#requestinterval" title="RequestInterval">RequestInterval</a>: <i>Double</i>
    <a href="#resourcepath" title="ResourcePath">ResourcePath</a>: <i>String</i>
    <a href="#searchstring" title="SearchString">SearchString</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### ChildHealthThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChildHealthchecks

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchAlarmName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchAlarmRegion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSni

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailureThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fqdn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsufficientDataHealthStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InvertHealthcheck

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MeasureLatency

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReferenceName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Regions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourcePath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SearchString

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.


# TF::Alicloud::QuotasQuotaAlarm

CloudFormation equivalent of alicloud_quotas_quota_alarm

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::QuotasQuotaAlarm",
    "Properties" : {
        "<a href="#productcode" title="ProductCode">ProductCode</a>" : <i>String</i>,
        "<a href="#quotaactioncode" title="QuotaActionCode">QuotaActionCode</a>" : <i>String</i>,
        "<a href="#quotaalarmname" title="QuotaAlarmName">QuotaAlarmName</a>" : <i>String</i>,
        "<a href="#threshold" title="Threshold">Threshold</a>" : <i>Double</i>,
        "<a href="#thresholdpercent" title="ThresholdPercent">ThresholdPercent</a>" : <i>Double</i>,
        "<a href="#webhook" title="WebHook">WebHook</a>" : <i>String</i>,
        "<a href="#quotadimensions" title="QuotaDimensions">QuotaDimensions</a>" : <i>[ <a href="quotadimensionsdefinition.md">QuotaDimensionsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::QuotasQuotaAlarm
Properties:
    <a href="#productcode" title="ProductCode">ProductCode</a>: <i>String</i>
    <a href="#quotaactioncode" title="QuotaActionCode">QuotaActionCode</a>: <i>String</i>
    <a href="#quotaalarmname" title="QuotaAlarmName">QuotaAlarmName</a>: <i>String</i>
    <a href="#threshold" title="Threshold">Threshold</a>: <i>Double</i>
    <a href="#thresholdpercent" title="ThresholdPercent">ThresholdPercent</a>: <i>Double</i>
    <a href="#webhook" title="WebHook">WebHook</a>: <i>String</i>
    <a href="#quotadimensions" title="QuotaDimensions">QuotaDimensions</a>: <i>
      - <a href="quotadimensionsdefinition.md">QuotaDimensionsDefinition</a></i>
</pre>

## Properties

#### ProductCode

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuotaActionCode

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuotaAlarmName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Threshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThresholdPercent

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebHook

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuotaDimensions

_Required_: No

_Type_: List of <a href="quotadimensionsdefinition.md">QuotaDimensionsDefinition</a>

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


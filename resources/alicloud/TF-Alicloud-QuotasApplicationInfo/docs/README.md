# TF::Alicloud::QuotasApplicationInfo

CloudFormation equivalent of alicloud_quotas_application_info

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::QuotasApplicationInfo",
    "Properties" : {
        "<a href="#auditmode" title="AuditMode">AuditMode</a>" : <i>String</i>,
        "<a href="#desirevalue" title="DesireValue">DesireValue</a>" : <i>Double</i>,
        "<a href="#noticetype" title="NoticeType">NoticeType</a>" : <i>Double</i>,
        "<a href="#productcode" title="ProductCode">ProductCode</a>" : <i>String</i>,
        "<a href="#quotaactioncode" title="QuotaActionCode">QuotaActionCode</a>" : <i>String</i>,
        "<a href="#quotacategory" title="QuotaCategory">QuotaCategory</a>" : <i>String</i>,
        "<a href="#reason" title="Reason">Reason</a>" : <i>String</i>,
        "<a href="#dimensions" title="Dimensions">Dimensions</a>" : <i>[ <a href="dimensionsdefinition.md">DimensionsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::QuotasApplicationInfo
Properties:
    <a href="#auditmode" title="AuditMode">AuditMode</a>: <i>String</i>
    <a href="#desirevalue" title="DesireValue">DesireValue</a>: <i>Double</i>
    <a href="#noticetype" title="NoticeType">NoticeType</a>: <i>Double</i>
    <a href="#productcode" title="ProductCode">ProductCode</a>: <i>String</i>
    <a href="#quotaactioncode" title="QuotaActionCode">QuotaActionCode</a>: <i>String</i>
    <a href="#quotacategory" title="QuotaCategory">QuotaCategory</a>: <i>String</i>
    <a href="#reason" title="Reason">Reason</a>: <i>String</i>
    <a href="#dimensions" title="Dimensions">Dimensions</a>: <i>
      - <a href="dimensionsdefinition.md">DimensionsDefinition</a></i>
</pre>

## Properties

#### AuditMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesireValue

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoticeType

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProductCode

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuotaActionCode

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuotaCategory

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reason

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dimensions

_Required_: No

_Type_: List of <a href="dimensionsdefinition.md">DimensionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ApproveValue

Returns the <code>ApproveValue</code> value.

#### AuditReason

Returns the <code>AuditReason</code> value.

#### EffectiveTime

Returns the <code>EffectiveTime</code> value.

#### ExpireTime

Returns the <code>ExpireTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### QuotaDescription

Returns the <code>QuotaDescription</code> value.

#### QuotaName

Returns the <code>QuotaName</code> value.

#### QuotaUnit

Returns the <code>QuotaUnit</code> value.

#### Status

Returns the <code>Status</code> value.


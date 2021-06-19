# TF::TencentCloud::ApiGatewayUsagePlan

Use this resource to create API gateway usage plan.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::ApiGatewayUsagePlan",
    "Properties" : {
        "<a href="#maxrequestnum" title="MaxRequestNum">MaxRequestNum</a>" : <i>Double</i>,
        "<a href="#maxrequestnumpresec" title="MaxRequestNumPreSec">MaxRequestNumPreSec</a>" : <i>Double</i>,
        "<a href="#usageplandesc" title="UsagePlanDesc">UsagePlanDesc</a>" : <i>String</i>,
        "<a href="#usageplanname" title="UsagePlanName">UsagePlanName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::ApiGatewayUsagePlan
Properties:
    <a href="#maxrequestnum" title="MaxRequestNum">MaxRequestNum</a>: <i>Double</i>
    <a href="#maxrequestnumpresec" title="MaxRequestNumPreSec">MaxRequestNumPreSec</a>: <i>Double</i>
    <a href="#usageplandesc" title="UsagePlanDesc">UsagePlanDesc</a>: <i>String</i>
    <a href="#usageplanname" title="UsagePlanName">UsagePlanName</a>: <i>String</i>
</pre>

## Properties

#### MaxRequestNum

Total number of requests allowed. Valid values: -1, [1,99999999]. The default value is -1, which indicates no limit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxRequestNumPreSec

Limit of requests per second. Valid values: -1, [1,2000]. The default value is -1, which indicates no limit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsagePlanDesc

Custom usage plan description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsagePlanName

Custom usage plan name.

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

#### AttachApiKeys

Returns the <code>AttachApiKeys</code> value.

#### AttachList

Returns the <code>AttachList</code> value.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### ModifyTime

Returns the <code>ModifyTime</code> value.


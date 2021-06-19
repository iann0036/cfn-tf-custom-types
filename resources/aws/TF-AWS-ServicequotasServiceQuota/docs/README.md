# TF::AWS::ServicequotasServiceQuota

Manages an individual Service Quota.

~> **NOTE:** Global quotas apply to all AWS regions, but can only be accessed in `us-east-1` in the Commercial partition or `us-gov-west-1` in the GovCloud partition. In other regions, the AWS API will return the error `The request failed because the specified service does not exist.`

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::ServicequotasServiceQuota",
    "Properties" : {
        "<a href="#quotacode" title="QuotaCode">QuotaCode</a>" : <i>String</i>,
        "<a href="#servicecode" title="ServiceCode">ServiceCode</a>" : <i>String</i>,
        "<a href="#value" title="Value">Value</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::ServicequotasServiceQuota
Properties:
    <a href="#quotacode" title="QuotaCode">QuotaCode</a>: <i>String</i>
    <a href="#servicecode" title="ServiceCode">ServiceCode</a>: <i>String</i>
    <a href="#value" title="Value">Value</a>: <i>Double</i>
</pre>

## Properties

#### QuotaCode

Code of the service quota to track. For example: `L-F678F1CE`. Available values can be found with the [AWS CLI service-quotas list-service-quotas command](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-service-quotas.html).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceCode

Code of the service to track. For example: `vpc`. Available values can be found with the [AWS CLI service-quotas list-services command](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/list-services.html).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

Float specifying the desired value for the service quota. If the desired value is higher than the current value, a quota increase request is submitted. When a known request is submitted and pending, the value reflects the desired value of the pending request.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Adjustable

Returns the <code>Adjustable</code> value.

#### Arn

Returns the <code>Arn</code> value.

#### DefaultValue

Returns the <code>DefaultValue</code> value.

#### Id

Returns the <code>Id</code> value.

#### QuotaName

Returns the <code>QuotaName</code> value.

#### RequestId

Returns the <code>RequestId</code> value.

#### RequestStatus

Returns the <code>RequestStatus</code> value.

#### ServiceName

Returns the <code>ServiceName</code> value.


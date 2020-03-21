# Terraform::AWS::ServicequotasServiceQuota

CloudFormation equivalent of aws_servicequotas_service_quota

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ServicequotasServiceQuota",
    "Properties" : {
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#quotacode" title="QuotaCode">QuotaCode</a>" : <i>String</i>,
        "<a href="#servicecode" title="ServiceCode">ServiceCode</a>" : <i>String</i>,
        "<a href="#value" title="Value">Value</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ServicequotasServiceQuota
Properties:
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#quotacode" title="QuotaCode">QuotaCode</a>: <i>String</i>
    <a href="#servicecode" title="ServiceCode">ServiceCode</a>: <i>String</i>
    <a href="#value" title="Value">Value</a>: <i>Double</i>
</pre>

## Properties

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QuotaCode

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceCode

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

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

#### QuotaName

Returns the <code>QuotaName</code> value.

#### RequestId

Returns the <code>RequestId</code> value.

#### RequestStatus

Returns the <code>RequestStatus</code> value.

#### ServiceName

Returns the <code>ServiceName</code> value.


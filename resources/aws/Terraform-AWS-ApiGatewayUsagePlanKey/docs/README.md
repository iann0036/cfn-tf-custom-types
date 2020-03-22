# Terraform::AWS::ApiGatewayUsagePlanKey

CloudFormation equivalent of aws_api_gateway_usage_plan_key

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ApiGatewayUsagePlanKey",
    "Properties" : {
        "<a href="#keyid" title="KeyId">KeyId</a>" : <i>String</i>,
        "<a href="#keytype" title="KeyType">KeyType</a>" : <i>String</i>,
        "<a href="#usageplanid" title="UsagePlanId">UsagePlanId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ApiGatewayUsagePlanKey
Properties:
    <a href="#keyid" title="KeyId">KeyId</a>: <i>String</i>
    <a href="#keytype" title="KeyType">KeyType</a>: <i>String</i>
    <a href="#usageplanid" title="UsagePlanId">UsagePlanId</a>: <i>String</i>
</pre>

## Properties

#### KeyId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsagePlanId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### Name

Returns the <code>Name</code> value.

#### Value

Returns the <code>Value</code> value.


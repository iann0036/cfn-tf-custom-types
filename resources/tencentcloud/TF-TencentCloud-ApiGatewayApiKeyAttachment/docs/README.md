# TF::TencentCloud::ApiGatewayApiKeyAttachment

Use this resource to API gateway attach access key to usage plan.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::ApiGatewayApiKeyAttachment",
    "Properties" : {
        "<a href="#apikeyid" title="ApiKeyId">ApiKeyId</a>" : <i>String</i>,
        "<a href="#usageplanid" title="UsagePlanId">UsagePlanId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::ApiGatewayApiKeyAttachment
Properties:
    <a href="#apikeyid" title="ApiKeyId">ApiKeyId</a>: <i>String</i>
    <a href="#usageplanid" title="UsagePlanId">UsagePlanId</a>: <i>String</i>
</pre>

## Properties

#### ApiKeyId

ID of API key.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsagePlanId

ID of the usage plan.

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

#### Id

Returns the <code>Id</code> value.


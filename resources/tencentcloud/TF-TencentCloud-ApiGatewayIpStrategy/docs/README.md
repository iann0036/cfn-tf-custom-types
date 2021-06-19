# TF::TencentCloud::ApiGatewayIpStrategy

Use this resource to create IP strategy of API gateway.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::ApiGatewayIpStrategy",
    "Properties" : {
        "<a href="#serviceid" title="ServiceId">ServiceId</a>" : <i>String</i>,
        "<a href="#strategydata" title="StrategyData">StrategyData</a>" : <i>String</i>,
        "<a href="#strategyname" title="StrategyName">StrategyName</a>" : <i>String</i>,
        "<a href="#strategytype" title="StrategyType">StrategyType</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::ApiGatewayIpStrategy
Properties:
    <a href="#serviceid" title="ServiceId">ServiceId</a>: <i>String</i>
    <a href="#strategydata" title="StrategyData">StrategyData</a>: <i>String</i>
    <a href="#strategyname" title="StrategyName">StrategyName</a>: <i>String</i>
    <a href="#strategytype" title="StrategyType">StrategyType</a>: <i>String</i>
</pre>

## Properties

#### ServiceId

The ID of the API gateway service.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StrategyData

IP address data.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StrategyName

User defined strategy name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StrategyType

Blacklist or whitelist.

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

#### CreateTime

Returns the <code>CreateTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### StrategyId

Returns the <code>StrategyId</code> value.


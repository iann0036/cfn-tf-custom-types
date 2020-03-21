# Terraform::HuaweiCloud::AsGroupV1 LbaasListeners

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#poolid" title="PoolId">PoolId</a>" : <i>String</i>,
    "<a href="#protocolport" title="ProtocolPort">ProtocolPort</a>" : <i>Double</i>,
    "<a href="#weight" title="Weight">Weight</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#poolid" title="PoolId">PoolId</a>: <i>String</i>
<a href="#protocolport" title="ProtocolPort">ProtocolPort</a>: <i>Double</i>
<a href="#weight" title="Weight">Weight</a>: <i>Double</i>
</pre>

## Properties

#### PoolId

Specifies the backend ECS group ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolPort

Specifies the backend protocol, which is the port on which
a backend ECS listens for traffic. The number of the port ranges from 1 to 65535.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Weight

Specifies the weight, which determines the portion of requests a
backend ECS processes compared to other backend ECSs added to the same listener. The value
of this parameter ranges from 0 to 100. The default value is 1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


# TF::Tfe::AgentToken

Each agent pool has its own set of tokens which are not shared across pools.
These tokens allow agents to communicate securely with Terraform Cloud.

~> **NOTE:** This resource requires using the provider with Terraform Cloud and a Terraform Cloud 
for Business account. 
[Learn more about Terraform Cloud pricing here](https://www.hashicorp.com/products/terraform/pricing).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Tfe::AgentToken",
    "Properties" : {
        "<a href="#agentpoolid" title="AgentPoolId">AgentPoolId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Tfe::AgentToken
Properties:
    <a href="#agentpoolid" title="AgentPoolId">AgentPoolId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
</pre>

## Properties

#### AgentPoolId

ID of the agent pool.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the agent token.

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

#### Token

Returns the <code>Token</code> value.


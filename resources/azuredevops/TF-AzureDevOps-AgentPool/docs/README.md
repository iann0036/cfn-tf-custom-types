# TF::AzureDevOps::AgentPool

Manages an agent pool within Azure DevOps.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureDevOps::AgentPool",
    "Properties" : {
        "<a href="#autoprovision" title="AutoProvision">AutoProvision</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pooltype" title="PoolType">PoolType</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureDevOps::AgentPool
Properties:
    <a href="#autoprovision" title="AutoProvision">AutoProvision</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pooltype" title="PoolType">PoolType</a>: <i>String</i>
</pre>

## Properties

#### AutoProvision

Specifies whether or not a queue should be automatically provisioned for each project collection. Defaults to `false`.
- `pool_type` - (Optional) Specifies whether the agent pool type is Automation or Deployment. Defaults to `automation`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the agent pool.
- `auto_provision` - (Optional) Specifies whether or not a queue should be automatically provisioned for each project collection. Defaults to `false`.
- `pool_type` - (Optional) Specifies whether the agent pool type is Automation or Deployment. Defaults to `automation`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoolType

Specifies whether the agent pool type is Automation or Deployment. Defaults to `automation`.

_Required_: No

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


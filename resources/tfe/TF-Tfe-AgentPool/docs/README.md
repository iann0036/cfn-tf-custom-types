# TF::Tfe::AgentPool

An agent pool represents a group of agents, often related to one another by sharing a common 
network segment or purpose. A workspace may be configured to use one of the organization's agent 
pools to run remote operations with isolated, private, or on-premises infrastructure.

~> **NOTE:** This resource requires using the provider with Terraform Cloud and a Terraform Cloud 
for Business account. 
[Learn more about Terraform Cloud pricing here](https://www.hashicorp.com/products/terraform/pricing).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Tfe::AgentPool",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#organization" title="Organization">Organization</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Tfe::AgentPool
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#organization" title="Organization">Organization</a>: <i>String</i>
</pre>

## Properties

#### Name

Name of the agent pool.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Organization

Name of the organization.

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


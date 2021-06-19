# TF::AzureStack::LbBackendAddressPool

Manages a LoadBalancer Backend Address Pool.

~> **NOTE:** When using this resource, the LoadBalancer needs to have a FrontEnd IP Configuration Attached

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureStack::LbBackendAddressPool",
    "Properties" : {
        "<a href="#loadbalancerid" title="LoadbalancerId">LoadbalancerId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureStack::LbBackendAddressPool
Properties:
    <a href="#loadbalancerid" title="LoadbalancerId">LoadbalancerId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
</pre>

## Properties

#### LoadbalancerId

The ID of the LoadBalancer in which to create the Backend Address Pool.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the Backend Address Pool.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the resource group in which to create the resource.

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

#### BackendIpConfigurations

Returns the <code>BackendIpConfigurations</code> value.

#### Id

Returns the <code>Id</code> value.

#### LoadBalancingRules

Returns the <code>LoadBalancingRules</code> value.


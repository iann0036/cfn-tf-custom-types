# Terraform::AzureStack::LbNatPool

Manages a Load Balancer NAT pool.

~> **NOTE** When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureStack::LbNatPool",
    "Properties" : {
        "<a href="#backendport" title="BackendPort">BackendPort</a>" : <i>Double</i>,
        "<a href="#frontendipconfigurationname" title="FrontendIpConfigurationName">FrontendIpConfigurationName</a>" : <i>String</i>,
        "<a href="#frontendportend" title="FrontendPortEnd">FrontendPortEnd</a>" : <i>Double</i>,
        "<a href="#frontendportstart" title="FrontendPortStart">FrontendPortStart</a>" : <i>Double</i>,
        "<a href="#loadbalancerid" title="LoadbalancerId">LoadbalancerId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureStack::LbNatPool
Properties:
    <a href="#backendport" title="BackendPort">BackendPort</a>: <i>Double</i>
    <a href="#frontendipconfigurationname" title="FrontendIpConfigurationName">FrontendIpConfigurationName</a>: <i>String</i>
    <a href="#frontendportend" title="FrontendPortEnd">FrontendPortEnd</a>: <i>Double</i>
    <a href="#frontendportstart" title="FrontendPortStart">FrontendPortStart</a>: <i>Double</i>
    <a href="#loadbalancerid" title="LoadbalancerId">LoadbalancerId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
</pre>

## Properties

#### BackendPort

The port used for the internal endpoint. Possible values range between 1 and 65535, inclusive.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendIpConfigurationName

The name of the frontend IP configuration exposing this rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendPortEnd

The last port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendPortStart

The first port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadbalancerId

The ID of the Load Balancer in which to create the NAT pool.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the NAT pool.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The transport protocol for the external endpoint. Possible values are `Udp` or `Tcp`.

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

#### FrontendIpConfigurationId

Returns the <code>FrontendIpConfigurationId</code> value.


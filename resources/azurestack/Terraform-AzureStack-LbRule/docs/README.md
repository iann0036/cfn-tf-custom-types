# Terraform::AzureStack::LbRule

Manages a Load Balancer Rule.

~> **NOTE** When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureStack::LbRule",
    "Properties" : {
        "<a href="#backendaddresspoolid" title="BackendAddressPoolId">BackendAddressPoolId</a>" : <i>String</i>,
        "<a href="#backendport" title="BackendPort">BackendPort</a>" : <i>Double</i>,
        "<a href="#enablefloatingip" title="EnableFloatingIp">EnableFloatingIp</a>" : <i>Boolean</i>,
        "<a href="#frontendipconfigurationname" title="FrontendIpConfigurationName">FrontendIpConfigurationName</a>" : <i>String</i>,
        "<a href="#frontendport" title="FrontendPort">FrontendPort</a>" : <i>Double</i>,
        "<a href="#idletimeoutinminutes" title="IdleTimeoutInMinutes">IdleTimeoutInMinutes</a>" : <i>Double</i>,
        "<a href="#loaddistribution" title="LoadDistribution">LoadDistribution</a>" : <i>String</i>,
        "<a href="#loadbalancerid" title="LoadbalancerId">LoadbalancerId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#probeid" title="ProbeId">ProbeId</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureStack::LbRule
Properties:
    <a href="#backendaddresspoolid" title="BackendAddressPoolId">BackendAddressPoolId</a>: <i>String</i>
    <a href="#backendport" title="BackendPort">BackendPort</a>: <i>Double</i>
    <a href="#enablefloatingip" title="EnableFloatingIp">EnableFloatingIp</a>: <i>Boolean</i>
    <a href="#frontendipconfigurationname" title="FrontendIpConfigurationName">FrontendIpConfigurationName</a>: <i>String</i>
    <a href="#frontendport" title="FrontendPort">FrontendPort</a>: <i>Double</i>
    <a href="#idletimeoutinminutes" title="IdleTimeoutInMinutes">IdleTimeoutInMinutes</a>: <i>Double</i>
    <a href="#loaddistribution" title="LoadDistribution">LoadDistribution</a>: <i>String</i>
    <a href="#loadbalancerid" title="LoadbalancerId">LoadbalancerId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#probeid" title="ProbeId">ProbeId</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
</pre>

## Properties

#### BackendAddressPoolId

A reference to a Backend Address Pool over which this Load Balancing Rule operates.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BackendPort

The port used for internal connections on the endpoint. Possible values range between 1 and 65535, inclusive.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableFloatingIp

Floating IP is pertinent to failover scenarios: a "floating” IP is reassigned to a secondary server in case the primary server fails. Floating IP is required for SQL AlwaysOn.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendIpConfigurationName

The name of the frontend IP configuration to which the rule is associated.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendPort

The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 1 and 65534, inclusive.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeoutInMinutes

Specifies the timeout for the Tcp idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to Tcp.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadDistribution

Specifies the load balancing distribution type to be used by the Load Balancer. Possible values are: `Default` – The load balancer is configured to use a 5 tuple hash to map traffic to available servers. `SourceIP` – The load balancer is configured to use a 2 tuple hash to map traffic to available servers. `SourceIPProtocol` – The load balancer is configured to use a 3 tuple hash to map traffic to available servers. Also known as Session Persistence, where  the options are called `None`, `Client IP` and `Client IP and Protocol` respectively.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadbalancerId

The ID of the Load Balancer in which to create the Rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the LB Rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProbeId

A reference to a Probe used by this Load Balancing Rule.

_Required_: No

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


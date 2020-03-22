# Terraform::Alicloud::SlbMasterSlaveServerGroup

A master slave server group contains two ECS instances. The master slave server group can help you to define multiple listening dimension.

-> **NOTE:** One ECS instance can be added into multiple master slave server groups.

-> **NOTE:** One master slave server group can only add two ECS instances, which are master server and slave server.

-> **NOTE:** One master slave server group can be attached with tcp/udp listeners in one load balancer.

-> **NOTE:** One Classic and Internet load balancer, its master slave server group can add Classic and VPC ECS instances.

-> **NOTE:** One Classic and Intranet load balancer, its master slave server group can only add Classic ECS instances.

-> **NOTE:** One VPC load balancer, its master slave server group can only add the same VPC ECS instances.

-> **NOTE:** Available in 1.54.0+

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::SlbMasterSlaveServerGroup",
    "Properties" : {
        "<a href="#deleteprotectionvalidation" title="DeleteProtectionValidation">DeleteProtectionValidation</a>" : <i>Boolean</i>,
        "<a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#servers" title="Servers">Servers</a>" : <i>[ <a href="servers.md">Servers</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::SlbMasterSlaveServerGroup
Properties:
    <a href="#deleteprotectionvalidation" title="DeleteProtectionValidation">DeleteProtectionValidation</a>: <i>Boolean</i>
    <a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#servers" title="Servers">Servers</a>: <i>
      - <a href="servers.md">Servers</a></i>
</pre>

## Properties

#### DeleteProtectionValidation

Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerId

The Load Balancer ID which is used to launch a new master slave server group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the master slave server group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Servers

_Required_: No

_Type_: List of <a href="servers.md">Servers</a>

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


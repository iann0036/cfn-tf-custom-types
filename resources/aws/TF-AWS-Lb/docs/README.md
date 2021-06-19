# TF::AWS::Lb

Provides a Load Balancer resource.

~> **Note:** `aws_alb` is known as `aws_lb`. The functionality is identical.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Lb",
    "Properties" : {
        "<a href="#customerownedipv4pool" title="CustomerOwnedIpv4Pool">CustomerOwnedIpv4Pool</a>" : <i>String</i>,
        "<a href="#dropinvalidheaderfields" title="DropInvalidHeaderFields">DropInvalidHeaderFields</a>" : <i>Boolean</i>,
        "<a href="#enablecrosszoneloadbalancing" title="EnableCrossZoneLoadBalancing">EnableCrossZoneLoadBalancing</a>" : <i>Boolean</i>,
        "<a href="#enabledeletionprotection" title="EnableDeletionProtection">EnableDeletionProtection</a>" : <i>Boolean</i>,
        "<a href="#enablehttp2" title="EnableHttp2">EnableHttp2</a>" : <i>Boolean</i>,
        "<a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>" : <i>Double</i>,
        "<a href="#internal" title="Internal">Internal</a>" : <i>Boolean</i>,
        "<a href="#ipaddresstype" title="IpAddressType">IpAddressType</a>" : <i>String</i>,
        "<a href="#loadbalancertype" title="LoadBalancerType">LoadBalancerType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
        "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#subnets" title="Subnets">Subnets</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#accesslogs" title="AccessLogs">AccessLogs</a>" : <i>[ <a href="accesslogsdefinition.md">AccessLogsDefinition</a>, ... ]</i>,
        "<a href="#subnetmapping" title="SubnetMapping">SubnetMapping</a>" : <i>[ <a href="subnetmappingdefinition.md">SubnetMappingDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Lb
Properties:
    <a href="#customerownedipv4pool" title="CustomerOwnedIpv4Pool">CustomerOwnedIpv4Pool</a>: <i>String</i>
    <a href="#dropinvalidheaderfields" title="DropInvalidHeaderFields">DropInvalidHeaderFields</a>: <i>Boolean</i>
    <a href="#enablecrosszoneloadbalancing" title="EnableCrossZoneLoadBalancing">EnableCrossZoneLoadBalancing</a>: <i>Boolean</i>
    <a href="#enabledeletionprotection" title="EnableDeletionProtection">EnableDeletionProtection</a>: <i>Boolean</i>
    <a href="#enablehttp2" title="EnableHttp2">EnableHttp2</a>: <i>Boolean</i>
    <a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>: <i>Double</i>
    <a href="#internal" title="Internal">Internal</a>: <i>Boolean</i>
    <a href="#ipaddresstype" title="IpAddressType">IpAddressType</a>: <i>String</i>
    <a href="#loadbalancertype" title="LoadBalancerType">LoadBalancerType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
    <a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>
      - String</i>
    <a href="#subnets" title="Subnets">Subnets</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#accesslogs" title="AccessLogs">AccessLogs</a>: <i>
      - <a href="accesslogsdefinition.md">AccessLogsDefinition</a></i>
    <a href="#subnetmapping" title="SubnetMapping">SubnetMapping</a>: <i>
      - <a href="subnetmappingdefinition.md">SubnetMappingDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CustomerOwnedIpv4Pool

The ID of the customer owned ipv4 pool to use for this load balancer.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DropInvalidHeaderFields

Indicates whether HTTP headers with header fields that are not valid are removed by the load balancer (true) or routed to targets (false). The default is false. Elastic Load Balancing requires that message header names contain only alphanumeric characters and hyphens. Only valid for Load Balancers of type `application`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableCrossZoneLoadBalancing

If true, cross-zone load balancing of the load balancer will be enabled.
This is a `network` load balancer feature. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDeletionProtection

If true, deletion of the load balancer will be disabled via
the AWS API. This will prevent Terraform from deleting the load balancer. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableHttp2

Indicates whether HTTP/2 is enabled in `application` load balancers. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeout

The time in seconds that the connection is allowed to be idle. Only valid for Load Balancers of type `application`. Default: 60.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Internal

If true, the LB will be internal.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddressType

The type of IP addresses used by the subnets for your load balancer. The possible values are `ipv4` and `dualstack`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerType

The type of load balancer to create. Possible values are `application`, `gateway`, or `network`. The default value is `application`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the LB. This name must be unique within your AWS account, can have a maximum of 32 characters,
must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen. If not specified,
Terraform will autogenerate a name beginning with `tf-lb`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamePrefix

Creates a unique name beginning with the specified prefix. Conflicts with `name`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

A list of security group IDs to assign to the LB. Only valid for Load Balancers of type `application`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnets

A list of subnet IDs to attach to the LB. Subnets
cannot be updated for Load Balancers of type `network`. Changing this value
for load balancers of type `network` will force a recreation of the resource.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessLogs

_Required_: No

_Type_: List of <a href="accesslogsdefinition.md">AccessLogsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetMapping

_Required_: No

_Type_: List of <a href="subnetmappingdefinition.md">SubnetMappingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### ArnSuffix

Returns the <code>ArnSuffix</code> value.

#### DnsName

Returns the <code>DnsName</code> value.

#### Id

Returns the <code>Id</code> value.

#### VpcId

Returns the <code>VpcId</code> value.

#### ZoneId

Returns the <code>ZoneId</code> value.


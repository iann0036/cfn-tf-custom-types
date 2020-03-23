# Terraform::AWS::Elb

Provides an Elastic Load Balancer resource, also known as a "Classic
Load Balancer" after the release of
[Application/Network Load Balancers](/docs/providers/aws/r/lb.html).

~> **NOTE on ELB Instances and ELB Attachments:** Terraform currently
provides both a standalone [ELB Attachment resource](elb_attachment.html)
(describing an instance attached to an ELB), and an ELB resource with
`instances` defined in-line. At this time you cannot use an ELB with in-line
instances in conjunction with a ELB Attachment resources. Doing so will cause a
conflict and will overwrite attachments.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::Elb",
    "Properties" : {
        "<a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>" : <i>[ String, ... ]</i>,
        "<a href="#connectiondraining" title="ConnectionDraining">ConnectionDraining</a>" : <i>Boolean</i>,
        "<a href="#connectiondrainingtimeout" title="ConnectionDrainingTimeout">ConnectionDrainingTimeout</a>" : <i>Double</i>,
        "<a href="#crosszoneloadbalancing" title="CrossZoneLoadBalancing">CrossZoneLoadBalancing</a>" : <i>Boolean</i>,
        "<a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>" : <i>Double</i>,
        "<a href="#instances" title="Instances">Instances</a>" : <i>[ String, ... ]</i>,
        "<a href="#internal" title="Internal">Internal</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
        "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#sourcesecuritygroup" title="SourceSecurityGroup">SourceSecurityGroup</a>" : <i>String</i>,
        "<a href="#subnets" title="Subnets">Subnets</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#accesslogs" title="AccessLogs">AccessLogs</a>" : <i>[ <a href="accesslogs.md">AccessLogs</a>, ... ]</i>,
        "<a href="#healthcheck" title="HealthCheck">HealthCheck</a>" : <i>[ <a href="healthcheck.md">HealthCheck</a>, ... ]</i>,
        "<a href="#listener" title="Listener">Listener</a>" : <i>[ <a href="listener.md">Listener</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::Elb
Properties:
    <a href="#availabilityzones" title="AvailabilityZones">AvailabilityZones</a>: <i>
      - String</i>
    <a href="#connectiondraining" title="ConnectionDraining">ConnectionDraining</a>: <i>Boolean</i>
    <a href="#connectiondrainingtimeout" title="ConnectionDrainingTimeout">ConnectionDrainingTimeout</a>: <i>Double</i>
    <a href="#crosszoneloadbalancing" title="CrossZoneLoadBalancing">CrossZoneLoadBalancing</a>: <i>Boolean</i>
    <a href="#idletimeout" title="IdleTimeout">IdleTimeout</a>: <i>Double</i>
    <a href="#instances" title="Instances">Instances</a>: <i>
      - String</i>
    <a href="#internal" title="Internal">Internal</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
    <a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>
      - String</i>
    <a href="#sourcesecuritygroup" title="SourceSecurityGroup">SourceSecurityGroup</a>: <i>String</i>
    <a href="#subnets" title="Subnets">Subnets</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#accesslogs" title="AccessLogs">AccessLogs</a>: <i>
      - <a href="accesslogs.md">AccessLogs</a></i>
    <a href="#healthcheck" title="HealthCheck">HealthCheck</a>: <i>
      - <a href="healthcheck.md">HealthCheck</a></i>
    <a href="#listener" title="Listener">Listener</a>: <i>
      - <a href="listener.md">Listener</a></i>
</pre>

## Properties

#### AvailabilityZones

The AZ's to serve traffic in.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionDraining

Boolean to enable connection draining. Default: `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionDrainingTimeout

The time in seconds to allow for connections to drain. Default: `300`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrossZoneLoadBalancing

Enable cross-zone load balancing. Default: `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeout

The time in seconds that the connection is allowed to be idle. Default: `60`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Instances

A list of instance ids to place in the ELB pool.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Internal

If true, ELB will be an internal ELB.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the ELB. By default generated by Terraform.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamePrefix

Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

A list of security group IDs to assign to the ELB.
Only valid if creating an ELB within a VPC.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceSecurityGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnets

A list of subnet IDs to attach to the ELB.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessLogs

_Required_: No

_Type_: List of <a href="accesslogs.md">AccessLogs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheck

_Required_: No

_Type_: List of <a href="healthcheck.md">HealthCheck</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Listener

_Required_: No

_Type_: List of <a href="listener.md">Listener</a>

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

#### DnsName

Returns the <code>DnsName</code> value.

#### Id

Returns the <code>Id</code> value.

#### SourceSecurityGroupId

Returns the <code>SourceSecurityGroupId</code> value.

#### ZoneId

Returns the <code>ZoneId</code> value.


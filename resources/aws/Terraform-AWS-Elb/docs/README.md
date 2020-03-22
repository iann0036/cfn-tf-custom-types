# Terraform::AWS::Elb

CloudFormation equivalent of aws_elb

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

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionDraining

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionDrainingTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrossZoneLoadBalancing

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Instances

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Internal

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamePrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceSecurityGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnets

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

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

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

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


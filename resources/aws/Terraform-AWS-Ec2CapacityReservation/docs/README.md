# Terraform::AWS::Ec2CapacityReservation

Provides an EC2 Capacity Reservation. This allows you to reserve capacity for your Amazon EC2 instances in a specific Availability Zone for any duration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::Ec2CapacityReservation",
    "Properties" : {
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#ebsoptimized" title="EbsOptimized">EbsOptimized</a>" : <i>Boolean</i>,
        "<a href="#enddate" title="EndDate">EndDate</a>" : <i>String</i>,
        "<a href="#enddatetype" title="EndDateType">EndDateType</a>" : <i>String</i>,
        "<a href="#ephemeralstorage" title="EphemeralStorage">EphemeralStorage</a>" : <i>Boolean</i>,
        "<a href="#instancecount" title="InstanceCount">InstanceCount</a>" : <i>Double</i>,
        "<a href="#instancematchcriteria" title="InstanceMatchCriteria">InstanceMatchCriteria</a>" : <i>String</i>,
        "<a href="#instanceplatform" title="InstancePlatform">InstancePlatform</a>" : <i>String</i>,
        "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#tenancy" title="Tenancy">Tenancy</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::Ec2CapacityReservation
Properties:
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#ebsoptimized" title="EbsOptimized">EbsOptimized</a>: <i>Boolean</i>
    <a href="#enddate" title="EndDate">EndDate</a>: <i>String</i>
    <a href="#enddatetype" title="EndDateType">EndDateType</a>: <i>String</i>
    <a href="#ephemeralstorage" title="EphemeralStorage">EphemeralStorage</a>: <i>Boolean</i>
    <a href="#instancecount" title="InstanceCount">InstanceCount</a>: <i>Double</i>
    <a href="#instancematchcriteria" title="InstanceMatchCriteria">InstanceMatchCriteria</a>: <i>String</i>
    <a href="#instanceplatform" title="InstancePlatform">InstancePlatform</a>: <i>String</i>
    <a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#tenancy" title="Tenancy">Tenancy</a>: <i>String</i>
</pre>

## Properties

#### AvailabilityZone

The Availability Zone in which to create the Capacity Reservation.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EbsOptimized

Indicates whether the Capacity Reservation supports EBS-optimized instances.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndDate

The date and time at which the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. Valid values: [RFC3339 time string](https://tools.ietf.org/html/rfc3339#section-5.8) (`YYYY-MM-DDTHH:MM:SSZ`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndDateType

Indicates the way in which the Capacity Reservation ends. Specify either `unlimited` or `limited`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EphemeralStorage

Indicates whether the Capacity Reservation supports instances with temporary, block-level storage.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceCount

The number of instances for which to reserve capacity.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceMatchCriteria

Indicates the type of instance launches that the Capacity Reservation accepts. Specify either `open` or `targeted`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstancePlatform

The type of operating system for which to reserve capacity. Valid options are `Linux/UNIX`, `Red Hat Enterprise Linux`, `SUSE Linux`, `Windows`, `Windows with SQL Server`, `Windows with SQL Server Enterprise`, `Windows with SQL Server Standard` or `Windows with SQL Server Web`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

The instance type for which to reserve capacity.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tenancy

Indicates the tenancy of the Capacity Reservation. Specify either `default` or `dedicated`.

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


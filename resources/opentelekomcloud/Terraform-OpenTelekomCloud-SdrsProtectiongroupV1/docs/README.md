# Terraform::OpenTelekomCloud::SdrsProtectiongroupV1

Manages a SDRS protection group resource within OpenTelekomCloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::SdrsProtectiongroupV1",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#domainid" title="DomainId">DomainId</a>" : <i>String</i>,
        "<a href="#drtype" title="DrType">DrType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#sourceavailabilityzone" title="SourceAvailabilityZone">SourceAvailabilityZone</a>" : <i>String</i>,
        "<a href="#sourcevpcid" title="SourceVpcId">SourceVpcId</a>" : <i>String</i>,
        "<a href="#targetavailabilityzone" title="TargetAvailabilityZone">TargetAvailabilityZone</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::SdrsProtectiongroupV1
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#domainid" title="DomainId">DomainId</a>: <i>String</i>
    <a href="#drtype" title="DrType">DrType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#sourceavailabilityzone" title="SourceAvailabilityZone">SourceAvailabilityZone</a>: <i>String</i>
    <a href="#sourcevpcid" title="SourceVpcId">SourceVpcId</a>: <i>String</i>
    <a href="#targetavailabilityzone" title="TargetAvailabilityZone">TargetAvailabilityZone</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Description

The description of a protection group. Changing this creates a new group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainId

Specifies the ID of an active-active domain. Changing this creates a new group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrType

Specifies the deployment model. The default value is migration indicating migration within a VPC.
Changing this creates a new group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of a protection group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAvailabilityZone

Specifies the source AZ of a protection group. Changing this creates a new group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceVpcId

Specifies the ID of the source VPC. Changing this creates a new group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetAvailabilityZone

Specifies the target AZ of a protection group. Changing this creates a new group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

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


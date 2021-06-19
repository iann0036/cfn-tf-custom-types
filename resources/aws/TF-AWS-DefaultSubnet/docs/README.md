# TF::AWS::DefaultSubnet

Provides a resource to manage a [default AWS VPC subnet](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/default-vpc.html#default-vpc-basics) in the current region.

The `aws_default_subnet` behaves differently from normal resources, in that Terraform does not _create_ this resource but instead "adopts" it into management.

The `aws_default_subnet` resource allows you to manage a region's default VPC subnet but Terraform cannot destroy it. Removing this resource from your configuration will remove it from your statefile and Terraform management.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::DefaultSubnet",
    "Properties" : {
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#customerownedipv4pool" title="CustomerOwnedIpv4Pool">CustomerOwnedIpv4Pool</a>" : <i>String</i>,
        "<a href="#mapcustomerownediponlaunch" title="MapCustomerOwnedIpOnLaunch">MapCustomerOwnedIpOnLaunch</a>" : <i>Boolean</i>,
        "<a href="#mappubliciponlaunch" title="MapPublicIpOnLaunch">MapPublicIpOnLaunch</a>" : <i>Boolean</i>,
        "<a href="#outpostarn" title="OutpostArn">OutpostArn</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::DefaultSubnet
Properties:
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#customerownedipv4pool" title="CustomerOwnedIpv4Pool">CustomerOwnedIpv4Pool</a>: <i>String</i>
    <a href="#mapcustomerownediponlaunch" title="MapCustomerOwnedIpOnLaunch">MapCustomerOwnedIpOnLaunch</a>: <i>Boolean</i>
    <a href="#mappubliciponlaunch" title="MapPublicIpOnLaunch">MapPublicIpOnLaunch</a>: <i>Boolean</i>
    <a href="#outpostarn" title="OutpostArn">OutpostArn</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AvailabilityZone

AZ for the subnet.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerOwnedIpv4Pool

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MapCustomerOwnedIpOnLaunch

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MapPublicIpOnLaunch

Whether instances launched into the subnet should be assigned a public IP address.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutpostArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Map of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

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

#### AssignIpv6AddressOnCreation

Returns the <code>AssignIpv6AddressOnCreation</code> value.

#### AvailabilityZoneId

Returns the <code>AvailabilityZoneId</code> value.

#### CidrBlock

Returns the <code>CidrBlock</code> value.

#### Id

Returns the <code>Id</code> value.

#### Ipv6CidrBlock

Returns the <code>Ipv6CidrBlock</code> value.

#### Ipv6CidrBlockAssociationId

Returns the <code>Ipv6CidrBlockAssociationId</code> value.

#### OwnerId

Returns the <code>OwnerId</code> value.

#### VpcId

Returns the <code>VpcId</code> value.


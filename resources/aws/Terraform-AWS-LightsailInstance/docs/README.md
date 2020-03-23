# Terraform::AWS::LightsailInstance

Provides a Lightsail Instance. Amazon Lightsail is a service to provide easy virtual private servers
with custom software already setup. See [What is Amazon Lightsail?](https://lightsail.aws.amazon.com/ls/docs/getting-started/article/what-is-amazon-lightsail)
for more information.

~> **Note:** Lightsail is currently only supported in a limited number of AWS Regions, please see ["Regions and Availability Zones in Amazon Lightsail"](https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail) for more details

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::LightsailInstance",
    "Properties" : {
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#blueprintid" title="BlueprintId">BlueprintId</a>" : <i>String</i>,
        "<a href="#bundleid" title="BundleId">BundleId</a>" : <i>String</i>,
        "<a href="#keypairname" title="KeyPairName">KeyPairName</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::LightsailInstance
Properties:
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#blueprintid" title="BlueprintId">BlueprintId</a>: <i>String</i>
    <a href="#bundleid" title="BundleId">BundleId</a>: <i>String</i>
    <a href="#keypairname" title="KeyPairName">KeyPairName</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
</pre>

## Properties

#### AvailabilityZone

The Availability Zone in which to create your
instance (see list below).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlueprintId

The ID for a virtual private server image
(see list below).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BundleId

The bundle of specification information (see list below).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyPairName

The name of your key pair. Created in the
Lightsail console (cannot use `aws_key_pair` at this time).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Lightsail Instance. Names be unique within each AWS Region in your Lightsail account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

launch script to configure server with additional user data.

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

#### Arn

Returns the <code>Arn</code> value.

#### CpuCount

Returns the <code>CpuCount</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Id

Returns the <code>Id</code> value.

#### Ipv6Address

Returns the <code>Ipv6Address</code> value.

#### IsStaticIp

Returns the <code>IsStaticIp</code> value.

#### PrivateIpAddress

Returns the <code>PrivateIpAddress</code> value.

#### PublicIpAddress

Returns the <code>PublicIpAddress</code> value.

#### RamSize

Returns the <code>RamSize</code> value.

#### Username

Returns the <code>Username</code> value.


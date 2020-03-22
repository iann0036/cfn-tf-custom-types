# Terraform::DigitalOcean::FloatingIpAssignment

Provides a resource for assigning an existing DigitalOcean Floating IP to a Droplet. This
makes it easy to provision floating IP addresses that are not tied to the lifecycle of your
Droplet.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::DigitalOcean::FloatingIpAssignment",
    "Properties" : {
        "<a href="#dropletid" title="DropletId">DropletId</a>" : <i>Double</i>,
        "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::DigitalOcean::FloatingIpAssignment
Properties:
    <a href="#dropletid" title="DropletId">DropletId</a>: <i>Double</i>
    <a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
</pre>

## Properties

#### DropletId

The ID of Droplet that the Floating IP will be assigned to.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

The Floating IP to assign to the Droplet.

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

#### Id

Returns the <code>Id</code> value.


# Terraform::Skytap::Network

Provides a Skytap Network resource. Networks are not top-level elements of the Skytap API.
Rather, they are elements properly contained within an environment.
Operations on them are implicitly on the containing environment.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Skytap::Network",
    "Properties" : {
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#environmentid" title="EnvironmentId">EnvironmentId</a>" : <i>String</i>,
        "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#subnet" title="Subnet">Subnet</a>" : <i>String</i>,
        "<a href="#tunnelable" title="Tunnelable">Tunnelable</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Skytap::Network
Properties:
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#environmentid" title="EnvironmentId">EnvironmentId</a>: <i>String</i>
    <a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#subnet" title="Subnet">Subnet</a>: <i>String</i>
    <a href="#tunnelable" title="Tunnelable">Tunnelable</a>: <i>Boolean</i>
</pre>

## Properties

#### Domain

Domain name for the Skytap network. Limited to 64 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentId

ID of the environment you want to attach the network to. If updating with a new one then the network will be recreated.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

Gateway IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

User-defined name of the network. Limited to 255 characters. UTF-8 character type.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

Defines the subnet address and subnet mask size in CIDR format (for example, 10.0.0.0/24). IP addresses for the VMs are assigned from this subnet and standard network services (DNS resolution, CIFS share, routes to Internet) are defined appropriately for it.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tunnelable

If true, this network can be connected to other networks.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.


# Terraform::CloudStack::VpnCustomerGateway

Creates a site to site VPN local customer gateway.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::CloudStack::VpnCustomerGateway",
    "Properties" : {
        "<a href="#cidr" title="Cidr">Cidr</a>" : <i>String</i>,
        "<a href="#dpd" title="Dpd">Dpd</a>" : <i>Boolean</i>,
        "<a href="#esplifetime" title="EspLifetime">EspLifetime</a>" : <i>Double</i>,
        "<a href="#esppolicy" title="EspPolicy">EspPolicy</a>" : <i>String</i>,
        "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>,
        "<a href="#ikelifetime" title="IkeLifetime">IkeLifetime</a>" : <i>Double</i>,
        "<a href="#ikepolicy" title="IkePolicy">IkePolicy</a>" : <i>String</i>,
        "<a href="#ipsecpsk" title="IpsecPsk">IpsecPsk</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::CloudStack::VpnCustomerGateway
Properties:
    <a href="#cidr" title="Cidr">Cidr</a>: <i>String</i>
    <a href="#dpd" title="Dpd">Dpd</a>: <i>Boolean</i>
    <a href="#esplifetime" title="EspLifetime">EspLifetime</a>: <i>Double</i>
    <a href="#esppolicy" title="EspPolicy">EspPolicy</a>: <i>String</i>
    <a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
    <a href="#ikelifetime" title="IkeLifetime">IkeLifetime</a>: <i>Double</i>
    <a href="#ikepolicy" title="IkePolicy">IkePolicy</a>: <i>String</i>
    <a href="#ipsecpsk" title="IpsecPsk">IpsecPsk</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
</pre>

## Properties

#### Cidr

The CIDR block that needs to be routed through this gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dpd

If DPD is enabled for the related VPN connection (defaults false).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EspLifetime

The ESP lifetime of phase 2 VPN connection to this
VPN Customer Gateway in seconds (defaults 86400).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EspPolicy

The ESP policy to use for this VPN Customer Gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

The public IP address of the related VPN Gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkeLifetime

The IKE lifetime of phase 2 VPN connection to this
VPN Customer Gateway in seconds (defaults 86400).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IkePolicy

The IKE policy to use for this VPN Customer Gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecPsk

The IPSEC pre-shared key used for this gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the VPN Customer Gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The name or ID of the project to create this VPN Customer
Gateway in. Changing this forces a new resource to be created.

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


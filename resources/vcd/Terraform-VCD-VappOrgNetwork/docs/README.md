# Terraform::VCD::VappOrgNetwork

Provides capability to attach an existing Org VDC Network to a vApp and toggle network features.

Supported in provider *v2.7+*

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VCD::VappOrgNetwork",
    "Properties" : {
        "<a href="#firewallenabled" title="FirewallEnabled">FirewallEnabled</a>" : <i>Boolean</i>,
        "<a href="#isfenced" title="IsFenced">IsFenced</a>" : <i>Boolean</i>,
        "<a href="#natenabled" title="NatEnabled">NatEnabled</a>" : <i>Boolean</i>,
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#orgnetworkname" title="OrgNetworkName">OrgNetworkName</a>" : <i>String</i>,
        "<a href="#retainipmacenabled" title="RetainIpMacEnabled">RetainIpMacEnabled</a>" : <i>Boolean</i>,
        "<a href="#vappname" title="VappName">VappName</a>" : <i>String</i>,
        "<a href="#vdc" title="Vdc">Vdc</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VCD::VappOrgNetwork
Properties:
    <a href="#firewallenabled" title="FirewallEnabled">FirewallEnabled</a>: <i>Boolean</i>
    <a href="#isfenced" title="IsFenced">IsFenced</a>: <i>Boolean</i>
    <a href="#natenabled" title="NatEnabled">NatEnabled</a>: <i>Boolean</i>
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#orgnetworkname" title="OrgNetworkName">OrgNetworkName</a>: <i>String</i>
    <a href="#retainipmacenabled" title="RetainIpMacEnabled">RetainIpMacEnabled</a>: <i>Boolean</i>
    <a href="#vappname" title="VappName">VappName</a>: <i>String</i>
    <a href="#vdc" title="Vdc">Vdc</a>: <i>String</i>
</pre>

## Properties

#### FirewallEnabled

Firewall service enabled or disabled. Configurable when `is_fenced` is true. Default is true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsFenced

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NatEnabled

NAT service enabled or disabled. Configurable when `is_fenced` and `firewall_enabled` is true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

The name of organization to use, optional if defined at provider level. Useful when
connected as sysadmin working across different organisations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrgNetworkName

An Org network name to which vApp network is connected. If not configured, then an isolated network is created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetainIpMacEnabled

Specifies whether the network resources such as IP/MAC of router will be retained across deployments. Configurable when `is_fenced` is true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VappName

The vApp this network belongs to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdc

The name of VDC to use, optional if defined at provider level.

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


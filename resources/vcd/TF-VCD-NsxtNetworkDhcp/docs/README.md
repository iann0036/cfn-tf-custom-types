# TF::VCD::NsxtNetworkDhcp

Provides a resource to manage DHCP pools for NSX-T Org VDC Routed network.

Supported in provider *v3.2+* and VCD 10.1+ with NSX-T backed VDCs.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VCD::NsxtNetworkDhcp",
    "Properties" : {
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#orgnetworkid" title="OrgNetworkId">OrgNetworkId</a>" : <i>String</i>,
        "<a href="#vdc" title="Vdc">Vdc</a>" : <i>String</i>,
        "<a href="#pool" title="Pool">Pool</a>" : <i>[ <a href="pooldefinition.md">PoolDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VCD::NsxtNetworkDhcp
Properties:
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#orgnetworkid" title="OrgNetworkId">OrgNetworkId</a>: <i>String</i>
    <a href="#vdc" title="Vdc">Vdc</a>: <i>String</i>
    <a href="#pool" title="Pool">Pool</a>: <i>
      - <a href="pooldefinition.md">PoolDefinition</a></i>
</pre>

## Properties

#### Org

The name of organization to use, optional if defined at provider level. Useful
when connected as sysadmin working across different organisations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrgNetworkId

ID of parent Org VDC Routed network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdc

The name of VDC to use, optional if defined at provider level.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pool

_Required_: No

_Type_: List of <a href="pooldefinition.md">PoolDefinition</a>

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


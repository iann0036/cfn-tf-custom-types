# Terraform::BIGIP::LtmSnat

`bigip_ltm_snat` Manages a snat configuration

For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::BIGIP::LtmSnat",
    "Properties" : {
        "<a href="#autolasthop" title="Autolasthop">Autolasthop</a>" : <i>String</i>,
        "<a href="#fullpath" title="FullPath">FullPath</a>" : <i>String</i>,
        "<a href="#mirror" title="Mirror">Mirror</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#partition" title="Partition">Partition</a>" : <i>String</i>,
        "<a href="#snatpool" title="Snatpool">Snatpool</a>" : <i>String</i>,
        "<a href="#sourceport" title="Sourceport">Sourceport</a>" : <i>String</i>,
        "<a href="#translation" title="Translation">Translation</a>" : <i>String</i>,
        "<a href="#vlans" title="Vlans">Vlans</a>" : <i>[ String, ... ]</i>,
        "<a href="#vlansdisabled" title="Vlansdisabled">Vlansdisabled</a>" : <i>Boolean</i>,
        "<a href="#origins" title="Origins">Origins</a>" : <i>[ <a href="origins.md">Origins</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::BIGIP::LtmSnat
Properties:
    <a href="#autolasthop" title="Autolasthop">Autolasthop</a>: <i>String</i>
    <a href="#fullpath" title="FullPath">FullPath</a>: <i>String</i>
    <a href="#mirror" title="Mirror">Mirror</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#partition" title="Partition">Partition</a>: <i>String</i>
    <a href="#snatpool" title="Snatpool">Snatpool</a>: <i>String</i>
    <a href="#sourceport" title="Sourceport">Sourceport</a>: <i>String</i>
    <a href="#translation" title="Translation">Translation</a>: <i>String</i>
    <a href="#vlans" title="Vlans">Vlans</a>: <i>
      - String</i>
    <a href="#vlansdisabled" title="Vlansdisabled">Vlansdisabled</a>: <i>Boolean</i>
    <a href="#origins" title="Origins">Origins</a>: <i>
      - <a href="origins.md">Origins</a></i>
</pre>

## Properties

#### Autolasthop

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FullPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mirror

Enables or disables mirroring of SNAT connections.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the snat.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Partition

Displays the administrative partition within which this profile resides.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Snatpool

Specifies the name of a SNAT pool. You can only use this option when automap and translation are not used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sourceport

Specifies whether the system preserves the source port of the connection. The default is preserve. Use of the preserve-strict setting should be restricted to UDP only under very special circumstances such as nPath or transparent (that is, no translation of any other L3/L4 field), where there is a 1:1 relationship between virtual IP addresses and node addresses, or when clustered multi-processing (CMP) is disabled. The change setting is useful for obfuscating internal network addresses.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Translation

Specifies the name of a translated IP address. Note that translated addresses are outside the traffic management system. You can only use this option when automap and snatpool are not used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vlans

Specifies the name of the VLAN to which you want to assign the SNAT. The default is vlans-enabled.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vlansdisabled

Disables the SNAT on all VLANs.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Origins

_Required_: No

_Type_: List of <a href="origins.md">Origins</a>

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


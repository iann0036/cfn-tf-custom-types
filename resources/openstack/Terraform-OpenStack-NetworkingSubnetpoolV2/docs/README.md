# Terraform::OpenStack::NetworkingSubnetpoolV2

Manages a V2 Neutron subnetpool resource within OpenStack.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::NetworkingSubnetpoolV2",
    "Properties" : {
        "<a href="#addressscopeid" title="AddressScopeId">AddressScopeId</a>" : <i>String</i>,
        "<a href="#defaultprefixlen" title="DefaultPrefixlen">DefaultPrefixlen</a>" : <i>Double</i>,
        "<a href="#defaultquota" title="DefaultQuota">DefaultQuota</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#ipversion" title="IpVersion">IpVersion</a>" : <i>Double</i>,
        "<a href="#isdefault" title="IsDefault">IsDefault</a>" : <i>Boolean</i>,
        "<a href="#maxprefixlen" title="MaxPrefixlen">MaxPrefixlen</a>" : <i>Double</i>,
        "<a href="#minprefixlen" title="MinPrefixlen">MinPrefixlen</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#prefixes" title="Prefixes">Prefixes</a>" : <i>[ String, ... ]</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#shared" title="Shared">Shared</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#valuespecs" title="ValueSpecs">ValueSpecs</a>" : <i>[ <a href="valuespecs.md">ValueSpecs</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::NetworkingSubnetpoolV2
Properties:
    <a href="#addressscopeid" title="AddressScopeId">AddressScopeId</a>: <i>String</i>
    <a href="#defaultprefixlen" title="DefaultPrefixlen">DefaultPrefixlen</a>: <i>Double</i>
    <a href="#defaultquota" title="DefaultQuota">DefaultQuota</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#ipversion" title="IpVersion">IpVersion</a>: <i>Double</i>
    <a href="#isdefault" title="IsDefault">IsDefault</a>: <i>Boolean</i>
    <a href="#maxprefixlen" title="MaxPrefixlen">MaxPrefixlen</a>: <i>Double</i>
    <a href="#minprefixlen" title="MinPrefixlen">MinPrefixlen</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#prefixes" title="Prefixes">Prefixes</a>: <i>
      - String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#shared" title="Shared">Shared</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#valuespecs" title="ValueSpecs">ValueSpecs</a>: <i>
      - <a href="valuespecs.md">ValueSpecs</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AddressScopeId

The Neutron address scope to assign to the
subnetpool. Changing this updates the address scope id of the existing
subnetpool.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultPrefixlen

The size of the prefix to allocate when the cidr
or prefixlen attributes are omitted when you create the subnet. Defaults to the
MinPrefixLen. Changing this updates the default prefixlen of the existing
subnetpool.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultQuota

The per-project quota on the prefix space that can be
allocated from the subnetpool for project subnets. Changing this updates the
default quota of the existing subnetpool.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The human-readable description for the subnetpool.
Changing this updates the description of the existing subnetpool.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpVersion

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsDefault

Indicates whether the subnetpool is default
subnetpool or not. Changing this updates the default status of the existing
subnetpool.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxPrefixlen

The maximum prefix size that can be allocated from
the subnetpool. For IPv4 subnetpools, default is 32. For IPv6 subnetpools,
default is 128. Changing this updates the max prefixlen of the existing
subnetpool.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinPrefixlen

The smallest prefix that can be allocated from a
subnetpool. For IPv4 subnetpools, default is 8. For IPv6 subnetpools, default
is 64. Changing this updates the min prefixlen of the existing subnetpool.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the subnetpool. Changing this updates the name of
the existing subnetpool.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefixes

A list of subnet prefixes to assign to the subnetpool.
Neutron API merges adjacent prefixes and treats them as a single prefix. Each
subnet prefix must be unique among all subnet prefixes in all subnetpools that
are associated with the address scope. Changing this updates the prefixes list
of the existing subnetpool.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

The owner of the subnetpool. Required if admin wants to
create a subnetpool for another project. Changing this creates a new subnetpool.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnetpool. If omitted, the
`region` argument of the provider is used. Changing this creates a new
subnetpool.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shared

Indicates whether this subnetpool is shared across
all projects. Changing this updates the shared status of the existing
subnetpool.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A set of string tags for the subnetpool.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueSpecs

Map of additional options.

_Required_: No

_Type_: List of <a href="valuespecs.md">ValueSpecs</a>

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

#### AllTags

Returns the <code>AllTags</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Id

Returns the <code>Id</code> value.

#### RevisionNumber

Returns the <code>RevisionNumber</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.


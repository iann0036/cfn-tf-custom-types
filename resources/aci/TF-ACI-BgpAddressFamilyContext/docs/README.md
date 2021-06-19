# TF::ACI::BgpAddressFamilyContext

Manages ACI BGP Address Family Context

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::BgpAddressFamilyContext",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#ctrl" title="Ctrl">Ctrl</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#edist" title="EDist">EDist</a>" : <i>String</i>,
        "<a href="#idist" title="IDist">IDist</a>" : <i>String</i>,
        "<a href="#localdist" title="LocalDist">LocalDist</a>" : <i>String</i>,
        "<a href="#maxecmp" title="MaxEcmp">MaxEcmp</a>" : <i>String</i>,
        "<a href="#maxecmpibgp" title="MaxEcmpIbgp">MaxEcmpIbgp</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#tenantdn" title="TenantDn">TenantDn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::BgpAddressFamilyContext
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#ctrl" title="Ctrl">Ctrl</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#edist" title="EDist">EDist</a>: <i>String</i>
    <a href="#idist" title="IDist">IDist</a>: <i>String</i>
    <a href="#localdist" title="LocalDist">LocalDist</a>: <i>String</i>
    <a href="#maxecmp" title="MaxEcmp">MaxEcmp</a>: <i>String</i>
    <a href="#maxecmpibgp" title="MaxEcmpIbgp">MaxEcmpIbgp</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#tenantdn" title="TenantDn">TenantDn</a>: <i>String</i>
</pre>

## Properties

#### Annotation

Annotation for BGP address family context object.
- `ctrl` - (Optional) Control state for BGP address family context object. Allowed value is "host-rt-leak".
- `e_dist` - (Optional) Administrative distance of EBGP routes for BGP address family context object. Default value is "20".
- `i_dist` - (Optional) Administrative distance of IBGP routes for BGP address family context object. Default value is "200".
- `local_dist` - (Optional) Administrative distance of local routes for BGP address family context object. Default value is "220".
- `max_ecmp` - (Optional) Maximum number of equal-cost paths for BGP address family context object. Default value is "16".
- `max_ecmp_ibgp` - (Optional) Maximum ECMP IBGP for BGP address family context object. Default value is "16".
- `name_alias` - (Optional) Name alias for BGP address family context object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ctrl

Control state for BGP address family context object. Allowed value is "host-rt-leak".
- `e_dist` - (Optional) Administrative distance of EBGP routes for BGP address family context object. Default value is "20".
- `i_dist` - (Optional) Administrative distance of IBGP routes for BGP address family context object. Default value is "200".
- `local_dist` - (Optional) Administrative distance of local routes for BGP address family context object. Default value is "220".
- `max_ecmp` - (Optional) Maximum number of equal-cost paths for BGP address family context object. Default value is "16".
- `max_ecmp_ibgp` - (Optional) Maximum ECMP IBGP for BGP address family context object. Default value is "16".
- `name_alias` - (Optional) Name alias for BGP address family context object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description for BGP address family context object.
- `annotation` - (Optional) Annotation for BGP address family context object.
- `ctrl` - (Optional) Control state for BGP address family context object. Allowed value is "host-rt-leak".
- `e_dist` - (Optional) Administrative distance of EBGP routes for BGP address family context object. Default value is "20".
- `i_dist` - (Optional) Administrative distance of IBGP routes for BGP address family context object. Default value is "200".
- `local_dist` - (Optional) Administrative distance of local routes for BGP address family context object. Default value is "220".
- `max_ecmp` - (Optional) Maximum number of equal-cost paths for BGP address family context object. Default value is "16".
- `max_ecmp_ibgp` - (Optional) Maximum ECMP IBGP for BGP address family context object. Default value is "16".
- `name_alias` - (Optional) Name alias for BGP address family context object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EDist

Administrative distance of EBGP routes for BGP address family context object. Default value is "20".
- `i_dist` - (Optional) Administrative distance of IBGP routes for BGP address family context object. Default value is "200".
- `local_dist` - (Optional) Administrative distance of local routes for BGP address family context object. Default value is "220".
- `max_ecmp` - (Optional) Maximum number of equal-cost paths for BGP address family context object. Default value is "16".
- `max_ecmp_ibgp` - (Optional) Maximum ECMP IBGP for BGP address family context object. Default value is "16".
- `name_alias` - (Optional) Name alias for BGP address family context object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IDist

Administrative distance of IBGP routes for BGP address family context object. Default value is "200".
- `local_dist` - (Optional) Administrative distance of local routes for BGP address family context object. Default value is "220".
- `max_ecmp` - (Optional) Maximum number of equal-cost paths for BGP address family context object. Default value is "16".
- `max_ecmp_ibgp` - (Optional) Maximum ECMP IBGP for BGP address family context object. Default value is "16".
- `name_alias` - (Optional) Name alias for BGP address family context object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalDist

Administrative distance of local routes for BGP address family context object. Default value is "220".
- `max_ecmp` - (Optional) Maximum number of equal-cost paths for BGP address family context object. Default value is "16".
- `max_ecmp_ibgp` - (Optional) Maximum ECMP IBGP for BGP address family context object. Default value is "16".
- `name_alias` - (Optional) Name alias for BGP address family context object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxEcmp

Maximum number of equal-cost paths for BGP address family context object. Default value is "16".
- `max_ecmp_ibgp` - (Optional) Maximum ECMP IBGP for BGP address family context object. Default value is "16".
- `name_alias` - (Optional) Name alias for BGP address family context object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxEcmpIbgp

Maximum ECMP IBGP for BGP address family context object. Default value is "16".
- `name_alias` - (Optional) Name alias for BGP address family context object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of BGP address family context object.
- `description` - (Optional) Description for BGP address family context object.
- `annotation` - (Optional) Annotation for BGP address family context object.
- `ctrl` - (Optional) Control state for BGP address family context object. Allowed value is "host-rt-leak".
- `e_dist` - (Optional) Administrative distance of EBGP routes for BGP address family context object. Default value is "20".
- `i_dist` - (Optional) Administrative distance of IBGP routes for BGP address family context object. Default value is "200".
- `local_dist` - (Optional) Administrative distance of local routes for BGP address family context object. Default value is "220".
- `max_ecmp` - (Optional) Maximum number of equal-cost paths for BGP address family context object. Default value is "16".
- `max_ecmp_ibgp` - (Optional) Maximum ECMP IBGP for BGP address family context object. Default value is "16".
- `name_alias` - (Optional) Name alias for BGP address family context object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

Name alias for BGP address family context object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantDn

Distinguished name of parent tenant object.
- `name` - (Required) Name of BGP address family context object.
- `description` - (Optional) Description for BGP address family context object.
- `annotation` - (Optional) Annotation for BGP address family context object.
- `ctrl` - (Optional) Control state for BGP address family context object. Allowed value is "host-rt-leak".
- `e_dist` - (Optional) Administrative distance of EBGP routes for BGP address family context object. Default value is "20".
- `i_dist` - (Optional) Administrative distance of IBGP routes for BGP address family context object. Default value is "200".
- `local_dist` - (Optional) Administrative distance of local routes for BGP address family context object. Default value is "220".
- `max_ecmp` - (Optional) Maximum number of equal-cost paths for BGP address family context object. Default value is "16".
- `max_ecmp_ibgp` - (Optional) Maximum ECMP IBGP for BGP address family context object. Default value is "16".
- `name_alias` - (Optional) Name alias for BGP address family context object.

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


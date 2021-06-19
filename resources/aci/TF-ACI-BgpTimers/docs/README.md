# TF::ACI::BgpTimers

Manages ACI BGP Timers

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ACI::BgpTimers",
    "Properties" : {
        "<a href="#annotation" title="Annotation">Annotation</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#grctrl" title="GrCtrl">GrCtrl</a>" : <i>String</i>,
        "<a href="#holdintvl" title="HoldIntvl">HoldIntvl</a>" : <i>String</i>,
        "<a href="#kaintvl" title="KaIntvl">KaIntvl</a>" : <i>String</i>,
        "<a href="#maxaslimit" title="MaxAsLimit">MaxAsLimit</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namealias" title="NameAlias">NameAlias</a>" : <i>String</i>,
        "<a href="#staleintvl" title="StaleIntvl">StaleIntvl</a>" : <i>String</i>,
        "<a href="#tenantdn" title="TenantDn">TenantDn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ACI::BgpTimers
Properties:
    <a href="#annotation" title="Annotation">Annotation</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#grctrl" title="GrCtrl">GrCtrl</a>: <i>String</i>
    <a href="#holdintvl" title="HoldIntvl">HoldIntvl</a>: <i>String</i>
    <a href="#kaintvl" title="KaIntvl">KaIntvl</a>: <i>String</i>
    <a href="#maxaslimit" title="MaxAsLimit">MaxAsLimit</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namealias" title="NameAlias">NameAlias</a>: <i>String</i>
    <a href="#staleintvl" title="StaleIntvl">StaleIntvl</a>: <i>String</i>
    <a href="#tenantdn" title="TenantDn">TenantDn</a>: <i>String</i>
</pre>

## Properties

#### Annotation

Annotation for bgp timers object.
- `description` - (Optional) Description for bgp timers object.
- `gr_ctrl` - (Optional) Graceful restart enabled or helper only for bgp timers object. Default value is "helper".
- `hold_intvl` - (Optional) Time period before declaring neighbor down for bgp timers object. Default value is "180".
- `ka_intvl` - (Optional) Interval time between keepalive messages for bgp timers object. Default value is "60".
- `max_as_limit` - (Optional) Maximum AS limit for bgp timers object. Default value is "0".
- `name_alias` - (Optional) Name alias for bgp timers object. Default value is "default".
- `stale_intvl` - (Optional) Stale interval for routes advertised by peer for bgp timers object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description for bgp timers object.
- `gr_ctrl` - (Optional) Graceful restart enabled or helper only for bgp timers object. Default value is "helper".
- `hold_intvl` - (Optional) Time period before declaring neighbor down for bgp timers object. Default value is "180".
- `ka_intvl` - (Optional) Interval time between keepalive messages for bgp timers object. Default value is "60".
- `max_as_limit` - (Optional) Maximum AS limit for bgp timers object. Default value is "0".
- `name_alias` - (Optional) Name alias for bgp timers object. Default value is "default".
- `stale_intvl` - (Optional) Stale interval for routes advertised by peer for bgp timers object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GrCtrl

Graceful restart enabled or helper only for bgp timers object. Default value is "helper".
- `hold_intvl` - (Optional) Time period before declaring neighbor down for bgp timers object. Default value is "180".
- `ka_intvl` - (Optional) Interval time between keepalive messages for bgp timers object. Default value is "60".
- `max_as_limit` - (Optional) Maximum AS limit for bgp timers object. Default value is "0".
- `name_alias` - (Optional) Name alias for bgp timers object. Default value is "default".
- `stale_intvl` - (Optional) Stale interval for routes advertised by peer for bgp timers object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HoldIntvl

Time period before declaring neighbor down for bgp timers object. Default value is "180".
- `ka_intvl` - (Optional) Interval time between keepalive messages for bgp timers object. Default value is "60".
- `max_as_limit` - (Optional) Maximum AS limit for bgp timers object. Default value is "0".
- `name_alias` - (Optional) Name alias for bgp timers object. Default value is "default".
- `stale_intvl` - (Optional) Stale interval for routes advertised by peer for bgp timers object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KaIntvl

Interval time between keepalive messages for bgp timers object. Default value is "60".
- `max_as_limit` - (Optional) Maximum AS limit for bgp timers object. Default value is "0".
- `name_alias` - (Optional) Name alias for bgp timers object. Default value is "default".
- `stale_intvl` - (Optional) Stale interval for routes advertised by peer for bgp timers object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxAsLimit

Maximum AS limit for bgp timers object. Default value is "0".
- `name_alias` - (Optional) Name alias for bgp timers object. Default value is "default".
- `stale_intvl` - (Optional) Stale interval for routes advertised by peer for bgp timers object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of bgp timers object.
- `annotation` - (Optional) Annotation for bgp timers object.
- `description` - (Optional) Description for bgp timers object.
- `gr_ctrl` - (Optional) Graceful restart enabled or helper only for bgp timers object. Default value is "helper".
- `hold_intvl` - (Optional) Time period before declaring neighbor down for bgp timers object. Default value is "180".
- `ka_intvl` - (Optional) Interval time between keepalive messages for bgp timers object. Default value is "60".
- `max_as_limit` - (Optional) Maximum AS limit for bgp timers object. Default value is "0".
- `name_alias` - (Optional) Name alias for bgp timers object. Default value is "default".
- `stale_intvl` - (Optional) Stale interval for routes advertised by peer for bgp timers object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NameAlias

Name alias for bgp timers object. Default value is "default".
- `stale_intvl` - (Optional) Stale interval for routes advertised by peer for bgp timers object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaleIntvl

Stale interval for routes advertised by peer for bgp timers object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantDn

Distinguished name of parent tenant object.
- `name` - (Required) Name of bgp timers object.
- `annotation` - (Optional) Annotation for bgp timers object.
- `description` - (Optional) Description for bgp timers object.
- `gr_ctrl` - (Optional) Graceful restart enabled or helper only for bgp timers object. Default value is "helper".
- `hold_intvl` - (Optional) Time period before declaring neighbor down for bgp timers object. Default value is "180".
- `ka_intvl` - (Optional) Interval time between keepalive messages for bgp timers object. Default value is "60".
- `max_as_limit` - (Optional) Maximum AS limit for bgp timers object. Default value is "0".
- `name_alias` - (Optional) Name alias for bgp timers object. Default value is "default".
- `stale_intvl` - (Optional) Stale interval for routes advertised by peer for bgp timers object.

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


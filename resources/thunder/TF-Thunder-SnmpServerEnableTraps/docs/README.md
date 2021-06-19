# TF::Thunder::SnmpServerEnableTraps

`thunder_snmp_server_enable_traps` Provides details about thunder snmp server enable traps

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SnmpServerEnableTraps",
    "Properties" : {
        "<a href="#all" title="All">All</a>" : <i>Double</i>,
        "<a href="#lldp" title="Lldp">Lldp</a>" : <i>Double</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#gslb" title="Gslb">Gslb</a>" : <i>[ <a href="gslbdefinition.md">GslbDefinition</a>, ... ]</i>,
        "<a href="#lsn" title="Lsn">Lsn</a>" : <i>[ <a href="lsndefinition.md">LsnDefinition</a>, ... ]</i>,
        "<a href="#network" title="Network">Network</a>" : <i>[ <a href="networkdefinition.md">NetworkDefinition</a>, ... ]</i>,
        "<a href="#routing" title="Routing">Routing</a>" : <i>[ <a href="routingdefinition.md">RoutingDefinition</a>, ... ]</i>,
        "<a href="#slb" title="Slb">Slb</a>" : <i>[ <a href="slbdefinition.md">SlbDefinition</a>, ... ]</i>,
        "<a href="#slbchange" title="SlbChange">SlbChange</a>" : <i>[ <a href="slbchangedefinition.md">SlbChangeDefinition</a>, ... ]</i>,
        "<a href="#snmp" title="Snmp">Snmp</a>" : <i>[ <a href="snmpdefinition.md">SnmpDefinition</a>, ... ]</i>,
        "<a href="#ssl" title="Ssl">Ssl</a>" : <i>[ <a href="ssldefinition.md">SslDefinition</a>, ... ]</i>,
        "<a href="#system" title="System">System</a>" : <i>[ <a href="systemdefinition.md">SystemDefinition</a>, ... ]</i>,
        "<a href="#vcs" title="Vcs">Vcs</a>" : <i>[ <a href="vcsdefinition.md">VcsDefinition</a>, ... ]</i>,
        "<a href="#vrrpa" title="VrrpA">VrrpA</a>" : <i>[ <a href="vrrpadefinition.md">VrrpADefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SnmpServerEnableTraps
Properties:
    <a href="#all" title="All">All</a>: <i>Double</i>
    <a href="#lldp" title="Lldp">Lldp</a>: <i>Double</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#gslb" title="Gslb">Gslb</a>: <i>
      - <a href="gslbdefinition.md">GslbDefinition</a></i>
    <a href="#lsn" title="Lsn">Lsn</a>: <i>
      - <a href="lsndefinition.md">LsnDefinition</a></i>
    <a href="#network" title="Network">Network</a>: <i>
      - <a href="networkdefinition.md">NetworkDefinition</a></i>
    <a href="#routing" title="Routing">Routing</a>: <i>
      - <a href="routingdefinition.md">RoutingDefinition</a></i>
    <a href="#slb" title="Slb">Slb</a>: <i>
      - <a href="slbdefinition.md">SlbDefinition</a></i>
    <a href="#slbchange" title="SlbChange">SlbChange</a>: <i>
      - <a href="slbchangedefinition.md">SlbChangeDefinition</a></i>
    <a href="#snmp" title="Snmp">Snmp</a>: <i>
      - <a href="snmpdefinition.md">SnmpDefinition</a></i>
    <a href="#ssl" title="Ssl">Ssl</a>: <i>
      - <a href="ssldefinition.md">SslDefinition</a></i>
    <a href="#system" title="System">System</a>: <i>
      - <a href="systemdefinition.md">SystemDefinition</a></i>
    <a href="#vcs" title="Vcs">Vcs</a>: <i>
      - <a href="vcsdefinition.md">VcsDefinition</a></i>
    <a href="#vrrpa" title="VrrpA">VrrpA</a>: <i>
      - <a href="vrrpadefinition.md">VrrpADefinition</a></i>
</pre>

## Properties

#### All

Enable all SLB traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lldp

Enable lldp traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gslb

_Required_: No

_Type_: List of <a href="gslbdefinition.md">GslbDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lsn

_Required_: No

_Type_: List of <a href="lsndefinition.md">LsnDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: List of <a href="networkdefinition.md">NetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Routing

_Required_: No

_Type_: List of <a href="routingdefinition.md">RoutingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slb

_Required_: No

_Type_: List of <a href="slbdefinition.md">SlbDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlbChange

_Required_: No

_Type_: List of <a href="slbchangedefinition.md">SlbChangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Snmp

_Required_: No

_Type_: List of <a href="snmpdefinition.md">SnmpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ssl

_Required_: No

_Type_: List of <a href="ssldefinition.md">SslDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### System

_Required_: No

_Type_: List of <a href="systemdefinition.md">SystemDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vcs

_Required_: No

_Type_: List of <a href="vcsdefinition.md">VcsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VrrpA

_Required_: No

_Type_: List of <a href="vrrpadefinition.md">VrrpADefinition</a>

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


# TF::AVI::Ipaddrgroup

The IpAddrGroup resource allows the creation and management of Avi IpAddrGroup

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Ipaddrgroup",
    "Properties" : {
        "<a href="#apicepgname" title="ApicEpgName">ApicEpgName</a>" : <i>String</i>,
        "<a href="#countrycodes" title="CountryCodes">CountryCodes</a>" : <i>[ String, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#marathonappname" title="MarathonAppName">MarathonAppName</a>" : <i>String</i>,
        "<a href="#marathonserviceport" title="MarathonServicePort">MarathonServicePort</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tenantref" title="TenantRef">TenantRef</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#addrs" title="Addrs">Addrs</a>" : <i>[ <a href="addrsdefinition.md">AddrsDefinition</a>, ... ]</i>,
        "<a href="#ipports" title="IpPorts">IpPorts</a>" : <i>[ <a href="ipportsdefinition.md">IpPortsDefinition</a>, ... ]</i>,
        "<a href="#markers" title="Markers">Markers</a>" : <i>[ <a href="markersdefinition.md">MarkersDefinition</a>, ... ]</i>,
        "<a href="#prefixes" title="Prefixes">Prefixes</a>" : <i>[ <a href="prefixesdefinition.md">PrefixesDefinition</a>, ... ]</i>,
        "<a href="#ranges" title="Ranges">Ranges</a>" : <i>[ <a href="rangesdefinition.md">RangesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Ipaddrgroup
Properties:
    <a href="#apicepgname" title="ApicEpgName">ApicEpgName</a>: <i>String</i>
    <a href="#countrycodes" title="CountryCodes">CountryCodes</a>: <i>
      - String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#marathonappname" title="MarathonAppName">MarathonAppName</a>: <i>String</i>
    <a href="#marathonserviceport" title="MarathonServicePort">MarathonServicePort</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tenantref" title="TenantRef">TenantRef</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#addrs" title="Addrs">Addrs</a>: <i>
      - <a href="addrsdefinition.md">AddrsDefinition</a></i>
    <a href="#ipports" title="IpPorts">IpPorts</a>: <i>
      - <a href="ipportsdefinition.md">IpPortsDefinition</a></i>
    <a href="#markers" title="Markers">Markers</a>: <i>
      - <a href="markersdefinition.md">MarkersDefinition</a></i>
    <a href="#prefixes" title="Prefixes">Prefixes</a>: <i>
      - <a href="prefixesdefinition.md">PrefixesDefinition</a></i>
    <a href="#ranges" title="Ranges">Ranges</a>: <i>
      - <a href="rangesdefinition.md">RangesDefinition</a></i>
</pre>

## Properties

#### ApicEpgName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CountryCodes

Populate the ip address ranges from the geo database for this country.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

User defined description for the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MarathonAppName

Populate ip addresses from tasks of this marathon app.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MarathonServicePort

Task port associated with marathon service port. If marathon app has multiple service ports, this is required. Else, the first task port is used.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the ip address group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRef

It is a reference to an object of type tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Addrs

_Required_: No

_Type_: List of <a href="addrsdefinition.md">AddrsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpPorts

_Required_: No

_Type_: List of <a href="ipportsdefinition.md">IpPortsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Markers

_Required_: No

_Type_: List of <a href="markersdefinition.md">MarkersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefixes

_Required_: No

_Type_: List of <a href="prefixesdefinition.md">PrefixesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ranges

_Required_: No

_Type_: List of <a href="rangesdefinition.md">RangesDefinition</a>

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


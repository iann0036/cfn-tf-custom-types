# TF::NSXT::PolicyDhcpServer

This resource provides a method for the management of a DHCP Server configurations.

This resource is applicable to NSX Global Manager, and NSX Policy Manager.

This resource is supported with NSX 3.0.0 onwards.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NSXT::PolicyDhcpServer",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#edgeclusterpath" title="EdgeClusterPath">EdgeClusterPath</a>" : <i>String</i>,
        "<a href="#leasetime" title="LeaseTime">LeaseTime</a>" : <i>Double</i>,
        "<a href="#nsxid" title="NsxId">NsxId</a>" : <i>String</i>,
        "<a href="#preferrededgepaths" title="PreferredEdgePaths">PreferredEdgePaths</a>" : <i>[ String, ... ]</i>,
        "<a href="#serveraddresses" title="ServerAddresses">ServerAddresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NSXT::PolicyDhcpServer
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#edgeclusterpath" title="EdgeClusterPath">EdgeClusterPath</a>: <i>String</i>
    <a href="#leasetime" title="LeaseTime">LeaseTime</a>: <i>Double</i>
    <a href="#nsxid" title="NsxId">NsxId</a>: <i>String</i>
    <a href="#preferrededgepaths" title="PreferredEdgePaths">PreferredEdgePaths</a>: <i>
      - String</i>
    <a href="#serveraddresses" title="ServerAddresses">ServerAddresses</a>: <i>
      - String</i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### Description

Description of the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Display name of the resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdgeClusterPath

The Policy path to the edge cluster for this DHCP Server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LeaseTime

IP address lease time in seconds. Valid values from `60` to `4294967295`. Default is `86400`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxId

The NSX ID of this resource. If set, this ID will be used to create the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredEdgePaths

Policy paths to edge nodes. The first edge node is assigned as active edge, and second one as standby edge.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerAddresses

DHCP server address in CIDR format. At most 2 supported; one IPv4 and one IPv6 address. Server address can also be specified on segment subnet level.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

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

#### Path

Returns the <code>Path</code> value.

#### Revision

Returns the <code>Revision</code> value.


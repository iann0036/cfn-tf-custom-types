# TF::NSXT::PolicyLbVirtualServer

This resource provides a method for the management of a Load Balancer Virtual Server.

This resource is applicable to NSX Policy Manager.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NSXT::PolicyLbVirtualServer",
    "Properties" : {
        "<a href="#accesslogenabled" title="AccessLogEnabled">AccessLogEnabled</a>" : <i>Boolean</i>,
        "<a href="#applicationprofilepath" title="ApplicationProfilePath">ApplicationProfilePath</a>" : <i>String</i>,
        "<a href="#defaultpoolmemberports" title="DefaultPoolMemberPorts">DefaultPoolMemberPorts</a>" : <i>[ String, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
        "<a href="#logsignificanteventonly" title="LogSignificantEventOnly">LogSignificantEventOnly</a>" : <i>Boolean</i>,
        "<a href="#maxconcurrentconnections" title="MaxConcurrentConnections">MaxConcurrentConnections</a>" : <i>Double</i>,
        "<a href="#maxnewconnectionrate" title="MaxNewConnectionRate">MaxNewConnectionRate</a>" : <i>Double</i>,
        "<a href="#nsxid" title="NsxId">NsxId</a>" : <i>String</i>,
        "<a href="#persistenceprofilepath" title="PersistenceProfilePath">PersistenceProfilePath</a>" : <i>String</i>,
        "<a href="#poolpath" title="PoolPath">PoolPath</a>" : <i>String</i>,
        "<a href="#ports" title="Ports">Ports</a>" : <i>[ String, ... ]</i>,
        "<a href="#servicepath" title="ServicePath">ServicePath</a>" : <i>String</i>,
        "<a href="#sorrypoolpath" title="SorryPoolPath">SorryPoolPath</a>" : <i>String</i>,
        "<a href="#accesslistcontrol" title="AccessListControl">AccessListControl</a>" : <i>[ <a href="accesslistcontroldefinition.md">AccessListControlDefinition</a>, ... ]</i>,
        "<a href="#clientssl" title="ClientSsl">ClientSsl</a>" : <i>[ <a href="clientssldefinition.md">ClientSslDefinition</a>, ... ]</i>,
        "<a href="#serverssl" title="ServerSsl">ServerSsl</a>" : <i>[ <a href="serverssldefinition.md">ServerSslDefinition</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NSXT::PolicyLbVirtualServer
Properties:
    <a href="#accesslogenabled" title="AccessLogEnabled">AccessLogEnabled</a>: <i>Boolean</i>
    <a href="#applicationprofilepath" title="ApplicationProfilePath">ApplicationProfilePath</a>: <i>String</i>
    <a href="#defaultpoolmemberports" title="DefaultPoolMemberPorts">DefaultPoolMemberPorts</a>: <i>
      - String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
    <a href="#logsignificanteventonly" title="LogSignificantEventOnly">LogSignificantEventOnly</a>: <i>Boolean</i>
    <a href="#maxconcurrentconnections" title="MaxConcurrentConnections">MaxConcurrentConnections</a>: <i>Double</i>
    <a href="#maxnewconnectionrate" title="MaxNewConnectionRate">MaxNewConnectionRate</a>: <i>Double</i>
    <a href="#nsxid" title="NsxId">NsxId</a>: <i>String</i>
    <a href="#persistenceprofilepath" title="PersistenceProfilePath">PersistenceProfilePath</a>: <i>String</i>
    <a href="#poolpath" title="PoolPath">PoolPath</a>: <i>String</i>
    <a href="#ports" title="Ports">Ports</a>: <i>
      - String</i>
    <a href="#servicepath" title="ServicePath">ServicePath</a>: <i>String</i>
    <a href="#sorrypoolpath" title="SorryPoolPath">SorryPoolPath</a>: <i>String</i>
    <a href="#accesslistcontrol" title="AccessListControl">AccessListControl</a>: <i>
      - <a href="accesslistcontroldefinition.md">AccessListControlDefinition</a></i>
    <a href="#clientssl" title="ClientSsl">ClientSsl</a>: <i>
      - <a href="clientssldefinition.md">ClientSslDefinition</a></i>
    <a href="#serverssl" title="ServerSsl">ServerSsl</a>: <i>
      - <a href="serverssldefinition.md">ServerSslDefinition</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### AccessLogEnabled

If set, all connections/requests sent to the virtual server are logged to access log.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationProfilePath

Application profile path for this virtual server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultPoolMemberPorts

Default pool member ports to use when member port is not defined on the pool.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### Enabled

Indicates whether to enable access list control option. Default is true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

Virtual Server IP address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogSignificantEventOnly

If true, significant events are logged in access log. This flag is supported since NSX 3.0.0.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConcurrentConnections

To ensure one virtual server does not over consume resources, connections to Virtual Server can be capped.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxNewConnectionRate

To ensure one virtual server does not over consume resources, connections to a member can be rate limited.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxId

The NSX ID of this resource. If set, this ID will be used to create the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistenceProfilePath

Path to persistence profile allowing related client connections to be sent to the same backend server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoolPath

Path for Load Balancer Pool.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

Virtual Server Ports.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServicePath

Virtual Server can be associated with Load Balancer Service.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SorryPoolPath

When load balancer can not select server in pool, the request would be served by sorry pool.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessListControl

_Required_: No

_Type_: List of <a href="accesslistcontroldefinition.md">AccessListControlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientSsl

_Required_: No

_Type_: List of <a href="clientssldefinition.md">ClientSslDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSsl

_Required_: No

_Type_: List of <a href="serverssldefinition.md">ServerSslDefinition</a>

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


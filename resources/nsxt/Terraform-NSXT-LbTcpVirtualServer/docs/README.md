# Terraform::NSXT::LbTcpVirtualServer

Provides a resource to configure lb tcp virtual server on NSX-T manager

~> **NOTE:** This resource requires NSX version 2.3 or higher.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NSXT::LbTcpVirtualServer",
    "Properties" : {
        "<a href="#accesslogenabled" title="AccessLogEnabled">AccessLogEnabled</a>" : <i>Boolean</i>,
        "<a href="#applicationprofileid" title="ApplicationProfileId">ApplicationProfileId</a>" : <i>String</i>,
        "<a href="#defaultpoolmemberports" title="DefaultPoolMemberPorts">DefaultPoolMemberPorts</a>" : <i>[ String, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
        "<a href="#maxconcurrentconnections" title="MaxConcurrentConnections">MaxConcurrentConnections</a>" : <i>Double</i>,
        "<a href="#maxnewconnectionrate" title="MaxNewConnectionRate">MaxNewConnectionRate</a>" : <i>Double</i>,
        "<a href="#persistenceprofileid" title="PersistenceProfileId">PersistenceProfileId</a>" : <i>String</i>,
        "<a href="#poolid" title="PoolId">PoolId</a>" : <i>String</i>,
        "<a href="#ports" title="Ports">Ports</a>" : <i>[ String, ... ]</i>,
        "<a href="#sorrypoolid" title="SorryPoolId">SorryPoolId</a>" : <i>String</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tag.md">Tag</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NSXT::LbTcpVirtualServer
Properties:
    <a href="#accesslogenabled" title="AccessLogEnabled">AccessLogEnabled</a>: <i>Boolean</i>
    <a href="#applicationprofileid" title="ApplicationProfileId">ApplicationProfileId</a>: <i>String</i>
    <a href="#defaultpoolmemberports" title="DefaultPoolMemberPorts">DefaultPoolMemberPorts</a>: <i>
      - String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
    <a href="#maxconcurrentconnections" title="MaxConcurrentConnections">MaxConcurrentConnections</a>: <i>Double</i>
    <a href="#maxnewconnectionrate" title="MaxNewConnectionRate">MaxNewConnectionRate</a>: <i>Double</i>
    <a href="#persistenceprofileid" title="PersistenceProfileId">PersistenceProfileId</a>: <i>String</i>
    <a href="#poolid" title="PoolId">PoolId</a>: <i>String</i>
    <a href="#ports" title="Ports">Ports</a>: <i>
      - String</i>
    <a href="#sorrypoolid" title="SorryPoolId">SorryPoolId</a>: <i>String</i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tag.md">Tag</a></i>
</pre>

## Properties

#### AccessLogEnabled

Whether access log is enabled. Default is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationProfileId

The application profile defines the application protocol characteristics.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultPoolMemberPorts

List of default pool member ports.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of this resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The display name of this resource. Defaults to ID if not set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Whether the virtual server is enabled. Default is true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

Virtual server IP address.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxConcurrentConnections

To ensure one virtual server does not over consume resources, affecting other applications hosted on the same LBS, connections to a virtual server can be capped. If it is not specified, it means that connections are unlimited.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxNewConnectionRate

To ensure one virtual server does not over consume resources, connections to a member can be rate limited. If it is not specified, it means that connection rate is unlimited.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PersistenceProfileId

Persistence profile is used to allow related client connections to be sent to the same backend server. Only source ip persistance profile is accepted.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoolId

Pool of backend servers. Server pool consists of one or more servers, also referred to as pool members, that are similarly configured and are running the same application.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

List of virtual server ports.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SorryPoolId

When load balancer can not select a backend server to serve the request in default pool or pool in rules, the request would be served by sorry server pool.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tag.md">Tag</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Revision

Returns the <code>Revision</code> value.


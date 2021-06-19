# TF::FortiOS::SystemWccp

Configure WCCP.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemWccp",
    "Properties" : {
        "<a href="#assignmentbucketformat" title="AssignmentBucketFormat">AssignmentBucketFormat</a>" : <i>String</i>,
        "<a href="#assignmentdstaddrmask" title="AssignmentDstaddrMask">AssignmentDstaddrMask</a>" : <i>String</i>,
        "<a href="#assignmentmethod" title="AssignmentMethod">AssignmentMethod</a>" : <i>String</i>,
        "<a href="#assignmentsrcaddrmask" title="AssignmentSrcaddrMask">AssignmentSrcaddrMask</a>" : <i>String</i>,
        "<a href="#assignmentweight" title="AssignmentWeight">AssignmentWeight</a>" : <i>Double</i>,
        "<a href="#authentication" title="Authentication">Authentication</a>" : <i>String</i>,
        "<a href="#cacheenginemethod" title="CacheEngineMethod">CacheEngineMethod</a>" : <i>String</i>,
        "<a href="#cacheid" title="CacheId">CacheId</a>" : <i>String</i>,
        "<a href="#forwardmethod" title="ForwardMethod">ForwardMethod</a>" : <i>String</i>,
        "<a href="#groupaddress" title="GroupAddress">GroupAddress</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#ports" title="Ports">Ports</a>" : <i>String</i>,
        "<a href="#portsdefined" title="PortsDefined">PortsDefined</a>" : <i>String</i>,
        "<a href="#primaryhash" title="PrimaryHash">PrimaryHash</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>Double</i>,
        "<a href="#returnmethod" title="ReturnMethod">ReturnMethod</a>" : <i>String</i>,
        "<a href="#routerid" title="RouterId">RouterId</a>" : <i>String</i>,
        "<a href="#routerlist" title="RouterList">RouterList</a>" : <i>String</i>,
        "<a href="#serverlist" title="ServerList">ServerList</a>" : <i>String</i>,
        "<a href="#servertype" title="ServerType">ServerType</a>" : <i>String</i>,
        "<a href="#serviceid" title="ServiceId">ServiceId</a>" : <i>String</i>,
        "<a href="#servicetype" title="ServiceType">ServiceType</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemWccp
Properties:
    <a href="#assignmentbucketformat" title="AssignmentBucketFormat">AssignmentBucketFormat</a>: <i>String</i>
    <a href="#assignmentdstaddrmask" title="AssignmentDstaddrMask">AssignmentDstaddrMask</a>: <i>String</i>
    <a href="#assignmentmethod" title="AssignmentMethod">AssignmentMethod</a>: <i>String</i>
    <a href="#assignmentsrcaddrmask" title="AssignmentSrcaddrMask">AssignmentSrcaddrMask</a>: <i>String</i>
    <a href="#assignmentweight" title="AssignmentWeight">AssignmentWeight</a>: <i>Double</i>
    <a href="#authentication" title="Authentication">Authentication</a>: <i>String</i>
    <a href="#cacheenginemethod" title="CacheEngineMethod">CacheEngineMethod</a>: <i>String</i>
    <a href="#cacheid" title="CacheId">CacheId</a>: <i>String</i>
    <a href="#forwardmethod" title="ForwardMethod">ForwardMethod</a>: <i>String</i>
    <a href="#groupaddress" title="GroupAddress">GroupAddress</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#ports" title="Ports">Ports</a>: <i>String</i>
    <a href="#portsdefined" title="PortsDefined">PortsDefined</a>: <i>String</i>
    <a href="#primaryhash" title="PrimaryHash">PrimaryHash</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>Double</i>
    <a href="#returnmethod" title="ReturnMethod">ReturnMethod</a>: <i>String</i>
    <a href="#routerid" title="RouterId">RouterId</a>: <i>String</i>
    <a href="#routerlist" title="RouterList">RouterList</a>: <i>String</i>
    <a href="#serverlist" title="ServerList">ServerList</a>: <i>String</i>
    <a href="#servertype" title="ServerType">ServerType</a>: <i>String</i>
    <a href="#serviceid" title="ServiceId">ServiceId</a>: <i>String</i>
    <a href="#servicetype" title="ServiceType">ServiceType</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### AssignmentBucketFormat

Assignment bucket format for the WCCP cache engine. Valid values: `wccp-v2`, `cisco-implementation`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssignmentDstaddrMask

Assignment destination address mask.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssignmentMethod

Hash key assignment preference. Valid values: `HASH`, `MASK`, `any`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssignmentSrcaddrMask

Assignment source address mask.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssignmentWeight

Assignment of hash weight/ratio for the WCCP cache engine.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authentication

Enable/disable MD5 authentication. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheEngineMethod

Method used to forward traffic to the routers or to return to the cache engine. Valid values: `GRE`, `L2`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheId

IP address known to all routers. If the addresses are the same, use the default 0.0.0.0.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardMethod

Method used to forward traffic to the cache servers. Valid values: `GRE`, `L2`, `any`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupAddress

IP multicast address used by the cache routers. For the FortiGate to ignore multicast WCCP traffic, use the default 0.0.0.0.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Password for MD5 authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ports

Service ports.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortsDefined

Match method. Valid values: `source`, `destination`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryHash

Hash method. Valid values: `src-ip`, `dst-ip`, `src-port`, `dst-port`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

Service priority.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

Service protocol.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReturnMethod

Method used to decline a redirected packet and return it to the FortiGate. Valid values: `GRE`, `L2`, `any`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouterId

IP address known to all cache engines. If all cache engines connect to the same FortiGate interface, use the default 0.0.0.0.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouterList

IP addresses of one or more WCCP routers.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerList

IP addresses and netmasks for up to four cache servers.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerType

Cache server type. Valid values: `forward`, `proxy`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceId

Service ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceType

WCCP service type used by the cache server for logical interception and redirection of traffic. Valid values: `auto`, `standard`, `dynamic`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

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


# TF::CheckPoint::ManagementServiceSctp

This resource allows you to execute Check Point Service Sctp.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementServiceSctp",
    "Properties" : {
        "<a href="#aggressiveaging" title="AggressiveAging">AggressiveAging</a>" : <i>[ <a href="aggressiveagingdefinition.md">AggressiveAgingDefinition</a>, ... ]</i>,
        "<a href="#color" title="Color">Color</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#ignoreerrors" title="IgnoreErrors">IgnoreErrors</a>" : <i>Boolean</i>,
        "<a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>" : <i>Boolean</i>,
        "<a href="#keepconnectionsopenafterpolicyinstallation" title="KeepConnectionsOpenAfterPolicyInstallation">KeepConnectionsOpenAfterPolicyInstallation</a>" : <i>Boolean</i>,
        "<a href="#matchforany" title="MatchForAny">MatchForAny</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>String</i>,
        "<a href="#sessiontimeout" title="SessionTimeout">SessionTimeout</a>" : <i>Double</i>,
        "<a href="#sourceport" title="SourcePort">SourcePort</a>" : <i>String</i>,
        "<a href="#syncconnectionsoncluster" title="SyncConnectionsOnCluster">SyncConnectionsOnCluster</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#usedefaultsessiontimeout" title="UseDefaultSessionTimeout">UseDefaultSessionTimeout</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementServiceSctp
Properties:
    <a href="#aggressiveaging" title="AggressiveAging">AggressiveAging</a>: <i>
      - <a href="aggressiveagingdefinition.md">AggressiveAgingDefinition</a></i>
    <a href="#color" title="Color">Color</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#ignoreerrors" title="IgnoreErrors">IgnoreErrors</a>: <i>Boolean</i>
    <a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>: <i>Boolean</i>
    <a href="#keepconnectionsopenafterpolicyinstallation" title="KeepConnectionsOpenAfterPolicyInstallation">KeepConnectionsOpenAfterPolicyInstallation</a>: <i>Boolean</i>
    <a href="#matchforany" title="MatchForAny">MatchForAny</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>String</i>
    <a href="#sessiontimeout" title="SessionTimeout">SessionTimeout</a>: <i>Double</i>
    <a href="#sourceport" title="SourcePort">SourcePort</a>: <i>String</i>
    <a href="#syncconnectionsoncluster" title="SyncConnectionsOnCluster">SyncConnectionsOnCluster</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#usedefaultsessiontimeout" title="UseDefaultSessionTimeout">UseDefaultSessionTimeout</a>: <i>Boolean</i>
</pre>

## Properties

#### AggressiveAging

Sets short (aggressive) timeouts for idle connections.aggressive_aging blocks are documented below.

_Required_: No

_Type_: List of <a href="aggressiveagingdefinition.md">AggressiveAgingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Color

Color of the object. Should be one of existing colors.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comments string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreErrors

Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IgnoreWarnings

Apply changes ignoring warnings.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepConnectionsOpenAfterPolicyInstallation

Keep connections open after policy has been installed even if they are not allowed under the new policy. This overrides the settings in the Connection Persistence page. If you change this property, the change will not affect open connections, but only future connections.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchForAny

Indicates whether this service is used when 'Any' is set as the rule's service and there are several service objects with the same source port and protocol.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Object name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Port number. To specify a port range add a hyphen between the lowest and the highest port numbers, for example 44-45.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionTimeout

Time (in seconds) before the session times out.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcePort

Source port number. To specify a port range add a hyphen between the lowest and the highest port numbers, for example 44-45.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyncConnectionsOnCluster

Enables state-synchronized High Availability or Load Sharing on a ClusterXL or OPSEC-certified cluster.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Collection of tag identifiers.tags blocks are documented below.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseDefaultSessionTimeout

Use default virtual session timeout.

_Required_: No

_Type_: Boolean

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


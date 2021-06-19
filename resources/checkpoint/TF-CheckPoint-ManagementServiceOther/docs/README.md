# TF::CheckPoint::ManagementServiceOther

This resource allows you to execute Check Point Service Other.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementServiceOther",
    "Properties" : {
        "<a href="#acceptreplies" title="AcceptReplies">AcceptReplies</a>" : <i>Boolean</i>,
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#aggressiveaging" title="AggressiveAging">AggressiveAging</a>" : <i>[ <a href="aggressiveagingdefinition.md">AggressiveAgingDefinition</a>, ... ]</i>,
        "<a href="#color" title="Color">Color</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#ignoreerrors" title="IgnoreErrors">IgnoreErrors</a>" : <i>Boolean</i>,
        "<a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>" : <i>Boolean</i>,
        "<a href="#ipprotocol" title="IpProtocol">IpProtocol</a>" : <i>Double</i>,
        "<a href="#keepconnectionsopenafterpolicyinstallation" title="KeepConnectionsOpenAfterPolicyInstallation">KeepConnectionsOpenAfterPolicyInstallation</a>" : <i>Boolean</i>,
        "<a href="#match" title="Match">Match</a>" : <i>String</i>,
        "<a href="#matchforany" title="MatchForAny">MatchForAny</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#overridedefaultsettings" title="OverrideDefaultSettings">OverrideDefaultSettings</a>" : <i>Boolean</i>,
        "<a href="#sessiontimeout" title="SessionTimeout">SessionTimeout</a>" : <i>Double</i>,
        "<a href="#syncconnectionsoncluster" title="SyncConnectionsOnCluster">SyncConnectionsOnCluster</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#usedefaultsessiontimeout" title="UseDefaultSessionTimeout">UseDefaultSessionTimeout</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementServiceOther
Properties:
    <a href="#acceptreplies" title="AcceptReplies">AcceptReplies</a>: <i>Boolean</i>
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#aggressiveaging" title="AggressiveAging">AggressiveAging</a>: <i>
      - <a href="aggressiveagingdefinition.md">AggressiveAgingDefinition</a></i>
    <a href="#color" title="Color">Color</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#ignoreerrors" title="IgnoreErrors">IgnoreErrors</a>: <i>Boolean</i>
    <a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>: <i>Boolean</i>
    <a href="#ipprotocol" title="IpProtocol">IpProtocol</a>: <i>Double</i>
    <a href="#keepconnectionsopenafterpolicyinstallation" title="KeepConnectionsOpenAfterPolicyInstallation">KeepConnectionsOpenAfterPolicyInstallation</a>: <i>Boolean</i>
    <a href="#match" title="Match">Match</a>: <i>String</i>
    <a href="#matchforany" title="MatchForAny">MatchForAny</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#overridedefaultsettings" title="OverrideDefaultSettings">OverrideDefaultSettings</a>: <i>Boolean</i>
    <a href="#sessiontimeout" title="SessionTimeout">SessionTimeout</a>: <i>Double</i>
    <a href="#syncconnectionsoncluster" title="SyncConnectionsOnCluster">SyncConnectionsOnCluster</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#usedefaultsessiontimeout" title="UseDefaultSessionTimeout">UseDefaultSessionTimeout</a>: <i>Boolean</i>
</pre>

## Properties

#### AcceptReplies

Specifies whether Other Service replies are to be accepted.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

Contains an INSPECT expression that defines the action to take if a rule containing this service is matched.
Example: set r_mhandler &open_ssl_handler sets a handler on the connection.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### IpProtocol

IP protocol number.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepConnectionsOpenAfterPolicyInstallation

Keep connections open after policy has been installed even if they are not allowed under the new policy. This overrides the settings in the Connection Persistence page. If you change this property, the change will not affect open connections, but only future connections.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Match

Contains an INSPECT expression that defines the matching criteria. The connection is examined against the expression during the first packet.
Example: tcp, dport = 21, direction = 0 matches incoming FTP control connections.

_Required_: No

_Type_: String

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

#### OverrideDefaultSettings

Indicates whether this service is a Data Domain service which has been overridden.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionTimeout

Time (in seconds) before the session times out.

_Required_: No

_Type_: Double

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


# TF::FortiOS::SystemClustersync

Configure FortiGate Session Life Support Protocol (FGSP) session synchronization.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemClustersync",
    "Properties" : {
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#hbinterval" title="HbInterval">HbInterval</a>" : <i>Double</i>,
        "<a href="#hblostthreshold" title="HbLostThreshold">HbLostThreshold</a>" : <i>Double</i>,
        "<a href="#ipsectunnelsync" title="IpsecTunnelSync">IpsecTunnelSync</a>" : <i>String</i>,
        "<a href="#peerip" title="Peerip">Peerip</a>" : <i>String</i>,
        "<a href="#peervd" title="Peervd">Peervd</a>" : <i>String</i>,
        "<a href="#slaveaddikeroutes" title="SlaveAddIkeRoutes">SlaveAddIkeRoutes</a>" : <i>String</i>,
        "<a href="#syncid" title="SyncId">SyncId</a>" : <i>Double</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#downintfsbeforesesssync" title="DownIntfsBeforeSessSync">DownIntfsBeforeSessSync</a>" : <i>[ <a href="downintfsbeforesesssyncdefinition.md">DownIntfsBeforeSessSyncDefinition</a>, ... ]</i>,
        "<a href="#sessionsyncfilter" title="SessionSyncFilter">SessionSyncFilter</a>" : <i>[ <a href="sessionsyncfilterdefinition.md">SessionSyncFilterDefinition</a>, ... ]</i>,
        "<a href="#syncvd" title="Syncvd">Syncvd</a>" : <i>[ <a href="syncvddefinition.md">SyncvdDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemClustersync
Properties:
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#hbinterval" title="HbInterval">HbInterval</a>: <i>Double</i>
    <a href="#hblostthreshold" title="HbLostThreshold">HbLostThreshold</a>: <i>Double</i>
    <a href="#ipsectunnelsync" title="IpsecTunnelSync">IpsecTunnelSync</a>: <i>String</i>
    <a href="#peerip" title="Peerip">Peerip</a>: <i>String</i>
    <a href="#peervd" title="Peervd">Peervd</a>: <i>String</i>
    <a href="#slaveaddikeroutes" title="SlaveAddIkeRoutes">SlaveAddIkeRoutes</a>: <i>String</i>
    <a href="#syncid" title="SyncId">SyncId</a>: <i>Double</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#downintfsbeforesesssync" title="DownIntfsBeforeSessSync">DownIntfsBeforeSessSync</a>: <i>
      - <a href="downintfsbeforesesssyncdefinition.md">DownIntfsBeforeSessSyncDefinition</a></i>
    <a href="#sessionsyncfilter" title="SessionSyncFilter">SessionSyncFilter</a>: <i>
      - <a href="sessionsyncfilterdefinition.md">SessionSyncFilterDefinition</a></i>
    <a href="#syncvd" title="Syncvd">Syncvd</a>: <i>
      - <a href="syncvddefinition.md">SyncvdDefinition</a></i>
</pre>

## Properties

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HbInterval

Heartbeat interval (1 - 10 sec).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HbLostThreshold

Lost heartbeat threshold (1 - 10).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpsecTunnelSync

Enable/disable IPsec tunnel synchronization. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Peerip

IP address of the interface on the peer unit that is used for the session synchronization link.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Peervd

VDOM that contains the session synchronization link interface on the peer unit. Usually both peers would have the same peervd.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlaveAddIkeRoutes

Enable/disable IKE route announcement on the backup unit. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyncId

Sync ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DownIntfsBeforeSessSync

_Required_: No

_Type_: List of <a href="downintfsbeforesesssyncdefinition.md">DownIntfsBeforeSessSyncDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionSyncFilter

_Required_: No

_Type_: List of <a href="sessionsyncfilterdefinition.md">SessionSyncFilterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Syncvd

_Required_: No

_Type_: List of <a href="syncvddefinition.md">SyncvdDefinition</a>

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


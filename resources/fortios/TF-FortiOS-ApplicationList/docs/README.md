# TF::FortiOS::ApplicationList

Configure application control lists.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::ApplicationList",
    "Properties" : {
        "<a href="#appreplacemsg" title="AppReplacemsg">AppReplacemsg</a>" : <i>String</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#controldefaultnetworkservices" title="ControlDefaultNetworkServices">ControlDefaultNetworkServices</a>" : <i>String</i>,
        "<a href="#deepappinspection" title="DeepAppInspection">DeepAppInspection</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#enforcedefaultappport" title="EnforceDefaultAppPort">EnforceDefaultAppPort</a>" : <i>String</i>,
        "<a href="#extendedlog" title="ExtendedLog">ExtendedLog</a>" : <i>String</i>,
        "<a href="#forceinclusionssldisigs" title="ForceInclusionSslDiSigs">ForceInclusionSslDiSigs</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#options" title="Options">Options</a>" : <i>String</i>,
        "<a href="#otherapplicationaction" title="OtherApplicationAction">OtherApplicationAction</a>" : <i>String</i>,
        "<a href="#otherapplicationlog" title="OtherApplicationLog">OtherApplicationLog</a>" : <i>String</i>,
        "<a href="#p2pblacklist" title="P2pBlackList">P2pBlackList</a>" : <i>String</i>,
        "<a href="#p2pblocklist" title="P2pBlockList">P2pBlockList</a>" : <i>String</i>,
        "<a href="#replacemsggroup" title="ReplacemsgGroup">ReplacemsgGroup</a>" : <i>String</i>,
        "<a href="#unknownapplicationaction" title="UnknownApplicationAction">UnknownApplicationAction</a>" : <i>String</i>,
        "<a href="#unknownapplicationlog" title="UnknownApplicationLog">UnknownApplicationLog</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#defaultnetworkservices" title="DefaultNetworkServices">DefaultNetworkServices</a>" : <i>[ <a href="defaultnetworkservicesdefinition.md">DefaultNetworkServicesDefinition</a>, ... ]</i>,
        "<a href="#entries" title="Entries">Entries</a>" : <i>[ <a href="entriesdefinition.md">EntriesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::ApplicationList
Properties:
    <a href="#appreplacemsg" title="AppReplacemsg">AppReplacemsg</a>: <i>String</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#controldefaultnetworkservices" title="ControlDefaultNetworkServices">ControlDefaultNetworkServices</a>: <i>String</i>
    <a href="#deepappinspection" title="DeepAppInspection">DeepAppInspection</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#enforcedefaultappport" title="EnforceDefaultAppPort">EnforceDefaultAppPort</a>: <i>String</i>
    <a href="#extendedlog" title="ExtendedLog">ExtendedLog</a>: <i>String</i>
    <a href="#forceinclusionssldisigs" title="ForceInclusionSslDiSigs">ForceInclusionSslDiSigs</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#options" title="Options">Options</a>: <i>String</i>
    <a href="#otherapplicationaction" title="OtherApplicationAction">OtherApplicationAction</a>: <i>String</i>
    <a href="#otherapplicationlog" title="OtherApplicationLog">OtherApplicationLog</a>: <i>String</i>
    <a href="#p2pblacklist" title="P2pBlackList">P2pBlackList</a>: <i>String</i>
    <a href="#p2pblocklist" title="P2pBlockList">P2pBlockList</a>: <i>String</i>
    <a href="#replacemsggroup" title="ReplacemsgGroup">ReplacemsgGroup</a>: <i>String</i>
    <a href="#unknownapplicationaction" title="UnknownApplicationAction">UnknownApplicationAction</a>: <i>String</i>
    <a href="#unknownapplicationlog" title="UnknownApplicationLog">UnknownApplicationLog</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#defaultnetworkservices" title="DefaultNetworkServices">DefaultNetworkServices</a>: <i>
      - <a href="defaultnetworkservicesdefinition.md">DefaultNetworkServicesDefinition</a></i>
    <a href="#entries" title="Entries">Entries</a>: <i>
      - <a href="entriesdefinition.md">EntriesDefinition</a></i>
</pre>

## Properties

#### AppReplacemsg

Enable/disable replacement messages for blocked applications. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

comments.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ControlDefaultNetworkServices

Enable/disable enforcement of protocols over selected ports. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeepAppInspection

Enable/disable deep application inspection. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnforceDefaultAppPort

Enable/disable default application port enforcement for allowed applications. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedLog

Enable/disable extended logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceInclusionSslDiSigs

Enable/disable forced inclusion of SSL deep inspection signatures. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

List name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

Basic application protocol signatures allowed by default. Valid values: `allow-dns`, `allow-icmp`, `allow-http`, `allow-ssl`, `allow-quic`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OtherApplicationAction

Action for other applications. Valid values: `pass`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OtherApplicationLog

Enable/disable logging for other applications. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### P2pBlackList

P2P applications to be black listed. Valid values: `skype`, `edonkey`, `bittorrent`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### P2pBlockList

P2P applications to be blocklisted. Valid values: `skype`, `edonkey`, `bittorrent`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReplacemsgGroup

Replacement message group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnknownApplicationAction

Pass or block traffic from unknown applications. Valid values: `pass`, `block`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnknownApplicationLog

Enable/disable logging for unknown applications. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultNetworkServices

_Required_: No

_Type_: List of <a href="defaultnetworkservicesdefinition.md">DefaultNetworkServicesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Entries

_Required_: No

_Type_: List of <a href="entriesdefinition.md">EntriesDefinition</a>

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


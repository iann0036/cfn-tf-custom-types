# TF::CheckPoint::ManagementThreatRule

This resource allows you to add/update/delete Check Point Threat Rule.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementThreatRule",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#destination" title="Destination">Destination</a>" : <i>[ String, ... ]</i>,
        "<a href="#destinationnegate" title="DestinationNegate">DestinationNegate</a>" : <i>Boolean</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#ignoreerrors" title="IgnoreErrors">IgnoreErrors</a>" : <i>Boolean</i>,
        "<a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>" : <i>Boolean</i>,
        "<a href="#installon" title="InstallOn">InstallOn</a>" : <i>[ String, ... ]</i>,
        "<a href="#layer" title="Layer">Layer</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#position" title="Position">Position</a>" : <i>[ <a href="positiondefinition.md">PositionDefinition</a>, ... ]</i>,
        "<a href="#protectedscope" title="ProtectedScope">ProtectedScope</a>" : <i>[ String, ... ]</i>,
        "<a href="#protectedscopenegate" title="ProtectedScopeNegate">ProtectedScopeNegate</a>" : <i>Boolean</i>,
        "<a href="#service" title="Service">Service</a>" : <i>[ String, ... ]</i>,
        "<a href="#servicenegate" title="ServiceNegate">ServiceNegate</a>" : <i>Boolean</i>,
        "<a href="#source" title="Source">Source</a>" : <i>[ String, ... ]</i>,
        "<a href="#sourcenegate" title="SourceNegate">SourceNegate</a>" : <i>Boolean</i>,
        "<a href="#track" title="Track">Track</a>" : <i>String</i>,
        "<a href="#tracksettings" title="TrackSettings">TrackSettings</a>" : <i>[ <a href="tracksettingsdefinition.md">TrackSettingsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementThreatRule
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#destination" title="Destination">Destination</a>: <i>
      - String</i>
    <a href="#destinationnegate" title="DestinationNegate">DestinationNegate</a>: <i>Boolean</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#ignoreerrors" title="IgnoreErrors">IgnoreErrors</a>: <i>Boolean</i>
    <a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>: <i>Boolean</i>
    <a href="#installon" title="InstallOn">InstallOn</a>: <i>
      - String</i>
    <a href="#layer" title="Layer">Layer</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#position" title="Position">Position</a>: <i>
      - <a href="positiondefinition.md">PositionDefinition</a></i>
    <a href="#protectedscope" title="ProtectedScope">ProtectedScope</a>: <i>
      - String</i>
    <a href="#protectedscopenegate" title="ProtectedScopeNegate">ProtectedScopeNegate</a>: <i>Boolean</i>
    <a href="#service" title="Service">Service</a>: <i>
      - String</i>
    <a href="#servicenegate" title="ServiceNegate">ServiceNegate</a>: <i>Boolean</i>
    <a href="#source" title="Source">Source</a>: <i>
      - String</i>
    <a href="#sourcenegate" title="SourceNegate">SourceNegate</a>: <i>Boolean</i>
    <a href="#track" title="Track">Track</a>: <i>String</i>
    <a href="#tracksettings" title="TrackSettings">TrackSettings</a>: <i>
      - <a href="tracksettingsdefinition.md">TrackSettingsDefinition</a></i>
</pre>

## Properties

#### Action

Action-the enforced profile.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comments string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

Collection of Network objects identified by the name or UID.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationNegate

True if negate is set for destination.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

Enable/Disable the rule.

_Required_: No

_Type_: Boolean

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

#### InstallOn

Which Gateways identified by the name or UID to install the policy on.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Layer

Layer that the rule belongs to identified by the name or UID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Rule name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Position

Position in the rulebase. Position blocks are documented below.

_Required_: Yes

_Type_: List of <a href="positiondefinition.md">PositionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtectedScope

Collection of objects defining Protected Scope identified by the name or UID.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtectedScopeNegate

True if negate is set for Protected Scope.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

Collection of Network objects identified by the name or UID.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceNegate

True if negate is set for service.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

Collection of Network objects identified by the name or UID.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceNegate

True if negate is set for source.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Track

Packet tracking.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TrackSettings

Threat rule track settings. track_settings block are documented below.

_Required_: No

_Type_: List of <a href="tracksettingsdefinition.md">TrackSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Exceptions

Collection of the rule's exceptions identified by UID.

#### Id

Returns the <code>Id</code> value.


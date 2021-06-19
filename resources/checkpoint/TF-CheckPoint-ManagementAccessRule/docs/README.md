# TF::CheckPoint::ManagementAccessRule

This resource allows you to add/update/delete Check Point Access Rule.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementAccessRule",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#actionsettings" title="ActionSettings">ActionSettings</a>" : <i>[ <a href="actionsettingsdefinition.md">ActionSettingsDefinition</a>, ... ]</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#content" title="Content">Content</a>" : <i>[ String, ... ]</i>,
        "<a href="#contentdirection" title="ContentDirection">ContentDirection</a>" : <i>String</i>,
        "<a href="#contentnegate" title="ContentNegate">ContentNegate</a>" : <i>Boolean</i>,
        "<a href="#customfields" title="CustomFields">CustomFields</a>" : <i>[ <a href="customfieldsdefinition.md">CustomFieldsDefinition</a>, ... ]</i>,
        "<a href="#destination" title="Destination">Destination</a>" : <i>[ String, ... ]</i>,
        "<a href="#destinationnegate" title="DestinationNegate">DestinationNegate</a>" : <i>Boolean</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#ignoreerrors" title="IgnoreErrors">IgnoreErrors</a>" : <i>Boolean</i>,
        "<a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>" : <i>Boolean</i>,
        "<a href="#inlinelayer" title="InlineLayer">InlineLayer</a>" : <i>String</i>,
        "<a href="#installon" title="InstallOn">InstallOn</a>" : <i>[ String, ... ]</i>,
        "<a href="#layer" title="Layer">Layer</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#position" title="Position">Position</a>" : <i>[ <a href="positiondefinition.md">PositionDefinition</a>, ... ]</i>,
        "<a href="#service" title="Service">Service</a>" : <i>[ String, ... ]</i>,
        "<a href="#servicenegate" title="ServiceNegate">ServiceNegate</a>" : <i>Boolean</i>,
        "<a href="#source" title="Source">Source</a>" : <i>[ String, ... ]</i>,
        "<a href="#sourcenegate" title="SourceNegate">SourceNegate</a>" : <i>Boolean</i>,
        "<a href="#time" title="Time">Time</a>" : <i>[ String, ... ]</i>,
        "<a href="#track" title="Track">Track</a>" : <i>[ <a href="trackdefinition.md">TrackDefinition</a>, ... ]</i>,
        "<a href="#vpn" title="Vpn">Vpn</a>" : <i>String</i>,
        "<a href="#usercheck" title="UserCheck">UserCheck</a>" : <i>[ <a href="usercheckdefinition.md">UserCheckDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementAccessRule
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#actionsettings" title="ActionSettings">ActionSettings</a>: <i>
      - <a href="actionsettingsdefinition.md">ActionSettingsDefinition</a></i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#content" title="Content">Content</a>: <i>
      - String</i>
    <a href="#contentdirection" title="ContentDirection">ContentDirection</a>: <i>String</i>
    <a href="#contentnegate" title="ContentNegate">ContentNegate</a>: <i>Boolean</i>
    <a href="#customfields" title="CustomFields">CustomFields</a>: <i>
      - <a href="customfieldsdefinition.md">CustomFieldsDefinition</a></i>
    <a href="#destination" title="Destination">Destination</a>: <i>
      - String</i>
    <a href="#destinationnegate" title="DestinationNegate">DestinationNegate</a>: <i>Boolean</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#ignoreerrors" title="IgnoreErrors">IgnoreErrors</a>: <i>Boolean</i>
    <a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>: <i>Boolean</i>
    <a href="#inlinelayer" title="InlineLayer">InlineLayer</a>: <i>String</i>
    <a href="#installon" title="InstallOn">InstallOn</a>: <i>
      - String</i>
    <a href="#layer" title="Layer">Layer</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#position" title="Position">Position</a>: <i>
      - <a href="positiondefinition.md">PositionDefinition</a></i>
    <a href="#service" title="Service">Service</a>: <i>
      - String</i>
    <a href="#servicenegate" title="ServiceNegate">ServiceNegate</a>: <i>Boolean</i>
    <a href="#source" title="Source">Source</a>: <i>
      - String</i>
    <a href="#sourcenegate" title="SourceNegate">SourceNegate</a>: <i>Boolean</i>
    <a href="#time" title="Time">Time</a>: <i>
      - String</i>
    <a href="#track" title="Track">Track</a>: <i>
      - <a href="trackdefinition.md">TrackDefinition</a></i>
    <a href="#vpn" title="Vpn">Vpn</a>: <i>String</i>
    <a href="#usercheck" title="UserCheck">UserCheck</a>: <i>
      - <a href="usercheckdefinition.md">UserCheckDefinition</a></i>
</pre>

## Properties

#### Action

\"Accept\", \"Drop\", \"Ask\", \"Inform\", \"Reject\", \"User Auth\", \"Client Auth\", \"Apply Layer\".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ActionSettings

Action settings. Action settings blocks are documented below.

_Required_: No

_Type_: List of <a href="actionsettingsdefinition.md">ActionSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comments string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Content

List of processed file types that this rule applies on.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentDirection

On which direction the file types processing is applied.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentNegate

True if negate is set for data.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomFields

Custom fields. Custom fields blocks are documented below.

_Required_: No

_Type_: List of <a href="customfieldsdefinition.md">CustomFieldsDefinition</a>

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

#### InlineLayer

Inline Layer identified by the name or UID. Relevant only if \"Action\" was set to \"Apply Layer\".

_Required_: No

_Type_: String

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

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Position

Position in the rulebase. Position blocks are documented below.

_Required_: Yes

_Type_: List of <a href="positiondefinition.md">PositionDefinition</a>

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

#### Time

List of time objects. For example: \"Weekend\", \"Off-Work\", \"Every-Day\".

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Track

Track Settings. Track Settings blocks are documented below.

_Required_: No

_Type_: List of <a href="trackdefinition.md">TrackDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vpn

Communities or Directional.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserCheck

_Required_: No

_Type_: List of <a href="usercheckdefinition.md">UserCheckDefinition</a>

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


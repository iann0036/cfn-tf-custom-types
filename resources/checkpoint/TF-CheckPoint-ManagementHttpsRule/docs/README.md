# TF::CheckPoint::ManagementHttpsRule

This resource allows you to execute Check Point Https Rule.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementHttpsRule",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#blade" title="Blade">Blade</a>" : <i>[ String, ... ]</i>,
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>String</i>,
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
        "<a href="#service" title="Service">Service</a>" : <i>[ String, ... ]</i>,
        "<a href="#servicenegate" title="ServiceNegate">ServiceNegate</a>" : <i>Boolean</i>,
        "<a href="#sitecategory" title="SiteCategory">SiteCategory</a>" : <i>[ String, ... ]</i>,
        "<a href="#sitecategorynegate" title="SiteCategoryNegate">SiteCategoryNegate</a>" : <i>Boolean</i>,
        "<a href="#source" title="Source">Source</a>" : <i>[ String, ... ]</i>,
        "<a href="#sourcenegate" title="SourceNegate">SourceNegate</a>" : <i>Boolean</i>,
        "<a href="#track" title="Track">Track</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementHttpsRule
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#blade" title="Blade">Blade</a>: <i>
      - String</i>
    <a href="#certificate" title="Certificate">Certificate</a>: <i>String</i>
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
    <a href="#service" title="Service">Service</a>: <i>
      - String</i>
    <a href="#servicenegate" title="ServiceNegate">ServiceNegate</a>: <i>Boolean</i>
    <a href="#sitecategory" title="SiteCategory">SiteCategory</a>: <i>
      - String</i>
    <a href="#sitecategorynegate" title="SiteCategoryNegate">SiteCategoryNegate</a>: <i>Boolean</i>
    <a href="#source" title="Source">Source</a>: <i>
      - String</i>
    <a href="#sourcenegate" title="SourceNegate">SourceNegate</a>: <i>Boolean</i>
    <a href="#track" title="Track">Track</a>: <i>String</i>
</pre>

## Properties

#### Action

Rule inspect level. "Bypass" or "Inspect".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Blade

Blades for HTTPS Inspection. Identified by Name or UID to enable the inspection for.
"Anti Bot","Anti Virus","Application Control","Data Awareness","DLP","IPS","Threat Emulation","Url Filtering".blade blocks are documented below.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Certificate

Internal Server Certificate identified by Name or UID,
otherwise, "Outbound Certificate" is a default value.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comments string.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

Collection of Network objects identified by Name or UID that represents connection destination.destination blocks are documented below.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestinationNegate

TRUE if "negate" value is set for Destination.

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

Which Gateways identified by the name or UID to install the policy on.install_on blocks are documented below.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Layer

Layer that holds the Object. Identified by the Name or UID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

HTTPS rule name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Position

Position in the rulebase.

_Required_: Yes

_Type_: List of <a href="positiondefinition.md">PositionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

Collection of Network objects identified by Name or UID that represents connection service.service blocks are documented below.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceNegate

TRUE if "negate" value is set for Service.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiteCategory

Collection of Site Categories objects identified by the name or UID.site_category blocks are documented below.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SiteCategoryNegate

TRUE if "negate" value is set for Site Category.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

Collection of Network objects identified by Name or UID that represents connection source.source blocks are documented below.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceNegate

TRUE if "negate" value is set for Source.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Track

"None","Log","Alert","Mail","SNMP trap","Mail","User Alert", "User Alert 2", "User Alert 3".

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


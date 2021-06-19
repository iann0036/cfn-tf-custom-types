# TF::CheckPoint::ManagementNatRule

This resource allows you to add/update/delete Check Point NAT Rule.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementNatRule",
    "Properties" : {
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#ignoreerrors" title="IgnoreErrors">IgnoreErrors</a>" : <i>Boolean</i>,
        "<a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>" : <i>Boolean</i>,
        "<a href="#installon" title="InstallOn">InstallOn</a>" : <i>[ String, ... ]</i>,
        "<a href="#method" title="Method">Method</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#originaldestination" title="OriginalDestination">OriginalDestination</a>" : <i>String</i>,
        "<a href="#originalservice" title="OriginalService">OriginalService</a>" : <i>String</i>,
        "<a href="#originalsource" title="OriginalSource">OriginalSource</a>" : <i>String</i>,
        "<a href="#package" title="Package">Package</a>" : <i>String</i>,
        "<a href="#position" title="Position">Position</a>" : <i>[ <a href="positiondefinition.md">PositionDefinition</a>, ... ]</i>,
        "<a href="#translateddestination" title="TranslatedDestination">TranslatedDestination</a>" : <i>String</i>,
        "<a href="#translatedservice" title="TranslatedService">TranslatedService</a>" : <i>String</i>,
        "<a href="#translatedsource" title="TranslatedSource">TranslatedSource</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementNatRule
Properties:
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#ignoreerrors" title="IgnoreErrors">IgnoreErrors</a>: <i>Boolean</i>
    <a href="#ignorewarnings" title="IgnoreWarnings">IgnoreWarnings</a>: <i>Boolean</i>
    <a href="#installon" title="InstallOn">InstallOn</a>: <i>
      - String</i>
    <a href="#method" title="Method">Method</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#originaldestination" title="OriginalDestination">OriginalDestination</a>: <i>String</i>
    <a href="#originalservice" title="OriginalService">OriginalService</a>: <i>String</i>
    <a href="#originalsource" title="OriginalSource">OriginalSource</a>: <i>String</i>
    <a href="#package" title="Package">Package</a>: <i>String</i>
    <a href="#position" title="Position">Position</a>: <i>
      - <a href="positiondefinition.md">PositionDefinition</a></i>
    <a href="#translateddestination" title="TranslatedDestination">TranslatedDestination</a>: <i>String</i>
    <a href="#translatedservice" title="TranslatedService">TranslatedService</a>: <i>String</i>
    <a href="#translatedsource" title="TranslatedSource">TranslatedSource</a>: <i>String</i>
</pre>

## Properties

#### Comments

Comments string.

_Required_: No

_Type_: String

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

#### Method

Nat method.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Rule name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginalDestination

Original destination.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginalService

Original service.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginalSource

Original source.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Package

Name of the package.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Position

Position in the rulebase. Position blocks are documented below.

_Required_: Yes

_Type_: List of <a href="positiondefinition.md">PositionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TranslatedDestination

Translated destination.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TranslatedService

Translated service.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TranslatedSource

Translated source.

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

#### AutoGenerated

Auto generated.

#### Id

Returns the <code>Id</code> value.

